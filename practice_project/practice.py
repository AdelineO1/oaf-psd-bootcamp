# Test whether numbers in a given range is prime
def is_prime(num):
    for n in range (0,9):
        if num%n==0:
            return False
        return True

if __name__=='main':
    print (is_prime(7)) # True
    print (is_prime(4)) # False
