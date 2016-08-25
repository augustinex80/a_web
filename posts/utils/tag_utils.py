class TagsCloud:
    css = [
        'tag1', 'tag2', 'tag3', 'tag4', 'tag5', 'tag6', 'tag7', 'tag8',
    ]

    def __init__(self, min_count, max_count):
        self.min_count = min_count
        self.max_count = max_count

    def get_css(self, count):
        size = self.max_count - self.min_count
        if 0 <= size < 8:
            a = len(self.css) - size
            index = count - self.min_count + a - 1
            print(index)
            return self.css[index]
        elif size >= 8:
            step = len(self.css) / size
            index = int((count - self.min_count) * step)
            return self.css[index]
        else:
            return self.css[-1]


