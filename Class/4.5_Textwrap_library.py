import textwrap # textwrap is a library that provides functions to format and wrap texts.

# 1. textwrap.wrap(): Breaks a long string into a list of lines of specified width.
text = "This is an example of a long string that needs to be wrapped into multiple lines."
wrapped_text = textwrap.wrap(text, width = 20) # This returns a list so 'wrapped_text' will be a list of strings, each with a maximum width of 20 characters.

print(wrapped_text) # Output: ['This is an example', 'of a long string', 'that needs to be', 'wrapped into', 'multiple lines.']
# In the output, the last line may be shorter than 20 characters if the total length of the string is not a multiple of 20.

# 2. textwrap.fill(): Similar to wrap() but returns a single string with embedded newlines instead of a list of strings.
filled_text = textwrap.fill(text, width = 10) # This will return a single string where the text is wrapped to a width of 10 characters and includes newline characters to seperate the lines.

print(filled_text) # Output: 

# This is an
# example of
# a long
# string
# that
# needs to
# be
# wrapped
# into
# multiple
# lines.
#  In the output, the last line may be shorter than 10 characters if the total length of the string is not a multiple of 10.

# 3. textwrap.shorten(): Shortens a string to a specified width, adding an ellipsis (...) if the string is too long.
shortened_text = textwrap.shorten(text, width = 10)

print(shortened_text) # `Output: "This is..." 
# In the output, the string is shortened to a maximum width of 10 characters, and an ellipsis is added at the end to indicate that the text has been truncated.

# 4. textwrap.indent(): Adds a specified prefix/string to the beginning of each line in a given text.
text2 = "Python is a very popular programming language.\nIt is widely used for many things such as web development and data science.\nIt is also a great language for beginners."
indented_text = textwrap.indent(text2, prefix = "->") # This will add the prefix "->" to the beginning of each line in the text. The output will have each line of the original text prefixed with "->".

print(indented_text) # Output:
# ->Python is a very popular programming language.
# ->It is widely used for many things such as web development and data science.
# ->It is also a great language for beginners.

# 5. textwrap.dedent(): Removes any common leading whitespace from every line in the input text.
text3 = """    This is an example of a text with leading whitespace."""
dedented_text = textwrap.dedent(text3) # This will remove the leading whitespace from the text. The output will be the same text without the leading spaces.
print(dedented_text)