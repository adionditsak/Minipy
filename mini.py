#!/usr/bin/env python

import os, sys, re

class Minify():

    """
        Minify files
    """

    def __init__(self):
        pass

    """ run standard minifying """
    def run(self, file_to_minify):

        for i in range(len(file_to_minify)):
            self.file_to_minify = file_to_minify[i]
            self.file_name = os.path.splitext(self.file_to_minify)
            self.file_name_minified = self.file_name[0] + '.min' + self.file_name[1]

            self.detect_file_type_and_execute()

    """ detect file type and execute """
    def detect_file_type_and_execute(self):
        if self.file_name[1] == '.css':
            print('')
            print('CSS file detected.')
            self.css() # run css compression
            self.size_calc() # calc size difference
        elif self.file_name[1] == '.js':
            print('')
            print('JS file detected.')
            self.js() # run js compression
            self.size_calc() # calc size difference
        else:
            self.help()

    """ read file """
    def read_file(self, filepath):
        try:
            with open(filepath, 'r') as f:
                return f.read()
        except:
            self.help()

    """ write minified version to file """
    def write_file(self, filepath):
        try:
            with open(self.file_name_minified, 'w+') as f:
                f.write(filepath)
        except:
            self.help()

    """ calculate size difference """
    def size_calc(self):
        self.file_size = os.path.getsize(self.file_to_minify)
        self.file_size_minified = os.path.getsize(self.file_name_minified)
        self.file_size_saved = self.file_size - self.file_size_minified
        self.file_size_saved_in_percentage = (100 * float(self.file_size_minified) / float(self.file_size)) - 100

        print('Done - take a look at ' + self.file_name_minified)
        print('You have saved ' + str(self.file_size_saved) + ' bytes (' + str(self.file_size_saved_in_percentage) + '%)')

    """ css minifying """
    def css(self):
        self.string = self.read_file(self.file_to_minify)
        self.strip_comments  = re.sub(r'/\*[\s\S]*?\*/', '', self.string)
        self.strip_urls = re.sub(r'url\((["\'])([^)]*)\1\)', r'url(\2)', self.strip_comments)
        self.strip_whitespace_and_linebreaks = self.strip_urls.replace('\n', '')
        self.strip_multiple_whitespaces = re.sub(' +', ' ', self.strip_whitespace_and_linebreaks)

        self.write_file(self.strip_multiple_whitespaces) # write minified css to file

    """ js minifying """
    def js(self):
        self.string = self.read_file(self.file_to_minify)
        self.strip_comments  = re.sub(r'/\*[\s\S]*?\*/', '', self.string)
        self.strip_one_line_comments = re.sub(r'\/\/(.*)', '', self.strip_comments)
        self.strip_whitespace_and_linebreaks = self.strip_one_line_comments.replace('\n', '')
        self.strip_multiple_whitespaces = re.sub(' +', ' ', self.strip_whitespace_and_linebreaks)

        self.write_file(self.strip_multiple_whitespaces) # write minified js to file

    """ run minifying with files from current dir """
    def glob(self):
        self.glob_list = [] # set list for files to minify

        for fname in os.listdir('.'):
            if fname.endswith('.js') or fname.endswith('.css'):
                self.glob_list.append(fname)

        print('Found following files in your current directory:')
        print(self.glob_list)

        print('Minifying of these has begun.')
        self.run(self.glob_list)


    """ help instructions """
    def help(self):
        print('')
        print('Instructions')
        print('Make sure that:')
        print('1): You are trying to compress a css or js file.')
        print('2): The file exists in your current folder.')
        print('3): You have not misspelled.')
        print('Use like $ python mini.py [-m|--minify,-c|--concat,-s|--scan-dir] [files]')
        print('Concat needs more than file as argument, to concat... obviously.')
        print('...')
        print('')


class Concat():

    """
        Minify and concat files
    """

    def __init__(self):

        self.files_to_concat = [] # set list for files to concat

    def run(self, file_to_concat):

        mini = Minify() # initiate minify class

        """
        if __name__ == '__main__':
            mini.run(sys.argv[2:]) # run minifying as cli
        else:
            mini.run(sys.argv) # run minifying as module
        """

        print('')
        print('Minifying done. Concatenating has begun.')

        for i in range(0, len(file_to_concat)):
            self.file_to_concat = file_to_concat[i]
            self.file_name = os.path.splitext(self.file_to_concat)
            self.file_name_minified = self.file_name[0] + '.min' + self.file_name[1]

            self.files_to_concat.append(self.file_name_minified)

        self.execute_concatenation() # run concatenation

    """ execute concatenation for minified files """
    def execute_concatenation(self):

        if self.file_name[1] == '.css':
            print('')
            print('CSS files detected. Creating concat.css.')
            self.concat_file = 'concat.css'
        elif self.file_name[1] == '.js':
            print('')
            print('JS files detected. Creating concat.js.')
            self.concat_file = 'concat.js'

        """ write the concat file """
        with open(self.concat_file, 'w+') as outfile:
            for fname in self.files_to_concat:
                with open(fname) as infile:
                    for line in infile:
                        outfile.write(line)


""" if run directly """
if __name__ == '__main__':

    mini = Minify()
    con = Concat()

    if len(sys.argv) > 2:
        if (sys.argv[1] == '-m') or (sys.argv[1] == '--minify') :
            mini.run(sys.argv[2:])
        elif (sys.argv[1] == '-s') or (sys.argv[1] == '--scan-dir'):
            mini.glob()
        elif (sys.argv[1] == '-c') or (sys.argv[1] == '--concat'):
            con.run(sys.argv[2:])
        else:
            mini.help()
    else:
        mini.help()
