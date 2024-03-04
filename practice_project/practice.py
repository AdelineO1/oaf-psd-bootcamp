# Test whether numbers in a given range is prime
def is_prime(num):
    for n in range (2, int(num**0.5) + 1):
        if num%n==0:
            return False
        return True

if __name__=='main':
    print (is_prime(5)) # True
    print (is_prime(8)) # False
