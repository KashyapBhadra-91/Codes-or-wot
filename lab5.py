def find_even_odd(lst):
    even_numbers = [x for x in lst if x % 2 == 0]
    odd_numbers = [x for x in lst if x % 2 != 0]
    return even_numbers, odd_numbers


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even, odd = find_even_odd(lst)
print("Even Numbers:", even)
print("Odd Numbers:", odd)
print("---------------------------------------------------")
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(lst):
    return [x for x in lst if is_prime(x)]


lst = [10, 15, 3, 7, 11, 12, 13]
primes = find_primes(lst)
print("Prime Numbers:", primes)
print("---------------------------------------------------")
def find_squares(lst):
    return [x ** 2 for x in lst]


lst = [1, 2, 3, 4, 5]
squares = find_squares(lst)
print("Squares of each element:", squares)
print("---------------------------------------------------")
def second_smallest(lst):
    unique_lst = list(set(lst))  
    unique_lst.sort()
    if len(unique_lst) > 1:
        return unique_lst[1]  
    else:
        return None  
lst = [7, 2, 5, 3, 8, 2]
second_small = second_smallest(lst)
print("Second Smallest Number:", second_small)
print("---------------------------------------------------")
