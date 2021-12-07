from clases.looger_info import log
import sys



def main_menu(menu:str = 'main'):
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
    while not ask.isdigit():
        log.warning(f'valor de tipo:{type(ask)} invalido, ingresa calores numericos "int" ')
        ask = input()
    else:
        ask = int(ask)
        return ask



if __name__ == '__main__':

    flag = False

    while not flag:
        main_menu()
        ask = input()
        ask = opt_val(ask)

        if ask == 1:
            pass
        elif ask == 2:
            pass
        elif ask == 3:
            pass
        elif ask == 4:
            pass
        elif ask == 5:
            pass
        else:
            pass
