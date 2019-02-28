import iomodule
import slide
import common

INPUT_FILE = 'data/b_lovely_landscapes.txt'
INPUT_FILE_B = 'data/b_lovely_landscapes.txt'
INPUT_FILE_C = 'data/c_memorable_moments.txt'
INPUT_FILE_D = 'data/d_pet_pictures.txt'
OUTPUT_FILE = 'test.txt'
test = iomodule.read_file(INPUT_FILE_D)
slides = common.generate(test)

iomodule.save_to_file(slides, OUTPUT_FILE)