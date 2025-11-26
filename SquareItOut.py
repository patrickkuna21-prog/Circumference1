def square_filter(start,end):
    numbers = list(range(start, end + 1))
    squares = [num ** 2 for num in numbers]
    even_squares = [sq for sq in squares if sq % 2 == 0]
    odd_squares = [sq for sq in squares if sq % 2 != 0]
    print("All squares:", squares)
    print("Even squares:", even_squares)
    print("Odd squares:", odd_squares)
square_filter(1,10)