documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }

def name_owner(num_doc):
  # num_doc = input('Введите номер документа: ')
  for document in documents:
    if document['number'] == num_doc:
      return(document['name'])

def num_shelf(num_doc):
  # num_doc = input('Введите номер документа: ')
  for key, values in directories.items():
    for value in values:
      if value == num_doc:
        return(key)

def full_name():
  for i in documents:
    text_values = ' '.join(list(i.values()))
    print('3)', text_values)

def new_doc(tip, nomer, name):
  # new_document = input('Введите тип документа: ')
  # new_num = input('Введите номер документа: ')
  # new_name = input('Введите имя владельца: ')
  # new_directories = input('Введите номер полки: ')
  # if new_directories in directories.keys():
  #   num_on_shelf = directories.get(new_directories)
  #   num_on_shelf.append(nomer)
    for new in documents:
      if tip not in new["type"] or nomer not in new["number"] or name not in new["name"]:
        documents.append({"type": tip, "number": nomer, "name": name})
        return documents[-1]
    print(documents)
    print(directories)
  # else:
  #   print('Полки с таким номером не существует')

def main():
  while True:
    user_input = input('Введите команду: ')
    if user_input.capitalize() == 'Определи владельца по номеру документа':
      number_doc = name_owner()
      if number_doc == None:
        print('1) Владельца документа с таким номером нет')
      else:
        print('1) Владелец документа с таким номером -', number_doc)
    elif user_input.capitalize()  == 'На какой полке находится документ':
      number_shelf = num_shelf()
      if (number_shelf == None):
        print('2) Такого документа нет')
      else:
        print('2) Данный документ находится на полке -', number_shelf)
    elif user_input.capitalize()  == 'Выведи всех участников':
      full_name()
    elif user_input.capitalize()  == 'Добавь новый документ':
      new_doc()
    elif user_input == '':
      print('Пока')
      break

