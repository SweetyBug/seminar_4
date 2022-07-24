def matches(dictionary_p, dictionary_w, dictionary_n, com):
    match = list(input('Введите информацию о матче, чтобы закончить введите "end": ').split(';'))
    if 'end' in match:
        return 1
    elif int(match[1]) > int(match[3]):
        if match[0] in dictionary_w:
            a = int(dictionary_w[match[0]])
            dictionary_w[match[0]] = a + 1
        else:
            dictionary_w[match[0]] = 1
        if match[2] in dictionary_p:
            b = int(dictionary_p[match[2]])
            dictionary_p[match[2]] = b + 1
        else:
            dictionary_p[match[2]] = 1
        if match[0].lower() not in com:
            com.append(match[0].lower())
        if match[2].lower not in com:
            com.append(match[2].lower())
        matches(dictionary_p, dictionary_w, dictionary_n, com)
    elif int(match[1]) < int(match[3]):
        if match[0] in dictionary_p:
            a = int(dictionary_p[match[0]])
            dictionary_p[match[0]] = a + 1
        else:
            dictionary_p[match[0]] = 1
        if match[2] in dictionary_w:
            b = int(dictionary_w[match[2]])
            dictionary_w[match[2]] = b + 1
        else:
            dictionary_w[match[2]] = 1
        if match[0].lower() not in com:
            com.append(match[0].lower())
        if match[2].lower() not in com:
            com.append(match[2].lower())
        matches(dictionary_p, dictionary_w, dictionary_n, com)
    elif int(match[1]) == int(match[3]):
        if match[0] in dictionary_n:
            a = int(dictionary_n[match[0]])
            dictionary_n[match[0]] = a + 1
        else:
            dictionary_n[match[0]] = 1
        if match[2] in dictionary_n:
            b = int(dictionary_n[match[2]])
            dictionary_n[match[2]] = b + 1
        else:
            dictionary_n[match[2]] = 1
        if match[0].lower() not in com:
            com.append(match[0].lower())
        if match[2].lower() not in com:
            com.append(match[2].lower())
        matches(dictionary_p, dictionary_w, dictionary_n, com)
def ochki(dictionary_p, dictionary_w, dictionary_n, com):
    for i in com:
        mas = [i]
        count_och = 0
        count_game = 0
        if i.title() in dictionary_w:
            count_game += int(dictionary_w[i.title()])
            count_och += int(dictionary_w[i.title()]) * 3
            mas.append(dictionary_w[i.title()])
        else:
            mas.append(0)
        if i.title() in dictionary_n:
            count_game += int(dictionary_n[i.title()])
            count_och += int(dictionary_n[i.title()])
            mas.append(dictionary_n[i.title()])
        else:
            mas.append(0)
        if i.title() in dictionary_p:
            count_game += int(dictionary_p[i.title()])
            mas.append(dictionary_p[i.title()])
        else:
            mas.append(0)
        mas.insert(1, count_game)
        mas.append(count_och)
