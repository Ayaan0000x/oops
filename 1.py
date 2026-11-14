class student:


    def __init__(self,name,age,favsubject):

        student.name=name
        student.age=age
        student.favsubject=favsubject


    def displays(self):


        print(f"my name is{self.name},my age is{self.age}and my fav subject is {self.favsubject}")



object1=student("ayaan",16,"maths")



object1.displays()


object2=student("alex",15,"biology")

object2.displays()
