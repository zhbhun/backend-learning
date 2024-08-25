
## 方案

- OpenCV：

  1. 图像预处理：使用灰度化、模糊处理、边缘检测（如 Canny 边缘检测）等方法预处理图像。
  2. 轮廓检测：使用 cv.findContours 函数找到图像中的轮廓。
  3. 选择四边形轮廓：从检测到的轮廓中选取最适合的四边形作为文档区域。
  4. 透视变换：使用 cv.getPerspectiveTransform 和 cv.warpPerspective 对文档进行矫正。

- [Scikit-Image](https://github.com/scikit-image/scikit-image)：Python 的图像处理库，提供了多种图像处理算法。
- PyTorch / TensorFlow：

  - 使用公开的文档检测数据集进行训练，如 [PubLayNet](https://github.com/ibm-aur-nlp/PubLayNet) 或 [Document Layout Analysis Dataset](https://paperswithcode.com/task/document-layout-analysis)，[DocLayNet](https://github.com/DS4SD/DocLayNet)。
  - 现有的一些预训练模型，如 [Mask R-CNN](https://github.com/matterport/Mask_RCNN)，也可以用于检测和分割文档区域。

## Project

- [OpenCV-Document-Scanner](https://github.com/andrewdcampbell/OpenCV-Document-Scanner) - An interactive document scanner built in Python using OpenCV featuring automatic corner detection, image sharpening, and color thresholding.
- [Document-Scanner](https://github.com/murtazahassan/Document-Scanner)
- [docscan](https://github.com/danielgatis/docscan)
- [DocScan](https://github.com/Ellebam/DocScan)
- https://github.com/dominiksinsaarland/DocSCAN

## Business

- [Pixelnetica](https://www.pixelnetica.com/products/document-scanning-sdk)

  https://play.google.com/store/apps/details?id=com.pixelnetica.sharpscan.app

- [HUAWEI HiAI Engine Document Correction](https://developer.huawei.com/consumer/cn/doc/hiai-Guides/document-correction-development-guide-0000001054051737)

## Reference

- [Automatic Document Scanner using OpenCV](https://learnopencv.com/automatic-document-scanner-using-opencv/)
- [Automatic Document Scanner using OpenCV](https://learnopencv.com/automatic-document-scanner-using-opencv/)
- [How to Build a Kick-Ass Mobile Document Scanner in Just 5 Minutes](https://pyimagesearch.com/2014/09/01/build-kick-ass-mobile-document-scanner-just-5-minutes/)
- [Zero-parameter, automatic Canny edge detection with Python and OpenCV](https://pyimagesearch.com/2015/04/06/zero-parameter-automatic-canny-edge-detection-with-python-and-opencv/)
- [4 Point OpenCV getPerspective Transform Example](https://pyimagesearch.com/2014/08/25/4-point-opencv-getperspective-transform-example/)
- [利用OpenCV检测图像中的长方形画布或纸张并提取图像内容](https://www.cnblogs.com/frombeijingwithlove/p/4226489.html?spm=a2c6h.12873639.article-detail.7.1934612fet75qC)
- [OpenCV Java 实现票据、纸张的四边形边缘检测与提取、摆正](https://www.cnblogs.com/josephkim/p/8319069.html)
- [Edge Detection for Image Processing](https://sdk.docutain.com/blogartikel/edge-detection-for-image-processing)
- [How to Build a Kick-Ass Mobile Document Scanner in Just 5 Minutes](https://pyimagesearch.com/2014/09/01/build-kick-ass-mobile-document-scanner-just-5-minutes/)
