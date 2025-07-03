def add(numbers):
    if numbers == "":
        return 0
    numbers = numbers.replace("\n", ",")
    parts = numbers.split(",")
    return sum(int(n) for n in parts)
