##import csv
##
##with open ("python.csv","w") as file_obj:
##
##    file_obj_csv = csv.writer(file_obj)
##
##    file_obj_csv.writerow(["name","age","runs"])
##    file_obj_csv.writerows(["dhoni","33","99"],["a","44","55"])

##import csv
##
##with open ("python.csv","w") as file_obj:
##
##    file_obj_csv = csv.writer(file_obj)
##
##    file_obj_csv.writerow(["name","age","runs"])
##    file_obj_csv.writerows([["dhoni","33","99"],["a","44","55"]])

##import csv
##
##with open ("python.csv","w",newline="") as file_obj:
##
##    file_obj_csv = csv.writer(file_obj)
##
##    file_obj_csv.writerow(["name","age","runs"])
##    file_obj_csv.writerows([["dhoni","33","99"],["a","44","55"]])

##import csv
##
##with open ("python1.csv","w",newline="") as file_obj:
##
##    file_obj_csv = csv.DictWriter(file_obj,["name","age","runs"])   #DictWriter where D & S are capital
##    file_obj_csv.writeheader()
##    file_obj_csv.writerows([{"name":"a","age":44,"runs":44}])

##import csv
##
##with open ("python1.csv","w",newline="") as file_obj:
##
##    file_obj_csv = csv.DictWriter(file_obj,["name","age","score"])
##    file_obj_csv.writeheader()
##    file_obj_csv.writerows([{"name":"a","age":44,",":44}])

##import pandas
##
##my_input = [["name","age","runs"],["dhoni",33,44],["kohli",33,183]]
##my_final_input = pandas.DataFrame (my_input)
##print(my_final_input)

##import pandas
##
##my_input = [["name","age","runs"],["dhoni",33,44],["kohli",33,183]]
##my_final_input = pandas.DataFrame (my_input)
##print(my_final_input)
##
##my_final_input.to_csv("mydata.csv")

#DataFrame(two dimension), Series(single dimension), panles(3 D)

import pandas

my_input = [["name","age","runs"],["dhoni",33,44],["kohli",33,183]]
my_final_input = pandas.DataFrame (my_input)
print(my_final_input)

my_final_input.to_csv("mydata.csv", index=None)
df = pandas.DataFrame(my_input)
df.drop([], axis = 1)
