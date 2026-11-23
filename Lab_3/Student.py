class Student:
    def __init__(self, name, phone, email, group):
        self.name = name
        self.phone = phone
        self.email = email
        self.group = group

    def __str__(self):
        return (
            f"Student name is {self.name}, "
            f"Phone is {self.phone}, "
            f"Email is {self.email}, "
            f"Group is {self.group}"
        )   