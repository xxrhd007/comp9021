# Written by *** for COMP9021


from math import sqrt
from itertools import permutations


# A number is a good prime if it is prime and consists of nothing but
# distinct nonzero digits.
# Returns True or False depending on whether the integer provided as
# argument is or is not a good prime, respectively.
# Will be tested with for number a positive integer at most equal to
# 50_000_000.
def is_good_prime(number):
    flag=True
    for i in range(2, number):
        if number % i == 0:
            flag=False
    if '0' not in str(number) and flag:
        if len(str(number))==len(set(str(number))):
            flag=True
        else:
            flag=False
    else:
        flag=False
    return flag
    # REPLACE PASS ABOVE WITH YOUR CODE

# pattern is expected to be a nonempty string consisting of underscores
# and distinct nonzero digits of length at most 7 (this does not need
# to be checked).
# Underscores have to be replaced by digits so that the resulting number
# is a good prime.
# The function prints out all solutions, if any, from smallest to largest.
def good_primes(pattern):
    pat=list(pattern)
    prime=sieve_of_primes_up_to(10**len(pat)-1)
    s=[]
    a=[]
    result=[]
    for i in range(10**(len(pat)-1),10**len(pat)):
        if prime[i]==True and '0' not in str(i):
            a.append(i)
    for x in a:
        if len(str(x))==len(set(str(x))):
            s.append(x)
    for num in s:
        flag1=True
        nums=list(map(str,str(num)))
        for i in range(len(nums)):
            if pat[i]!='_' and pat[i]!=nums[i]:
                flag1=False
        if flag1==True:
            result.append(num)
    for x in result:
        print(x)
    # REPLACE PASS ABOVE WITH YOUR CODE

def sieve_of_primes_up_to(n):
    sieve = [False, False] + [True] * (n - 1)
    for p in range(2, round(sqrt(n)) + 1):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return sieve
