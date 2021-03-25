# opening a file and writing data into that file
f=open("wish.txt",'w')
f.write("hello\n")
f.write("python\n")
f.write("how are you")
print("data written to the file successfully")
f.close()
