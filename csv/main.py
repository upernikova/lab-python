import random
import csv
from transliterate import translit
import time

txt_file_path = "fio.txt"
with open(txt_file_path, "r", encoding='utf-8') as txt_file:
    lines = txt_file.readlines()

faculty = input("Введите факультет: ")
admission_year = input("Введите год поступления: ")
group = input("Введите группу: ")
course = input("Введите курс: ")

csv_list = []
start_time = time.time()


for line in lines:
    full_name = line.strip()
    last_name, first_name, middle_name = full_name.split(maxsplit=2)
    username = f"{first_name[0]}{last_name}{admission_year}"
    password = random.randint(1000, 9999)
    username_english = translit(last_name, 'ru', reversed=True)
    faculty_english = translit(faculty, 'ru', reversed=True)
    email = f"{username_english}.{faculty_english}@Gmail.com"
    csv_list.append([last_name, first_name, middle_name, password, email, "Гомель", 0, faculty, group + " " + admission_year, course])

csv_file_path = "fio_students.csv"
with open(csv_file_path, "w", newline="", encoding='utf-8-sig') as csv_file:
    writer = csv.writer(csv_file, delimiter=";")
    writer.writerow(["Фамилия", "Имя", "Отчество", "Пароль", "Email", "Город", "maildisplay", "Факультет", "Группа", "Курс"])
    writer.writerows(csv_list)

print(f"CSV файл успешно создан: {csv_file_path}")

end_time = time.time()
print(f"Время работы программы: {end_time - start_time} ")