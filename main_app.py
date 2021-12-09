from clases.cls_users import Users
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
    """Validacion del password ingresado, para que cumpla con los requerimientos predefinidos

    Args:
        pwd (str): password ingresada por el usuario

    Returns:
        str: password que cumple con el formato predefinido.
    """
    invalid_words = ['/', '>', '<', '=', '\\', '&', '%', '#', '(', ')', ' ']
    pwd_ok = ''
    while not pwd_ok:
        for char in pwd:
            if not char in invalid_words and len(pwd) >= 6:
                pwd_ok = pwd
                break
            else:
                if len(pwd) < 6:
                    log.warning('La contraseña debe ser de una longitud minima de 6 caracteres.')
                for char in pwd:
                    if char in invalid_words:
                        log.warning(f'La contraseña no debe incluir caracteres especiales {invalid_words} ni espacios en blanco.')
                pwd = input('Ingresa una contraseña valida: ')
    return pwd_ok

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
            wordkey = fmt_pass(input('Ingresa el password: '))
            user = Users(user_name=name, email=email, password=wordkey)
            row = DAOAPP.mk_reg(user)
            print(f'Se ingreso correctamente: {row} registro')

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
