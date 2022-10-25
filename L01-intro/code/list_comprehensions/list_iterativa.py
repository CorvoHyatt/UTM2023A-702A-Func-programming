
def func():
    squares = []
    for value in range(1, 11):
        square = value ** 2
        squares.append(square)

    print(squares)

if __name__ == '__main__':
    func()