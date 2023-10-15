
def c_tuition(district_code, credits_taken):
    cost_per_credit = 250.00 if district_code == 'I' else 500.00
    return credits_taken * cost_per_credit
  
file_name = "yus.txt"

try:
    with open(file_name, "r") as file:
        lines = file.readlines()
except FileNotFoundError:
    print(f"File {file_name} not found.")
    exit()


total_tuition_owed = 0.0
student_count = 0


for i in range(0, len(lines), 3):
    last_name = lines[i].strip()
    district_code = lines[i + 1].strip()
    credits_taken = int(lines[i + 2].strip())

    
    tuition_owed = c_tuition(district_code, credits_taken)

    
    
    print("lastname", last_name)
    print("credits taken", credits_taken)
    print("tuitionowned", tuition_owed)

    
    total_tuition_owed += tuition_owed
    student_count += 1


print("tto",total_tuition_owed) 
print("Numstudnets", student_count)
      

file.close()

