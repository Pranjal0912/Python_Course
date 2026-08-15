# Write a program that returns a list of unique elements from the given list. The order of elements in the output list does not matter. The output list should not contain any duplicate elements.

# Helper function
def unique(*args):
    nums = set(args)
    return list(nums)



# Main function
if __name__ == "__main__": 
    nums = input("Enter the numbers: ")
    nums = [int(n) for n in nums.split()] # First we split the string which we got from the user based on whitespaces in to a list then got a new list by typecasting each element of that string list to int.
    print(unique(*nums)) # Using "*" for unpacking each element of the list



# Below is the approach that we can use if we were told to retain the original order of the elements in the output list. In that case we can use the following code:

def unique2(*args):
    # Now each object in 'args' tuple is a tuple of two elements where the first element is the index of the number in the original list and the second element is the number itself. This way we can retain their original order passed by the user.
    dict1 = {}
    for n in args:
        if n[1] not in dict1:
            dict1[n[1]]=n[0]
    list1 = list(dict1.keys())
    print(list1)

# Now lets see what if we were told to retain the orignal order of the elements in the output list. In that case we can use the following code:

nums = input("Enter the numbers: ") # Here ' nums ' is a string with whitespaces
nums = nums.split() # Now ' nums ' is converted to a list of string with each number 
# Lets convert it to a list of int:
for i in range(len(nums)):
    nums[i] = int(nums[i]) # Now ' nums ' is a list of int
    
# Lets now make a view object that takes pairs index and the number at that index in ' nums ' list
new = enumerate(nums)
# Now we will unpack each element from that view object and pass it to the function ' unique2 ':
unique2(*new)