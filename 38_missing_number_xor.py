def find_missing_number(numbers, n):
    missing = 0
    for number in range(n + 1):
        missing ^= number
    for number in numbers:
        missing ^= number
    return missing
