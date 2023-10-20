# Escreva a função fizzbuzz que recebe como parâmetro um número inteiro e devolve
# 
# 'Fizz' se o número for divisível por 3 e não for divisível por 5;
# 
# 'Buzz' se o número for divisível por 5 e não for divisível por 3;
# 
# 'FizzBuzz' se o número for divisível por 3 e por 5;
# 
# Caso o número não seja divisível 3 e também não seja divisível por 5,
#ela deve devolver o número recebido como parâmetro.

def fizzbuzz (x):
    if (x%3) == 0 and (x%5) != 0:
        return 'Fizz'
    elif (x%3) != 0 and (x%5) == 0:
        return 'Buzz'
    elif (x%3) == 0 and (x%5) == 0:
        return 'FizzBuzz'
    else:
        return x
    
def test_fizz():
    assert fizzbuzz(3) == 'Fizz'

def test_buzz():
    assert fizzbuzz(5) == 'Buzz'

def test_fizz_buzz():
    assert fizzbuzz(15) == 'FizzBuzz'

def test_notfizz():
    assert fizzbuzz(4) == 4