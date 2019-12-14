#Breaking chocolate problem
#Level: 7 kyu
'''
Your task is to split the chocolate bar of given dimension n x m into small squares. 
Each square is of size 1x1 and unbreakable. Implement a function that will return minimum number of breaks needed.
For example if you are given a chocolate bar of size 2 x 1 you can split it to single squares in just one break, 
but for size 3 x 1 you must do two breaks.
'''
def breakChocolate(n, m):
    if n == 0: return 0
    return (n-1)+(n)*(m-1)
