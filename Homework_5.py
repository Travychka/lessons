#1
#my_str = "What is your name?"

#a
#print(my_str[2])

#b
#print(my_str[-2])

#c
#print(my_str[ : 5])

#d
#print(my_str[ : -2])

#e
#print(my_str[ : : 2])

#f
#print(my_str[1: : 2])

#g
#print(my_str[ : :-1])

#h
#print(my_str[ : :-2])

#i
#print(len(my_str))

#2
#my_str_2 = "You set your own mood"
#space = my_str_2.count(" ")
#words = space + 1
#print(words)

#3
#не зрозуміла яке має бути дано

#4



my_str_4 = "hello! help yourself so you can help others. you are a hero."

h_ind_first = my_str_4.find("h")
h_ind_last = my_str_4.rfind("h")

#або порахувати
#h_ind_all = my_str_4.count("h")

print(h_ind_first)
print(h_ind_last)
#print(h_ind_all)

# або написати підняти всі h і тільки перший і останній знову поміняти на маленькі.

# Або можна зробити через вайл луп. Шукає індекс h, якщо знайшло то шукає дальше
# індекс вказуємо попередній +1 звідки шукати наступну h , і так поки буде, якщо не буде то там елс і виходить брейк
#