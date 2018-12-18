import os


class ReadTxt():
    def __init__(self, filename):
        self.filename = os.getcwd()+os.sep+"data"+os.sep+filename

    # os.getcwd() + os.sep + "data" + os.sep +

    def readtxt(self):
        list = []
        with open(self.filename, "r", encoding="utf-8") as f:
            for i in f.readlines():
                list.append(i.strip().split(","))
            return list

if __name__ == '__main__':
    print(ReadTxt().readtxt("./data/data.txt"))
