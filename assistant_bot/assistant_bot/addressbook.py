import pickle
from collections import UserDict

from record import *
import saveload as saveload
# from assistant_bot.record import *
# import assistant_bot.saveload as saveload

class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
        self.load_file()

    def add_record(self, record):
        self.data[record.name.value] = record

    def delete_contact(self, name):
        del self.data[name]

    def get_contact(self, name):
        if name in self.data:
            contact_info = []
            phones_list = ', '.join(
                [phone.value for phone in self.data[name].phones])
            contact_info.append(f"Phones: {phones_list}")
            if self.data[name].b_day:
                b_day = self.data[name].b_day.value
                contact_info.append(f"Burned: {b_day}")
            if self.data[name].email:
                contact_info.append(f"Email: {self.data[name].email.value}")
            if self.data[name].notes:
                notes_list = []
                string_tags = ""
                for text, tags in self.data[name].notes.items():
                    if tags:
                        string_tags = ", ".join(tags)
                    notes_list.append(f"{text}, #{string_tags}")
                notes_string = "; ".join(notes_list)
                contact_info.append(f"Notes: {notes_string}")
            if self.data[name].address:
                address_list = self.data[name].address.value
                contact_info.append(f"Lives: {address_list.title()}")

            return f"Contact - {name.capitalize()} have next information: {[item for item in contact_info]}"
        else:
            return f"There is no contacts with this data"

    def find_text(self, text):
        search_list = []
        for key, value in self.data.items():
            if value.notes:
                for note, tags in value.notes.items():
                    if note.find(text) != -1:
                        search_list.append(f"{key.title()}: {note}, #{tags}")
        if len(search_list) > 0:
            return search_list
        else:
            return f"There is no contacts with this data"

    def find_tag(self, tag):
        search_list = []
        for key, value in self.data.items():
            if value.notes:
                for note, tags in value.notes.items():
                    if tag in tags:
                        search_list.append(f"{key.title()}: {note}, #{tags}")
        if len(search_list) > 0:
            return search_list
        else:
            return f"There is no contacts with this data"

    def search_contacts(self, name):
        search_list = []
        for key, value in self.data.items():
            if name in key:
                search_list.append(self.get_contact(key))
            elif name in value.get_info():
                search_list.append(self.get_contact(key))
        if len(search_list) > 0:
            return search_list
        else:
            return f"There is no contacts with this data"

    def iterator(self, count=5):
        contact_list = []
        for contact in self.data.values():
            contact_list.append(contact)
            if len(contact_list) == count:
                yield contact_list
                contact_list = []
        if contact_list:
            yield contact_list

    def save_file(self):
        saveload.save_file(self.data)

    def load_file(self):
        self.data = saveload.load_file()

    def get_bdays(self, timedelta):
        self.list_bdays = {}
        for item in self.data:
            if isinstance(self.data[item].day_to_b_day(), int) and self.data[item].day_to_b_day() <= int(timedelta):
                self.list_bdays.update(
                    {self.data[item].day_to_b_day(): item.capitalize()})
        self.list_bdays = sorted(self.list_bdays.items())
        return self.list_bdays
