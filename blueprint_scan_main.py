import pytesseract
import pyscreenshot

# Outline:
# On run
#   Screenshot current game screen
#       Output Screenshot to a file (Overwrite existing to save space)
#           Process screenshot using tesseract
#               Copy blueprint names from screenshot to clipboard for pasting into excel

pic = pyscreenshot.grab(bbox=(0, 0, 1280, 1440)) # bbox = (X1,Y1,X2,Y2) X1,Y1 I think these are the corners of the screen maybe?
pic.show()
pic.save("ss.png") 