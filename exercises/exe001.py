from passlib.hash import pbkdf2_sha256 as cryp


class User:

    def __init__(self, name: str, last_name: str, email: str, password: str) -> None:
        self.__name: str = name
        self.__last_name: str = last_name
        self.__email: str = email
        self.__password: str = cryp.hash(password, rounds=200000, salt_size=16)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        self.__name = new_name

    @property
    def last_name(self) -> str:
        return self.__last_name

    @last_name.setter
    def last_name(self, new_last_name: str) -> None:
        self.__last_name = new_last_name

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, new_email: str) -> None:
        self.__email = new_email

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, new_password: str) -> None:
        self.__password = cryp.hash(new_password, rounds=200000, salt_size=16)

    def check_password(self, password: str) -> bool:
        if cryp.verify(password, self.password):
            return True
        return False


nome: str = input('Seu primeiro nome: ')
sobrenome: str = input('Seu sobrenome: ')
e_mail: str = input('E-mail: ')
senha: str = input('Senha: ')

user1: User = User(nome, sobrenome, e_mail, senha)
print('Usuário criado com sucesso!')

senha = input('Senha: ')

if user1.check_password(senha):
    print('Acesso permitido')

# print(f'Senha criptografada: {user1._User__password}')
