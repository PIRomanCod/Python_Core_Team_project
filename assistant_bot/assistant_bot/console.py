#work in progress

from prompt_toolkit import prompt
from prompt_toolkit.completion import NestedCompleter
from functions import *


name_dict = dict()
name_dict_ext = dict()
for name in users:
    name_dict.update({name: None})
    name_dict_ext.update({name: { 
		'phones': {'0': None,},
		'notes': None,
		'b_day': None,
		'email': {'0': None},
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


text = prompt('# ', completer=completer)
#print('You said: %s' % text)