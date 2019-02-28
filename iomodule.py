def parse(line, number):
    data = line.split(' ')
    return number, data[0], int(data[1]), data[2:]


def read_file(filepath):
    with open(filepath) as fp:
        number_of_files = int(fp.readline().strip())
        i = 0
        for line in fp:
            yield parse(line.strip(), i)
            i += 1


def save_to_file(slide_list, output_filename):
    with open(output_filename, 'w') as fp:
        fp.writelines(str(len(slide_list)))
        fp.write('\n')
        for slide in slide_list:
            fp.write(str(slide))
            fp.write('\n')


