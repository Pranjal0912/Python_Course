header = ['Name', 'Age', 'City']
data = [['james', 25, 'New York'], ['lily', 30, 'Los Angeles'], ['mike', 35, 'Chicago'], ['sarah', 28, 'Houston']]

# For each column, create a dictionary where every unique column value becomes a key, and all rows containing that value are stored together in a list.

result = []

for i in range(len(header)):
    newdict = {}
    for row in data:
        if row[i] not in newdict:
            newdict[row[i]] = [row]
        else:
            newdict[row[i]].append(row)

    result.append(newdict)

print(result)

# If i wanted to create a list of dictionaries where each element of the list 'header' is a key and the corresponding value is the element of the list 'data' at the same index, I can use the following code:

result = []

for row in data:
    newdict = {}
    for i in range(len(header)):
        newdict[header[i]] = row[i]

    result.append(newdict)

print(result)

# The above code can be simplified using a list comprehension and the zip function as follows:

result = [dict(zip(header, row)) for row in data]
print(result)
