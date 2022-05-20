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
from matplotlib import pyplot as plt
from PIL import Image
from pytesseract import pytesseract
import os


x=1
i=0
while x!=0:
    camera=cv2.VideoCapture(1)
    ret,frame=camera.read()
    plt.imshow(frame)
    while True:
        _,image=camera.read()
        cv2.imshow('text det',image)
        o=cv2.waitKey(5)
        if o==ord('q'):
            i+=1
            cv2.imawrite('test'+str(i)+'.jpg',image)
            break
        elif o==ord('a'):
            x=0
            break
    camera.release()
    cv2.destroyAllWindows()

g=[]
def tesseract(j):
        path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        image_path = j
        img = Image.open(image_path)
        pytesseract.tesseract_cmd = path_to_tesseract
        text = pytesseract.image_to_string(img)
        print(text[:-1])
        x=text.split()
        return x[-1]
    
def recherche(n):
    os.chdir(n)
    l=os.listdir(n)
    p=[]
    s=[]
    for i in l:
        if i[-4:]=='.jpg':
            s.append(i)
    for j in s:   
        try :
            tesseract(j)
        except:    
            print('erreur')

recherche('C:\\Users\\Roudy\\Desktop')


