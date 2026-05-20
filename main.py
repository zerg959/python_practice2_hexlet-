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