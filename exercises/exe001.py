from passlib.hash import pbkdf2_sha256 as cryp


class User:

    def __init__(self, name, last_name, email, password):
        self.__name = name
        self.__last_name = last_name
        self.__email = email
        self.__password = cryp.hash(password, rounds=200000, salt_size=16)

    @property
    def name(self):
        return self.__name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def email(self):
        return self.__email

    @property
    def password(self):
        return self.__password

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @last_name.setter
    def last_name(self, new_last_name):
        self.__last_name = new_last_name

    @email.setter
    def email(self, new_email):
        self.__email = new_email

    @password.setter
    def password(self, new_password):
        self.__password = cryp.hash(new_password, rounds=200000, salt_size=16)

    def check_password(self, password):
        if cryp.verify(password, self.password):
            return True
        return False


name = str(input('Seu primeiro nome: '))
last_name = str(input('Seu sobrenome: '))
email = str(input('E-mail: '))
password = str(input('Senha: '))

user1 = User(name, last_name, email, password)
print('Usuário criado com sucesso!')

password = str(input('Senha: '))

if user1.check_password(password):
    print('Acesso permitido')

# print(f'Senha criptografada: {user1._User__password}')
