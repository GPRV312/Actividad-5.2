# main.py
from menu_module import menu_principal
from otro_modulo import alguna_funcion  # Importar funciones de otro módulo

def main():
    print("Iniciando aplicación...")
    menu_principal()
    # Puedes llamar aquí funciones de otros módulos
    alguna_funcion()

if __name__ == '__main__':
    main()