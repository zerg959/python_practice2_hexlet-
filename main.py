### Задача 1

# Дан массив целых чисел. Нужно найти максимальную сумму трёх неповторяющихся элементов массива.

# **Примечания:**
# - размер массива не меньше 3;
# - элементы могут быть нулевыми или отрицательными;
# - в массиве могут встречаться дубликаты, при суммировании они не учитываются

myarr = {2,1,8,0,6,4,8,6,2,4}
def triSum(myarr):
    unique_nums = set(myarr)
    sorted_nums = sorted(unique_nums)
    answer = sum(sorted_nums[-3:])
    return answer


print(triSum(myarr))
### Задача 4
# Реализовать функцию `compress_images()`, которая:
# - принимает на вход директорию;
# - находит внутри неё картинки;
# - уменьшает свойство `size` в их метаданных в 2 раза;
# - возвращает обновлённую директорию со сжатыми картинками и всеми остальными данными.

# Картинками считаются все файлы, заканчивающиеся на `.jpg`.
original_directory = {
    'photo1.jpg': {'size': 100, 'par1': 80, 'par2': 600},
    'photo2.jpg': {'size': 150, 'par4': 1200, 'par3': 900},
    'document.txt': {'size': 2048},
        'second_dir': {
            'photo3.jpg': {'size': 150, 'par4': 1200, 'par3': 900}
            },'document2.txt': {'size': 2048},
            }
def compress_images(mydict):
    for filename, file_data in mydict.items():
        if filename.lower().endswith('.jpg'):
            if 'size' in file_data:
                old_size = file_data['size']
                new_size = old_size / 2
                file_data['size'] = new_size
    return mydict
print(compress_images(original_directory))

### Задача 3

# Прыгающее число — это число, в котором все соседние цифры отличаются на 1.

# Нужно вернуть:
# - `"Jumping!!"` — если число прыгающее;
# - `"Not!!"` — если нет.
def jumping_num(mynum):
    num_str = str(mynum)
    if len(num_str) == 1:
        return "Jumping!!"
    
    for i in range(len(num_str) - 1):
        current_digit = int(num_str[i])
        next_digit = int(num_str[i + 1])

        if abs(current_digit - next_digit) != 1:
            return "Not!!"    
    return "Jumping!!"

testnum = 4343456
print(jumping_num(testnum))


### Задача 5

# Создать класс, имитирующий экран выбора, где курсор может перемещаться влево и вправо.

# Требования:
# - курсор начинается с индекса `0`;
# - метод `display()` возвращает строковое представление списка;
# - выбранный элемент отображается в квадратных скобках;
# - методы `to_the_right` и `to_the_left` перемещают курсор;
# - когда курсор доходит до конца, он возвращается к началу.
class Menu:
    def __init__(self, items):
        self.items = items
        self.cursor_index = 0

    def display(self):
        result = []
        for i, item in enumerate(self.items):
            if i == self.cursor_index:
                result.append(f"[{item}]")
            else:
                result.append(str(item))
        return "[" + ", ".join(result) + "]"

    def to_the_right(self):
        self.cursor_index = (self.cursor_index + 1) % len(self.items)

    def to_the_left(self):
        self.cursor_index = (self.cursor_index - 1) % len(self.items)

x = Menu([1,2,3,4])
print(x.display())
x.to_the_left()
print(x.display())
x.to_the_left()
print(x.display())
x.to_the_right()
print(x.display())
x.to_the_right()
print(x.display())