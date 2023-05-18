#directory is a nothing but a folder normally we have folder in our system same as that we can make
#certaim number of operation in directory
#Directory mainly uses for file managemant
#for EX take you have a project which contains many files take it contains 1000 files
#these files are categoriized by folders or directories which will be easy to us
import os#OS module helps us to perform director
print(os.getcwd)#this will show us our current working path
os.chdir('F:\PYTHON\\Documents')#on first our current dir is 'F:\PYTHON' now it changed to 'F:\PYTHON\documents'
print(os.getcwd())
print(os.listdir())#this is used to shows the files in the directory
#now we create new directory
#os.mkdir('Navee')
print(os.listdir())
os.rename('Navee','Vic')#this is used to rename the directory we have created
os.remove('nn.txt')#this is used to delete the file
os.removedirs('Navee')#this command is used to delete the directory or folder
print(os.listdir())
