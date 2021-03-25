# with keyword
with open("abc.txt",'w') as f:
    f.write("welcome\n")
    f.write("to\n")
    f.write("python")
    print("is file closed:",f.closed)
print("is file closed:",f.closed)
