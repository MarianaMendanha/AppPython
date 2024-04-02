# Gerenciador de eventos

class AlgumaCoisa:
    def __enter__(self):
        print('Estou entrando')

    def __exit__(self, exc_typr, exc_val, exc_tb):
        print('Estou saindo')


with AlgumaCoisa() as ola:
    print('Estou no meio')
