#string,list, tuple and dictionary, numbers
##set and frozen set

#1. Mutable --- list and dictionary --- (you can modify the existing object using number)
#2. Immutable --- string, tuple, numbers

##data = "Netzwerk"
##print(data)
##print(type(data))

##data = 'Netzwerk'
##print(data)

##data = ('Netzwerk')
##print(data)

##data = """Netzwerk"""
##print(data)

##'''Below line is for declaring string data'''

##data = '''this is programming language'''
##print(data)

##data = '''this is programming language
##and i love this'''
##print(data)

##data = "this is programming language \
##and i love this"
##print(data)

name = "dhoni"
age = 30
city = " pune"

##data="my catain plays even at the age of"
##print(data)

##data = "my captain " + name + " plays even at the age of " + age  #this case is applicable if we use age as comment like name otherwise we have to use str you can see it below example
##print(data)

##data = "My captain " +name+ " plays even at the age of " +str(age)
##print(data)

##data = "my captain %s plays even at the age of %d"%(name,age)         # %s stands for numbers or name but %d stands for only numbers
##print(data)

##data = "my captain %s plays even at the age of %d"%(name,name)
##print(data)

##data = "my captain %s plays even at the age of %d"%(age,age)
##print(data)

##data = "my captain {} plays even at the age of {}".format(name,age)
##print(data)

##data = f"my captain plays even at the age of "
##print(data)
