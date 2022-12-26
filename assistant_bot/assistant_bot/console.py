try:
    from prompt_toolkit import prompt
    from prompt_toolkit.completion import NestedCompleter
    notoolkit = False
except ModuleNotFoundError:
    print('try:')
    print('pip install prompt_toolkit')
    #добавил зависимость в setup.py
    notoolkit = True
    
from functions import *

def get_input(p):
#взял команды из текущего хелпа. нужно будет тут модифицировать при изменених

    if not notoolkit:
        name_dict = dict()
        name_dict_ext = dict()
        for name in users:
            name_dict.update({name: None})
            name_dict_ext.update({name: { 
                'phones': {str(phone): None for phone in users[name].phones},
                'note': None,
                'notes': {'all': None},
                'birthday': None,
                'email': {str(users[name].email) if users[name].email else '0': None},
                'address': None}})

        completer = NestedCompleter.from_nested_dict({
            'help': None,
            'add_contact': None,
            'add_phone': name_dict,
            'add_note': name_dict,
            'edit': name_dict_ext,
            'search': name_dict,
            'delete_info': name_dict_ext,
            'delete_contact': name_dict,
            'days_to_birthday': name_dict,
            'find_tag': None,
            'find_text': None,
            'birthday_list': None,
            'show_all': None,
            'sort': None,
            'exit': None,
            'good_bye': None,
            'close': None,
            })


        return prompt(p, completer=completer)
    else:
        return input(p)