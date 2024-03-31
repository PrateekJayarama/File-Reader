import pyttsx3
speak1=pyttsx3.init()
speak1.setProperty('voice','english')
speak1.setProperty('rate',150)
speak1.say("this is Tom I will be Accessing Your file to be converted to speech")
speak1.runAndWait()
filename=input("Enter the File to Read:")
fname1=open(filename,'r')
speak2=pyttsx3.init()
speak2.setProperty('voice','english')
speak2.say(fname1.readlines())
speak2.runAndWait()
fname1.close()

