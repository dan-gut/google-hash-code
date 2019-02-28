class Slide(object):
    def __init__(self):
        self.photos = []
        self.tags = set()

    def add_photo(self, photo):
        assert len(self.photos) < 2
        if len(self.photos) > 0:
            assert self.photos[0][1] == 'V'
            assert photo[1] == 'V'
        self.photos.append(photo)
        self.tags.update(photo[-1])

    def __str__(self):
        if len(self.photos) > 1:
            assert self.photos[0][1] == 'V' and self.photos[1][1] == 'V'
        else:
            assert self.photos[0][1] == 'H'
        return ' '.join([str(x[0]) for x in self.photos])
