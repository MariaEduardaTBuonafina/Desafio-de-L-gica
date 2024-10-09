'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
opc = 0 # variavel que armazena a opçao do usuario
contador_paciente = 0 # variavel que conta quantos pacientes foram cadastrados

qtd_abaixo = 0 # armazena a quantdade de pacientes abaixo do peso
qtd_normal = 0 # armazena a quantdade de pacientes com o peso normal
qtd_sobrepeso = 0 # # armazena a quantdade de pacientes com sobrepeso
qtd_ob1 = 0 # armazena a quantdade de pacientes com obesidade I 
qtd_ob2 = 0 # armazena a quantdade de pacientes com obesidade II 
qtd_ob3 = 0 # armazena a quantdade de pacientes com obesidade III

imc_total = 0 # armazena a soma dos IMC's para poder calcular a média depois

while (opc != 3): # enquanto a opçao do usuario for diferente de 3, execute:
    opc = int(input(''' ---===<<< MENU >>>===--- 
    (1) Cadastrar paciente
    (2) Exibção geral
    (3) Sair
    
    Digite a sua opção: '''))
    
    if opc == 1: # se a opcao do usuario for igual a 1: cadastre o paciente 
        print("---===<<< CADASTRAR PACIENTE >>>===---") 
        nome = input("Informe o nome do paciente: ") # pega o nome do paciente
        peso = float(input("Informe o peso do paciente: ")) # pega o peso do paciente em forma decimal
        altura = float(input("Informe a altura do paciente: ")) # pega a altura do paciente em forma decimal
        imc = peso / altura**2 # calcula o IMC e salva o valor na variavel IMC
        
        if imc < 18.5: # classifica o IMC do paciente
            print("O paciente está abaixo do peso!")
            qtd_abaixo+=1 # se o paciente estiver abaixo do peso, "+1" é adicionado na variavel
            
        elif (imc >= 18.5) and (imc < 25): # classifica o IMC do paciente
            print("O paciente está com o peso normal!")
            qtd_normal+=1 # se o paciente estiver com o peso normal, "+1" é adicionado na variavel
            
        elif (imc >= 25) and (imc < 30): # classifica o IMC do paciente
            print("O paciente está com sobrepeso!")
            qtd_sobrepeso+=1 # se o paciente estiver com sobrepeso, "+1" é adicionado na variavel
            
        elif (imc >= 30) and (imc < 35): # classifica o IMC do paciente
            print("O paciente está com obesidade grau I!")
            qtd_ob1+=1 # se o paciente estiver com obesidade I, "+1" é adicionado na variavel
            
        elif (imc >= 35) and (imc < 40): # classifica o IMC do paciente
            print("O paciente está com obesidade grau II!")
            qtd_ob2+=1 # se o paciente estiver com obesidade II, "+1" é adicionado na variavel
            
        else:
            print("Obesidade Grau III (Mórbida)!") # classifica o IMC do paciente
            qtd_ob3+=1 # se o paciente estiver com obesidade III, "+1" é adicionado na variavel
        
        contador_paciente+=1 # toda vez que um paciente for cadastrado, "+1" é somado na variavel
        imc_total += imc # vai somando todos os IMC's dos pacientes e armazenando na variável
    
    elif opc == 2: # se o usuario escolher a opcao 2
        print("---===<<< EXIBIR >>>===---")
        print(f'Quantidade total dos pacientes: {contador_paciente}') # exibe a quantidade total de pacientes cadastrados
        
        media_geral = imc_total / contador_paciente # calcula a média geral de todos os IMC's cadastrados
        print(f'Média geral do IMC: {media_geral}') # exibe a media geral dos IMC's
        
        # aqui é exibido a quantidade total de quantos pacientes foram classificados abaixo:
        print(f'Quantidade de pacientes abaixo do peso: {qtd_abaixo}')
        print(f'Quantidade de pacientes com o peso normal: {qtd_normal}')
        print(f'Quantidade de pacientes com sobrepeso: {qtd_sobrepeso}')
        print(f'Quantidade de pacientes com obesidade grau I: {qtd_ob1}')
        print(f'Quantidade de pacientes com obesidade grau II: {qtd_ob2}')
        print(f'Quantidade de pacientes com obesidade grau III: {qtd_ob3}')
    
    elif opc == 3: # se o usuario escolher a opcao 3:
        print("Saindo do sistema...") # exibe uma mensagem para avisá-lo que o sistema ta sendo fechado
        break; # quebra o while
        
    else: # se o usuario digitar algum numero que nao esteja entre 1 e 3 (inclusos):
        print("Opção inválida! Digite um número entre 1-3.") # ele avisa o usuario que so é permitido numeros entre 1 e 3 (inclusos) 