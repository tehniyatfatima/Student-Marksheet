  #marksheet
name=input("enter your name")
f_name=input("enter your father name")
roll_no=int(input("enter your roll no "))
isl=int(input("enter your islamiat marks"))
english=int(input("enter your english marks"))
ict=int(input("enter your ict marks"))
pf=int(input("enter your maths marks"))
physics=int(input("enter your physics marks"))
calculus=int(input("enter your calulus marks"))
total=(isl+english+ict+pf+physics+calculus)
per=(total/600)*100


print("-------STUDENT MARK SHEET--------")
print("student name",name)
print("student's father name",f_name)
print("student roll no is",roll_no)
print("total marks out of 600 are",total)
print("percentage of student is",per)
if per>=80:
     print(" student Grade A-ONE")
elif per>=70:
     print(" student Grade A")
elif per>=60:
     print(" student Grade B")
elif per>=50:
     print(" student grade C")
elif per>=40:
     print(" student grade D")
else:
    print("FAIL")

input("press enter for close program")
