# //actual file

import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd=r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# Function to extract points (P1 to P7) from the first image
def extract_points(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    points = pytesseract.image_to_data(thresholded, output_type=pytesseract.Output.DICT)
    
    extracted_points = []
    for i in range(len(points['text'])):
        text = points['text'][i]
        if text.startswith("P") and text[1:8].isdigit():
            x = points['left'][i]
            y = points['top'][i]
            extracted_points.append((text, (x, y)))
    
    return extracted_points

# Function to extract levels (L1 & L2) from the second image
def extract_levels(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    levels = pytesseract.image_to_data(thresholded, output_type=pytesseract.Output.DICT)
    
    extracted_levels = {}
    for i in range(len(levels['text'])):
        text = levels['text'][i]
        if text.startswith("L") and text[1:3].isdigit():
            y = levels['top'][i]
            extracted_levels[text] = y
    
    return extracted_levels

# Extract points from the first image
points = extract_points("AssignmentImage-1.png")

# Extract levels from the second image
levels = extract_levels("AssignmentImage-2.png")

# Print the extracted data
print("Extracted Points:")
for point, coordinates in points:
    print(f"{point}: {coordinates}")

print("\nExtracted Levels:")
for level, y_coordinate in levels.items():
    print(f"{level}: {y_coordinate}")
