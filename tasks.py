import sys
import math

inp1 = sys.argv[1]
inp2 = sys.argv[2].lower()
inp3 = int(sys.argv[3])

def correct_signs(inp1):
        test1 = eval(inp1)
        print("Given expression {0} is {1}".format(inp1,test1))

def count_vowels(inp2):

        count = 0
        a = ['a','e','i','o','u']
        for i in list(inp2):
                if i in a:
                        count+=1
                else:
                        count = count
        print("The word {0} contains {1} vowels".format(inp2,count))

def cars_needed(inp3):

        test3 = math.ceil(inp3/5)
        print("Number of cars needed for {0} members is {1}".format(inp3,test3))

correct_signs(inp1)
count_vowels(inp2)
cars_needed(inp3)
