def square(n):
    squares = []
    for number in n:
        squares.append(number*number)
    return squares
num = [1,2,3,4,5]
print(square(num)) # [1,4,9,16,25]