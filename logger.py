
def log(x):
    with open('HomeWorkPython 13.12.22/file.txt', 'a', encoding='utf-8') as f:
        f.write(f'{x}\n')
    with open('HomeWorkPython 13.12.22/file.csv', 'a', encoding='utf-8') as f:
        f.write(f'{x}\n')



