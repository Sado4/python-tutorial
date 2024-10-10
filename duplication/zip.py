# zip
# zipとは、2つのリストをペアにして、タプルのリストを作成することができる関数

my_list = [1, 2, 3, 4, 5]
my_list2 = [6, 7, 8, 9, 10]

for i, value in zip(my_list, my_list2):
    print(i, value)
