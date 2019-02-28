import itertools
import points
import slide

def common_elements(slide1, slide2):
    return len(slide1.tags & slide2.tags)


def make_slides(photos):
    verticals = []
    horizontals = []
    slides = []
    for p in photos:
        if p[1] == 'H':
            horizontals.append(p)
        else:
            verticals.append(p)
    for h in horizontals:
        s = slide.Slide()
        s.add_photo(h)
        slides.append(s)
    verticals = sorted(verticals, key=lambda v: len(v[-1]))
    for i in range(len(verticals)//2):
        s = slide.Slide()
        s.add_photo(verticals[i])
        s.add_photo(verticals[-1-i])
        slides.append(s)
    return slides


def make_optimal_chain(slides):
    chains = itertools.permutations(slides)
    maximal = None
    max_score = -1
    i = 0
    for chain in chains:
        #TODO SCORE
        score = points.chain_pts(chain)
        if score > max_score:
            max_score = score
            maximal = chain
    return maximal


def make_chunks(slides, chunksize=8):
    n_chunks = len(slides) // chunksize
    if n_chunks > 1:
        return [slides[i:i + chunksize] for i in range(0, len(slides), chunksize)]

def generate(photos, chunksize=6):
    slides = make_slides(photos)
    chunks = make_chunks(slides, chunksize)
    n_chunks = len(chunks)
    slides = []
    i = 0
    for chunk in chunks:
        print("{:.2%}".format(i/n_chunks))
        slides.extend(make_optimal_chain(chunk))
        i+=1
    print(points.chain_pts(slides))
    return slides
