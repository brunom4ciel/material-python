import sys

def iniciar_app(argv) -> None:
    for value in argv:
        print(value)

if __name__ == '__main__':
    iniciar_app(sys.argv)