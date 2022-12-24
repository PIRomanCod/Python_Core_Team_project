from fields import *
# from assistant_bot.fields import *

class Record(Field):
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.b_day = None
        self.email = None
        self.notes = {}
        self.address = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def add_note(self, text, hashtag=''):
        self.notes.update({text: hashtag})

    def change_attr(self, attribute, old_value=None, new_value=None):
        if attribute not in ["name", "phones", "b_day", "email", "notes", "address"]:
            raise IndexError("You didn't write an attribute")
        self.attribute = getattr(self, attribute)
        if attribute == "phones":
            for item in self.phones:
                if item.value == old_value:
                    if new_value not in self.phones:
                        item.value = new_value
                        return True
        elif attribute == "notes":
            self.notes[old_value] = new_value
            return True
        elif attribute == "b_day":
            self.b_day = Birthday(new_value)
            return True
        elif attribute == "address":
            self.address = Address(new_value)
            return True
        elif attribute == "email":
            self.email = Email(new_value)
            return True

    def delete_attribute(self, attribute, item=None):
        if attribute == "phones":
            for phone in self.phones:
                if phone.value == item:
                    self.phones.remove(phone)
                    return True
                else:
                    return "Contact hasn't such info"
        elif attribute == "notes":
            try:
                if self.notes:
                    self.notes.pop(item, "There is no such notes")
                # if self.notes:
                #     self.notes.clear()
                    return True
            except KeyError:
                return "There is not such notes"
        elif attribute == "b_day":
            self.b_day = None
            return True
        elif attribute == "address":
            self.address = None
            return True
        elif attribute == "email":
            self.email = None
            return True

    def get_info(self):
        b_day_info = ''
        email_info = ''
        notes_info = ''
        address_info = ''
        phones_info = [phone.value for phone in self.phones]

        if self.b_day:
            b_day_info = f'Burned: {self.b_day.value}'
        if self.email:
            email_info = f'Email: {self.email.value}'
        if self.notes:
            notes_list = []
            string_tags = ""
            for text, tags in self.notes.items():
                if tags:
                    string_tags = ", ".join(tags)
                notes_list.append(f"{text}, #{string_tags}")
            notes_string = "; ".join(notes_list)
            notes_info = f"Notes: {notes_string}"
        if self.address:
            address_info = f'Lives: {self.address.value.capitalize()}'
        return f"Contact - {self.name.value.capitalize()} : phones: {', '.join(phones_info)} {b_day_info} {email_info} {notes_info} {address_info}"

    def day_to_b_day(self):
        if not self.b_day:
            return "The contact's birthday date not defined yet"
        current_date = datetime.now().date()
        b_day_date = datetime.strptime(
            self.b_day.value, '%d/%m/%Y').date()
        new_date_for_b_day = b_day_date.replace(year=current_date.year)

        if new_date_for_b_day < current_date:
            new_date_for_b_day = new_date_for_b_day.replace(
                year=current_date.year + 1)
        return (new_date_for_b_day - current_date).days

    def __str__(self):
        return f'{self.name, self.phones, self.b_day, self.email, self.notes, self.address}'

    def __repr__(self):
        return f'{self.name, self.phones, self.b_day, self.email, self.notes, self.address}'
