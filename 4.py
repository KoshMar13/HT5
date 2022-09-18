# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def rle(text):
    result = list()
    count = 0
    if len(text) == 1:
        result.append((1, (text[0])))
        return result
    for i in range(len(text)):
        count += 1
        if (i + 1) == len(text) or text[i] != text[i+1]:
            result.append((count, (text[i])))
            count = 0
    return result


def unrle(lst):
    result = ""
    for i in lst:
        result += i[0]*i[1]
    return result


with open("inp4.txt", "r", encoding='utf8') as finp:
    for line in finp:
        inp = line.split()
    # print(inp)
ans = rle(line)

# print(*ans)
ans2 = unrle(ans)
# print(ans2)

with open('output4.txt', 'w') as fout:
    fout.write(str(ans))
    fout.write('\n'*2)
    fout.write(ans2)
