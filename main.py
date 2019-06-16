class Contact:
    def __init__(self, first_name, second_name, phone_number, favorite_number=False, *args, **kwargs):
        self.first_name = first_name
        self.second_name = second_name
        self.phone_number = phone_number
        self.favorite_number = favorite_number
        self.other_info_args = args
        self.other_info_kwarg = kwargs

    def __str__(self):
        def set_string_favorite_number():
            if self.favorite_number:
                return 'да'
            else:
                return 'нет'

        print(f'Имя: {self.first_name} \n'
              f'Фамилия: {self.second_name}\n'
              f'Телефон: {self.phone_number}\n'
              f'В избранных: {set_string_favorite_number()}\n'
              f'Дополнительная информация: ')
        for item in self.other_info_args:
            print(item)
        for item in self.other_info_kwarg.items():
            print(f'\t{item[0]} : {item[1]}')
        return ''


class PhoneBook(Contact):
    contact_list = []

    def __init__(self, phonebook_name):
        super(Contact, self).__init__()
        self.phonebook_name = phonebook_name

    def add_contact(self, contact):
        self.contact_list.append(contact)

    def get_contacts(self):
        for contact in self.contact_list:
            print(contact)

    def delete_contact(self):
        phone_number = input('Введите номер телефона контакта который хотите удалить: ')
        for contact in self.contact_list:
            if phone_number == contact.phone_number:
                self.contact_list.remove(contact)

    def find_by_first_name_and_second_name(self):
        fist_name = input('Введите имя человека контакт которого хотите найти: ')
        second_name = input('Введите фамилию человека контакт которого хотите найти: ')
        for contact in self.contact_list:
            if fist_name == contact.first_name and second_name == contact.second_name:
                print('Это контакт: ')
                print(contact)

    def get_favorite_numbers(self):
        for contact in self.contact_list:
            if contact.favorite_number:
                print(contact)


def adv_print(*args, **kwarg):
    start = kwarg.get('start', '')
    max_line = kwarg
    in_file = kwarg.get('in_file', False)
    for_print = args
    print(start)
    if len(for_print[0]) >= int(max_line['max_line']):
        print('\n' + for_print[0])
    else:
        print(for_print[0])
    if in_file:
        with open('data/any_data_file.txt', 'a', encoding='utf8') as file:
            file.write(for_print[0])


if __name__ == '__main__':
    jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
    print(jhon)
    serg = Contact('Se', 'Ku', '+700', favorite_number=True, telegram='@SeK', email='Sek@smith.com')
    My_book = PhoneBook("It's my telephone contact_list")
    My_book.add_contact(jhon)
    My_book.add_contact(serg)
    My_book.get_contacts()
    My_book.get_favorite_numbers()
    My_book.delete_contact()
    My_book.get_contacts()
    My_book.find_by_first_name_and_second_name()
    adv_print('any_string', start='qwe', max_line=2, in_file=True)
