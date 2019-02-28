from iomodule import read_file


def get_tags_slides_dict(path_to_file):
    data_gen = read_file(path_to_file)
    tags_on_slides = {}
    counter = 0
    for item in data_gen:
        for tag in item[3]:
            if tag in tags_on_slides:
                tags_on_slides[tag].append(counter)
            else:
                tags_on_slides[tag] = [counter]
        counter += 1

    out_dict = remove_keys_with_less_than_2_ids(tags_on_slides)
    with open('out.txt', 'w') as fout:
        fout.write(str(out_dict))
    return tags_on_slides


def remove_keys_with_less_than_2_ids(a_dict):
    out_dict = {}
    for key in a_dict:
        if len(a_dict[key]) >= 2:
            out_dict[key] = a_dict[key]
    return out_dict


if __name__ == '__main__':
    tags_slides_dict = get_tags_slides_dict('data/c_memorable_moments.txt')
    print(tags_slides_dict['tw52'])
