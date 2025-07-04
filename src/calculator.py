import re

def add(numbers):
    if numbers == "":
        return 0

    delimiter = ","
    if numbers.startswith("//"):
        delimiter_line, numbers = numbers.split("\n", 1)
        if delimiter_line.startswith("//["):
            delimiters = re.findall(r"\[(.*?)\]", delimiter_line)
            delimiter = "|".join(map(re.escape, delimiters))
        else:
            delimiter = re.escape(delimiter_line[2:])

    numbers = re.sub(r"\n", ",", numbers)
    parts = re.split(delimiter, numbers)

    negatives = [int(n) for n in parts if n and int(n) < 0]
    if negatives:
        raise Exception(f"negative numbers not allowed {','.join(map(str, negatives))}")

    return sum(int(n) for n in parts if n and int(n) <= 1000)
