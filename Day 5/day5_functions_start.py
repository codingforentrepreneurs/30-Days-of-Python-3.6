items = ["Mic", "Phone", 323.12, 3123.123, "Justin", "Bag", "Cliff Bars", 134]

str_items = []
num_items = []


for i in items:
    if isinstance(i, float) or isinstance(i, int):
        num_items.append(i)
    elif isinstance(i, str):
        str_items.append(i)
    else:
        pass


print(str_items)

print(num_items)