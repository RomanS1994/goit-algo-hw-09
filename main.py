
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

# print(f'Монети для здачі {find_coins_greedy(amount)}') 





# Функція динамічного програмування
def find_min_coins(quantity: int) -> dict:
    """
    Функція, що знаходить мінімальну кількість монет для заданої суми
    за допомогою динамічного програмування.
    :param amount: сума, яку потрібно видати покупцеві
    :return: словник з кількістю монет кожного номіналу
    """
    coins = [50, 25, 10, 5, 2, 1]  # Доступні номінали монет
    dp = [float('inf')] * (quantity + 1)
    dp[0] = 0
    # print(dp)
    coin_used = [0] * (quantity + 1)
    
    for coin in coins:
        for j in range(coin, quantity + 1):
            if dp[j - coin] + 1 < dp[j]:
                dp[j] = dp[j - coin] + 1
                coin_used[j] = coin
    
    if dp[quantity] == float('inf'):
        return {}  # Якщо сума не може бути досягнута
    


    change = {}
    while quantity > 0:
        coin = coin_used[quantity]
        if coin in change:
            change[coin] += 1
        else:
            change[coin] = 1
        quantity -= coin
    
    return change


# Тест
amount = 113
result = find_min_coins(amount)
# print(result)  


import time

def test_algorithms(sums):
    print("Тестування алгоритмів на різних сумах:\n")
    
    for sum_ in sums:
        print(f"Сума для розміну: {sum_}")
        
        # Тест - жадібний алгоритм
        start_time = time.time()
        greedy_result = find_coins_greedy(sum_)
        greedy_time = time.time() - start_time
        greedy_coins = sum(greedy_result.values())
        
        # Тест - алгоритм динамічного програмування
        start_time = time.time()
        dp_result = find_min_coins(sum_)
        dp_time = time.time() - start_time
        dp_coins = sum(dp_result.values())
        
        print(f"Жадібний алгоритм: {greedy_result} (Кількість монет: {greedy_coins})")
        print(f"Час виконання жадібного алгоритму: {greedy_time:.6f} секунд")
        print(f"Динамічне програмування: {dp_result} (Кількість монет: {dp_coins})")
        print(f"Час виконання динамічного програмування: {dp_time:.6f} секунд")
        print("-" * 50 + "\n")

if __name__ == "__main__":
    # Тестуємо на різних сумах
    test_sums = [113, 43, 235, 250000]
    test_algorithms(test_sums)