f = open("./str.txt", encoding='utf-8')
while True:
    line = f.readline()
    if line:
        try:
            row = line.split("：")
            print(f'[**{row[0]}**]({row[1]})')
        except IndexError:
            pass

    else:
        break