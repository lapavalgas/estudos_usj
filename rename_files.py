import os

usj = "usj"
studies = "studies"

i=0

for nome_atual in os.listdir("D:\Workspace\estudos_usj"):

    if os.path.isdir(nome_atual):

        novo_nome = ''
        isValid = False

        if nome_atual[0:7] == "ads_usj":
            novo_nome = f'{nome_atual[8:16]}_{usj}_{nome_atual[17:]}'
            isValid = True
            # print(novo_nome)
        elif nome_atual[0:7] == "studies":
            novo_nome = f'{nome_atual[8:16]}_{studies}_{nome_atual[17:]}'
            isValid = True
            # print(novo_nome)
        else:
            novo_nome = nome_atual
            isValid = False

        path   = os.path.join("D:\Workspace\estudos_usj", nome_atual)
        target = os.path.join("D:\Workspace\estudos_usj", novo_nome)
        print(f'\npath . : {path} \ntarget : {target}\n')

        if isValid:
            
            os.rename(path, target)