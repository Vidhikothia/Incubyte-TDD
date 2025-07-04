def add(numbers):
    if numbers == "":
        return 0

    delimiter = ","
    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)
        delimiter = parts[0][2:]
        numbers = parts[1]

    numbers = numbers.replace("\n", delimiter)
    parts = numbers.split(delimiter)
    
    negatives = [int(n) for n in parts if n and int(n) < 0]
    if negatives:
        raise Exception(f"negative numbers not allowed {','.join(map(str, negatives))}")
    
    return sum(int(n) for n in parts if n and int(n) <= 1000)

