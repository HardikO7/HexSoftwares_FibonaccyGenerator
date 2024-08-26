# fibonaccy series generator 
series_len = int(input("Enter the series lenth : \n"))

fibonacci_sequence = []
def fibonacci(series_len):
    if series_len < 0:
        return "choose a positive number. "
    first_term = 0
    second_term = 1
    if series_len == 1:
        fibonacci_sequence.append(first_term)
    elif series_len == 2:
        fibonacci_sequence.extend([first_term,second_term])
    else:
        fibonacci_sequence.extend([first_term,second_term])
        for i in range (2,series_len):
            next_terms = first_term + second_term
            fibonacci_sequence.append(next_terms)
            first_term = second_term
            second_term = next_terms
    return fibonacci_sequence
        
print(fibonacci(series_len))
        