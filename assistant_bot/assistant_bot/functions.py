from assistant_bot.input_error import *
from assistant_bot.addressbook import *


def parser(user_input):
    parsed_input = user_input.lower().strip().split()
    return handler(parsed_input)


@input_error
def handler(parsed_input):
    if parsed_input[0] in commands_dict:
        if len(parsed_input) == 1:
            action = commands_dict.get(parsed_input[0])()
        else:
            action = commands_dict.get(parsed_input[0])(
                (" ").join(parsed_input[1:]))
    else:
        raise KeyError
    return action


def hello():
    return f"How can I help you? Enter: 'help' for manual"


def add(string):
    new_elem = string.split()
    if users.data.get(new_elem[0]):
        return "Contact already exist"

    record = Record(new_elem[0])
    record.add_phone(new_elem[1])
    users.add_record(record)
    return f"You added new contact: {new_elem[0]} with phone number: {new_elem[1]}"


def add_phone(string):
    new_elem = string.split()
    if users.data.get(new_elem[0]):
        record = users.data[new_elem[0]]
        record.add_phone(new_elem[1])
        return f"You added contact {new_elem[0]} with number {new_elem[1]}"
    else:
        return "There is no contact with this name"


def change_attr(string):
    new_elem = string.split()
    if new_elem[0] not in users.data:
        raise NoUserError
    else:
        record = users.data[new_elem[0]]
        if record.change_attr(new_elem[1], new_elem[2], (" ").join(new_elem[3:])) is True:
            return f"You changed for contact {new_elem[0].capitalize()} attribute {new_elem[1]} from {new_elem[2]} to {(' ').join(new_elem[3:])}"
        else:
            return "Attribute doesn't exist"


def delete_attribute(string):
    new_elem = string.split()
    record = users.data[new_elem[0]]
    if record.delete_attribute(new_elem[1], new_elem[2]) is True:
        return f"For contact {new_elem[0]} attribute: {new_elem[1]} was deleted"
    else:
        return "Attribute doesn't exist"


def search(string):
    new_elem = string.split()
    result = users.search_contacts(new_elem[0])
    if type(result) == list:
        result = '\n'.join(result)
    return result


def show_all():
    if not users.data:
        return "AddressBook is empty"
    result = [record.get_info() for page in users.iterator()
              for record in page]
    return '\n'.join(result)


def delete_contact(string):
    new_elem = string.split()
    users.delete_contact(new_elem[0])
    return f"You delete contact {new_elem[0]}"


def days_to_bday(string):
    new_elem = string.split()
    record = users[new_elem[0]]
    return f" Contact {string} has {record.day_to_b_day()} till his Birthday"


def birthday_list(timedelta):
    after = []
    for i in users.get_bdays(timedelta):
        a, b = i
        after.append(str(a) + " days till " + b + "'s Birthday")
    return '\n'.join(after)


def stop():
    return "Good bye!"


def manual():
    return '''Please enter one of the commands:
    >>hello,
    >>add_contact 'name' 'number (3 operator and 7 numbers digit)',
    >>add_phone 'name' 'number (3 operator and 7 numbers digit)',
    >>edit 'name' 'attribute (one of: phones, notes, b_day, email, address)' 'old_value, if not defined = 0' 'new_value', for notes: 'hashtag' 'notes text',
    >>search 'name' or 'part of info',
    >>delete_info 'name' 'attribute (one of: phones, notes, b_day, email, address)' 'value',
    >>delete_contact 'name',
    >>days_to_bday 'name',
    >>birthday_list 'period days',
    >>show_all",
    >>exit, >>good_bye, >>close
    '''


commands_dict = {"hello": hello,
                 "help": manual,
                 "add_contact": add,
                 "add_phone": add_phone,
                 "edit": change_attr,
                 "search": search,
                 "delete_info": delete_attribute,
                 "delete_contact": delete_contact,
                 "days_to_bday": days_to_bday,
                 "birthday_list": birthday_list,
                 "show_all": show_all,
                 "exit": stop}

users = AddressBook()
