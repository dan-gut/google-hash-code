import common
import iomodule as io
from slide import Slide

def pair_pts(slide_A, slide_B):
    com = common.common_elements(slide_A, slide_B)
    inAnotB = len(slide_A.tags - slide_B.tags)
    inBnotA = len(slide_B.tags - slide_A.tags)
    return min(com, inAnotB, inBnotA)

def chain_pts(slides):
    points = 0
    for i in range(len(slides)-1):
        points += pair_pts(slides[i], slides[i+1])
    return points


if __name__ == "__main__":
    data = list(io.read_file("c_memorable_moments.txt"))
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
                SlideList.append(tmp_slide)
        else:
            tmp_slide = Slide()
            tmp_slide.add_photo(photo)
            SlideList.append(tmp_slide)

    print(chain_pts(SlideList))

