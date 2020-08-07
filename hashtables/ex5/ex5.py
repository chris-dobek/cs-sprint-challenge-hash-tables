# Your code here



def finder(files, queries):

    result = []
    
    d = dict()

    for file in files:
        parts = file.split("/")
        filename = parts[-1]
        if filename not in d:
            d[filename] = []
        d[filename].append(file)

    for q in queries:
        if q in d:
            result.extend(d[q])

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
