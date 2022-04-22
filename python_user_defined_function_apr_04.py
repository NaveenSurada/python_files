##print("hello")
##print("welcome to my world")

##def My_fun():  #function definition without argument or signature or parameter

##    print("hello")
##    print("welcome to my world")
##My_fun()  #Function calling


##def My_fun(name): #function definition with argument or signature or parameter
##
##    print("hello",name)
##    print("Welcome to my world")
##
##My_fun("dhoni")   #Function calling
##My_fun("kohli")

##def My_fun(name): #function definition with argument or signature or parameter
##
##    if isinstance(name,str):
##        print("hello",name)
##        print("Welcome to my world")
##
##My_fun("dhoni")   #Function calling
##My_fun("kohli")
##My_fun(4)

##def My_fun(name,country): #function definition with argument or signature or parameter
##
##    if isinstance(name,str) and isinstance(country):
##        print("hello",name)
##        print("Welcome to my world")
##
##My_fun("dhoni","india")   #Function calling
##My_fun("kohli","bangalore")
##My_fun("bajji",4)

##def My_fun(name,country): #function definition with argument or signature or parameter
##
##    if isinstance(name,str) and isinstance(country,str):
##        print("hello",name,"from",country)
##        print("Welcome to my world")
##
##My_fun("dhoni","india")   #Function calling
##My_fun("kohli","bangalore")
##My_fun("bajji",4)

##def My_fun(name,country): #function definition with argument or signature or parameter
##
##    if isinstance(name,str):
##        if isinstance(country,str):
##            print("hello",name,"from",country)
##            print("Welcome to my world")
##
##My_fun("dhoni","india")   #Function calling
##My_fun("kohli","bangalore")

##def My_fun(name,country): #function definition with argument or signature or parameter
##
##    if isinstance(name,str) and isinstance(country,str):
##        print("hello",name,"from",country)
##        print("Welcome to my world")
##
##My_fun(country="india",name="dhoni")   #Function calling
##My_fun("kohli","bangalore")

##def My_fun(name,country="india"): #function definition with argument or signature or parameter
##
##    if isinstance(name,str) and isinstance(country,str):
##        print("hello",name,"from",country)
##        print("Welcome to my world")
##
##My_fun("dhoni")
##My_fun("kohli","bangalore")

##def My_fun(name,country=None): #function definition with argument or signature or parameter
##    print("hello",name,"from",country)
##
##
##My_fun("dhoni")
##My_fun("kohli","bangalore")

##def My_fun(name="sachin",country=None): #function definition with argument or signature or parameter
##    print("hello",name,"from",country)
##
##
##My_fun("dhoni")
##My_fun("kohli","bangalore")

##def My_fun(name="sachin",country=None): #function definition with argument or signature or parameter
##    print("hello",name,"from",country)
##
##
##My_fun()
##My_fun("dhoni")
##My_fun("kohli","bangalore")

##def My_fun(name="sachin",country): #function definition with argument or signature or parameter
##    print("hello",name,"from",country)
##
##My_fun()

##def Student_passed(*names):
##
##    print(names)
##
##Student_passed("dhoni")
##Student_passed("kohli","sachin")

#*args means it can take any number of arguments
#output will be in the form of tuple

##def Student_passed(**names):
##
##    print(names)
##
##Student_passed(name="dhoni")
##Student_passed(name="kohli",age=33)

#*args means data with keys
#output will be in the form of dictionary

##def Student_mark(eng,math, student_name):
##
##    total= eng + math
##    return
##
##print(Student_mark(40,50,"dhoni"))

##def Student_mark(eng,math, student_name):
##
##    total= eng + math
##    return
##    print("welcome")
##
##output=(Student_mark(40,50,"dhoni"))
##print(output)

##def Student_mark(eng,math, student_name):
##
##    total= eng + math
##    return total 
##    print("welcome")
##
##output=(Student_mark(40,50,"dhoni"))
##print(output)

##def Student_mark(eng,math, student_name):
##
##    total= eng + math
##    return total,student_name
##    print("welcome")
##
##output=(Student_mark(40,50,"dhoni"))
##print(output)

##def Student_mark(eng,math, student_name):
##
##    total= eng + math
##    return total,student_name
##    print("welcome")
##
##output,output1=(Student_mark(40,50,"dhoni"))
##print(output)
##print(output1)

#Scoping

##var=100 #outside variable(global)
##def fun():
##    var= 10  #local variable
##    print(var)
##print(var)
##fun()
##print(var)

##var=100 #outside variable(global)
##def fun():
##    global var
##    var= 10  #local variable
##    print(var)
##print(var)
##fun()
##print(var)

##counter=0
##def fun():
##    global counter
##    print("hello",counter)
##    counter = counter + 1
##    if counter == 101:
##        return
##    fun()
##fun()

##counter=0
##def fun():
##    global counter
##    print("hello",counter)
##    counter = counter + 1
##    if counter<101:
##        fun()
##fun()

counter=0
def fun():
    global counter
    print("hello",counter)
    counter = counter + 1
    while counter<101:
        fun()
fun()
