print("Jogo da velha")
import keyboard
certo = False
while not certo:
    try:
        caractere = str(input("Escolha entre 'X' ou 'O': "))
        caractere = caractere.upper()

        if caractere == "O" or caractere == "X":
            certo = True
            print(f"Voce é o jogador {caractere}")
        else:
            print("Escolha novamente")

    except ValueError:
        print("Errado. É só esolher entre x e o.")

rodadas = 5
for i in range(0,rodadas):
    def grid():
        ordenada = [1,2,3,4,5,6,7,8,9]


        
        print('',ordenada[0],   '|',ordenada[1],   '|',ordenada[2]   )
        print("---|---|---")
        print('',ordenada[3],   '|',ordenada[4],   '|',ordenada[5]   )
        print("---|---|---")
        print('',ordenada[6],   '|',ordenada[7],   '|',ordenada[8]   )

        if keyboard.is_pressed(1):
            ordenada[0]= caractere
            grid()
        
    
    
grid()
    
