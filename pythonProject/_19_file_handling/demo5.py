# writing text into file by using writelines method
f=open("wish3.txt",'w')
list=['satish\n','anil\n','pradhyum\n','durga']
f.writelines(list)
print("list of line written to the file successfully")
