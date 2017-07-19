#uses python3
import sys

# function returns the best value of combinations less than total W of the knapsack by creating smaller subproblems or subcombinations w 
#value of the items are same but different weights
def knapsack(W,w):
    capacity=[0]*(W+1) # create an array for initializing W to 0
    
    for i in range(len(w)): # increases value of i
        for j in range(W,w[i]-1, -1):
            capacity[j]=max(capacity[j], capacity[j-w[i]]+ w[i])
    return capacity[W]

if __name__ == '__main__':
    
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split())) #W is capacity of knapsack, n is number of items and *w is weights of the items n.
    print(knapsack(W, w))
    
