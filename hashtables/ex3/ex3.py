def intersection(arrays):

    d = dict()

    for arr in arrays:
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
    result = [x for x in d if d[x]==len(arrays)]

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
