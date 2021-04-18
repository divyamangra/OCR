import os
import cv2
import pytesseract

path=input("Please Enter the path of folder where images are present\n")
path.replace('/','\\')
path.replace("\\","\\")
arr=os.listdir(path)
unchecked=[]
for i in arr:
    print("image name: "+str(i))
    img=cv2.imread(path+'\\'+i)
    pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    try:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        image_text=pytesseract.image_to_string(img).lower()
        print(image_text)
    except:
        unchecked.append(i)
print("list of files not checked\n", unchecked)
