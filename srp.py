"""
Single responsability Principle
One class must be implemented with only one
reason
"""
# Maneira correta
class User:
    def __init__(self, name: str):
        self.name = name

    def get_name(self):
        pass


class UserDB:
    def get_user(self, id) -> User:
        pass

    def save(self, user: User):
        pass




# Maneira errada
class UserAcoplado:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        pass

    def save(self, user=User):
        pass
