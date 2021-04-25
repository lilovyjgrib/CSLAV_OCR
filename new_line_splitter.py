def get_strings(boxes, threshn):
    def pre_strings(boxes, edge, threshn):
        boxes.sort(key=lambda box: box['rect'][edge])
        strings = []
        for box in boxes:
            box['mark'] = 1
        for idx, box in enumerate(boxes):
            if box['mark'] == 1:
                strings.append([])
                strings[-1].append(box)
                strings[-1][-1].pop('mark')
                box['mark'] = 0
                for idx1 in range(idx, len(boxes)):
                    fut = boxes[idx1]['rect'][edge]
                    cur = box['rect'][edge]
                    if boxes[idx1]['mark'] == 1 and abs(cur - fut) < threshn:
                        strings[-1].append(boxes[idx1])
                        strings[-1][-1].pop('mark')
                        boxes[idx1]['mark'] = 0
        return strings

    def find_string_mean(string, t):
        string_mean = 0
        for el in string:
            if t == 'topline':
                string_mean += el['rect'][1]
            if t == 's':
                string_mean += (el['rect'][3] - el['rect'][1]) * (el['rect'][2] - el['rect'][0])
        string_mean = string_mean / len(string)
        return string_mean

    strings_by_b = pre_strings(boxes, 3, threshn)
    strings = strings_by_b
    i = 1
    while i < len(strings):
        string = strings_by_b[i]
        prevstring = strings_by_b[i - 1]
        mean_t = find_string_mean(prevstring, 'topline')
        mean_s = find_string_mean(prevstring, 's')
        j = 0
        while j < len(string):
            el = string[j]
            el_s = (el['rect'][3] - el['rect'][1]) * (el['rect'][2] - el['rect'][0])
            if abs(el['rect'][1] - mean_t) < 10 and el_s / mean_s < 4:
                prevstring.append(el)
                del string[j]
            else:
                j += 1
        if [] in strings:
            strings.remove([])
        else:
            i += 1
    for idx in range(len(strings)):
        strings[idx].sort(key=lambda string: string['rect'][0])

    return strings