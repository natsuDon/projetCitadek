import re
from nltk.corpus import stopwords
class DataCleaner :

    def __init__(self):
        i=0

    def clean_data(self, dataToClean):
        # cette fonction prend en paramètre un tableau
        lines = []
        # lower
        for line in dataToClean:
            line = line.lower()
            # remove special characters
            line = re.sub('[^a-z\s]', '', line)
            line = ' '.join([w for w in line.split() if len(w) > 1])

            lines.append(line)
        return lines
