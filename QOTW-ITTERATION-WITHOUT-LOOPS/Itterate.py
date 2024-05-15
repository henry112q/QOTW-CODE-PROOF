# to create a loop without using a loop
# Idea fo goto - Fail python dose not have goto could try C# for this
# Extra make it work like a usual loop where there can be code around it to make it work better
# input be like loop(start,end-1,counter name , code that will be run)

from os import *

class Looping:
    def __init__(self,start,end,counter,code):
        self.start = start
        self.end = end-1
        self.counter = counter
        self.code = code
        
        
def Loop(startAndEnd,counter,code):
    start = startAndEnd[0]
    end = startAndEnd[-1]
    looping_instance = Looping(start,end-1,counter,code)
x = False
if __name__ == "__main__":
    if x == True:
        Loop([1,4],"count","count")