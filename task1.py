
# Функція жадібного алгоритму
def find_coins_greedy(quantity: int):
    """
    Функція, що знаходить мінімальну кількість монет для заданої суми
    за допомогою жадібного алгоритму.
    Params: сума, яку потрібно видати покупцеві
    Return: словник з кількістю монет кожного номіналу
    """
    result = {}
    coins = [50, 25, 10, 5, 2, 1]
    
    for el in coins:
        result[el] = 0
        while quantity >= el:
            quantity -= el
            result[el] += 1  



    return result




# Тест

amount = 113

print(f'Монети для здачі {find_coins_greedy(amount)}') 




