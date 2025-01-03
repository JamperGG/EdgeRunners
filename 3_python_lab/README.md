# Звіт: Опис класу `TK_41` та його методів

## Опис класу `TK_41`

У класі `TK_41` була реалізована модель студента з кількома основними атрибутами та методами для обробки інформації про нього. Клас надає можливість працювати з такими даними, як прізвище, ім'я, оцінки та стипендія.

### Атрибути:
- **Класові атрибути**: були створені змінні, що відносяться до самого класу, зокрема для збереження загальної кількості студентів та сумарних оцінок.
- **Інкапсуляція**: для деяких атрибутів використано приватний доступ, щоб вони були доступні лише всередині класу, та захищений доступ, який дозволяє використовувати ці атрибути тільки в межах класу або його нащадків.
- **Стипендія**: для кожного студента зберігається інформація про стипендію, яка змінюється в залежності від результатів сесії.

### Конструктор:
Конструктор класу ініціалізує всі основні атрибути студента, включаючи оцінку, прізвище, ім'я та групу. У цьому ж методі також відбувається оновлення загальних статистичних даних для класу, таких як кількість студентів та сума їхніх оцінок.

### Методи:
- **Публічні методи**: основний метод для обчислення стипендії після сесії, методи для роботи з хобі, а також додаткові методи для взаємодії з об'єктами класу.
- **Захищені методи**: методи, які можуть бути викликані тільки в межах класу та його нащадків.
- **Приватні методи**: ці методи призначені для внутрішнього використання в класі і не повинні бути викликані ззовні.

### Альтернативні конструктори:
Також були реалізовані альтернативні конструктори, що дозволяють створювати об'єкти класу з використанням повного імені студента, розділеного на прізвище та ім'я. Це дозволяє зручніше створювати об'єкти класу, не передаючи ці атрибути окремо.

## 2. Основні проблеми

### Проблема з доступом до приватних методів:
Приватні методи не можуть бути викликані безпосередньо ззовні класу. Це може створити труднощі, якщо розробник хоче звернутись до цих методів з інших частин програми.

### Рішення:
Для роботи з приватними методами рекомендується використовувати їх лише всередині класу або створювати для них публічні чи захищені методи доступу. Також можна використовувати спеціальні можливості Python для обходу обмежень доступу, хоча це не є рекомендованим з точки зору інкапсуляції.


