# wap number of occurences of each letter present in the given string

word=input("enter some word:")
d={}
for x in word:
    d[x]=d.get(x,0)+1
for k,v in d.items():
    print("{} occured {} times".format(k,v))

# wap number of occurences of each letter present in the given string by using sorted() function

word=input("enter some word:")
d={}
for x in word:
    d[x]=d.get(x,0)+1
print(d)
print(sorted(d))
for k,v in sorted(d.items()):
    print("{} occured {} times".format(k,v))

# wap number of occurences of each vowel present in the given string
word=input("enter some word:")
vowels={'a','e','i','o','u'}
d={}
for x in word:
    if x in vowels:
        d[x]=d.get(x,0)+1
for k,v in sorted(d.items()):
    print("{} occured {} times".format(k,v))
# wap print student name corresponding marks
n=int(input("enter the number of students:"))
d={}
for i in range(n):
    name=input("enter student name:")
    marks=eval(input("enter student marks:"))
    d[name]=marks
print(d)
while True:
    name=input("enter student name to get marks:")
    marks=d.get(name,-1)
    if marks==-1:
        print("student not found")
    else:
        print("the marks of {}:{}".format(name,marks))
        option=input("do you want to find another student marks[yes|no]:")
        if option=="no":
            break
print("thanks for using our application")
