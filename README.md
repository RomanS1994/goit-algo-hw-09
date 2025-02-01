# Висновки щодо ефективного використання алгоритмів розміну монет

##  Аналіз жадібного алгоритму

###  Переваги:
- **Дуже швидке виконання**: працює за `O(N)`, де `N` – кількість номіналів монет.
- **Простота реалізації**: проходить по списку монет і видає найбільші можливі номінали.
- **Ефективний для фіксованого набору монет** (наприклад, нашого `50, 25, 10, 5, 2, 1`).

###  Недоліки:
- Не завжди знаходить **оптимальне рішення**, якщо набір монет змінюється.

### ⏳ Час виконання (результати тестування):
- `113`: **0.000003 секунд**
- `43`: **0.000002 секунд**
- `235`: **0.000001 секунд**
- `250000`: **0.000268 секунд**

##  Аналіз алгоритму динамічного програмування

###  Переваги:
- **Завжди знаходить мінімальну кількість монет**.
- Гарантовано працює для будь-якого набору номіналів.

###  Недоліки:
- **Повільніший** за жадібний алгоритм (`O(N * M)`, де `M` – сума).
- Використовує додаткову пам’ять (`O(M)`).

### ⏳ Час виконання (результати тестування):
- `113`: **0.000029 секунд**
- `43`: **0.000011 секунд**
- `235`: **0.000056 секунд**
- `250000`: **0.100393 секунд** (значно довше, ніж жадібний)

##  Висновки
- **Жадібний алгоритм** є **найкращим вибором**, якщо набір монет фіксований, як у більшості валют.
- **Алгоритм динамічного програмування** потрібен, якщо набір монет може змінюватися або потрібно знайти гарантовано мінімальну кількість.
- Для **великих чисел** жадібний алгоритм **виконується у 1000 разів швидше**.

##  Рекомендації щодо використання
| Алгоритм | Коли використовувати |
|----------|---------------------|
| Жадібний | Якщо набір монет фіксований і швидкість важливіша за оптимальність |
| Динамічне програмування | Якщо набір монет змінюється або потрібне 100% мінімальне рішення |

---

Якщо набір монет стандартний (наприклад, євро або долар) – **жадібний алгоритм достатній**.  
Якщо ж потрібно враховувати нестандартні монети – **варто використовувати динамічне програмування**.

