#work in progress
try:
    from prompt_toolkit import prompt
    from prompt_toolkit.completion import NestedCompleter
    notoolkit = False
except ModuleNotFoundError:
    print('try:')
    print('pip install prompt_toolkit')
    #пока заглушка. в установщик добавлю зависимость
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
                'phones': {phone: None for phone in users[name].phones},
                'notes': None,
                'b_day': None,
                'email': {str(users[name].email) if users[name].email else '0': None},
                'address': None}})

        completer = NestedCompleter.from_nested_dict({
            'hello': None,
            'add_contact': None,
            'add_phone': None,
            'edit': name_dict_ext,
            'search': name_dict,
            'delete_info': name_dict_ext,
            'delete_contact': name_dict,
            'days_to_bday': name_dict,
            'birthday_list': None,
            'show_all': None,
            'exit': None,
            'good_bye': None,
            'close': None,
            })


        return prompt(p, completer=completer)
    else:
        return input(p)