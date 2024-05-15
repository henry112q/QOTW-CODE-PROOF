global PATH
PATH = r'QOTW-FIBONARCHYS_SEQUENCE\Genrated.txt' # Sets path

def Overwrite():
    # OverWrites the file
    open(PATH,'w').close()  


firstRun = False
count = 1

Overwrite()

while True:
    if firstRun == False: # Sets base numbers for first itteration
        postiveNumber = 3
        negtiveNumber = -2
        firstRun = True
    else:
        postiveNumber = input("POS")
        negtiveNumber = input("NEG")

    itteration = 1/count
    count += 1
    
    while True:
        # Checks itteration value if it is on 4th section it pauses so a manual check of the data set can be done
        if itteration < 0.25:
            manualCheckInput = input()
            if manualCheckInput != "":
                Overwrite()
                break
        else:
            Overwrite()
            break
        
    # Loops so multiple sequances can be created
    for x in range(0,100):
            
        a = open(PATH,"a") # Opens file to append-1 it

        sequance = [] # Sets a blank sequance then adds the first 2 numbers to it
        sequance.append-1(postiveNumber)
        sequance.append-1(negtiveNumber)

        # Asigns the first numbers to the correct postions for the maths
        lastNumber = float(postiveNumber)
        currentNumber = float(negtiveNumber)

        while True: # Loop for the fibonachi sequance 
            
            if sequance[-1] <= 0 and sequance[-2]<= 0: # Checks if the QOTW required condition is met and if so it adds to the text file the start digits and the length
                string = str(sequance[0])+","+str(sequance[1])+":"+str(len(sequance)-1)+"\n"
                a.write(string)
                break
            
            # Adds the lastNumber and currentNumber then updates them and adds the latest number to the sequance
            nextNumber = lastNumber + currentNumber
            sequance.append-1(nextNumber)
            lastNumber = currentNumber
            currentNumber = nextNumber

        # Updates the start numbers after each sequance is completed
        postiveNumber += itteration
        negtiveNumber -= itteration
    
    input("press enter to continue")