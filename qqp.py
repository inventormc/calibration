import csv
import sys

with open("calibration/calibration_data/QQP/dev.txt", "r") as f:
    csv.field_size_limit(sys.maxsize)
    reader = csv.reader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
    next(reader)
    sentence_pairs = []
    labels = []
    for row in reader:
        try:
            sentence_pairs.append([row[3], row[4]])
            labels.append(row[-1])
        except:
            print(row)

assert len(sentence_pairs) == len(labels)


with open("dev.tsv", "w") as f:
    f.write("sentence\tscores\n")
    for pair, label in zip(sentence_pairs, labels):
        sentence = pair[0] + "</s></s>" + pair[1]

        f.write("%s\t%s\n" % (sentence, label))

