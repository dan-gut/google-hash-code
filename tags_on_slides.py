from iomodule import read_file


def get_tags_slides_dict(path_to_file):
    data_gen = read_file(path_to_file)
    tags_on_slides = {}
    counter = 0
    for item in data_gen:
        for tag in item[2]:
            if tag in tags_on_slides:
                tags_on_slides[tag].append(counter)
            else:
                tags_on_slides[tag] = []
        counter += 1
    with open('out.txt', 'w') as fout:
        fout.write(str(tags_on_slides))
    return tags_on_slides


if __name__ == '__main__':
    tags_slides_dict = get_tags_slides_dict('data/c_memorable_moments.txt')
    print(tags_slides_dict['tw52'])
