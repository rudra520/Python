#4.3.10 SECTION QUIZ
#Question 1: What is the output of the following snippet?
def hi():
    return
    print("Hi!")

hi()


#Question 2: What is the output of the following snippet?
def is_int(data):
    if type(data) == int:
        return True
    elif type(data) == float:
        return False

print(is_int(5))
print(is_int(5.0))
print(is_int("5"))

#Question 3: What is the output of the following snippet?
def even_num_lst(ran):
    lst = []
    for num in range(ran):
        if num % 2 == 0:
            lst.append(num)
    return lst

print(even_num_lst(11))

#Question 4: What is the output of the following snippet?
def list_updater(lst):
    upd_list = []
    for elem in lst:
        elem **= 2
        upd_list.append(elem)
    return upd_list

foo = [1, 2, 3, 4, 5]
print(list_updater(foo))



