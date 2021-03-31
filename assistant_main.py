import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os

import random  #used in images
from PIL import Image # Python Imaging Library

#importing my files 
from my_functions import speak
from my_functions import takeCommand
from my_functions import sub_command
from my_functions import find_file_name
from my_functions import testing_model
from my_functions import get_category
import sys 
#import module1.image_classifier

#speak("Hey Janet, How you doing?")
speak("Starting Personal Voice Assistant")
#wishMe()
 
#testing
if __name__ == "__main__":
    #takeCommand()
    while True:
    # if 1:
        query = takeCommand().lower()
        
        if 'stop' in query:   #stop the assistant
            speak("ok!,see you soon")
            sys.exit()
        # Logic for executing tasks based on query
        elif 'what is your name' in query:
            speak("My name is Zara")
            
        elif 'what is' in query:
            speak('Searching Wikipedia...')
            query = query.replace("what is", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            #my code Janet
            #get -> specifies registered browser
            #open --> arg1 = url, arg2 = to tell assistant to open in same-tab,new-tab,new window
            webbrowser.get("chrome").open("youtube.com", new=2) 

        elif 'open google' in query:
            webbrowser.get("chrome").open('google.com', new=2)
            #webbrowser.open("google.com", new=2)

        elif 'open stack overflow' in query:
            webbrowser.get("chrome").open("stackoverflow.com", new=2)   

        elif 'tell me the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Janet, the time is {strTime}")
        
        elif 'open document' in query: #my code /janet
            # speak("opening document")
            # power = r"C:\\Users\\lenovo\\Desktop\\word file.txt"
            # os.startfile(power)
            
            #janet
            speak("Tell me the drive name!")
            drive_name = sub_command()
            speak("Tell me the file name!")
            file_name = sub_command().lower()
            path = f"{drive_name}:\\"
            find_file_name((drive_name+":"), file_name)          
        
        elif 'show birthday pictures' in query: #my code /janet
            path="E:\\NEWWWWWWWWWWWWWWWWWW\\IACSD\\project work\\images\\"
            files=os.listdir(path)
            d=random.choice(files)  #chooses random image and display
            #os.startfile(d)
            #print(d)
            print(query)
            img = Image.open(path+d)
            img.show()
        
        elif "show pictures" in query:
            categories = get_category()            
            testing_model(categories)
            pass
            
        else:
            speak("I'm sorry, i don't have an answer for this.")