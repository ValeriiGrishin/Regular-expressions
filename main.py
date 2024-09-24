import re
import csv

PATTERN = re.compile(r'(\+7|7|8)?\s?\(?(\d{3})\)?\s?\-?(\d{3})\s?\-?(\d{2})\s?\-?(\d{2})(\s?)\(?(доб.)?\s?(\d*)?\)?')
SUBST_PATTERN = r'+7(\2)\3-\4-\5\6\7\8'

with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
    
# TODO 1: выполните пункты 1-3 ДЗ
#основная функция, выполняющая замену
def main(contact_list: list):
  new_list = list()
  for unit in contact_list:
    full_name = ' '.join(unit[:3]).split(' ')
    result = [full_name[0], full_name[1], full_name[2], unit[3], unit[4], re.sub(PATTERN, SUBST_PATTERN, unit[5]), unit[6]]
    new_list.append(result)    
  return union(new_list)

# функция объединения
def union(contacts: list):
    for contact in contacts:
        last_name = contact[0]
        first_name = contact[1]
        for new_contact in contacts:
            new_last_name = new_contact[0]
            new_first_name = new_contact[1]
            if first_name == new_first_name and last_name == new_last_name:
                if contact[2] == "": contact[2] = new_contact[2]
                if contact[3] == "": contact[3] = new_contact[3]
                if contact[4] == "": contact[4] = new_contact[4]
                if contact[5] == "": contact[5] = new_contact[5]
                if contact[6] == "": contact[6] = new_contact[6]
#убираем задвоение
    result_list = list()
    for i in contacts:
        if i not in result_list:
            result_list.append(i)
    return result_list

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(main(contacts_list))