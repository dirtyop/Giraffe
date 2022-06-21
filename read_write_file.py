employee_file = open("employees1.txt", "w")
if employee_file.readable():
    print(employee_file.read())
employee_file.write("\nKelly - customer service")
employee_file.close()

