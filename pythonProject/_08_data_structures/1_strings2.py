# finding substrings:
# find() method
# syntax      nameofthestring.find(substring)
# index() method
# syntax      nameofthestring.index(substring)
# finding sub string by using find method
s="Python programming language"
print(s.find("python"))
print(s.find("programming"))
print(s.find("hello"))  # substring not given in main string output is -1
print(s.find("z"))
print(s.find("ing"))
print(s.find("p"))
print(s.find("a",1,20))        # s.find(substring,begin,end)      # end=end-1 index
# finding substring by using index method
s="Python programming language"
print(s.index("Python"))
# print(s.index("hello"))    valueerror
# handling error while finding sub string by using index method
# s="Python programming language"
# print(s.index("hello"))
# except ValueError:
# print("not found")

# counting substring in the given string:
# count() method
# syntax      nameofthestring.count(substring)
s="sunny leone sunny leone pavani pavani"
print(s.count("sunny"))
print(s.count("pavani"))
print(s.count("sunny",8,15))
print(s.count("sunny",8,len(s)))
s="aabbbababbababbabbabab"
print(s.count("a"))
print(s.count("a",4,18))
print(s.count("a",7,len(s)))

# replacing a string with another string:
# replace() method
# syntax      nameofthestring.replace(old string,new string)
# replacing string by using replace method
s1="java programming language"
s2=s1.replace("java","python")
print(s1)
print(s2)
print(id(s1))
print(id(s2))
s1="ababbababbababab"
s2=s1.replace("a","b")
print(s1)
print(s2)
print(id(s1))
print(id(s2))
# splitting of strings:

# split() method
# splitting string by using split() method
s="Python programming language"
l=s.split()
print(l)
for x in l:
    print(x)
s="Python programming,language"
l=s.split(",")
for x in l:
    print(x)

s="02-03-2018"
l=s.split("-")
for x in l:
    print(x)
print(type(l))
print(type(s))
s="splitting string by using split method"
l=s.split(' ',3)
for x in l:
    print(x)
s="10,20,30,40,50,60,70,80"
l=s.split(',',3)
for x in l:
    print(x)

# rsplit() method
s="splitting string by using split method"
l=s.rsplit(' ',3)
for x in l:
    print(x)
s="10,20,30,40,50,60,70,80"
l=s.rsplit(',',3)
for x in l:
    print(x)
s="10,20,30,40,50,60,70,80"
l=s.rsplit(',',-1)
for x in l:
    print(x)

# joining of strings:
# join() method
# s=seperator.join(group of strings)     #group of strings like list, tuple
# seperator is - joining string by using join method
l=['sunny','leone','sexy']
s='-'.join(l)
print(s)
print(type(l))
print(type(s))
# seperator is : joinig string by using join method
t=('kajal','agarwal','figer')
s=':'.join(t)
print(t)
print(type(t))
print(type(s))
# no seperator joining string by using join method
t=('siva','rama','krishna')
s=''.join(t)
print(s)
# seperator is space joining string by using join method
t=('mehrin','looks','like','beauty')
s=' '.join(t)
print(s)




