import pytesseract
import pyscreenshot
import argparse
import cv2



# Outline:
# On run
#   Screenshot current game screen
#       Output Screenshot to a file (Overwrite existing to save space)
#           Process screenshot using tesseract
#               Copy blueprint names from screenshot to clipboard for pasting into excel


import pytesseract
import pyscreenshot
import argparse
import cv2

# Set pytesseract configuration parameters
config = '--psm 6'

# Capture screenshot
bbox = (0, 100, 1280, 500)
image = pyscreenshot.grab(bbox=bbox)
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

# Preprocess image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 3)
gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# Perform OCR
text = pytesseract.image_to_string(gray, config=config)

# Print OCR result
print(text)


"""
# old version
image = cv2.imread("ss.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

text = pytesseract.image_to_string(image)
print(text) """