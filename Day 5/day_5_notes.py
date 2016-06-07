items = ["Microphone",  "Phone", 5502.22, "Camera", 312.33, "Cliff Bars", 423.00, "Climbing Shoes", 132, "Laptop", "Rope"]

str_items = []
int_items = []

# same list

# a-z 
str_items.sort(key=str.lower)

# z-a
str_items.sort(key=str.lower, reverse=True)


# Smallest - Largest
int_items.sort()

# Largest - Smallest
int_items.sort(reverse = True)



#To not modify the current list, use "sorted"
new_list = sorted(str_items, reverse=True)

numbers = [13, 123, 333, 423, 2341]

total = sum(numbers)
average = total/len(numbers) #rounded
average_abs = total/(len(numbers) * 1.0)
average_abs_2 = sum(numbers)/float(len(numbers))




