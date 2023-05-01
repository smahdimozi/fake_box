#first  i want to take number of box in archive
# afer that i want to write a def count for us the time that each name is exist in list that filled by people

#### give number from sina
archive_num = int(input())

#### def for wirte list of dead people
people_fill = []

def list_fillbox(countinu = 'y', *arg, **kwarg):
    
    while countinu == 'y':
        people_fill.append(input())
        duplicate_people_fill = list(dict.fromkeys(nima_list))
        countinu = input(f'do you want keep input?')
    return people_fill, duplicate_people_fill

#### finde the duplitcate name
duplicate_people_fill = list_fillbox()[1]

#### counter time of name
number_of_repetetive_name = {}
def counter_repetetive_name(list1=[], list2=[]):
    for i in list1:
        name = i
        number_of_repetetive_name[name] = list2.count(i)
    return number_of_repetetive_name

people_repeats = counter_repetetive_name(duplicate_nima_list, people_fill)

#### finde the fake grave
for i in list(people_num.keys()) :
    if people_repeats[i] == 1:
        fake_box = i
        break
    elif people_repeats[i] % 2 == 1:
        fake_box = i
        break
