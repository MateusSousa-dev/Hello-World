cores = {'invertido':'\33[7m',
         'limpo':'\33[m',
         'vermelho':'\33[7;31m',
         'amarelo':'\33[7;33m',
         'verde':'\33[7;32m',
         'azul':'\33[7;34m'}

for cor in cores:
    print(f'{cores[cor]}Hello World!{cores["limpo"]}')
    print(f'{cores[cor]}Olá Mundo!{cores["limpo"]}')
