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

pic = pyscreenshot.grab(bbox=(0, 0, 1280, 1440)) # bbox = (X1,Y1,X2,Y2) X1,Y1 I think these are the corners of the screen maybe?
#pic.show()
pic.save("ss.png")

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "path to input image for OCR")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

text = pytesseract.image_to_string(image)
print(text)