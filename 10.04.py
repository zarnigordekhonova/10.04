import random
from collections import Counter


# numbers = {}
# for i in range(1, 10+1):
#     numbers[i] = (random.randint(1, 100))
#
# print(numbers)

# 1-masala

def sort_by_values(dict):
    print(sorted(dict.items(), key= lambda item: item[1]))

# sort_by_values({1: 65, 2: 42, 3: 97, 4: 84, 5: 23, 6: 3, 7: 32, 8: 69, 9: 13, 10: 38})


# 2-masala

def update_dic(new_d, d2, d3):
    new_d.update(d2)
    new_d.update(d3)
    print(new_d)

# update_dic({1:10, 2:20}, {3:30, 4:40}, {5:50,6:60})

# 3 - masala

def dict_square(n):
    new_d = {}
    for i in range(1, n+1):
        new_d[i] = i ** 2
    print(new_d)

# dict_square(10)

# 4 - masala
def sum_values(dict_name):
    print(f'Dict ning value lari qiymati {sum(dict_name.values())} ga teng!')

# sum_values({1: 65, 2: 42, 3: 97, 4: 84, 5: 23, 6: 3, 7: 32, 8: 69, 9: 13, 10: 38})


# 5 - masala

def max_values(dict_name):
    print(f'Dict ning value lari ichidagi eng katta son {max(dict_name.values())} ga teng!')

# max_values({1: 65, 2: 42, 3: 97, 4: 84, 5: 23, 6: 3, 7: 32, 8: 69, 9: 13, 10: 38})


# 6 - masala

def min_values(dict_name):
    print(f'Dict ning value lari ichidagi eng kichik son {min(dict_name.values())} ga teng!')

# min_values({1: 65, 2: 42, 3: 97, 4: 84, 5: 23, 6: 3, 7: 32, 8: 69, 9: 13, 10: 38})


# 8 - masala

def unique_values_dict(dict):
    s = set()
    for i in dict:
        for value in i.values():
            s.add(value)
    print(s)

# unique_values_dict([{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}])


# 9 - masala
def count_dict(word):
    for i in word:
        print(i, word.count(i), 'ta')

# count_dict('assalom')

# 10 - masala
def max_letter_dict(word):
    word_count = Counter(word)
    m, count = word_count.most_common(1)[0]
    print(f'Eng kop takrorlangan harf: {m}, {count} marta!')

# max_letter_dict('mexanizasiyalashtirilganmi')

# 11 - masala


















