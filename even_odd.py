#find if sum of even element numbers or odd element numbers is greater

def solution(numbers):
    even_sum = sum(numbers[i] for i in range(0, len(numbers), 2))
    odd_sum = sum(numbers[i] for i in range(1, len(numbers), 2))
    
    if even_sum > odd_sum:
        return "even"
    elif odd_sum > even_sum:
        return "odd"
    else:
        return "equal"
