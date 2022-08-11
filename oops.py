class Student(object):
     attr = "stud" #attribute

     def __init__(name,dept,subject):
        name.dept= dept
        name.subject=subject

     def details(name):
        #print('My name is  {}\t'.format(name.dept))
        print("and subject she handles is {}".format(name.subject))

class Topper(Student):

    def details(name):
        print(" {} is class topper in {}".format(name.dept,name.subject)) #polymorphishm
        

class Teacher(Student):  #inheritance
    def __init__(name, dept, subject,teacher):
        name.teacher = teacher

        Student.__init__(name,dept,subject)

    def identify(name):
        print("{} is the Class teacher of {}".format(name.dept,name.teacher))


#obj instant

a=Teacher("Saritha","Electronics","Ramesh")
a.identify()
a.details()

b=Topper("Sumesh","SSD")
b.details()
