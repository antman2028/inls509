# The following code is used to calculate the similarity between vectors
# Using the following methods: Jaccard, Cosine, and Euclidean Distance.
# By Toni S
import math
from collections import Counter

def jaccardSimilarity(string1,string2):
    """Calculates the Jaccard similarity between two vectors"""
    v1=string1.split(" ")
    v2=string2.split(" ")

    intersection = set()
    for x in v1: 
        if x in v2: 
            intersection.add(x)
    union = set()
    for x in v1: union.add(x)
    for y in v2: union.add(y)
    
    res = 1-(len(intersection)/len(union))
    
    print("The Jaccard similarity of:\nv1="+str(string1)+"\nv2="+str(string2)+"\n="+str(res))
    
    
def euclideanDistance(vector1,vector2):
    """Calculates the Euclidean distance between two vectors"""
    if len(vector2)!=len(vector1): 
        print("Vectors must be the same length")
        return
    
    sum = 0
    for i in range(len(vector1)):
        sum += ((vector1[i]-vector2[i])*(vector1[i]-vector2[i]))
    
    res = math.sqrt(sum)
    print("The Euclidean distance of:\nv1="+str(vector1)+"\nv2="+str(vector2)+"\n="+str(res))    
    
def cosineSimilarity(vector1,vector2):
    """Calculates the cosine similarity between two vectors"""
    if len(vector2)!=len(vector1): 
        print("Vectors must be the same length")
        return
    
    value1 = 0
    value2 = 0
    value3 = 0
    
    for i in range(len(vector1)):
        value1 += vector1[i]*vector2[i]
        value2 += vector1[i]*vector1[i]
        value3 += vector2[i]*vector2[i]

    res = (value1/(math.sqrt(value2)*math.sqrt(value3)))
    print("The Cosine similarity of:\nv1="+str(vector1)+"\nv2="+str(vector2)+"\n="+str(res))

def createVectorsFromStrings(v1,v2):
    v1Words, v2Words = Counter(v1.split(" ")),Counter(v2.split(" "))
    v1Vector,v2Vector = [],[]
    words = set().union(v1Words,v2Words)
    for word in words:
        if v1Words.get(word,0)!=0: v1Vector.append(v1Words[word])
        else: v1Vector.append(0)
        if v2Words.get(word,0)!=0: v2Vector.append(v2Words[word])
        else: v2Vector.append(0)
    return [v1Vector,v2Vector]


def eulideanDistanceWithWords(string1, string2):
    """Calculates the cosine similarity between two strings"""
    newVectors = createVectorsFromStrings(string1,string2)
    return euclideanDistance(newVectors[0],newVectors[1])

# Example 1 ~ Jaccard Similarity
D1,D2,D3 = "Go Heels", "Go Duke", "Go Heels Go"
jaccardSimilarity(D1,D2)
jaccardSimilarity(D1,D3)
# Example 2 ~ Euclidean Distance
X,Y = [0,3], [4,0]
euclideanDistance(X,Y)
# Example 3 ~ Cosine Similarity
X,Y = [1,math.sqrt(3)],[1,0]
cosineSimilarity(X,Y)
# Example 4 ~ Euclidean Distance with vectors comprised of words
# Testing how the Euclidean Distance folmula would work with comparing two strings
    
sentence1 = "I love playing football with my friends"
sentence2 = "I hate waching and playing basketball"

eulideanDistanceWithWords(sentence1,sentence2)