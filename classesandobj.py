class students:
    def __init__(self, name, usn, percentage):
        self.name = name
        self.usn = usn
        self.percentage = percentage

    def marks(self):
        return int(self.percentage)

    def details(self):
        print("name: " + self.name + " Usn: " +
              self.usn + " Percentage: " + self.percentage)


l = []
totalm = 0
for i in range(3):
    print("Name , Usn , Percentage")
    [name, usn, percentage] = [x for x in input("").split(" ")]
    student = students(name, usn, percentage)
    lmarks1 = student.marks()
    if(lmarks1 > totalm):
        totalm = lmarks1
        reqstudent = student
reqstudent.details()
