from clases.cls_users import Users
from clases.DAO import DAOAPP

def main_menu():
    home_menu = ['Crear Usuario', 'Ver usuarios', 'Actualizar usuario', 'Eliminar Usuario', 'Salir']
    num = 1
    for opt in home_menu:
        print(f'{num}.- {opt}')



if __name__ == '__main__':
    main_menu()
