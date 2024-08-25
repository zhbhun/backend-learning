import cv2
import numpy as np
import glob
import time


def order_points(pts):
    '''Rearrange coordinates to order:
       top-left, top-right, bottom-right, bottom-left'''
    rect = np.zeros((4, 2), dtype='float32')
    pts = np.array(pts)
    s = pts.sum(axis=1)
    # Top-left point will have the smallest sum.
    rect[0] = pts[np.argmin(s)]
    # Bottom-right point will have the largest sum.
    rect[2] = pts[np.argmax(s)]

    diff = np.diff(pts, axis=1)
    # Top-right point will have the smallest difference.
    rect[1] = pts[np.argmin(diff)]
    # Bottom-left will have the largest difference.
    rect[3] = pts[np.argmax(diff)]
    # return the ordered coordinates
    return rect.astype('int').tolist()


def scan(img):
    # Resize image to workable size
    dim_limit = 1080
    max_dim = max(img.shape)
    if max_dim > dim_limit:
        resize_scale = dim_limit / max_dim
        img = cv2.resize(img, None, fx=resize_scale, fy=resize_scale)

    # Create a copy of resized original image for later use
    orig_img = img.copy()

    # Repeated Closing operation to remove text from the document.
    kernel = np.ones((5, 5), np.uint8)
    morphology_ex = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=3)
    cv2.imwrite('outputs/0_morphology_ex.jpg', morphology_ex)

    # Convert to Grayscale
    gray = cv2.cvtColor(morphology_ex, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('outputs/0_gray.jpg', gray)

    # Apply Gaussian Blur
    # gray = cv2.GaussianBlur(gray, (11, 11), 0)
    gaussian_blur = cv2.GaussianBlur(gray, (3, 3), 0)
    cv2.imwrite('outputs/0_gaussian_blur.jpg', gaussian_blur)

    # Edge Detection.
    canny = cv2.Canny(gaussian_blur, 0, 200)
    cv2.imwrite('outputs/0_canny.jpg', canny)
    dilate = cv2.dilate(canny, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 4)))
    cv2.imwrite('outputs/0_dilate.jpg', dilate)

    # Find contours and select the largest one
    contours, _ = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    largest_contour = max(contours, key=cv2.contourArea)
    contour = cv2.drawContours(np.zeros(img.shape, dtype=np.uint8), [largest_contour], -1, (255, 255, 255), thickness=2)
    contour = cv2.cvtColor(contour, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('outputs/0_contour.jpg', contour)

    # Hough transform to detect lines
    lines = cv2.HoughLinesP(contour, 1, np.pi / 180, threshold=50, minLineLength=50, maxLineGap=100)
    line = np.zeros(img.shape, dtype=np.uint8)
    if lines is not None:
        for item in lines:
            # line 是一个二维数组，提取出起点和终点坐标
            x1, y1, x2, y2 = item[0]
            # 在图片上绘制线条，颜色为白色，线宽为1
            line = cv2.line(line, (x1, y1), (x2, y2), (255, 255, 255), thickness=2)
    cv2.imwrite('outputs/0_line.jpg', line)

    # Merge lines with similar direction and position
    def merge_lines(lines):
        merged_lines = []
        for current in lines:
            if len(merged_lines) == 0:
               merged_lines.append(current)
            else:
                for i, merged in enumerate(merged_lines):
                    if is_similar_line(current, merged):
                        merged_lines[i] = merge_two_lines(current, merged)
                        break
                else:
                    merged_lines.append(current)
        return merged_lines
    def is_similar_line(line1, line2, angle_threshold=np.pi / 36, position_threshold=10):
        # Check if the lines are in similar direction
        theta1 = np.arctan2((line1[1] - line1[3]), (line1[0] - line1[2]))
        theta2 = np.arctan2((line2[1] - line2[3]), (line2[0] - line2[2]))
        if abs(theta1 - theta2) > angle_threshold:
            return False

        # Check if the lines are close to each other in both x and y directions
        if (abs(line1[0] - line2[0]) < position_threshold and
            abs(line1[1] - line2[1]) < position_threshold and
            abs(line1[2] - line2[2]) < position_threshold and
            abs(line1[3] - line2[3]) < position_threshold):
            return True

        return False
    def merge_two_lines(line1, line2):
        # Merge two lines by taking the outermost points
        points = [line1[:2], line1[2:], line2[:2], line2[2:]]
        points = sorted(points, key=lambda x: (x[0], x[1]))
        return [points[0][0], points[0][1], points[-1][0], points[-1][1]]
    merged_lines = lines
    if lines is not None:
        merged_lines = merge_lines([line[0] for line in lines])
    merged_line = np.zeros(img.shape, dtype=np.uint8)
    if merged_lines is not None:
        for line in merged_lines:
          x1, y1, x2, y2 = line
          merged_line = cv2.line(merged_line, (x1, y1), (x2, y2), (255, 255, 255), 2)
    cv2.imwrite('outputs/0_merge_line.jpg', merged_line)

    #
    def distance(p1, p2):
        return np.linalg.norm(np.array(p1) - np.array(p2))

    # Function to check if four points form a quadrilateral
    def form_quadrilateral(line1, line2, line3, line4, epsilon=10):
        points = [line1[:2], line1[2:], line2[:2], line2[2:], line3[:2], line3[2:], line4[:2], line4[2:]]
        points = list(set([tuple(p) for p in points]))  # Remove duplicates
        if len(points) != 4:
            return False, None

        # Check if the lines form a closed quadrilateral within an allowable error
        points = sorted(points, key=lambda p: (p[0], p[1]))
        d1 = distance(points[0], points[1])
        d2 = distance(points[1], points[2])
        d3 = distance(points[2], points[3])
        d4 = distance(points[3], points[0])
        if abs(d1 - d3) < epsilon and abs(d2 - d4) < epsilon:
            return True, np.array(points, dtype="int32")
        return False, None

    # Search for the best quadrilateral
    max_area = 0
    best_quad = None

    for i in range(len(merged_lines)):
        for j in range(i + 1, len(merged_lines)):
            for k in range(j + 1, len(merged_lines)):
                for l in range(k + 1, len(merged_lines)):
                    is_quad, quad = form_quadrilateral(merged_lines[i], merged_lines[j], merged_lines[k], merged_lines[l])
                    if is_quad:
                        area = cv2.contourArea(quad)
                        if area > max_area:
                            max_area = area
                            best_quad = quad

    # Draw the largest quadrilateral
    if best_quad is not None:
        final_image = cv2.polylines(orig_img, [best_quad], isClosed=True, color=(0, 0, 255), thickness=3)
        return final_image
        # cv2.imwrite('outputs/0_final_image.jpg', final_image)

    return merged_line


for img_path in glob.glob('inputs/1.jpg'):
    try:
        start_time = time.time()  # 开始计时

        img = cv2.imread(img_path)
        print(img_path)

        scanned_img = scan(img)

        # cv2.imshow("scanner", scanned_img)
        cv2.imwrite('outputs/' + img_path.split('/')[-1], scanned_img)

        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000
        print(f"{img_path.split('/')[-1]}: {elapsed_time:.2f} ms")
    except Exception as e:
        print(e)

cv2.destroyAllWindows()
