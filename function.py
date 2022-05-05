######################                                                                                                                   
# FUNÇÕES UTILIZADAS #                                                                                                                   
######################                                                                                                                   
                                                                                                                                         
def warning():                                                                                                                           
    print("Favor digitar apenas NÚMEROS INTEIROS entre 0 e 4 !!!!")                                                                      
    input("Pressione [ENTER]")                                                                                                           
                                                                                                                                         
def warningArray():                                                                                                                      
    sizeCities = int(len(cities))                                                                                                        
    print(f"Favor digitar apenas NÚMEROS INTEIROS ENTRE 0 e {sizeCities-1}")                                                             
    input("Pressione [ENTER]")                                                                                                           
                                                                                                                                         
def clearScreen():                                                                                                                       
    print("\n" * 25)                                                                                                                     
                                                                                                                                         
def menu():                                                                                                                              
    clearScreen()                                                                                                                        
    print("""                                                                                                                            
Menu                                                                                                                                     
0-	Finalizar o Programa                                                                                                                 
1-	Adicionar cidades                                                                                                                    
2-	Listar as cidades da lista                                                                                                           
3-	Alterar o nome de alguma cidade digitada                                                                                             
4-	Excluir uma cidade da lista                                                                                                          
""")                                                                                                                                     
                                                                                                                                         
def addCity():                                                                                                                           
    city = input("Informe o nome da cidade: ").upper()                                                                                   
    if city in cities:                                                                                                                   
        print(f"A cidade {city} já está cadastrada!!!")                                                                                  
        printCities()                                                                                                                    
    else:                                                                                                                                
        cities.append(city)                                                                                                              
                                                                                                                                         
def printCities():                                                                                                                       
    print(f"As cidades cadastradas até agora foram:")                                                                                    
    totalCities = len(cities)                                                                                                            
    print("CODIGO - CIDADE")                                                                                                             
    for x in range (0,totalCities,1):                                                                                                    
        print("  ",x,"  - ",cities[x])                                                                                                   
    input("Pressione [ENTER]")                                                                                                           
                                                                                                                                         
def updateCity():                                                                                                                        
    printCities()                                                                                                                        
    sizeCities = int(len(cities))                                                                                                        
    updateWho = int(input("Informe o código da cidade a ser alterado: "))                                                                
    if updateWho >= 0 and updateWho < sizeCities:                                                                                        
        newCity = input(f"Informe o novo nome a ser inserido na cidade de código {updateWho} ").upper()                                  
        cities[updateWho] = newCity                                                                                                      
        print("Confira a lista de cidades atualizadas:")                                                                                 
        printCities()                                                                                                                    
    else:                                                                                                                                
        warningArray()                                                                                                                   
                                                                                                                                         
def delCity():                                                                                                                           
    printCities()                                                                                                                        
    sizeCities = int(len(cities))                                                                                                        
    deleteWho = int(input("Informe o código da cidade a ser deletada: "))                                                                
    if deleteWho >= 0 and deleteWho < sizeCities:                                                                                        
        del (cities[deleteWho])                                                                                                          
        print("Confira a lista de cidades atualizadas:")                                                                                 
        printCities()                                                                                                                    
    else:                                                                                                                                
        warningArray()   