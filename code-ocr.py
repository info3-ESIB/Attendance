####from PIL import Image
####from pytesseract import pytesseract
####  
#### Defining paths to tesseract.exe
#### and the image we would be using
####path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
####image_path = r"C:\Users\user\Desktop\info3\481.jpg"
####  
#### Opening the image & storing it in an image object
####img = Image.open(image_path)
####  
#### Providing the tesseract executable
#### location to pytesseract library
####pytesseract.tesseract_cmd = path_to_tesseract
####  
#### Passing the image object to image_to_string() function
#### This function will extract the text from the image
####text = pytesseract.image_to_string(img)
####  
#### Displaying the extracted text
####print(text[:-1])

import cv2
from PIL import Image
from pytesseract import pytesseract

camera=cv2.VideoCapture(0)

while True:
    _,image=camera.read()
    cv2.imshow('text det',image)
    if cv2.waitKey(5)==ord('q'):
        cv2.imwrite('test.jpg',image)
        break
camera.release()
cv2.destroyAllWindows()

def tesseract():
        path_to_tesseract = r"C:\Users\Roudy\Downloads"
        image_path = r"test.jpg"
        img = Image.open(image_path)
        pytesseract.tesseract_cmd = path_to_tesseract
        text = pytesseract.image_to_string(img)
        print(text[:-1])
tesseract()        

    

 

