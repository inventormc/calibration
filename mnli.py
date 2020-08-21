import csv
import sys

def get_label(text_label):
    if text_label == "contradiction":
        return "0"
    elif text_label == "neutral":
        return "1"
    elif text_label == "entailment":
        return "2"


with open("calibration/calibration_data/MNLI/dev.txt", "r") as f:
    csv.field_size_limit(sys.maxsize)
    reader = csv.reader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
    next(reader)
    sentence_pairs = []
    labels = []
    for row in reader:
        sentence_pairs.append([row[8], row[9]])
        labels.append(get_label(row[-1]))


with open("dev.tsv", "w") as f:
    f.write("sentence\tscores\n")
    for pair, label in zip(sentence_pairs, labels):
        sentence = pair[0] + "</s></s>" + pair[1]

        f.write("%s\t%s\n" % (sentence, label))

