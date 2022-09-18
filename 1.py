# Напишите программу, удаляющую из текста все слова, содержащие "абв".
# Входные и выходные данные хранятся в отдельных текстовых файлах.

sample = input('Insert removing text: ')
with open('input1.txt', 'r', encoding='utf8') as finp:
    for line in finp:
        inp = line.split()
        for i in inp:
            if sample in inp:
                inp.remove(sample)
        ans = ' '.join(inp)
        print(ans)
with open('output1.txt', 'w') as fout:
    fout.write(ans)
