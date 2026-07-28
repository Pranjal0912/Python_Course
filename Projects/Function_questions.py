# 1. This program finds the maximum of three numbers using a function with only positional arguments only

def maximum_of_three(a, b, c, /):
    if a>b:
        if a>c:
            return a
        else:
            return c
    elif b>c:
        return b
    else:
        return c

if __name__ == "__main__":

    num = maximum_of_three(12,10,15)
    print(num)

# 2. This program finds the simiple interest using a function with only keyword arguments only

def simple_interest(*, P, R, T):
    """This function calculates simple interest given Principal amount, Rate and Time."""
    simpleInterest = int((P*R*T)/100)
    return simpleInterest

if __name__ == "__main__":

    cost = simple_interest(P = 1000, R = 2, T = 10)
    print(cost)

# 3. Write a program to detect if the sentence is a Pangram Phrase or not 
# PS:- A Pangram is a sentence that contains every letter of the alphabet at least once.

def pangram_check(sentence):
    """This function checks if a given sentence is a Pangram Phrase or not."""
    new = ""
    for char in sentence:
        if ord(char) >= 65 and ord(char) <= 122:
            new += char
    set_1 = set(new.lower())
    set_1.discard(" ")
    # print(len(set_1), set_1)
    return True if len(set_1) == 26 else False


if __name__ == "__main__":

    phrase = "The #%#@564quick brown fox jumps over the lazy dog"
    if pangram_check(phrase):
        print("The sentence is a Pangram!")
    else:
        print("The sentence is not a Pangram!")