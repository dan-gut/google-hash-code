import iomodule as io
from random import shuffle
from slide import Slide

data = list(io.read_file("a_example.txt"))
SlideList = []

tmp_ver = []
for photo in data:
    if photo[1] == 'V':
        tmp_ver.append(photo)
        if len(tmp_ver) == 2:
            tmp_slide = Slide()
            tmp_slide.add_photo(tmp_ver[0])
            tmp_slide.add_photo(tmp_ver[1])
            tmp_ver = []
    else:
        tmp_slide = Slide()
        tmp_slide.add_photo(photo)

    SlideList.append(tmp_slide)

io.save_to_file(SlideList, "test.txt")