import os
import numpy as np
from my_functions import speak
from datetime import datetime

now = datetime.now()
print(now)
#image processing will be done here using these 
from skimage.io import imread #reading image  [collection of algos for image processing & CV]
from skimage.transform import resize #to resize because images will not be of same size

#flattening data (need to define globally so that it can be used in other functions too)
print('Started')
target=[]
images = []
flat_data= []

datadir = 'E:\\NEWWWWWWWWWWWWWWWWWW\\IACSD\\project work\\images_dataset'
categories = ['dog','horse','squirrel','cow']


for category in categories:
    class_num = categories.index(category)   #kind of doing label encoding here
    path=os.path.join(datadir,category)   #creating paths which we'll be iterating through

    for img in os.listdir(path):
        img_array=imread(os.path.join(path,img))
        img_resized = resize(img_array,(150,150,3))  #resizing here
        flat_data.append(img_resized.flatten())   #flattening images
        target.append(class_num)

#incase our flat data doesn't convert into array we do following
flat_data = np.array(flat_data)
target = np.array(target)
images = np.array(images)

np.unique(target,return_counts=True)

print('   Resizing and Flattening completed...')

#******************************************************SPLITTING DATA
print('   SPLITTING DATA...')
from sklearn.model_selection import train_test_split

xtrain,xtest,ytrain,ytest = train_test_split(flat_data,target,test_size=0.3,random_state=42)  #changing random state will make out accuracy change too

#******************************************************SVC modelling DATA
print('  SVC Model data...')
from sklearn.model_selection import GridSearchCV  #helps select best parameters
from sklearn import svm

param_grid =[ 
          {'C':[1,10,100,1000],'kernel':['linear']},
          {'C':[1,10,100,1000],'gamma':[0.001,0.0001],'kernel':['rbf']},
]

svc = svm.SVC(probability=True,gamma = 'auto')
clf = GridSearchCV(svc,param_grid)
clf.fit(xtrain,ytrain)      #will get best values to put in model 
#print(clf.fit(xtrain,ytrain)) 


print('   Modelling part completed...')

y_pred = clf.predict(xtest)
print('Predixted value :',y_pred)  #predicted value
print('Original value : ', ytest)

from sklearn.metrics import accuracy_score,confusion_matrix

print(accuracy_score(y_pred,ytest))  #changes according to random_state in above 

print(confusion_matrix(y_pred,ytest))

import pickle
pickle.dump(clf,open('new_models\\DHSC.p','wb'))  #new file img_model.p will be made   #wb = writing byte
speak('   Model saved...')

now = datetime.now()
print(now)