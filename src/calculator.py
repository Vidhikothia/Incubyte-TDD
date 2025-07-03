def add(numbers):
    if numbers == "":
        return 0
    parts = numbers.split(",")
    return sum(int(n) for n in parts)
