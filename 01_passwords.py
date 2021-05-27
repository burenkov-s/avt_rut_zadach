#! python3
"""
Программа для хранения паролей
"""
import sys
import os
import getpass
import pyperclip

pw_file = 'C:\\Users\\bWX5325469\\Downloads\\projects\\01_password.txt'
pw_dict = {} #{resource_name:[login, password]}

def add_password(resource_name, pw_dict):
	print('Введите логин:')
	login = input()
	print('Введите пароль:')
	password = getpass.getpass()
	pw_dict[resource_name] = [login, password]
"""
		for element in pw_dict:
		print(element, pw_dict[element], file = filename)


	if os.path.isfile(filename):
		add_pw_file = open(filename, 'a')
	else:
		add_pw_file = open(filename, 'w')
	password = getpass.getpass('Введите пароль:')
	print(entry_id ,resource_name, login, password, file = add_pw_file, sep =':')
	add_pw_file.close()
"""
def get_password(resource_name, pw_dict):
	print("Логин: ", pw_dict[resource_name][0])
	print("Пароль: ", pw_dict[resource_name][1])

"""
	if os.path.isfile(filename):
		if os.stat(filename).st_size == 0:
			print("Файл пуст.")
		else:
			get_pw_file = open(filename, 'r')
			for line in get_pw_file.readlines():
				get_entry_id, get_resource_name, get_login, get_password = line.split(':')
				if login == get_login:
					get_password = get_password.strip()
					print(get_login, get_password)
	else:
		print("Файл отсутствует.")
"""
def delete_password(resource_name, pw_dict):
	try:
		del pw_dict[resource_name]
		print("Запись удалена.")
	except KeyError:
		print("Запись отсутствует.")

def copy_password(resource_name, pw_dict):
	pyperclip.copy(pw_dict[resource_name][1])
	print("Скопирован пароль для логина ", pw_dict[resource_name][0])

def show_passwords(pw_dict):
	for element in pw_dict:
		print(element, pw_dict[element][0], pw_dict[element][1])

def load_passwords(filename):
	if os.path.isfile(filename):
		if os.stat(filename).st_size == 0:
			print("Файл пуст.")
		else:
			load_file = open(filename, 'r')
			for line in load_file.readlines():
#				entry_number, resource_name, login, password = line.split()
				resource_name, login, password = line.split()
				pw_dict[resource_name] = [login, password.strip()]
			load_file.close()
	else:
		print("Файл отсутствует.")
	return (pw_dict)

def write_passwords(pw_dict, filename):
	write_file = open(filename, 'w')
	for element in pw_dict:
		print(element, pw_dict[element][0], pw_dict[element][1], file = write_file)
	write_file.close()


if len(sys.argv) < 2:
	print('Использование: python 01_passwords.py [название ресурса]')
	sys.exit()

resource_name = sys.argv[1]

while True:
	pw_dict = load_passwords(pw_file)
#	print (pw_dict)
	print(	'1. Добавить\n'
			'2. Найти\n'
			'3. Удалить\n'
			'4. Скопировать\n'
			'5. Вывести на экран\n'
			'0. Выход\n')

	menu_choice = input()

	if menu_choice == '1':
		add_password(resource_name, pw_dict)

	if menu_choice == '2':
		get_password(resource_name, pw_dict)

	if menu_choice == '3':
		delete_password(resource_name, pw_dict)

	if menu_choice == '4':
		copy_password(resource_name, pw_dict)

	if menu_choice == '5':
		show_passwords(pw_dict)

	if menu_choice == '0':
		write_passwords(pw_dict, pw_file)
		sys.exit()


	write_passwords(pw_dict, pw_file)
