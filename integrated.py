import cv2
import os,glob
from os import listdir,makedirs
import shutil, random
from PIL import Image
import sys
from os.path import isfile,join

a = input("Enter the case 1.bgr2rgb  2.rename  3.move files  4.resize  5.video2frame  6.mutipleclass");
str = ""
def bgr2rgb():
	path = input("enter the source folder") # Source Folder
	assert os.path.exists(path), "I did not find the file at, "+str(path)
	dstpath = input("enter the destination folder") # Destination Folder
	assert os.path.exists(dstpath), "I did not find the file at, "+str(dstpath)
	try:
	    makedirs(dstpath)
	except:
		print ("Directory already exist, images will be written in same folder")
	# Folder won't used
	files = list(filter(lambda f: isfile(join(path,f)), listdir(path)))
	for image in files:
		try:
			img = cv2.imread(os.path.join(path,image))
			gray = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
			dstPath = join(dstpath,image)
			cv2.imwrite(dstPath,gray)
		except:
			print ("{} is not converted".format(image))
	for fil in glob.glob("*.jpg"):
		try:
			image = cv2.imread(fil) 
			gray_image = cv2.cvtColor(os.path.join(path,image), cv2.COLOR_BGR2RGB) # convert to rgb
			cv2.imwrite(os.path.join(dstpath,fil),gray_image)
		except:
			print('{} is not converted')
	
def rename():
	path = raw_input("enter the path of the folder")
	assert os.path.exists(path), "I did not find the file at, "+str(path)
	for filename in os.listdir(path):
    
		filename2 = path + "/"+filename
		print(filename2)
	os.rename(filename2,path + "/"+"rgb_"+filename)
# filename = "0001.txt"
# os.rename(filename,"rgb_"+filename)

def movefiles():
	dirpath = 'FINAL_IMAGES'
	dirpath1 = 'FINAL_LABELS'
	destDirectory = 'VALIDATION_DATASET'

	filenames = random.sample(os.listdir(dirpath), 720)
	for fname in filenames:
    		srcpath = os.path.join(dirpath, fname)
    		fname1 = fname[:-3]+"txt"
    		srcpath1 = os.path.join(dirpath1, fname1)
    		# print(srcpath,srcpath1)
    		shutil.move(srcpath, destDirectory)
    		shutil.move(srcpath1, destDirectory)
    		print("success")
    		
def resize():
	# print(os.listdir())
	path = input("enter the Path")
	dirs = os.listdir( path )
	# print(dirs)
	def resize():
		for item in dirs:
        	# print(path+item)
        	# print(os.path.isfile(path+item))
			if os.path.isfile(path+item):
					im = Image.open(path+item)
					f, e = os.path.splitext(path+item)
					imResize = im.resize((800,608), Image.ANTIALIAS)
            	#imResize.save(f + ' resized.jpg', 'JPEG', quality=90)
					imResize.save(f +'.jpg', 'JPEG', quality=90)
					print("success")

	resize()

def multipleclass():
	path = input("enter the path")
	assert os.path.exists(path), "I did not find the file at, "+str(path)
	# Read every file in directory
	for filename in os.listdir(path):
		filename = path + "/"+filename
		print(filename)
		f = open(filename)
		lines = f.readlines()
		f.close()
		f = open(filename, 'w')
		for line in lines:
			if line[0] == "0": 
				f.write("1"+ line[1:])
			else:
				f.write("0"+ line[1:])
			f.close()

def video2frame():
	video_names = os.listdir(input("enter the path of video"))
	assert os.path.exists(video_names), "I did not find the file at, "+str(path)
	print(video_names)
	frameRate = 0.33 #//it will capture image in each 0.5 second
	count=1
	if True:
		for i in video_names:
			i = "videos/" + i
			print("started ", video_names.index(i),"/",len(video_names), i)
			vidcap = cv2.VideoCapture(i)
			def getFrame(sec):
				vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
				hasFrames,image = vidcap.read()
				if hasFrames:
					cv2.imwrite("frames/"+"video"+str(count)+".jpg", image)     # save frame as JPG file
				return hasFrames
			sec = 0
			success = getFrame(sec)
			while success:
				count = count + 1
				sec = sec + frameRate
				sec = round(sec, 2)
				success = getFrame(sec)
video2frame()

if a == 1:
	bgr2rgb()
elif a == 2:
	rename()
elif a == 3:
	movefiles()
elif a == 4:
	resize()
elif a == 5:
        video2frame()
else:
	multipleclass()

my_switch = {1: bgr2rgb, 2: rename, 3: movefiles, 4: resize, 5: multipleclass}
