'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
opc = 0
contador_paciente = 0 

qtd_abaixo = 0 
qtd_normal = 0 
qtd_sobrepeso = 0 
qtd_ob1 = 0 
qtd_ob2 = 0 
qtd_ob3 = 0 

imc_total = 0 

while (opc != 3):
    opc = int(input(''' ---===<<< MENU >>>===--- 
    (1) Cadastrar paciente
    (2) Exibção geral
    (3) Sair
    
    Digite a sua opção: '''))
    
    if opc == 1:
        print("---===<<< CADASTRAR PACIENTE >>>===---") 
        nome = input("Informe o nome do paciente: ") 
        peso = float(input("Informe o peso do paciente: ")) 
        altura = float(input("Informe a altura do paciente: ")) 
        imc = peso / altura**2 
        
        if imc < 18.5: 
            print("O paciente está abaixo do peso!")
            qtd_abaixo+=1
            
        elif (imc >= 18.5) and (imc < 25): 
            print("O paciente está com o peso normal!")
            qtd_normal+=1 
            
        elif (imc >= 25) and (imc < 30): 
            print("O paciente está com sobrepeso!")
            qtd_sobrepeso+=1 
            
        elif (imc >= 30) and (imc < 35): 
            print("O paciente está com obesidade grau I!")
            qtd_ob1+=1 l
            
        elif (imc >= 35) and (imc < 40): 
            print("O paciente está com obesidade grau II!")
            qtd_ob2+=1 
            
        else:
            print("Obesidade Grau III (Mórbida)!") 
            qtd_ob3+=1 
        
        contador_paciente+=1 
        imc_total += imc 
    
    elif opc == 2: 
        print("---===<<< EXIBIR >>>===---")
        print(f'Quantidade total dos pacientes: {contador_paciente}') 
        
        media_geral = imc_total / contador_paciente
        print(f'Média geral do IMC: {media_geral}') 
        
        print(f'Quantidade de pacientes abaixo do peso: {qtd_abaixo}')
        print(f'Quantidade de pacientes com o peso normal: {qtd_normal}')
        print(f'Quantidade de pacientes com sobrepeso: {qtd_sobrepeso}')
        print(f'Quantidade de pacientes com obesidade grau I: {qtd_ob1}')
        print(f'Quantidade de pacientes com obesidade grau II: {qtd_ob2}')
        print(f'Quantidade de pacientes com obesidade grau III: {qtd_ob3}')
    
    elif opc == 3: 
        print("Saindo do sistema...") 
        break; 
        
    else: 
        print("Opção inválida! Digite um número entre 1-3.") 