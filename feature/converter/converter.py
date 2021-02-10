class Converter:

    def __init__(self, text):
        self.text = text

    def split_text(self):
        new_text = []
        for element in self.text:
            element = element.strip('\r')
            string = element.split(',')
            new_text.append(string)
        return new_text

    def join_text(self):
        new_text = self.split_text()
        all_text = []
        for j in range(1, len(new_text)):
            if len(new_text[j]) <= 1:
                continue
            else:
                row = {}
                for i in range(len(new_text[0])):
                    row[new_text[0][i]] = new_text[j][i]
                all_text.append('{%s}' % ', '.join(['"{}":"{}"'.format(k, v) for k, v in row.items()]))
                self.text = all_text
        return self.text






