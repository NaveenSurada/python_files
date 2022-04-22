##var=[]
##print(dir(var))

##'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

##var={"Friend":"madhu","love":"future"}
##var["Movie"]= "no time to die"            #it adds
##print(var)

##var={"Friend":"madhu","love":"100%"}
##var["Friend"]= "shaad"                    #it replaces
##print(var)

##var=["Friend","madhu","love","future"]
##var.append("movi")                        #in case of append we have to metion in 1st bracket what we want to insert and it's only useable in case of list.
##print(var)

##var=["friend", "madhu","love"]
##var.append('movi')
##print (var)

##var={"Friend":"madhu","love":"future"}
##var.clear()                               #in case of tuple and string it's not going to work
##print(var)

##var={"Friend":"madhu","love":"100%"}
##x=var.copy()                                #in case of tuple and string it's not going to work
##print(x)

##var="Friend madhu love "
##x=var.count("madhu")                        #in case of dictionary and set it's not going to work
##print(x)

##var=["Friend","madhu","love","100%"]
##var.extend("modi")                        #it is applicable only in case of list and this function only takes one value if we need more then we use bracket
##print(var)                                #if we right a word in extend function then it will add alphabets individually but if we want add whole word then we have to write that word in another bracket.
 
##var=["Friend","madhu","love","100%"]
##var.extend(("mo","di"))
##var.extend("di")
##print(var)

##var=["Friend","madhu","love","100%"]      #it's not usable in case of set and dictionary
##x=var.index("love")
##print(x)

##var=["Friend","madhu","love","100%"]
##var.insert(4,"modi")                      # it's only usable in case of list
##var.insert(3,"kgf")
##print(var)

##var=["Friend","madhu","love","100%"]
##x= var.pop(3)
##print(x)

##var=["Friend","madhu","love","100%"]
##x= var.pop(3)
##print(var)

##var={"Friend","madhu","love","100%"}
##x= var.pop()
##y=var.pop()                               #in case of tuple and string it's not usable
##print(var)
##print(x)

##var={"Friend":"madhu","love":"100%"}
##x= var.pop("love")
##print(var)

##var="Friend madhu love 100%"
##var.remove("100%")                        #in case of tuple, string and dictionary it's not usable
##print(var)

##var=["Friend","madhu","love","100%"]
##var.reverse()                               #it's only usable in case of list
##print(var)
##var=["Friend","madhu","love","100%"]
##var.sort()                                 #it's only usable in case of list
##print(var)

##var=["Friend","madhu","love","100%"]
##x=var.sort(reverse=False)
##print(x)

##y=["Friend","madhu","love","100%"]
##for i in y:
##    print(i)

##y=("Friend","madhu","love","100%")
##for i in y:
##    print(i,end=" ")

##y=("Friend","madhu","love","100%")
##for i in enumerate(y):
##    print(i)

##y=("Friend","madhu","love","100%")
##for i in y:
##    print(i)

##var={"Friend":"madhu","love":"future"}
##print(var, end="hehehehe")

##class taxi:
##    def __init__(self, model, capacity, variant):
##        self.__model = model                 #__model is private to taxi class
##        self.__capacity = capacity
##        self.__variant = variant
##
##    def getmodel(self):                     #getmodel()is accessible outside the class
##        return self.__model
##
##    def getcpacity(self):                   #getcapacity() function is accessible to class vehicle
##        return self.__capacity
##
##    def setcapacity(self,capacity):         #setcapacity() is accessible outside the class
##        self.__capacity= capacity
##
##    def getvariant(self):                   #getvariant() function is accessible to class vehicle
##        return self.__variant
##
##    def setvariant(self,variant):           #setvariant() is accessible outside the class
##        self.__variant = variant
##
##class vehicle(taxi):
##
##    def __init__(self, model, capacity, variant, color):
##        # call parent constructor to set model and color
##        super().__init__(model,capacity,variant)
##        self.__color = color
##
##    def vehicleinfo(self):
##        return self.getmodel()+ " " + self.getvariant() + "in" + self.__color + "with" + self.getcapacity() + "seats"
##
###in method getinfo we can call getmodel(),getcapacity() as they are accessible in the child class through inheritence
##
##v1 = vehicle("i20 active" ,"4", "sx", "bronze")
##print(v1.vehicleinfo())
##print(v1.getmodel())                        # vehicle has no method getmodel() but it is accessible via vechile class

##file_obj = open("mad.xls","w")
##file_obj.write("india is my country")
##file_obj.close()

##file_obj = open("mad.csv","w")
##file_obj.write("india is my country")
##file_obj.close()

##file_obj = open("mad.doc","w")
##file_obj.write("india is my country")
##file_obj.close()

##file_obj = open("mad.pdf","a")
##file_obj.write("\n")
##file_obj.write("and i am proud to be indian")
##file_obj.close()

##file_obj = open("mad.xls","a")
##file_obj.write("\n")
##file_obj.write("and i am proud to be indian")
##file_obj.close()

##file_obj = open("mad.xls","a")
##file_obj.write("\n")
##file_content = input("and i am proud to be indian")
##file_obj.write(file_content)
##file_obj.close()

var = "my name is suriya"
output=var.lcenter*
print(output)
