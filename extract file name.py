#extract file name
#Level: 6 kyu
'''
You have to extract a portion of the file name as follows:

Assume it will start with date represented as long number
Followed by an underscore
Youll have then a filename with an extension
it will always have an extra extension at the end     
'''


import re     
class FileNameExtractor:
    def extract_file_name(dirty_file_name):
        return re.search('^\d+_(.*)\..*$', dirty_file_name).group(1)
