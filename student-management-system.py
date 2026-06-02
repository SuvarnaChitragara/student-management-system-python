students = []
while True:
  print("Choose the opertaion : ")
  print("1.Add Student")
  print("2.View Student")
  print("3.Search Student")
  print("4.Remove Student")
  print("5.Exit")
  choice = int(input())
  if choice == 1:
    n = int(input("Enter number of students: "))
    for i in range(n):
      name = input("Enter name : ")
      marks = int(input("Enter marks : "))
      student = {
          "name" : name,
          "marks" : marks
      }
      students.append(student)
  elif choice == 2:
    for s in students:
      print("Name : ",s["name"] ,",", "Marks : ",s["marks"])
  elif choice == 3:
    name = input("Enter the student name to search : ")
    found = False
    for s in students:
        if s["name"] == name:
            print("Student Found")
            print("Name:", s["name"])
            print("Marks:", s["marks"])
            found = True
            break
    if found == False:
        print("Student not found")
  elif choice == 4:
        name = input("Enter student name to remove: ")
        found = False
        for s in students:
            if s["name"] == name:
                students.remove(s)
                print("Student removed successfully")
                found = True
                break
        if found == False:
            print("Student not found")
  elif choice == 5:
    print("Exiting...")
    break
  else:
    print("Invalid Choice")
