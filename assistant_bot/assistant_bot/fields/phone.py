from fields.field import *

class Phone(Field):
    @Field.value.setter
    def value(self, phone):
        if phone.isdigit() and len(phone) == 10:
            self._value = phone
        else:
            raise VerificationError
