##file_obj = open("mad.txt","w")        #w stands for write
##file_obj.write("india is my country")
##file_obj.close()

##file_obj = open(r"Downloads\mad.txt","w")
##file_obj.write("india is my country")
##file_obj.close()

##file_obj = open("mad.txt","w")
##file_obj.write("python programme")
##file_obj.close()

##file_obj = open("mad.txt","a")        #a stands for append
##file_obj.write("\n")
##file_obj.write("new programme")
##file_obj.close()

##file_obj = open("mad.txt","a")
##file_obj.write("\n")
##file_content = input("enter the file content")
##file_obj.write(file_content)
##file_obj.close()

##file_obj = open("mad.txt","x")          #x stands for new file creation
##file_obj.write("\n")
##file_content = input("enter the file content")
##file_obj.write(file_content)
##file_obj.close()

#context manager

##with open("mad.txt","a") as file_obj:
##    file_obj.write("\n")
##    file_content = input("enter the file content")
##    file_obj.write(file_content)

##with open("mad.txt","r") as file_obj:   #r stands for read
##    file_output = file_obj.read()
##    print(file_output)

##with open("mad.txt","r") as file_obj:
##    file_output = file_obj.read(2)
##    print(file_output)
##    file_output1 = file_obj.read()
##    print(file_output1)

##with open("mad.txt","r") as file_obj:
##    file_output = file_obj.readline()
##    print(file_output)
##    file_output1 = file_obj.readline()
##    print(file_output1)

##with open("mad.txt","r") as file_obj:
##    file_output = file_obj.readline(2)
##    print(file_output)
##    file_output1 = file_obj.readline()
##    print(file_output1)

##with open("mad.txt","r") as file_obj:
##    file_output = file_obj.readline(2)
##    print(file_output)
##    file_output1 = file_obj.readline(1)
##    print(file_output1)
