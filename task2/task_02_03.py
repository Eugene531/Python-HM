print([i if (i % 3 and i % 5) else [['Fizz', 'FizzBuzz'][i % 5 == 0], 'Buzz'][i % 3 != 0] for i in range(1, 101)])
