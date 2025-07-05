import re

def add(numbers):
    # If the input is an empty string, return 0
    if numbers == "":
        return 0

    delimiter = ","  # Default delimiter is a comma

    # Check if there's a custom delimiter defined at the beginning
    if numbers.startswith("//"):
        delimiter_line, numbers = numbers.split("\n", 1)  # Separate delimiter declaration from numbers

        if delimiter_line.startswith("//["):
            # Handle multiple or long custom delimiters (e.g. //[***][%%])
            delimiters = re.findall(r"\[(.*?)\]", delimiter_line)
            delimiter = "|".join(map(re.escape, delimiters))  # Combine them into a regex pattern
        else:
            # Handle single-character custom delimiter (e.g. //;\n)
            delimiter = re.escape(delimiter_line[2:])  # Escape special regex characters if any

    # Replace newline characters with commas (to normalize mixed input like "1\n2,3")
    numbers = re.sub(r"\n", ",", numbers)

    # Split the string into number parts using the final delimiter(s)
    parts = re.split(delimiter, numbers)

    # Check for negative numbers and raise an exception if any are found
    negatives = [int(n) for n in parts if n and int(n) < 0]
    if negatives:
        raise Exception(f"negative numbers not allowed {','.join(map(str, negatives))}")

    # Convert all valid parts to integers, ignoring empty strings and numbers > 1000
    return sum(int(n) for n in parts if n and int(n) <= 1000)
