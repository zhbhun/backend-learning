
## 方案

- OpenCV：

  1. 图像预处理：使用灰度化、模糊处理、边缘检测（如 Canny 边缘检测）等方法预处理图像。
  2. 轮廓检测：使用 cv.findContours 函数找到图像中的轮廓。
  3. 选择四边形轮廓：从检测到的轮廓中选取最适合的四边形作为文档区域。
  4. 透视变换：使用 cv.getPerspectiveTransform 和 cv.warpPerspective 对文档进行矫正。

  ---

  - [Receipt OCR Part 1: Image segmentation by OpenCV](https://www.kaggle.com/code/dmitryyemelyanov/receipt-ocr-part-1-image-segmentation-by-opencv)

- [Scikit-Image](https://github.com/scikit-image/scikit-image)：Python 的图像处理库，提供了多种图像处理算法。
- PyTorch / TensorFlow：

  - 使用公开的文档检测数据集进行训练，如 [PubLayNet](https://github.com/ibm-aur-nlp/PubLayNet) 或 [Document Layout Analysis Dataset](https://paperswithcode.com/task/document-layout-analysis)，[DocLayNet](https://github.com/DS4SD/DocLayNet)。
  - 现有的一些预训练模型，如 [Mask R-CNN](https://github.com/matterport/Mask_RCNN)，也可以用于检测和分割文档区域。
  - https://universe.roboflow.com/realtimeprojects/document-detector
  - [Google ML Kit Document scanner](https://developers.google.com/ml-kit/vision/doc-scanner)

## Project

- Python

    - [docdetect](https://github.com/alessandrozamberletti/docdetect) - Real-time detection of documents in images
    - [DocProj](https://github.com/xiaoyu258/DocProj?tab=readme-ov-file) - Document Rectification and Illumination Correction using a Patch-based CNN
    - [OpenCV-Document-Scanner](https://github.com/andrewdcampbell/OpenCV-Document-Scanner) - An interactive document scanner built in Python using OpenCV featuring automatic corner detection, image sharpening, and color thresholding.
    - [Document-Scanner](https://github.com/murtazahassan/Document-Scanner)
    - [docscan](https://github.com/danielgatis/docscan)
    - [DocScan](https://github.com/Ellebam/DocScan)
    - https://github.com/dominiksinsaarland/DocSCAN

- iOS

    - [WeScan](https://github.com/WeTransfer/WeScan)

- Android

    - [Google ML Kit Document scanner](https://developers.google.com/ml-kit/vision/doc-scanner)

- JS

    - [jscanify](https://github.com/puffinsoft/jscanify?tab=readme-ov-file) - Open-source Javascript mobile document scanner.

## Sass

- https://www.filestack.com/docs/transformations/intelligence/document-detection/
- [Pixelnetica](https://www.pixelnetica.com/products/document-scanning-sdk)

  https://play.google.com/store/apps/details?id=com.pixelnetica.sharpscan.app

- [HUAWEI HiAI Engine Document Correction](https://developer.huawei.com/consumer/cn/doc/hiai-Guides/document-correction-development-guide-0000001054051737)
- [Genius Scan](https://help.thegrizzlylabs.com/article/398-better-automatic-document-detection)
- https://sdk.docutain.com/
- https://scanbot.io/

## Production

- 全能扫描王
- 白描
- Dropbox
- 夸克扫描王

## Reference

- https://www.google.com/search?q=document+detection&newwindow=1&sca_esv=442ff8e4c6d9f12b&sxsrf=ADLYWILtifYpcBIyoctb3SCX3eko1VFsRQ%3A1724600782422&ei=zlHLZt62GZDBkPIPxdHA0Q4&ved=0ahUKEwje1Y_IvpCIAxWQIEQIHcUoMOoQ4dUDCA8&uact=5&oq=document+detection&gs_lp=Egxnd3Mtd2l6LXNlcnAiEmRvY3VtZW50IGRldGVjdGlvbjIIEAAYgAQYywEyCBAAGIAEGMsBMggQABiABBjLATIIEAAYgAQYywEyCBAAGIAEGMsBMggQABiABBjLATIIEAAYgAQYywEyBBAAGB4yBhAAGB4YDzIEEAAYHkj4T1CiCVj1S3AEeAGQAQCYAYYHoAH9D6oBCzItMS4xLjAuMS4xuAEDyAEA-AEBmAIIoAKUEMICBxAjGLADGCfCAgoQABiwAxjWBBhHwgIOEC4YgAQYxwEYywEYrwHCAgoQABiABBgKGMsBmAMAiAYBkAYIkgcNNC4wLjEuMS4xLjAuMaAHhhU&sclient=gws-wiz-serp
- [Fast and Accurate Document Detection for Scanning](https://dropbox.tech/machine-learning/fast-and-accurate-document-detection-for-scanning)
- [Automatic Document Scanner using OpenCV](https://learnopencv.com/automatic-document-scanner-using-opencv/)
- [Document Detection in Python](https://medium.com/intelligentmachines/document-detection-in-python-2f9ffd26bf65)
- [How to Build a Kick-Ass Mobile Document Scanner in Just 5 Minutes](https://pyimagesearch.com/2014/09/01/build-kick-ass-mobile-document-scanner-just-5-minutes/)
- [Zero-parameter, automatic Canny edge detection with Python and OpenCV](https://pyimagesearch.com/2015/04/06/zero-parameter-automatic-canny-edge-detection-with-python-and-opencv/)
- [4 Point OpenCV getPerspective Transform Example](https://pyimagesearch.com/2014/08/25/4-point-opencv-getperspective-transform-example/)
- [利用OpenCV检测图像中的长方形画布或纸张并提取图像内容](https://www.cnblogs.com/frombeijingwithlove/p/4226489.html?spm=a2c6h.12873639.article-detail.7.1934612fet75qC)
- [OpenCV Java 实现票据、纸张的四边形边缘检测与提取、摆正](https://www.cnblogs.com/josephkim/p/8319069.html)
- [Edge Detection for Image Processing](https://sdk.docutain.com/blogartikel/edge-detection-for-image-processing)
- [How to Build a Kick-Ass Mobile Document Scanner in Just 5 Minutes](https://pyimagesearch.com/2014/09/01/build-kick-ass-mobile-document-scanner-just-5-minutes/)
- [Part 1: ID Documents Detection with YOLOv8 and Orientation Correction](https://medium.com/@paul_lefevre/id-documents-detection-with-yolov8-plus-rotation-e991192e74d2)
- [Real-time Document Localization in Natural Images by Recursive Application of a CNN](https://khurramjaved.com/RecursiveCNN.pdf)
