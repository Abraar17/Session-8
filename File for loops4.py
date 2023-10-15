
def extprice(quant, price):
    return quant * price


file_name = "orderdata.txt"

try:
    with open(file_name, "r") as file:
        lines = file.readlines()
except FileNotFoundError:
    print(f"File {file_name} not found.")
    exit()

total_extended_price = 0.0
order_count = 0


order_amounts = []


for i in range(0, len(lines), 3):
    item = lines[i].strip()
    quantity = int(lines[i + 1].strip())
    price = float(lines[i + 2].strip())

    
    extended_price = extprice(quantity, price)

    

    print("item" ,item)
    print("quant" , quantity)

    print("Price", price)
    print("extprice", extended_price)
   
    

    
    total_extended_price += extended_price
    order_count += 1

    
    order_amounts.append(extended_price)


print("totalexp", total_extended_price)
print("noo", order_count)

if order_count > 0:
    average_order = total_extended_price / order_count

    print("avo", average_order )


file.close()

