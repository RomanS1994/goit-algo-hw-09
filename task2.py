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
print(result)  
