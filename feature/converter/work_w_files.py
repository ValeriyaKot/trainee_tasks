import sys
from converter import Converter


def open_csv_file(csv_file):
    with open(csv_file) as f_obj:
        file = f_obj.read()
        text = file.split('\n')
        return text


def write_json_file(json_file, text):
    converter = Converter(text)
    f_obj = open(json_file, 'w')
    f_obj.write('[%s]' % ', '.join('{}'.format(el) for el in converter.join_text()))
    f_obj.close()


my_text = open_csv_file(sys.argv[1])
write_json_file(sys.argv[2], my_text)
