class ReadTxt:
    def __init__(self):
        self.words_dict = {}

    def read_file(self):
        with open('words.txt') as file:
            words = file.readlines()
            for word in words:
                word = word.replace('\n', '')
                self.words_dict[word] = ''
        return self.words_dict
        # print(self.words_dict)


# read_txt_file = ReadTxt()
# read_txt_file.read_file()
