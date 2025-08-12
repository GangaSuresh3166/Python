# f=open('file1.py','x')   //create new file=x
# f=open('file1.py','a')   //append file=a  it will add new statement and return existing and new statement together
# f=open('file1.py','a')   //write file=w it will remove existing statement and return new statement
# f.write("Hello.")
# f.write("\nWorld.")
# f.close()   


# f=open('file1.py','r')
# for each in f:
    # print(each)   
# print(f.readline())   //single line output 
# print(f.readline())
# print(f.read())       //full file output


# with open('file1.py','r')as f:    //storing datas in file to a variable
#     data=f.read()
# print(data)


# f=open('file1.py','r')
# print(f.read(12))          //printing output from the file by number of characters given


# with open('file1.py','r')as f:
#     data=f.readlines()
# for line in data:
#     word=line.split()
#     print(word)


