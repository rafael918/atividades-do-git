"""Exercício de revisão 01                                                                                                                  
                                                                                                                                         
Faça um algoritmo que, através da digitação pelo teclado, armazene em uma lista vários nomes de cidades brasileiras.                     
Exemplo:                                                                                                                                 
Digite uma nova cidade: CANOAS                                                                                                           
                                                                                                                                         
Seu programa deverá utilizar o seguinte menu:                                                                                            
                                                                                                                                         
Menu                                                                                                                                     
0-	Finalizar o Programa                                                                                                                 
1-	Adicionar cidades                                                                                                                    
2-	Listar as cidades da lista                                                                                                           
3-	Alterar o nome de alguma cidade digitada                                                                                             
4-	Excluir uma cidade da lista                                                                                                          
Escolha:                                                                                                                                 
                                                                                                                                         
Obs:                                                                                                                                     
- Você não deve aceitar duas cidades com o mesmo nome.                                                                                   
- Você deverá utilizar o máximo de funções que conseguires.                                                                              
"""                                                                                                                                      
                                                                                                                                         
######################                                                                                                                   
# FUNÇÕES UTILIZADAS #                                                                                                                   
######################                                                                                                                   
                                                                                                                                         
from function import  warning,  warningArray, clearScreen, menu, addCity,  printCities, updateCity, delCity                                                                                                            
                                                                                                                                         
######################                                                                                                                   
# PROGRAMA PRINCIPAL #                                                                                                                   
######################                                                                                                                   
selection = int()                                                                                                                        
cities = ["PORTO ALEGRE", "CANOAS", "CACHOEIRINHA", "NOVO AHMBRUGO", "GRAVATAÍ"] #deixei essas cadastradas pra nao ter que ficar digitand
                                                                                                                                         
while True:                                                                                                                              
    menu()                                                                                                                               
    try:                                                                                                                                 
        selection = int(input("Informe a opção desejada: "))                                                                             
        if selection == 0:                                                                                                               
            print("ENCERRANDO O PROGRAMA...!!!")                                                                                         
            break                                                                                                                        
        elif selection == 1:                                                                                                             
            addCity()                                                                                                                    
        elif selection == 2:                                                                                                             
            printCities()                                                                                                                
        elif selection == 3:                                                                                                             
            updateCity()                                                                                                                 
        elif selection == 4:                                                                                                             
            delCity()                                                                                                                    
        elif selection < 0 or selection > 4:                                                                                             
            warning()                                                                                                                    
    except:                                                                                                                              
        warning()                                                                                                                        
                                                                                                                                         
                                                                                                                                         
print("PROGRAMA ENCERRADO!!!")