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
    verticals = sorted(verticals, lambda v: len(v[-1]))