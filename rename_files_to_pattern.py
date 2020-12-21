import os

for nome_atual in os.listdir(".\\"):

    print('\n')

    novo_nome = nome_atual

    if (nome_atual.__contains__('-')):
        novo_nome = novo_nome.replace('-', '')
        novo_nome = novo_nome.replace(' ', '_')
        for i in novo_nome:
            index = novo_nome.index(i)
            if novo_nome[index].isupper() and novo_nome[index+1].islower():
                novo_nome = novo_nome[0:index] + "_" + novo_nome[index:]
        novo_nome = novo_nome.lower()
        novo_nome = novo_nome.replace('__', '_')
        novo_nome = novo_nome
        print(novo_nome)

    if (not nome_atual.__contains__('certificate')):
        path   = os.path.join(".\\", nome_atual)
        target = os.path.join(".\\", novo_nome)
        os.rename(path, target)
        print(f'\npath . : {path} \ntarget : {target}\n')

