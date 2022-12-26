from addressbook import AddressBook
from input_error import input_error
from record import Record
from exc import NoUserError, NoteExistError
import cleaner


# from assistant_bot.input_error import *
# from assistant_bot.addressbook import *


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
    searching_result = search(new_elem[1])
    if new_elem[1] in searching_result:
        return f"The phone number already exist for contact: '{searching_result.split()[2]}'"
    record = Record(new_elem[0])
    record.add_phone(new_elem[1])
    users.add_record(record)
    return f"You added new contact: {new_elem[0].capitalize()} with phone number: {new_elem[1]}"


def add_phone(string):
    new_elem = string.split()
    if users.data.get(new_elem[0]):
        searching_result = search(new_elem[1])
        if new_elem[1] in searching_result:
            return f"The phone number already exist for contact: '{searching_result.split()[2]}'"
        record = users.data[new_elem[0]]
        record.add_phone(new_elem[1])
        return f"You added contact {new_elem[0]} with number {new_elem[1]}"
    else:
        return "There is no contact with this name"


def add_note(string):
    list_elem = string.split('#')
    hashtag = list_elem[1:]
    hashtag_clear = [item.strip() for item in hashtag]
    new_elem = list_elem[0].split()
    name = new_elem[0]
    text = " ".join(new_elem[1:])
    if users.data.get(name):
        if users.data[name].notes.get(text):
            raise NoteExistError
        record = users.data[name]
        record.add_note(text, hashtag_clear)
        users.add_record(record)
        return f"Note: '{text}' with tag: {hashtag_clear} added to contact {name.title()}."
    else:
        return "There is no contact with this name."


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
    if record.delete_attribute(new_elem[1], (" ").join(new_elem[2:])) is True:
        return f"For contact {new_elem[0]} attribute: {new_elem[1]} was deleted"
    else:
        return "Attribute doesn't exist"


def find_tag(string):
    new_elem = string.split()
    if new_elem[0]:
        string_result = ""
        result = users.find_tag(new_elem[0])
        if type(result) == list:
            string_result = "\n".join(result)
        else:
            string_result = result
        return string_result
    else:
        return "The command need more args"


def find_text(string):
    if string:
        string_result = ""
        result = users.find_text(string)
        if type(result) == list:
            string_result = "\n".join(result)
        else:
            string_result = result
        return string_result
    else:
        return "The command need more args"


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


def days_to_birthday(string):
    new_elem = string.split()
    record = users[new_elem[0]]
    return f" Contact {string} has {record.day_to_birthday()} till his Birthday"


def birthday_list(timedelta):
    after = []
    for i in users.get_birthdays(timedelta):
        a, b = i
        after.append(str(a) + " days till " + b + "'s Birthday")
    return '\n'.join(after)


def sort_files(string):
    cleaner.start(string)
    return f" Files in {string} have been sorted"


def stop():
    return "Good bye!"


def manual():
    return '''Please enter one of the commands:
    >>hello,
    >>add_contact 'name' 'number (3 operator and 7 numbers digit)',
    >>add_phone 'name' 'number (3 operator and 7 numbers digit)',
    >>add_note: 'name'(or 'unnamed') 'the note text' '#hashtag' '#hashtag'...
    >>search 'name' or 'part of info',
    >>edit 'name' 'phones' 'old_value, if not defined = 0' 'new_value', 
                  'note' 'start with.. - change if only one match found'  '->' 'new text' (hashtag stay the same)
                  'birthday' 'old_value, if not defined = 0' 'new_value',
                  'email' 'old_value, if not defined = 0' 'new_value',
                  'address' 'old_value, if not defined = 0' 'new_value'   
    >>delete_info 'name' 'phones' 'value',
                         'note' 'start with..' - delete if only one match found
                         'notes' 'all'  - delete all notes
                         'birthday' 'value'
                         'email' 'value',
                         'address' 'value',  
    >>delete_contact 'name',
    >>days_to_birthday 'name',
    >>find_tag 'tag'
    >>find_text 'text'
    >>birthday_list 'period days',
    >>show_all",
    >>sort, 'path to folder' (full path to folder which needs to be sorted),
    >>exit, >>good_bye, >>close
    '''


commands_dict = {"hello": hello,
                 "help": manual,
                 "add_contact": add,
                 "add_phone": add_phone,
                 "add_note": add_note,
                 "edit": change_attr,
                 "search": search,
                 "delete_info": delete_attribute,
                 "delete_contact": delete_contact,
                 "days_to_birthday": days_to_birthday,
                 "find_tag": find_tag,
                 "find_text": find_text,
                 "birthday_list": birthday_list,
                 "show_all": show_all,
                 "sort": sort_files,
                 "exit": stop}

users = AddressBook()
