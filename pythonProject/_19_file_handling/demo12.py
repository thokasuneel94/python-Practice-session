# seek() method
data="jathirathnalu movie is excellent"
f=open("abc.txt",'w')
f.write(data)
with open("abc.txt",'r+') as f:
    text=f.read()
    print(text)
    print("the current cursor position:",f.tell())
    f.seek(24)
    print("the current cursor position:",f.tell())
    f.write("comedy movie")
    f.seek(0)
    text=f.read()
    print("data after modification")
    print(text)

