# Attendance
Verifies the presence of students at a certain event

Members: 
        Roudy El sayi (210060)
        Rayan Jabbour(210360)
        Carl Helou(211530)
        Karl Azzi(211626)

We are here developping an OCR system to know wether a student attendant a certain event or class or not. 
The name.xlsx file is a file containing the names and family names of each student in the info 3 class of 2022 with their respective IDs. The

the code-names.py program will be converting those infos into another excel sheet named presence.xlsx in the format: Name Father Name Family Name assigned to the Id of each student. 

The code-ocr will open the camera of the computer, waits uyntil a command is given(q key)takes a pic of the id and interprets it to get the Matricule of each student. 

The code-presence program will be saving in the same excel sheet the date of the event and which student attended and which student didn't. 
for now it is randomly chosen because the projectis still not finished.

finally the code-email.py program willsend to the doctor the excel file whenever the program is run. 

for now, to test the codes sent, you can fill the excel table presence with random values in the status(present or absent) for the date of today(or whatever date you are running the code on). to do so, make sure that all the files are in the same folder (directory) and run code-names then code-presence. the chart should fill with the ids in the first column, full name in second and on the third the date on top and the status of each student(randomly chosen)

you can open the ocr and try it with any latin caracter card or document. (it might give an errror the code is not done yet) you will notice there ocr2 and ocr1. you can try both of them, the ocr2 should be our final version but we are still encoutering some minor errors.


you can run the code-email to send an email to anyone, just follow the instructions(dont worry, we will not use your password anywhere, unless you give us bad grades :))

please make sure that all these libraries are downloaded:

opencv2(pip install opencv-python)
pandas(pip)
matplotlib(pip)
smtplib(pip)
pytesseract(https://github.com/UB-Mannheim/tesseract/wiki)

we hope you do like the project and the work we put into it.

we learned a great deal of informations, as how to use pytessaract and pandas mainly.
