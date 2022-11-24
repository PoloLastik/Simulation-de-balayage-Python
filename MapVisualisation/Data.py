import numpy as np

def getEmptyArray(size_x,size_y):
    return np.zeros((size_x,size_y))

class Map:
    size_x = 0
    size_y = 0
    array = None

    def __init__(self,array,*args,**kwargs):
        self.setArray(array)
        

    def setPosObstacle(self,x,y):
        if x>self.size_x:
            raise IndexError("Taille x trop importante :" + str(x))
        if y>self.size_y:
            raise IndexError("Taille y trop importante :" + str(y))
        self.array[x,y] = 1
    
    def setPosNoObstacle(self,x,y):
        if x>self.size_x:
            raise IndexError("Taille x trop importante :" + str(x))
        if y>self.size_y:
            raise IndexError("Taille y trop importante :" + str(y))
        self.array[x,y] = 0

    def setArray(self,array):
        self.array = array
        self.size_x,self.size_y = self.array.shape
    
    def setArrayWithList(self,dataList):
        self.array = np.array(dataList)
        self.size_x, self.size_y = self.array.shape

    def getObstacleAtPos(self,x,y):
        return (self.array[x,y]==1)
    
    def addLine(self,line=None):
        newline = line if line else np.zeros((1,self.size_y))
        print(newline)
        self.array = np.append(self.array,newline,axis=0)
        self.size_x, self.size_y = self.array.shape

    def addColumn(self,line=None):
        newline = line if line else np.zeros((self.size_x,1))
        print(newline)
        self.array = np.append(self.array,newline,axis=1)
        self.size_x, self.size_y = self.array.shape
    
    def getRow(self,row):
        return self.array[row]
        
    def getColumn(self,column):
        return self.array[:,column]

if __name__ == "__main__":
    pass