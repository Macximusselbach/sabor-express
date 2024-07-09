import os;

lista_restaurantes = [{'nome': 'Res 1', 'categoria': 'Japonês', 'ativo': False},
                      {'nome': 'Res 2', 'categoria': 'Chinês', 'ativo': True}];

def exibir_nome_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      
""");

def exibir_opcoes():
    print('1. Cadastrar restaurante');
    print('2. Listar restaurantes');
    print('3. Alterar estado do restaurante');
    print('4. Sair\n');

def finalizar_app():
    exibir_mensagem(' ');
    print('Finalizando o app\n');

def voltar_menu_principal():
    input('\nAperte uma tecla para retornar ao menu principal. ');
    main();

def exibir_mensagem(mensagem):
    os.system('cls');
    print(mensagem);

def opcao_invalida():
    exibir_mensagem('Opção inválida, por favor selecione novamente! ');
    main();

def cadastrar_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante

    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes

    '''
    exibir_mensagem('Bem vindo ao cadastro de restaurantes!\n');

    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ');
    categoria_restaurante = input(f'Digite a categoria do restaurante {nome_restaurante}: ');
    lista_restaurantes.append({'nome': nome_restaurante, 'categoria': categoria_restaurante, 'ativo': False});

    exibir_mensagem(f'\nO restaurante {nome_restaurante} foi cadastrado com sucesso!');
    voltar_menu_principal();

def listar_restaurantes():
    exibir_mensagem('Listando todos restaurantes!\n');

    print(f'{'Nome do restaurante:'.ljust(22)} | {'Categoria:'.ljust(20)} | Estado:');
    for restaurante in lista_restaurantes:
        estado = 'ativado' if restaurante['ativo'] else 'desativado';
        print(f'- {restaurante['nome'].ljust(20)} | {restaurante['categoria'].ljust(20)} | {estado}');
    
    voltar_menu_principal();

def alternar_estado_restaurante():
    exibir_mensagem('Alternando estado do restaurante!');
    nome_restaurante = input('\nDigite o nome do restaurante que deseja alterar o estado: ');

    restaurante_encontrado = False;
    for restaurante in lista_restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True;
            restaurante['ativo'] = not restaurante['ativo'];
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!';
            exibir_mensagem(mensagem);
    
    if not restaurante_encontrado:
        exibir_mensagem(f'O restaurante {nome_restaurante} não foi encontrado!');
    
    voltar_menu_principal();

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '));

        if opcao_escolhida == 1:
            cadastrar_restaurante();
        elif opcao_escolhida == 2:
            print(listar_restaurantes());
        elif opcao_escolhida == 3:
            print(alternar_estado_restaurante());
        elif opcao_escolhida == 4:
            finalizar_app();
        else:
            exibir_mensagem(' ');
            opcao_invalida();
    except:
        opcao_invalida();

def main():
    exibir_nome_programa();
    exibir_opcoes();
    escolher_opcoes();

if __name__ == '__main__':
    main();