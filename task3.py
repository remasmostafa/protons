class MagicalContact:
    def __init__(self, name, email, phone_number):
        self.__name = name
        self.__email = email
        self.__phone_number = phone_number

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_phone_number(self):
        return self.__phone_number

    def set_email(self, email):
        self.__email = email

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def describe(self):
        print(f"Name: {self.__name}, {self.__email}, Phone: {self.__phone_number}")


class WizardorWitch(MagicalContact):
    VALID_HOUSES = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    def __init__(self, name, email, phone_number, wand, house):
        super().__init__(name, email, phone_number)

        if house not in WizardorWitch.VALID_HOUSES:
            raise ValueError(f"Invalid house: {house}. Must be one of {WizardorWitch.VALID_HOUSES}")

        self.__wand = wand  # dict: {"length": "11 inches", "wood": "Holly", "core": "phoenix feather"}
        self.__house = house

    def get_wand(self):
        return f"{self.__wand['length']}, {self.__wand['wood']}, {self.__wand['core']}"

    def get_house(self):
        return self.__house

    def describe(self):
        print(
            f"Name: {self.get_name()}, {self.get_email()}, Phone: {self.get_phone_number()} | "
            f"Wand: {self.get_wand()} | House: {self.__house}"
        )


class MagicalCreature(MagicalContact):
    def __init__(self, name, email, phone_number, species, is_tame):
        super().__init__(name, email, phone_number)
        self.__species = species
        self.__is_tame = is_tame

    def get_species(self):
        return self.__species

    def is_tame(self):
        return self.__is_tame

    def describe(self):
        tame_status = "Tame" if self.__is_tame else "Wild"
        print(
            f"Name: {self.get_name()}, {self.get_email()}, Phone: {self.get_phone_number()} | "
            f"Species: {self.__species}, Status: {tame_status}"
        )

class MagicalContactBook:
    def __init__(self):
        self.__contacts = []

    def add_contact(self, contact):
        if isinstance(contact, MagicalContact):
            self.__contacts.append(contact)
        else:
            raise TypeError("Only MagicalContact objects can be added.")

    def list_contacts(self):
        for contact in self.__contacts:
            contact.describe()

    def find_contact(self, name):
        for contact in self.__contacts:
            if contact.get_name().lower() == name.lower():
                contact.describe()
                return
        print(f"Contact '{name}' not found.")
