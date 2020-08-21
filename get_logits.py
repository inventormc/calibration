filename = "output/QQP_roberta-base_distill.json"
data_path = "calibration_data/QQP/train.txt"
write_name = "qqp-distill.tsv"
import csv
import json

with open(filename, 'r') as handle:
    all_logits = [json.loads(line)["logits"] for line in handle]

with open(data_path, 'r') as f:
    i = 0
    reader = csv.reader(f, delimiter='\t')
    next(reader)
    sentence_pairs=[]
    for line in reader:
        i += 1
        try:
            sentence_pairs.append((line[3],line[4]))
        except Exception as e:
            print(i)

print(len(all_logits), len(sentence_pairs))
assert len(all_logits) == len(sentence_pairs)

with open(write_name, "w") as f:
    f.write("sentence\tscores\n")
    for pair, rating in zip(sentence_pairs, all_logits):
        sentence = pair[0] + "</s></s>" + pair[1]

        f.write("%s\t%.6f %.6f\n" % (sentence, *rating))
