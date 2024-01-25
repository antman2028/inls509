# The following code is used to calculate the similarity between vectors
# Using the following methods: Jaccard, Cosine, and Euclidean Distance.
import math

def jaccardSimilarity(vector1,vector2):
    """Calculates the Jaccard similarity between two vectors"""
    
    if len(vector2)!=len(vector1): 
        print("Vectors must be the same length")
        return
    
    intersection = [x for x in vector1 if x in vector2]
    union = set()
    for x in vector1: union.add(x)
    for y in vector2: union.add(y)
    
    res = 1-(len(intersection)/len(union))
    
    print("The Jaccard similarity of:\nv1="+str(vector1)+"\nv2="+str(vector2)+"\n="+str(res))
    
    
def euclideanDistance(vector1,vector2):
    """Calculates the Euclidean distance between two vectors"""
    if len(vector2)!=len(vector1): 
        print("Vectors must be the same length")
        return
    
    sum = 0
    for i in len(range(vector1)):
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
    
    
vector1 = ["Go","Heels","Go"]
vector2 = ["Go","Heels"]