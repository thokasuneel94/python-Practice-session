# handling binary data:
# it is very common requirement to read or write binary data like images,video files,audio files etc
# wap to read image file and write to a new image file
f1=open("guido.jpg","rb")
f2=open("newpic.jpg","wb")
bytes=f1.read()
f2.write(bytes)
print("new image is available with the name:newpic.jpg")