import random

def printMatrix(tMatrix):
    for fila in tMatrix:
        print()
        for elemento in fila:
            print(f"{elemento:4}", end="")
        print()
        
def checkWin(tMatrix):
    winDetected = "-"
    if tMatrix[0][0] == tMatrix[0][1] == tMatrix[0][2] and tMatrix[0][0] != "-":
        winDetected = tMatrix[0][0]
    if tMatrix[1][0] == tMatrix[1][1] == tMatrix[1][2] and tMatrix[1][0] != "-":
        winDetected = tMatrix[1][0] 
    if tMatrix[2][0] == tMatrix[1][2] == tMatrix[2][2] and tMatrix[2][0] != "-":
        winDetected = tMatrix[2][0]
    if tMatrix[0][0] == tMatrix[1][0] == tMatrix[2][0] and tMatrix[2][0] != "-":
        winDetected = tMatrix[0][0]
    if tMatrix[0][1] == tMatrix[1][1] == tMatrix[2][1] and tMatrix[0][1] != "-":
        winDetected = tMatrix[0][1]
    if tMatrix[0][2] == tMatrix[1][2] == tMatrix[2][2] and tMatrix[0][2] != "-":
        winDetected = tMatrix[0][2]
    if tMatrix[0][0] == tMatrix[1][1] == tMatrix[2][2] and tMatrix[0][0] != "-":
        winDetected = tMatrix[0][0]
    if tMatrix[0][2] == tMatrix[1][1] == tMatrix[2][0] and tMatrix[0][2] != "-":
        winDetected = tMatrix[0][2]
    return winDetected
        
        
            
            
def tictactoe():
    finalizarJuego = 0
    tMatrix = [["-",'-','-'],["-",'-','-'],["-",'-','-']]
    times = 0
    while finalizarJuego != 1:
        player = 1
        machinePlayed = 1
        while player != 0:
            row = int(input("Type the row you want to be: "))
            col = int(input("Type the column you want to be: "))
            if tMatrix[row-1][col-1] == 'x' or tMatrix[row-1][col-1] == 'o':
                print("This place is busy, please take another one.")
            else:
                tMatrix[row-1][col-1] = 'x'
                player = 0
                times = times + 1
                
        printMatrix(tMatrix)
        if checkWin(tMatrix) != '-':
            finalizarJuego = 1
            print("X's Wins the game!")

            
        while machinePlayed != 0 and finalizarJuego != 1:
            print("Machine played!")
            if tMatrix[1][1] == '-':
                tMatrix[1][1] = 'o'
                machinePlayed = 0
                times = times + 1
            elif tMatrix[1][1] == 'x' and times == 1:
                corners = [0,2]
                cornerSelect = random.randint(0,1)
                cornerSelect2 = random.randint(0,1)
                tMatrix[corners[cornerSelect]][corners[cornerSelect2]] = 'o'
                machinePlayed = 0
                times = times + 1
            if times >= 2: 
                while machinePlayed == 1:
                    for i in range(len(tMatrix)):
                        for j in range(len(tMatrix[i])):
                            if machinePlayed == 1:
                                if tMatrix[i][j] == '-':
                                    randomPosibility = random.randint(0,1)
                                    if  randomPosibility == 1:
                                        tMatrix[i][j] = 'o'
                                        machinePlayed = 0
                                        times = times + 1
            printMatrix(tMatrix)
            
            if checkWin(tMatrix) != '-':
                finalizarJuego = 1
                print("O's Wins the game!")
            
                    
            
      
tictactoe()
                
            
        
        
    
