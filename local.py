"""
    Utility functions
"""
def check_sign(i):
    '''
        Returns true if the value read from standard input is negative
    '''
    while i > 10:
        print('Please input a number')
        n = int(input())
        if n < 0:
            break
    return n

o = check_sign(11)
print('Negative number is detected: ', o)
