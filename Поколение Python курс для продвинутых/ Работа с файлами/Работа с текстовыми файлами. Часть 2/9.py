from functools import reduce
def read_csv():
    with open('data.csv') as file:
        keys = file.readline().strip().split(',')
        data = list(map(lambda line: dict(zip(keys, line.strip().split(','))), file.readlines()))
        return data