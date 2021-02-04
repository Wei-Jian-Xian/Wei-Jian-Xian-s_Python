from playsound import playsound
from os import walk

def search_files(files):
    '''
    参数：files：起始文件位置
    '''
    temp =[]
    for i in walk(files):
        for a in list(i[2]):
            temp += [str(i[0]) + '\\' + str(a)]
    return temp

for i in search_files('sounds'):
    try:
        playsound(i)
    except:
        print(f'in {i} ,We meet Some Unknown Error')