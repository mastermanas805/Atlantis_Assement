"""
Task -  A building has 20 floors and 5 lifts. Each floor of the building has
        a lift lobby. A user can be on any of the 20 floors and can request a lift. 
        The positions of the lifts are denoted by a 5-length array of random numbers 
        representing the current floor position (and direction of) of each lift. 
        If no direction is given, it means that the lift is sitting idle on that floor. 
        
        Example:

            lift_position = [0, 1D, 12, 4U, 19D]

        Write a python program to allot to most efficiently lift to a user who requests 
        it from any floor with intention of going up or down. On running the program the 
        lift position should be randomly initialized. 

Observation -   It's a implementation based problem. It can be done by calculating min 
                distance b/w the floor and lift



"""
import random

class lift:
    up = 1
    down = -1
    still = 0

    def __init__(self):
        self.genCombinations()
        # self.currState = [[0,0], [1,-1], [12,0], [4,1], [19,-1]]
        self.currState = random.sample(self.combinations, 5)
        self.printState()
        n = input("Enter a request? ")
        n = [int(n[:-1]), 1 if n[-1] == "U" else -1]
        
        dis   = 999
        l = -2

        for i in range(5):
            x = self.distance(n, self.currState[i])
            if x < dis:
                dis = x
                l = i
        
        print("Lift ", l+1)

    def genCombinations(self):
        combinations  = [[0,self.up], [20, self.down]]
        combinations += [[i,j] for j in [1,0,-1] for i in range(1,20)]
        self.combinations = combinations
    
    def printState(self):
        for i in self.currState:
            print(i[0], end="")
            if(i[1] == 1):
                print("U",end="")
            elif(i[1] == -1):
                print("D",end="")
            print(" ",end="")
        
        print()

    @staticmethod
    def distance(a: list,b: list):
        x = 0
        #lift is still
        if b[1] == 0:
            return abs(a[0]-b[0])
        #Request for going Up
        elif a[1] == 1:
            #lift below requesting floor and going up
            if(b[0]<=a[0] and b[1] == 1):
                return abs(a[0] - b[0])
            #lift going down
            else:
                return b[0] + a[0]
        #Reuest for going down
        else:
            #Lift above requesting floor and going down
            if(b[0]>=a[0] and b[1] == -1):
                return b[0] - a[0]
            #Lift going up
            else:
                return (20-b[0]) + (20-a[0])



def main() -> None:
    w = lift()
  
if __name__=="__main__":
    main()