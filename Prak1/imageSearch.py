import os
from pathlib import Path
from typing import List
from PIL import Image
import imagehash

from AVLTree import AVLTree




def getImagePaths(filePath: str): #create a list with images from the filepath
    os.chdir(filePath)
    listOfAllImagePaths : List = os.listdir()
    pathsToImages= dict()
    for item in listOfAllImagePaths:
            #pathList: List=[]
            inputHash = imagehash.average_hash(Image.open(item))
            pathsToImages[inputHash]=item
    return pathsToImages

def get(imagePath: str,filePath: str): #returns a list with the pathes of the picture in the filepath
    print(getImagePaths(filePath).get(imagehash.average_hash(Image.open(imagePath))))
    



file = r"C:\\Users\\Ahmad Bannout\Documents\\Prak1\\Cats\\"
image1 = r"C:\Users\Ahmad Bannout\Desktop\11.jpg"   
value1=imagehash.average_hash(Image.open(image1))
image2=r"C:\Users\Ahmad Bannout\Desktop\Test.jpg"
value2=imagehash.average_hash(Image.open(image2)) 
get(image1,file)

avlTree= AVLTree()

def insertImagesInAVLTree(filePath:str,avlTree:AVLTree):
    os.chdir(filePath)
    listOfAllImagePaths : List = os.listdir()
    for item in listOfAllImagePaths:
            #pathList: List=[]
            inputHash = str(imagehash.average_hash(Image.open(item)))
            avlTree.insert(inputHash,item)
#use i=int(s,16) to convert hex into decimal

def hamming_Distanz(value1,valu2):
    distance=0
    L=len(value1)
    for i in range(L):
        if value1[i] !=valu2[i]:
            distance+=1
    return distance
def findMostSimilarImageInAvlTree(imagePath:str,avlTree:AVLTree):
    if avlTree.root!=None:
        return _findMostSimilarImageInAvlTree(imagePath,avlTree.root)
    else:
        return None

def _findMostSimilarImageInAvlTree(imagePath:str,cur_node):
    inputhash=str(imagehash.average_hash(Image,open(imagePath)))
    if inputhash!=cur_node.hashValue:
        if hamming_Distanz(input,cur_node.hashValue)<=hamming_Distanz(inputhash,cur_node.left_child.valueHash) and hamming_Distanz(input,cur_node.hashValue)<=hamming_Distanz(inputhash,cur_node.left_child.valueHash):
            return cur_node
        elif inputhash> cur_node.hashValue and cur_node.right_child is not None:
                return _findMostSimilarImageInAvlTree(imagePath,cur_node.right_child)
        elif inputhash< cur_node.hashValue and cur_node.left_child is not None:
                return _findMostSimilarImageInAvlTree(imagePath,cur_node.left_child) 
    else:
        if cur_node.left_child!=None and cur_node.right_child!=None:
            if hamming_Distanz(cur_node.left_child.hashValue,inputhash)<=hamming_Distanz(cur_node.right_child.hashValue,inputhash):
                return cur_node.left_child
            elif hamming_Distanz(cur_node.left_child.hashValue,inputhash)>=hamming_Distanz(cur_node.right_child.hashValue,inputhash):
                return cur_node.right_child
        elif cur_node.left_child ==None:
            return cur_node.right_child
        elif cur_node.right_child ==None:
            return cur_node.left_child
        else:
            return cur_node.parent
        



insertImagesInAVLTree(file,avlTree)





