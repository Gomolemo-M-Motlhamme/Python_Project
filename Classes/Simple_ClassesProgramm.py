#output classe
class Output:
    def __init__(self, name, GPA):
        self.name = name
        self.GPA = GPA

    def myMethord(self):
        credit = self.GPA * 10

        print("=============Credit Info===============")
        print("Student name: "+ self.name)
        print("Student's GPA: "+ str(self.GPA))
        print("GPA credit is: "+"R"+ str(credit))
        print("=======================================")

#====================User srceen==================
print("\n")
name = str(input("Enter student name: ")) #get user input

GPA = int(input("Enter student GPA: ")) #get user input
print("\n")

user_Output = Output(name,GPA) #pass user info to function
user_Output.myMethord() #call function
#================================================