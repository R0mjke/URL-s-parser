import json
import requests  # импортируем модуль
# открываем файл для записи, в режиме wb
file = open(r'C:\Users\Air\Desktop\test.txt', "wb")
url = requests.get("http://openphish.com/feed.txt")  # делаем запрос
# записываем содержимое в файл; как видите - content запроса
file.write(url.content)
file.close()  # файл скачан

file = open(r'C:\Users\Air\Desktop\test2.txt')  # открываем файл
line = file.readline()  # читаем первую срочку



while(line):

    double_slash = line.find('://')  # находим позицию шебанг
    # находим первый слеш после шебанга
    second_slash = (line.find('/', double_slash + 3))

    protocol = line[0:double_slash]
    domain = line[double_slash + 3: second_slash]
    rel = line[second_slash + 1:]
    
    
    
    
    x = {
        "protocol": protocol,
        "domain": domain,
        "rel_url": rel.rstrip()
    }

    y = json.dumps(x)

    print(y)
    

    line = file.readline()
file.close()
