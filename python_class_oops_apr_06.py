#python is unstructured programming
#python can be made as structured programming if its follows "class" principles
#class is collection of object
#object is real world entity
#class is kind of template or wrapper  to hold things
#object is anything which takes memory
#class is mainly to give the property of inheritance or extensibility

##var="dhoni"
##print(var)
##
##def fun():
##    print("welcome")
##
##fun()

##class my_class:
##
##    var="dhoni"
##
##    def fun():
##        print("welcome")
##        
##print(my_class.var)
##my_class.fun()

##class my_class:
##
##    def var():
##        print("dhoni")
##
##    def fun():
##        print("welcome")
##        
##my_class.var()
##my_class.fun()

##class my_class:
##
##    var="dhoni"
##    var1="kohli"
##
##    def fun():
##        print("welcome")
##        print("to ipl")
##
##print(my_class.var,my_class.var1)
##my_class.fun()

##class my_class:
##
##    var="dhoni"
##    var1="kohli"
##
##    def fun():
##        print("welcome","to ipl")
##
##print(my_class.var,my_class.var1)
##my_class.fun()

##class my_class:
##
##    var="dhoni"
##    var1="kohli"
##
##    def fun():
##        print("welcome")
##        print("to ipl")
##
##print(my_class.var,my_class.var1)
##my_class.fun()

##class my_class:
##
##    var="dhoni"
##    var1="kohli"
##
##    def fun():
##        print("welcome")
##        print("to ipl")
##my=my_class                       #my is called object preference of the"my_class"
##print(my.var,my.var1)
##my.fun()

#class with constructor:

##class my_class:
##
##    def new(name):
##        print("hello")
##        
##    def fun(name,age):
##        print("welcome")
##        
##my=my_class
##my.fun("sonu",33)
##my.new("dhoni")

##class my_class:
##
##    def __init__(mad,name,age):
##        mad.name=name
##        mad.age=age
##
##    def new(mad):
##        print(mad.name)
##        
##    def fun(mad):
##        print(mad.name,mad.age)
##        
##my=my_class("dhoni",33)
##my.fun()
##my.new()

##class my_class:
##
##    def __init__(mad,name,joke):
##        mad.name=name
##        mad.joke=joke
##
##    def new(mad):
##        print(mad.name)
##        
##    def fun(mad):
##        print(mad.name,mad.joke)
##        
##my=my_class("dhoni",33)
##my.fun()
##my.new()

#my_class is called as constructor class
#my is called as object reefrence with single  instant memory(single instant memory)
#my_class() will have one hidden object inside
#whenever you create constructor , an attribute called __init__ is created automatically
#we can use that__init__ if we need to initialize the data inside the class
#attribute or magic method or dunder method is anything that contain double underscore on either  side
#self is similarly to my
#my is the object reference for external class
#self is the object reference for internal class

##class my_class:
##
##    def __init__(mad,name,age):
##
##        mad.name=name
##        mad.age=age
##
##    def new(mad,country):
##        print(mad.name,country)
##        
##    def fun(mad):
##        print(mad.name,mad.age)
##        
##my=my_class("dhoni",33)
##my.fun()
##my.new("india")

##class my_class:
##    'author: mohan s, date april 04 this class is for demo' # this line is called comment string to run this we use my._doc_ function
##
##    def __init__(mad,name,age):
##
##        mad.name=name
##        mad.age=age
##
##    def new(mad,country):
##        print(mad.name,country)
##        
##    def fun(mad):
##        print(mad.name,mad.age)
##        
##my=my_class("dhoni",33)
##print(my.__doc__)
##my.fun()
##my.new("india")

##class my_class:
##
##    def fun(self):
##        print("welcome to python")
##        
##my=my_class()
##my.fun()

##class my_class(object):
##
##    def fun(self):
##        print("welcome to python")
##        
##my=my_class()
##my.fun()

##class my_class(object):
##
##    def __init__(self):
##        print("hello")
##
##    def fun(self):
##        print("welcome to python")
##        
##my=my_class()
##my.fun()

##class my_class(object):
##
##    def __init__(self):
##        print("hello")
##
##    def fun(self):
##        print("welcome to python")
##    def new(self):
##        print("my second fumction")
##    
##my=my_class()
##my.fun()
##my.new()

##class my_class(object):
##
##    def __init__(self):
##        print("hello")
##
##    def fun(self):
##        print("welcome to python")
##    def __new(self):
##        print("my second fumction")
##    
##my=my_class()
##my.fun()
##my.new()

#Access specifier  ---Private,Public

##class my_class:
##
##    def __init__(self,name,age):
##
##        self.name=name
##        self.age=age
##
##    def one(self):
##        print("one",self.name)
##        
##class second_class(my_class):
##    
##    def two(self):
##        print("two",self.name,self.age)
##    
##my=second_class("dhoni",33)
##my.one()
##my.two()

##class my_class:
##
##    def __init__(self,name,age):
##
##        self.name=name
##        self.age=age
##
##    def two(self):
##        print("one",self.name)
##        
##class second_class(my_class):
##    
##    def two(self):
##        print("two",self.name,self.age)
##    
##my=second_class("dhoni",33)
##my.two()

##class my_class:
##
##    def __init__(self,name,age):
##
##        self.name=name
##        self.age=age
##
##    def two(self):
##        print("one",self.name)
##        
##class second_class(my_class):
##    
##    def two(self):
##        print("two",self.name,self.age)
##    
##my=second_class("dhoni",33)
##my.two()
##my_parent = my_class("dhoni",34)
##my.two

#Method resolution order
#Near by search

##class A:
##    def fun(self):
##        print("a")
##class B:
##    def fun(self):
##        print("b")
##class C:
##    def fun(self):
##        print("c")
##class D(B,C):
##    def fun(self):
##        print("d")
##d= D()
##d.fun()

##class A:
##    def fun(self):
##        print("a")
##class B:
##    def fun(self):
##        print("b")
##class C:
##    def fun(self):
##        print("c")
##class D(B,C):
##    pass
####    def fun(self):
####        print("d")
##d= D()
##d.fun()

##class A:
##    def fun(self):
##        print("a")
##class B:
##    def fun(self):
##        print("b")
##class C:
##    def fun(self):
##        print("c")
##class D(C,B):
##    pass
####    def fun(self):
####        print("d")
##d= D()
##d.fun()

##class A:
##    def fun(self):
##        print("a")
##class B:
##    def fun(self):
##        print("b")
##class C:
##    def fun(self):
##        print("c")
##class D(C,B):
##    
####    def fun(self):
####        print("d")
##d= D()
##d.fun()
