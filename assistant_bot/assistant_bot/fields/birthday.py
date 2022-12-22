from fields.field import *
from datetime import datetime, date, timedelta

class Birthday(Field):

    @Field.value.setter
    def value(self, b_day: str) -> date:
        current_date = datetime.now().date()
        b_day_date = datetime.strptime(b_day, '%d/%m/%Y').date()
        if b_day_date > current_date:
            raise ValueError("You entered date that earlier current date")
        self._value = b_day
