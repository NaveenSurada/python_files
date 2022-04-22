##var = {}
##print (var)
##print(type(var))
      
##var={"dhoni",33}
##print(var)
##print(type(var))

##var = {"name": "dhoni", "age":33}
##print(var)
##print(type(var))
      
##var={"name":"dhoni","age":33}
##print(var[0]) #no index based direct data retrieval in dictionary

#in dictionary datas are manipulated or used via key
#dictionary is called key value pair because each data we use needs to be stored with specific key
#storing data with key is generally called as "Hashing" or "Hashtable"

##var={"name":"dhoni","age":33}
##print(var["age"])

##var={"name":"dhoni","age":33}
##var["name"]="kohli"
##print(var)

#dictionary is mutable type

##var={"name":"dhoni","age":33,"name":"arjun"}
##print(var)

#keys are unique
#dictionary is called as "unordered collection"

##var={"name":"dhoni",9:33,98.9:"arjun",("a","B"):"veena",True:"rahul"}
##var["name"]="kohli"
##print(var)

##var={"name":"dhoni"}
##var["country"]="india"
##print (var)

##var={"name":"dhoni","team":"csk"}
##output = var["team"]
##print(output)

##var={"name":"dhoni","team":"csk"}
##var1={"age":33}
##output = var + var1
##print(output)

##var={"name":"dhoni","team":"csk"}
##var1={"age":33}
##var2={"lang":"eng"}
##output={**var,**var1,**var2}
##print(output)

##var ={"name":["dhoni","kohli"],"team":("csk","rcb"),"sports":{"cricket":["sachin","dravid"]}}
##print(var)

##var ={"name":["dhoni","kohli"],"team":("csk","rcb"),"sports":{"cricket":["sachin","dravid"]}}
##output= var["team"] [1]
##print(output)

##var ={"name":["dhoni","kohli"],"team":("csk","rcb"),"sports":{"cricket":["sachin","dravid"]}}
##var["name"][1]= "rohit"
##print(var)

##var ={"name":["dhoni","kohli"],"team":("csk","rcb"),"sports":{"cricket":["sachin","dravid"]}}
##output= var["country"]
##print(output)
##print("welcome")

##var ={"name":["dhoni","kohli"],"team":("csk","rcb"),"sports":{"cricket":["sachin","dravid"]}}
##output= var.get("country",)
##print(output)
##print("welcome")

var ={"name":["dhoni","kohli"],"team":("csk","rcb"),"sports":{"cricket":["sachin","dravid"]}}
output= var.get("country","sorry key not found")
print(output)
print("welcome")

