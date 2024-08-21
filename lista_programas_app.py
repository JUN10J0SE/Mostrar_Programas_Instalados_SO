#orograma que lista os appp nstalados no pc

#biblioteca externa pelo PIP
import winapps

#laco 
for item in winapps.list_installed():
    print(f'Programa: {item.name}.')
    print(f'Versao: {item.version}.')
    print(f'Data da Instalação: {item.install_date}.')
    print(f'Data da Publicação: {item.publisher}.')
    print(f'Local da Desinstalação: {item.uninstall_string}.')
    print('_'*50)

