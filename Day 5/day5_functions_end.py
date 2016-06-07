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


def parse_lists(abc):
    str_list_items = []
    num_list_items = []
    for i in abc:
        if isinstance(i, float) or isinstance(i, int):
            num_list_items.append(i)
        elif isinstance(i, str):
            str_list_items.append(i)
        else:
            pass
    return str_list_items, num_list_items


print(parse_lists(items))

list_item = [123, 3234, "adfasd"]
items2 = ["Mic", "Phone", list_item]

print(parse_lists(items2))


items3 = ["Mic", "Phone", 323.12, 3123.123, "Justin", "Bag", "Cliff Bars", 134]



sum([123, 323, 423])



def my_sum(my_num_list):
    total = 0
    for i in my_num_list:
        if isinstance(i, float) or isinstance(i, int):
            total += i
    return total

    #if isinstance(i, float) or isinstance(i, int):

def count_nums(my_num_list):
    total = 0
    for i in my_num_list:
        if isinstance(i, float) or isinstance(i, int):
            total += 1
    return total

sum(items3)

my_sum(items3)


def my_avg(my_num_list):
    the_sum = my_sum(my_num_list)
    #num_of_items = len(my_num_list)
    num_of_items = count_nums(my_num_list)
    return the_sum / (num_of_items * 1.0)


my_avg(items3)













