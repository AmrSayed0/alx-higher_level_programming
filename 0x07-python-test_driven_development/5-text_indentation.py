#!/usr/bin/python3

def text_indentation(text):
    # Check if text is a valid string
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    # Create a list of separators
    separators = ['.', '?', ':']

    # Loop over each separator and replace it with the separator followed by two new lines
    for sep in separators:
        text = text.replace(sep, sep + "\n\n")

    # Split the formatted text into lines, strip any leading or trailing whitespaces, and join them back together with newlines
    lines = [line.strip() for line in text.split("\n")]
    formatted_text = "\n".join(lines)

    # Print the formatted text
    print(formatted_text)
