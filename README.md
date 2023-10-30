# Stock Chart Analysis README

## Introduction

This Python script is designed to extract marked points and levels from stock chart images using the OpenCV and Tesseract OCR libraries.

## Dependencies

Before running the code, you need to ensure that you have the following dependencies installed:

- Python 3.x
- OpenCV (`opencv-python-headless`)
- Tesseract OCR (`pytesseract`)
- Tesseract executable (install Tesseract-OCR from [Tesseract GitHub](https://github.com/tesseract-ocr/tesseract))

You can install OpenCV and Tesseract using pip:

```bash
pip install opencv-python-headless pytesseract
```

# Stock Chart Analysis README

## Setup

### Tesseract Configuration

Ensure that the Tesseract executable (`tesseract_cmd`) is correctly set in the script. You may need to update the `pytesseract.pytesseract.tesseract_cmd` line to point to your Tesseract executable path.

## Running the Code

1. Place the images "AssignmentImage-1.png" and "AssignmentImage-2.png" in the same directory as your Python script.

2. Run the script by executing the following command:

```bash
python stock_chart_analysis.py
```

## Design Decisions

The code follows the following design decisions:

- **Separate Functions**: Two separate functions are defined to extract points and levels from different images. This separation allows for flexibility and modularity.

- **Thresholding**: Binarization using thresholding is applied to the images to enhance text visibility. This is especially useful when text may not be in clear contrast with the background.

- **OCR Usage**: Tesseract OCR is used to recognize and extract text from the images. The `pytesseract.image_to_data` method is employed with a dictionary (`DICT`) output type to get structured data.

- **Data Output**: Extracted points and levels are presented in a structured format (list and dictionary) to facilitate further processing.

## Additional Considerations

- **Error Handling**: The code includes basic error handling. If the images are not found or if the OCR recognition is challenging due to image quality, the code will still run and produce empty results.

## Bonus Points (Optional)

The following bonus points can be considered for further enhancing the functionality of the code:

- **Robustness**: While the code includes basic error handling, for improved robustness, you may consider implementing specific error checks and recovery mechanisms for challenging cases. This can help handle scenarios where the input image quality may vary, or when OCR recognition faces difficulties.

- **Scalability**: The code can be further extended to process multiple stock chart images concurrently. By accepting a list of image paths and processing them in a loop, you can analyze multiple images at once. This can be especially valuable if you have a large number of stock charts to process simultaneously.

- **Performance**: The current code provides a straightforward solution for accuracy. Performance optimization can be achieved through techniques such as parallel processing for multiple images. This involves processing each image in a separate thread or process, allowing for improved efficiency and reduced processing time when analyzing a large number of images.


