# Напишите программу, которая получает на вход
# название книги, фамилию автора и год выпуска.
# Полученные данные должны быть преобразованы в словарь
# и в таком представлении выведены в консоль.

# Mine didn't pass the test

book_input = list(input("Enter book credentials: ").split())
book_dict = {
    'name': book_input[0],
    'author': book_input[1],
    'published': book_input[2],
}
print(book_dict)

# Expected solution

# title = input("Введите название книги:")
# author = input("Введите фамилию автора:")
# year = int(input("Введите год издания:"))
#
# book = {'title': title,
#         'author': author,
#         'year': year}
#
# print(book)
