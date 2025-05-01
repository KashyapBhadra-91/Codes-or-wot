# Modify an element of a tuple.

tuple1 = (1,2,3,4,5,6,7,8,9,10)
list1 = list(tuple1)
list1[0]=0
tuple1=tuple(list1)
print(tuple1)


#Problem1
list1=["shreya",("Jaitin",),("jeel","shreyash"),"krupa"]
boys = sum(len(name) for name in list1 if isinstance(name,tuple))
girls = sum(1 for name in list1 if isinstance(name,str))
print(f"Number of Boys: {boys}\nNumber of Girls: {girls}")



#Problem2

Students = [("354","Prince","18"),("375","Jaitin","20"),("376","Parin","19")]

Roll_No=[student[0] for student in Students]
Names=[student[1] for student in Students]
Ages=[student[2] for student in Students]

print(f"Roll Numbers: {Roll_No}")
print(f"Names: {Names}")
print(f"Ages: {Ages}")



#Problem3
from datetime import date
date1 = (16,2,2024)
date2 = (18,2,2025)
d1=date(date1[2],date1[1],date1[0])
d2=date(date2[2],date2[1],date2[0])
difference= abs((d2-d1).days)
print(f"Days between two Dates: {difference}")




List = [("Ice-Cream",50),("Samosa",20),("Chocolate",10)]
sort = sorted(List, key = lambda List: List[1],reverse = False)
print(sort)


