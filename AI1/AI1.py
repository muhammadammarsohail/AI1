import collections
import math

############################################################
# Problem 3a

def findAlphabeticallyLastWord(text):
    """
    Given a string |text|, return the word in |text| that comes last
    alphabetically (that is, the word that would appear last in a dictionary).
    A word is defined by a maximal sequence of characters without whitespaces.
    You might find max() and list comprehensions handy here.
    """
    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    # raise Exception("Not implemented yet")
    return max(text.lower().split())

print(findAlphabeticallyLastWord("The quick brown fox jumps over the lazy dog"))

    # END_YOUR_CODE

############################################################
# Problem 3b


def euclideanDistance(loc1, loc2):
    """
    Return the Euclidean distance between two locations, where the locations
    are pairs of numbers (e.g., (3, 5)).
    """
    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    #raise Exception("Not implemented yet")
    return math.sqrt((loc1[0]-loc2[0])**2 + (loc1[1]-loc2[1])**2)
    # END_YOUR_CODE

print(euclideanDistance((9,7), (3,2)))

############################################################
# Problem 3c

def mutateSentences(sentence):
    """
    Given a sentence (sequence of words), return a list of all "similar"
    sentences.
    We define a sentence to be similar to the original sentence if
      - it as the same number of words, and
      - each pair of adjacent words in the new sentence also occurs in the original sentence
        (the words within each pair should appear in the same order in the output sentence
         as they did in the orignal sentence.)
    Notes:
      - The order of the sentences you output doesn't matter.
      - You must not output duplicates.
      - Your generated sentence can use a word in the original sentence more than
        once.
    Example:
      - Input: 'the cat and the mouse'
      - Output: ['and the cat and the', 'the cat and the mouse', 'the cat and the cat', 'cat and the cat and']
                (reordered versions of this list are allowed)
    """
    # BEGIN_YOUR_CODE (our solution is 20 lines of code, but don't worry if you deviate from this)
    raise Exception("Not implemented yet")
    # END_YOUR_CODE

############################################################
# Problem 3d

def sparseVectorDotProduct(v1, v2):
    """
    Given two sparse vectors |v1| and |v2|, each represented as collections.defaultdict(float), return
    their dot product.
    You might find it useful to use sum() and a list comprehension.
    This function will be useful later for linear classifiers.
    """
    # BEGIN_YOUR_CODE (our solution is 4 lines of code, but don't worry if you deviate from this)
    #raise Exception("Not implemented yet")
    a=b=0; ans = [];
    while a < len(v1) and b < len(v2):
        if v1[a][0] == v2[b][0]:
            ans.append(v1[a][1] * v2[b][1])
            a += 1
            b += 1
        elif v1[a][0] < v2[b][0]:
            a += 1
        else: 
            b += 1
    return sum(ans)

print(sparseVectorDotProduct( [(2,3), (5,4)] , [(1,7), (2,6), (5,3)] ))

    # END_YOUR_CODE

############################################################
# Problem 3e

def incrementSparseVector(v1, scale, v2):
    """
    Given two sparse vectors |v1| and |v2|, perform v1 += scale * v2.
    This function will be useful later for linear classifiers.
    """
    # BEGIN_YOUR_CODE (our solution is 2 lines of code, but don't worry if you deviate from this)
    #raise Exception("Not implemented yet")
    a=b=0;
    while a < len(v1) and b < len(v2):
        if v1[a][0] == v2[b][0]:
            v1[a] = tuple([v1[a][0], v1[a][1] + scale * v2[b][1]])
            a += 1
            b += 1
        elif v1[a][0] < v2[b][0]:
            a += 1
        else:
            v1.insert(a, tuple([v2[b][0], 0 + scale * v2[b][1]]))
            a+=1
            b+=1
    while b < len(v2):
        v1.append(v2[b])
        b+=1
    return v1
          

    # END_YOUR_CODE

print(incrementSparseVector([(2,3), (5,4)] , 5 , [(1,7), (2,6), (5,3)] ))

############################################################
# Problem 3f

def findSingletonWords(text):
    """
    Splits the string |text| by whitespace and returns the set of words that
    occur exactly once.
    You might find it useful to use collections.defaultdict(int).
    """
    # BEGIN_YOUR_CODE (our solution is 4 lines of code, but don't worry if you deviate from this)
    raise Exception("Not implemented yet")
    # END_YOUR_CODE

############################################################
# Problem 3g

def computeLongestPalindromeLength(text):
    """
    A palindrome is a string that is equal to its reverse (e.g., 'ana').
    Compute the length of the longest palindrome that can be obtained by deleting
    letters from |text|.
    For example: the longest palindrome in 'animal' is 'ama'.
    Your algorithm should run in O(len(text)^2) time.
    You should first define a recurrence before you start coding.
    """
    # BEGIN_YOUR_CODE (our solution is 19 lines of code, but don't worry if you deviate from this)
    #raise Exception("Not implemented yet")
    
    # END_YOUR_CODE
