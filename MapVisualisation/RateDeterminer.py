import numpy as np
import Data as dt
import csv_data as csv
import copy

SlewArr = None
Itineraire = []

class Position:
    x = 0
    y = 0
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Form:
    pos = Position(0,0)
    size_x = 0
    size_y = 0

    def __init__(self,x,y,final_x,final_y,accessPos=None):
        self.accessPos = accessPos
        self.pos = Position(x,y)
        self.size_x = final_x - x
        self.size_y = final_y - y


    def defineAccessPos(self,arr):
        
        AccessPos = None
        maxArrayPos = Position(arr.shape)

        #1
        if self.pos.x > 0:
            # Parcours de la ligne su^périeure de la forme pour trouver un accès
            
            currentPos = Position(self.pos.x-1,self.pos.y)
            
            while( (AccessPos == None)  or (currentPos.y < (self.pos.y + self.size_y) ) ):
                
                if (arr[currentPos.x,currentPos.y] == 0):AccessPos = currentPos
                else:currentPos.y +=1
        #2
        if (self.pos.x + self.size_x) < maxArrayPos.x and AccessPos == None:
            # Parcours ligne inférieurs
            currentPos = Position((self.pos.x+self.size_x), self.pos.y)
            
            while((AccessPos == None) or (currentPos.y<self.pos.y + self.size_y)):
                
                if (arr[currentPos.x,currentPos.y] == 0):AccessPos = currentPos
                else:currentPos.y +=1
        #3 
        if self.pos.y > 0 and AccessPos == None:
            #Sinon la colonne gauche 
            currentPos = Position(self.pos.x,self.pos.y-1)
            
            while((AccessPos == None) or (currentPos.x<self.pos.x + self.size_x)):
                
                if (arr[currentPos.x,currentPos.y] == 0):AccessPos = currentPos
                currentPos.x +=1
        #4
        if (self.pos.y + self.size_y) < maxArrayPos.y and AccessPos == None:
            #Sinon la colonne droite
            currentPos = Position(self.pos.x,(self.pos.y + self.size_y))
            
            while((AccessPos == None) or (currentPos.x<self.pos.x + self.size_x)):
                
                if (arr[currentPos.x,currentPos.y] == 0):AccessPos = currentPos
                currentPos.x +=1
        
        if AccessPos == None:
            raise ValueError("AccessFinder : No Position found !")
        self.accessPos = AccessPos

def tryToCreateForm(arr,x,y,size_x,size_y):
    possibility = True
    print("Lets go !")
    for cur_x in range(x,x+size_x):
        for cur_y in range(y,y+size_y):
            if arr[cur_x,cur_y] == 1: possibility = False
            print("At pos :" + str(x) + str(y) + ": cell :" + str(arr[cur_x,cur_y]))
            print(possibility)
    return possibility

def setArraytoOne(arr,x,y,size_x,size_y):
    for cur_x in range(x,x+size_x):
        for cur_y in range(y,cur_y):
            arr[cur_x,cur_y] = 1

def getForms(Arr):
    newArr = []
    newArr = copy.deepcopy(Arr)
    forms = []
    curseur = Position(0,0)
    print(newArr.shape)
    # Premier essai de créer des formes de taille en X min de 2
    while(not IsArrayEmpty(newArr)):
        for x in range(newArr.shape[0]):
            for y in range(newArr.shape[1]):
                
                if newArr[x,y] == 0:
                    print("Trying to create form at pos :")
                    print((x,y))
                    extend_x = 1
                    extend_y = 1
                    
                    while(tryToCreateForm(newArr,x,y,extend_x,extend_y)):
                        extend_x +=1
                    
                    while(tryToCreateForm(newArr,x,y,extend_x,extend_y)):
                        extend_y +=1
                    
                    if extend_x >= 2:
                        print("Creating form :")
                        print((x,y,extend_x,extend_y))
                        forms.append(Form(x,y,extend_x,extend_y))
                        setArraytoOne(newArr,x,y,extend_x,extend_y)

        #Second essai ou la on sen fou de la taille de x
        
        for x in range(newArr.shape[0]):
            for y in range(newArr.shape[1]):
                
                if newArr[x,y] == 0:
                    
                    extend_x = 1
                    extend_y = 1
                    
                    while(tryToCreateForm(newArr,x,y,extend_x,extend_y)):
                        extend_x +=1
                    
                    while(tryToCreateForm(newArr,x,y,extend_x,extend_y)):
                        extend_y +=1
                    forms.append(Form(x,y,extend_x,extend_y))
                    setArraytoOne(newArr,x,y,extend_x,extend_y)

        return forms, IsArrayToOne(newArr)

def posAvancerNordwithExternArray(pos):
    pos[0] -= 1
    return pos

def posAvancerSudwithExternArray(pos):
    pos[0] += 1
    return pos

def posAvancerEstwithExternArray(pos,arr):
    pos[1] +=1
    return pos

def posAvancerOuestwithExternArray(pos,arr):
    pos[1] -= 1
    return pos

def IsArrayToOne(arr):
    isToOne = True
    for x in range(arr,arr.shape[0]):
        for y in range(arr,arr.shape[1]):
            if arr[x,y] != 1:
                isToOne = False
    return isToOne

def IsArrayEmpty(arr):
    isEmpty = True
    for x in range(arr.shape[0]):
        for y in range(arr.shape[1]):
            if arr[x,y] != 1:
                isEmpty = False
                break
    return isEmpty

def isObstacleNord(Arr,pos):
    '''
    Detecte un obstacle au Nord axe 0 sens -
    '''
    val = True
    if pos[0]>0:val = (Arr[pos[0]-1,pos[1]] == 1)
    return val

def isObstacleSud(Arr,pos):
    '''
    Detecte un obstacle au Sud axe 0 sens +
    '''
    val = True
    if pos[0]<Arr.shape[0]:val =(Arr[pos[0]+1,pos[1]] == 1)
    return val

def isObstacleEst(Arr,pos):
    '''
    Detecte un obstacle à l'ouest de l'axe 1 sens +
    '''
    val = True
    if pos[1]<Arr.shape[1]:val =(Arr[pos[0],pos[1]+1] == 1)
    return val

def findItinaryToPos(pos_one,final_pos,array):
    '''
        y 1 , 2 , 3
    x  
    1
    2
    3
    '''
    itinary = []
    currentPos = pos_one
    while(currentPos[0] != final_pos[0] or currentPos[1] != final_pos[1]):
        
        move_done = False
        previous_case = case
        case = ""
        """
        if currentPos[0] < final_pos[0]:case = "sud"
        elif currentPos[:pass        
        """
        if not isObstacleSud(array,currentPos):
            currentPos = posAvancerSudwithExternArray(currentPos)
            itinary.add("sud")
            move_done = True
        
        if currentPos[0] > final_pos[0] and not isObstacleNord(array,currentPos) and not move_done:
            currentPos = posAvancerNordwithExternArray(currentPos)
            itinary.add("Nord")
            move_done = True

        if currentPos[1] < final_pos[1] and not isObstacleEst(array,currentPos) and not move_done:
            currentPos = posAvancerEstwithExternArray(currentPos)
            itinary.add("est")
            move_done = True
        
        if currentPos[1] > final_pos[1] and not isObstacleSud(array,currentPos) and not move_done:
            currentPos = posAvancerOuestwithExternArray(currentPos)
            itinary.add("ouest")
            move_done = True
        '''
        if move_done == False:pass
        '''


    return itinary


def isObstacleOuest(Arr,pos):
    '''
    Detecte un obstacle à l'ouest de l'axe 1 sens -
    '''
    val = True
    if pos[1]>0:val = (Arr[pos[0],pos[1]-1] == 1)
    return val

def posAvancerNord(pos):
    global SlewArr,Itineraire
    SlewArr[pos] = 1
    pos[0] -= 1
    Itineraire.append("Nord")

def posAvancerSud(pos):
    global SlewArr,Itineraire
    SlewArr[pos] = 1
    pos[0] += 1
    Itineraire.append("Sud")

def posAvancerEst(pos):
    global SlewArr,Itineraire
    SlewArr[pos] = 1
    pos[1] +=1
    Itineraire.append("Est")

def posAvancerOuest(pos):
    global SlewArr,Itineraire
    SlewArr[pos] = 1
    pos[1] -= 1
    Itineraire.append("Ouest")

def AvancerEstSinonSud(pos,arr):
    while(not isObstacleEst(arr,pos)):
            posAvancerEst(pos)
    while(isObstacleEst(arr,pos)):
            posAvancerSud(pos)

def AvancerOuestSinonSud(pos,arr):
    pass

def getItinary(map):
    '''
    Start a the right top of the tab
    '''
    global SlewArr
    pos = (0,0)
    arr = map.array
    Slewarr = copy.deepcopy(arr)
    forms, completed = getForms(arr)
    if not completed: raise("Forms getter wrong, incomplete process:")
    for form in forms:
        pass
if __name__ == "__main__":
    map = csv.read()
    forms = getForms(map.array )
    counter = 0
    for form in forms:
        counter += form.size_x*form.size_y
        print("Size" + str(form.size_x*form.size_y))
    print("Counter : " + str(counter))


