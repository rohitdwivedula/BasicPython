# Functions Assignment
# Write a Python function that takes a number as a parameter and check the number is prime or not.

def prime_or_not (n):
    if(n==1):
        return 0
    elif(n==2):
        return 1
    i=3
    while(i<=math.sqrt(n)+1):
        if(n%i == 0):
            return 0
        i+=1
    return 1
'''
2. Write a Python function to check if a number is perfect or not. A perfect
number is a positive integer that is equal to the sum of all its positive divisors,
excluding the number itself. Equivalently, a perfect number is equal to half
the sum of all its positive divisors, including itself.
Example: 6 is the first perfect number, as 1, 2, and 3 are its proper divisors,
and 1+2+3 = 6. The next perfect number is 28, followed by 496 and 8128.
'''

def is_perfect(n):
    div_sum = 0
    i=1
    while(i!=n):
        if(n%i == 0):
            div_sum+=i
        i+=1
    if(div_sum == n):
        return 1
    return 0;

'''
3. Write a Python function that checks whether a passed string is a palindrome or
not.
'''
def isPalindrome(text):
    i = 0
    j = len(text) - 1
    while(i<j):
        if(text[i] == text[j]):
            i+=1
            j-=1
        else:
            return 0
    return 1

'''
4. Write a Python function that prints the first n rows of Pascal’s triangle.
'''



'''
5. Write a Python program that accepts a hyphen-separated sequence of words
as input and prints the words in a hyphen-separated sequence after sorting
them alphabetically. Sample Items: green-red-yellow-black-white
Expected Result: black-green-red-white-yellow
'''


'''
6. Write a Python script to convert the Celsius scale to the Fahrenheit scale, and
vice-versa.
'''
def Cels_to_Farh(cels):
    return ((9.00/5.00) * cels) + 32.0

def Fahr_to_Cels(fahr):
    return (fahr - 32.00)*(5.00/9.00)

'''
7. Rewrite the solution to the previous problem to use lambda functions.
'''

'''
8. Implement the functions map(), filter() and reduce() with user-defined
functions. As an additional exercise, modify these functions to return
generators instead of lists, to make them more efficient.
'''

'''
9. Write a function to compute n C r and n P r. Try using reduce() to solve this
problem.
'''

'''
10. Write a decorator that measures the running time of the decorated functions,
i.e. the time taken for the function from the moment it is called to the point
where it finishes executing. Print this time. The inbuilt time module can come in
handy.
'''
