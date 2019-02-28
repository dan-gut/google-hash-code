def parse(line):
    data = line.split(' ')
    return data[0], int(data[1]), data[2:]


def read_file(filepath):
    with open(filepath) as fp:
        number_of_files = int(fp.readline().strip())
        for line in fp:
            yield parse(line.strip())

