global PATH
PATH = r'QOTW-FIBONARCHYS_SEQUENCE\Genrated.txt' # Sets path

def Overwrite():
    # OverWrites the file
    open(PATH,'w').close()  

def SelectingPostiveAndNegtiveNumbers(count):
    startSub = 100/(count*2)
    bestLine = "1,-1:1"
    # Itterates through the file to check
    with open(PATH) as fibonachiSequence:
        for line in fibonachiSequence:
            if float(line.split(':')[1].strip()) > float(bestLine.split(':')[1].strip()):
                bestLine = line
    
    # posive number is the values before the , so a single number
    postiveNumber = float(bestLine.split(",")[0].strip()) - startSub
    # negtive number is all the values before the : then out of this we get rid of all the values before the ,
    negtiveNumber = float((bestLine.split(":")[0]).split(",")[1].strip()) + startSub
    
    # Checks that postive an d negtive numbers are in range
    if postiveNumber <= 0:
        postiveNumber = 1
    if negtiveNumber >= 0:
        negtiveNumber = -1
        
    return postiveNumber , negtiveNumber

firstRun = False
count = 1

Overwrite()

while True:
    if firstRun == False: # Sets base numbers for first itteration
        postiveNumber = 3
        negtiveNumber = -2
        firstRun = True
    else:
        postiveNumber = SelectingPostiveAndNegtiveNumbers(count)[0]
        negtiveNumber = SelectingPostiveAndNegtiveNumbers(count)[1]

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
            
        a = open(PATH,"a") # Opens file to append it

        sequance = [] # Sets a blank sequance then adds the first 2 numbers to it
        sequance.append(postiveNumber)
        sequance.append(negtiveNumber)

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
            sequance.append(nextNumber)
            lastNumber = currentNumber
            currentNumber = nextNumber

        # Updates the start numbers after each sequance is completed
        postiveNumber += itteration
        negtiveNumber -= itteration
    
    input("press enter to continue")