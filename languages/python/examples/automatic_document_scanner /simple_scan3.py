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
    morphology_ex = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=5)
    cv2.imwrite('outputs/0_morphology_ex.jpg', morphology_ex)

    # Convert to Grayscale
    gray = cv2.cvtColor(morphology_ex, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('outputs/0_gray.jpg', gray)

    # Apply Gaussian Blur
    gaussian_blur = cv2.GaussianBlur(gray, (3, 3), 0)
    cv2.imwrite('outputs/0_gaussian_blur.jpg', gaussian_blur)

    # Edge Detection.
    canny = cv2.Canny(gaussian_blur, 0, 200)
    cv2.imwrite('outputs/0_canny.jpg', canny)
    dilate = cv2.dilate(canny, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)))
    cv2.imwrite('outputs/0_dilate.jpg', dilate)

    # Finding contours for the detected edges.
    contours, hierarchy = cv2.findContours(dilate, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    #
    def approximate_contour_to_quadrilateral(contour):
        # Approximate the contour to a polygon with fewer vertices
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * peri, True)

        # Ensure the result is a quadrilateral
        if len(approx) == 4:
            return approx.reshape(-1, 2)
        else:
            # If not a quadrilateral, attempt to use the convex hull
            hull = cv2.convexHull(contour)
            hull_peri = cv2.arcLength(hull, True)
            hull_approx = cv2.approxPolyDP(hull, 0.02 * hull_peri, True)
            if len(hull_approx) == 4:
                return hull_approx.reshape(-1, 2)
        return None
    max_contour = max(contours, key=cv2.contourArea)
    contour = cv2.drawContours(np.zeros(img.shape, dtype=np.uint8), [max_contour], -1, (255, 255, 255), thickness=2)
    contour = cv2.cvtColor(contour, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('outputs/0_contour.jpg', contour)
    quadrilateral = approximate_contour_to_quadrilateral(max_contour)
    if quadrilateral is not None:
        temp = cv2.drawContours(gray, [quadrilateral], -1, (0, 255, 0), 2)
        cv2.imwrite('outputs/0_temp.jpg', temp)

    # Keeping only the largest detected contour.
    page = sorted(contours, key=cv2.contourArea, reverse=True)[:5]

    # Detecting Edges through Contour approximation
    if len(page) == 0:
        return orig_img
    # loop over the contours
    for c in page:
        # approximate the contour
        epsilon = 0.02 * cv2.arcLength(c, True)
        corners = cv2.approxPolyDP(c, epsilon, True)
        # if our approximated contour has four points
        if len(corners) == 4:
            break
    # Sorting the corners and converting them to desired shape.
    corners = sorted(np.concatenate(corners).tolist())
    # For 4 corner points being detected.
    # Rearranging the order of the corner points.
    corners = order_points(corners)

    # Finding Destination Co-ordinates
    w1 = np.sqrt((corners[0][0] - corners[1][0]) ** 2 + (corners[0][1] - corners[1][1]) ** 2)
    w2 = np.sqrt((corners[2][0] - corners[3][0]) ** 2 + (corners[2][1] - corners[3][1]) ** 2)
    # Finding the maximum width.
    w = max(int(w1), int(w2))

    h1 = np.sqrt((corners[0][0] - corners[2][0]) ** 2 + (corners[0][1] - corners[2][1]) ** 2)
    h2 = np.sqrt((corners[1][0] - corners[3][0]) ** 2 + (corners[1][1] - corners[3][1]) ** 2)
    # Finding the maximum height.
    h = max(int(h1), int(h2))

    # Final destination co-ordinates.
    destination_corners = order_points(np.array([[0, 0], [w - 1, 0], [0, h - 1], [w - 1, h - 1]]))

    h, w = orig_img.shape[:2]
    # Getting the homography.
    homography, mask = cv2.findHomography(np.float32(corners), np.float32(destination_corners), method=cv2.RANSAC,
                                          ransacReprojThreshold=3.0)
    # Perspective transform using homography.
    un_warped = cv2.warpPerspective(orig_img, np.float32(homography), (w, h), flags=cv2.INTER_LINEAR)
    # Crop
    final = un_warped[:destination_corners[2][1], :destination_corners[2][0]]
    return final


for img_path in glob.glob('inputs/10.jpg'):
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
