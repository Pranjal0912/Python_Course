url_name = input("Give the URL/URI of the website: ")
# Sample URL = https://www.udemy.com/course
protocol = url_name[:url_name.find(":")] # string slicing till the index where ':' first appears in the string 
domain_name = url_name.split(".")[1] # split the string into 3 parts based on "." and give the element at index = 1 for domain name 
page_name = url_name[url_name.rfind("/")::1] # string slicing starting from the last '/' till the end 

print(f'''--URL/URI Parsing---
- Protocol: {protocol}
- Domain Name: {domain_name}
- Page Name: {page_name}''')

