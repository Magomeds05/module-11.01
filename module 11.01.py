import multiprocessing
import datetime

def read_info(name):
    data = [] #Создавать локальный список
    with open(name, 'r', encoding= 'utf-8') as file: #Открывать файл name для чтения.
        while True:
            str_ = file.readline()
            if not str_:
                break
            data.append(str_)


filenames = [f'./file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':
    start = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames) #для применения функции к каждому элементу итерируемого объекта
    end = datetime.datetime.now()
    print("Многопроцессный:", end - start)
    start = datetime.datetime.now()
    for i in filenames:
        read_info(i)
    end = datetime.datetime.now()
    result_time = end - start
    print("Линейный: ", result_time)





