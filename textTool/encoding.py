import os
import sys
import fileinput
import codecs

path=os.listdir('DEFS/')#weg zum Ordner


def encode_file(file_path, encoding):
    temp_file_path = file_path + '.temp'
    with codecs.open(file_path, 'r', encoding=encoding) as f_in:
        with codecs.open(temp_file_path, 'wb') as f_out:
            f_out.write(f_in.read().encode('utf-16'))
    os.replace(temp_file_path, file_path)
    

    

for file in path:
    input = 'DEFS/'+file
    encode_file(input, 'ansi')
    encode_file(input, 'utf-8')