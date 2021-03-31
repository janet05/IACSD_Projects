import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import webbrowser
import os
from os import walk
import numpy as np
import matplotlib.pyplot as plt

engine = pyttsx3.init('sapi5')  #sapi is microsoft inbuilt voice 
voice= engine.getProperty('voices') #getting details of current voice
#print(voice[0],"\n", voice[1])
engine.setProperty('voice', voice[1].id)

#register chrome path to open all web based content using chrome browser only!!
chrome_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))

#*************************************************************************************************
def speak(audio):
    engine.setProperty('rate', 190)
    engine.say(audio)
    engine.runAndWait()
  
#*************************************************************************************************
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am your Voice Assistant. Please tell me how may I help you")       

#*************************************************************************************************
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        speak("I'm sorry, i don't understand")
        return "None"
    return query

#*************************************************************************************************

#janet

def find_file_name(drive, filename):
    #this will find all files in the drive
    f = []      #List which has all files name
    for (dirpath, dirnames, filenames) in walk(drive):
        f.extend(filenames)
    #this will separate filename and extension
    for i in f:
        base=os.path.basename(i)
        name = os.path.splitext(base)[0]
        #this will now find the filename
        if name.lower() == filename.lower():
            #this will again search 
            for root, dirs, files in os.walk(drive):
                #this will find file name
                if i in files:    #using i bcoz it has proper extension with filename
                    p=(os.path.join(root, i)) #returns absolute path
                    os.startfile(p) #opens file
    
#*************************************************************************************************

def sub_command():  #for assistant to ask the user
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("waiting for reply: ")
        r.pause_threshold=1
        audio = r.listen(source)
    
    try:
        print("recognising reply :")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User replied: {query}\n")

    except Exception:
        # print(e)    
        speak("I'm sorry, i don't understand")
        return "None"
    return query


#*************************************************************************************************
def get_category():
    speak('What pictures do you want me to show?')
    reply = True
    speak('Plese tell me the category')
    r = sub_command()
    categories = [r]
   
    speak(f"Searching {categories} related images")
    return categories


#*************************************************************************************************
def load_model(categories):
    pass

#print(load_model(['dog','butterfly']))
#*************************************************************************************************

#*************************************************************************************************

def testing_model(category):
    from shutil import copyfile
        #categories = ['horse','butterfly','cat','dog','elephant','cow','spider','squirrel','car','plane','cycle']
    #categories= ['car','plane','cycle']
    try:
        for i in category:
            import pickle
            speak('     loading Model...')
            if i=='cat' or i=='dog':
                model = pickle.load(open('model\\cats_dogs.p','rb'))  #rb= reading byte
                categories=['cat','dog']
            elif i=='horse' or i=='candles':
                model = pickle.load(open('model\\butterfly_horse .p','rb'))  #rb= reading byte
                categories=['horse', 'candles']
            elif i=='balloon' or i=='squirrel':
                model = pickle.load(open('model\\balloon_squirrel30_10_98.p','rb'))  
                categories=['balloon','squirrel']
            elif i=='car' or i=='cycle' or i == 'plane':
                model = pickle.load(open('model\\transportation.p','rb'))
                categories= ['car','plane','cycle']
            else:
                break
            #******************************************************Testing
            speak('  Testing started...')
            #scikit-image : collection of algorithms for image processing and computer vision
            from skimage.io import imread #reading image
            from skimage.transform import resize #to resize because images will not be of same size
            
            #Walking through all files
            f =[]
            dest = "E:/NEWWWWWWWWWWWWWWWWWW/IACSD/project work/images_dataset/resulting_images/"
            path = "E:/NEWWWWWWWWWWWWWWWWWW/IACSD/project work/images_dataset/prediction"
            for dir, subdir, files in walk("E:/NEWWWWWWWWWWWWWWWWWW/IACSD/project work/images_dataset/prediction"):
                f.extend(files)
                
                for i in f:
                    base = os.path.basename(i)
                    ext = base.split('.')[1]
                    #checking if it is an image file by extension
                    if ext.lower() in ['jpg','jfif','jpeg','png',]:
                    #testing brand new image
                        flat_data = []
                        
                        #url = input('Enter url')
                        url = path+'/'+base
                        print(url)
                        img = imread(url)
                        
                        img_resized = resize(img,(150,150,3))
                        flat_data.append(img_resized.flatten())
                        flat_data = np.array(flat_data)
                        #print(img.shape)
                        #plt.imshow(img_resized)
                        y_out = model.predict(flat_data)
                        y_out = categories[y_out[0]]
                        # print(type(y_out))
                        # print(type(category[0]))
                        print(f'predicted output : {y_out}')   #this displays the type of image
                        print("-"*100)
                        if y_out == category[0]:
                            copyfile(url,(dest+'/'+base))                        
        os.startfile(dest) 
    except Exception as e:
        print(e)
        print("Error occured")


