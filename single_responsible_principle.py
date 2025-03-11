def math_operations(numbers : list[int]) -> None:
    print(f"Mean is {sum(numbers)/len(numbers)}")
    print(f"Max is {max(numbers)}")

def mean(numbers : list[int]) -> float:
    return sum(numbers)/len(numbers)

def max_value(numbers : list[int]) -> float:
    return max(numbers)