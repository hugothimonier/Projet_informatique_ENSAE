from PIL import Image
import os

print('current directory : ' ,os.getcwd())

# get the files in the directory :

files = os.listdir()

# for resizing
basewidth = 200

# edit all the files of the directory
for f in files : 
	print(f)
	if 'png' in f:
		img = Image.open(f)
		wpercent = (basewidth/float(img.size[0]))
		hsize = int((float(img.size[1])*float(wpercent)))
		img = img.resize((basewidth,hsize), Image.ANTIALIAS)
		img.save('resized_images/resized_'+f) 

print('resizing complete.')