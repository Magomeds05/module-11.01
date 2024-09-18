import multiprocessing
import datetime

#Создайте функцию read_info(name), где name - название файла. Функция должна:
#Создавать локальный список all_data.
#Открывать файл name для чтения.
#Считывать информацию построчно (readline), пока считанная строка не окажется пустой.
#Во время считывания добавлять каждую строку в список all_data.
#Этих операций достаточно, чтобы рассмотреть преимущество многопроцессного выполнения программы над линейным.
#Создайте список названий файлов в соответствии с названиями файлов архива.
#Вызовите функцию read_info для каждого файла по очереди (линейно) и измерьте время выполнения и выведите его в консоль.
#Вызовите функцию read_info для каждого файла, используя многопроцессный подход: контекстный менеджер with и объект Pool. Для вызова функции используйте метод map, передав в него функцию read_info и список названий файлов. Измерьте время выполнения и выведите его в консоль.

def read_info(name):
    data = [] #Создавать локальный список
    with open(name, 'r') as file: #Открывать файл name для чтения.
        while True:
            str_ = file.readline()
            if not str_:
                break
            data.append(str_)

# Линейный вызов
filenames = [f'./file {number}.txt' for number in range(1, 5)]
start = datetime.datetime.now()
for i in filenames:
    read_info(i)
end = datetime.datetime.now()
result_time = end - start
print(result_time)


if __name__ == '__main__':
    start = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames) #для применения функции к каждому элементу итерируемого объекта
    #end = datetime.datetime.now()
    #print(end - start)




