import datetime
import multiprocessing

def  read_info(name):
    all_data = []
    with open(name) as file:
        while True:
            line = file.readline()
            all_data.append(line)
            if not line:
                break

filelenames = [f'./file {number}.txt' for number in range(1, 5)]

# линейный вызов
start = datetime.datetime.now()
for file in filelenames:
    read_info(file)
end = datetime.datetime.now()
print(f'{end - start} (линейный)')


# мультипроцессорный вызов
if __name__ == '__main__':
    start = datetime.datetime.now()
    with multiprocessing.Pool(processes=len(filelenames)) as pool:
        pool.map(read_info, filelenames)
    end = datetime.datetime.now()
    print(f'{end - start} (многопроцессорный)')