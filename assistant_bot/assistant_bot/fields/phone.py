from fields.field import *
from exc import VerificationError

# from assistant_bot.fields.field import *
# from assistant_bot.exc import VerificationError

class Phone(Field):
    @Field.value.setter
    def value(self, phone):
        if phone.isdigit() and len(phone) == 10:
            self._value = phone
        else:
            raise VerificationError
