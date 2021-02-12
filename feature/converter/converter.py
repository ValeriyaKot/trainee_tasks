import sys


class Converter(object):

    def __init__(self, first_file_name, second_file_name):
        self.first_file_name = first_file_name
        self.second_file_name = second_file_name
        self.first_file = None
        self.second_file = None
        self.content = ''

    def convert(self):
        raise NotImplementedError

    def open_file(self):
        self.first_file = open(self.first_file_name)
        self.content = self.first_file.read()
        self.second_file = open(self.second_file_name, 'w')

    def close_file(self):
        self.first_file.close()
        self.second_file.close()


class CsvToJsonConverter(Converter):

    def __init__(self, first_file_name, second_file_name):
        super(CsvToJsonConverter, self).__init__(first_file_name, second_file_name)

    def convert(self):
        self.open_file()
        self.split_text()
        self.join_text()
        self.close_file()

    def split_text(self):
        rows = self.content.split('\n')
        rows_list = []
        for element in rows:
            element = element.strip('\r').split(',')
            rows_list.append(element)
        return rows_list

    def join_text(self):
        rows_list = self.split_text()
        complete_text_list = []
        for j in range(1, len(rows_list)):
            if len(rows_list[j]) <= 1:
                continue
            else:
                row = {}
                for i in range(len(rows_list[0])):
                    row[rows_list[0][i]] = rows_list[j][i]
                complete_text_list.append('{%s}' % ', '.join(['"{}":"{}"'.format(k, v) for k, v in row.items()]))
        self.second_file.write('[%s]' % ', '.join('{}'.format(el) for el in complete_text_list))


if __name__ == "__main__":
    converter = CsvToJsonConverter(sys.argv[1], sys.argv[2])
    converter.convert()
