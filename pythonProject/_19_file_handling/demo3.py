# instead of overriding the content,appending the text to file
f=open("wish1.txt",'a')
f.write("hello\n")
f.write("python\n")
f.write("how are you")
print("data written to the file successfully")
f.close()
