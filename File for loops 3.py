
def cbonus(salary):
    if salary >= 100000.00:
        return 0.20 * salary
    elif salary == 50000.00:
        return 0.15 * salary
    else:
        return 0.10 * salary


file_name = "employee.txt"

try:
    with open(file_name, "r") as file:
        lines = file.readlines()
except FileNotFoundError:
    print(f"File {file_name} not found.")
    exit()


total_bonus = 0.0


for i in range(0, len(lines), 2):
    last = lines[i].strip()
    salary = float(lines[i + 1].strip())

    
    bonus = cbonus(salary)
    print()
  
    print("Employee ", last)
    print("Salary ", salary)
    print("Bonus ", bonus)
    total_bonus += bonus
  
print("total bonus ", total_bonus)


file.close()
