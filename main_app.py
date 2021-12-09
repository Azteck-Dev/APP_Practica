from clases.looger_info import log
from clases.DAO import DAOAPP
import sys



def main_menu(menu:str = 'main'):
    """Despliegue de menu principal o secundario.

    Args:
        menu (str, optional): Muestra en pantalla un estilo de menu determinado por el paramatro indicado [main/ update]. Defaults to 'main'.
    """
    match menu:
        case 'main':
            home_menu = [
                'Crear Usuario',
                'Ver usuarios',
                'Actualizar usuario',
                'Eliminar Usuario',
                'Salir'
            ]
            num = 1
            print('\nElije una de las opciones(1-5):\n')
            for opt in home_menu:
                print(f'\t\t{num}.- {opt}')
                num += 1
        case 'update':
            upd_menu = [
                'Actualizar todos los datos.',
                'Actualizar Username.',
                'Actualizar email.',
                'Actualizar password',
                'Salir'
            ]
            print('\nActualizar usuario elija una de las opciones:(1-5) \n')
            num = 1
            for opt in upd_menu:
                print(f'\t\t{num}.- {opt}')
                num += 1
        case _:
            log.error(f"<'{menu}'> no esta definido.")
            sys.exit()

def opt_val(ask: str):
    """Toma la entrada del usuario y determina si es un digito para su conversion a tipo 
    entero.

    Args:
        ask (str): Entrada a validar para su conversion a entero

    Returns:
        [int]: entrada convertida en valor numerico tipo 'int'
    """
    while not ask.isdigit():
        log.warning(f"valor de tipo:{type(ask)} invalido, ingresa valores numericos <class 'int'>")
        ask = input()
    else:
        ask = int(ask)
        return ask

def fmt_pass(pwd: str):
    invalid_words = ['/', '>', '<', '=', '\\', '&', '%', '#', '(', ')']
    while invalid_words:
        if not pwd in invalid_words:
            if len(pwd) > 6:
                return pwd
        else:
            log.warning('Formato de contraseña invalido, vuelve a ingresarla.')
            pwd = input('')

if __name__ == '__main__':

    flag = False

    while not flag:
        main_menu()
        ask = input()
        ask = opt_val(ask)
        #Crear usuario.
        if ask == 1:
            name = input('\nIngresa el nombre de usuario: ')
            email = input('Ingresa el correo electronico: ')
            wordkey = input('Ingresa el password: ')
            fmt_pass(wordkey)
        # Consulta de usuarios.
        elif ask == 2:
            pass
        # Actualizar usuario.
        elif ask == 3:
            pass
        # Eliminar usuario.
        elif ask == 4:
            pass
        # salir
        elif ask == 5:
            flag = True
        else:
            pass
