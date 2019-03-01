import random
from tags_on_slides import get_tags_slides_dict


def delete_all_elements_containing(a_dict, id):
    out_dict = {}
    for key in a_dict:
        if not id in a_dict[key]:
            out_dict[key] = a_dict[key]
    return out_dict

# d = {'a': [1, 4], 'b': [4, 6], 'c': [5, 7]}
# new_d = delete_all_elements_containing(d, 1)
# print(new_d)


tags_slides_dict = get_tags_slides_dict('data/b_lovely_landscapes.txt')

tag = random.choice(list(tags_slides_dict.keys()))
# tag = 'tr5fv'
sequence = [tags_slides_dict[tag][0], tags_slides_dict[tag][1]]
tags_slides_dict = delete_all_elements_containing(tags_slides_dict, sequence[-2])
print(sequence)

while len(tags_slides_dict) > 0:
    # to ponizej mozna by chyba zoptymalizowac
    # https://stackoverflow.com/questions/11963711/what-is-the-most-efficient-way-to-search-nested-lists-in-python
    # https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary
    for key in tags_slides_dict:
        last_id = sequence[-1]
        if last_id in tags_slides_dict[key]:
            interesting_item = tags_slides_dict[key].copy()
            interesting_item.remove(last_id)
            new_id = interesting_item[0]
            sequence.append(new_id)
            break

    tags_slides_dict = delete_all_elements_containing(tags_slides_dict, sequence[-2])
    print(len(sequence), len(tags_slides_dict))

print(sequence)

# sequence >> output format