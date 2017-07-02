# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 07:45:30 2017

@author: user
"""

import os
import shutil
import send2trash
import zipfile



#shutil.copy(source,destination) copy the file at the path source 
#to the folder at the path destination.
#if destination is a filename, it will be used as as the newe name of the copied file

os.chdir('C:\\')
#print (shutil.copy('C:\\Users\\user\\Desktop\\spam.txt','C:\\Users\\user\\Desktop\\delicious'))
#this copies the text file spam to the file delicious
#the file spam is still there in the desktop
#but the file is also in the file delicious
#the return value of shutil.copy is the path of the copied file

#shutil.copytree copy an entire folder and every folder and file contained in it.
#shutil.copytree(source,destination)

#shutil.copytree('C:\\Users\\user\\Desktop\\delicious','C:\\Users\\user\\Desktop\\delicious_backup')
#this creates a folder named delicious_backup that has the same content as the file delicious
#note that copytree creates a folder unlike shutil.copy
#this means copytree will give you an error if the destination is a folder that already exists.

#shutil.move(source, destination) moves the file or the folder at the path source to the path desitnation 
#also returns a string of the absoulte path of the new locatoin

#print (shutil.move('C:\\Users\\user\\Desktop\\spam.txt','C:\\Users\\user\\Desktop\\hi'))
#moves text file called spam in desktop to a file called hi

#print (shutil.move('C:\\Users\\user\\Desktop\\spam.txt','C:\\Users\\user\\Desktop\\hi\\notspam.txt'))
#moves the spam file to hi folder and renames spam to notspam

#if destination folder does not exist in directory
#then, the file will be renamed to the desitation name
#because it will be assumed that destination is specifying a filename

#also, the folders that make up the destiation must already exist

#Calling os.unlink(path) will delete the file at path.
#
#Calling os.rmdir(path) will delete the folder at path. This folder must be empty of any files or folders.
#
#Calling shutil.rmtree(path) will remove the folder at path, and all files and folders it contains will also be deleted.

#using above function calls may accidentally delete files you don't want to.
#so it's better to do something like.....
#for filename in os.listdir():
    #if filename.ends with ('.rxt.'):
        #os.unlink(filename) --> comment this line out
        #print (filename) --> this will show which file will be deleted if you uncomment the above comment

#send2trash module sends deleted file to recycle bin, unlike rmtree which irreversibly deletes files and folders 

baconFile = open('C:\\Users\\user\\Desktop\\bacon2.txt','a') #creates the file
#I don't have permission to change file unless it's in Desktop (unless I specify it's in desktop, it will giv eme permission error)
baconFile.write('Bacon is not a vegetable.')

baconFile.close()
send2trash.send2trash('C:\\Users\\user\\Desktop\\bacon2.txt')
#sends bacon2.txt to trash can

#os.walk() is given a single string of the path of the folder
#then it will 'walk through' the folder, and return
#1. a string of the current folder's name
#2. a list of strings of the folders in the current folder
#3. a listo f strings of the files in the current folder

#for folderName, subfolders, filenames in os.walk('C:\\Users\\user\\Desktop\\delicious'):
#    print ('The current folder is ' +folderName)
#    
#    for subfolder in subfolders:
#        print ('SUBFOLDER OF ' + folderName + ': ' + subfolder)
#    for filename in filenames:
#        print ('File Inside ' + folderName + ': ' + filename)

exampleZip = zipfile.ZipFile('C:\\Users\\user\\Desktop\\example.zip')
#print (exampleZip.namelist()) 
#print out names of file in zipefile

spaminfo = exampleZip.getinfo('example/Bernie_Sanders.jpg')
#don't use exmpple.zip, use example
#also, use forward slash (/), backward slash (\) don't wark
#it also doesn't work with folders, it only works with files
#print (spaminfo.file_size) #print out file size of the file
#print (spaminfo.compress_size) #compressed size

#exampleZip.close() #close the file
#os.chdir('C:\\Users\\user\\Desktop') #move the folder with example.zip to current working directory
#exampleZip = zipfile.ZipFile('C:\\Users\\user\\Desktop\\example.zip')
#print (exampleZip.extractall('C:\\Users\\user\\Desktop\\life'))
#extract all files, apparently you need to search for this folder

#print (exampleZip.extract('example/Bernie_Sanders.jpg','C:\\Users\\user\\Desktop\\death'))
#extarct single file, also need to serach for this folder
#string you pass to extract() must match one of the strings in the list returned by namelist()

newZip = zipfile.ZipFile('C:\\Users\\user\\Desktop\\new.zip','w')
newZip.write('C:\\Users\\user\\Desktop\\spam.txt', compress_type = zipfile.ZIP_DEFLATED)
newZip.close()

#creates a new ZIP file named new.zip that has the compressed contents of spam.txt
#write mode erasea all exisitng content of a zip file
#if you want to add files, use a as in append mode



