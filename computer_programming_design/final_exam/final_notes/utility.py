def is_prime(n):
    """Check whether a number is prime or not"""
    if n==1:
        return False
    for i in range(2,n):
        if n % i ==0:
            return False
    return True

def is_palindrome(s):
    """Check a string is palindrome"""
    for i in range(len(s)):
        if s[i] != s[-i-1]:
            return False
    return True

if __name__ == "__main__":
    for i in range(1,100):
        print('%d is prime? %s' %(i ,is_prime(i)))
    strings=['madam','123','12321']
    for s in strings:
        print('%s is palindrome? %s' %(s, is_palindrome(s)))