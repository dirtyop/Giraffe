employee_file = open("employees2.txt", "w")
if employee_file.readable():
    print(employee_file.read())
employee_file.write("\nKelly - customer service")
employee_file.close()

