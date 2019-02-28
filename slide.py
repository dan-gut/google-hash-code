class Slice(object):
    def __init__(self):
        self.photos = []
        self.tags = []

    def add_photo(self, photo):
        assert len(self.photos) < 2
        if len(self.photos) > 0:
            assert self.photos[0][1] == 'V'
        self.photos.append(photo)
        self.tags.extend(photo[-1])

