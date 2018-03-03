import operator
from collections import defaultdict, Counter

data = []
output_name = []
data_list = Counter()
n = int(input())
for i in range(n):
    name, score = input().split()
    score = int(score)
    data_list[name] += score
    data.append((name, data_list[name]))
max_value = max(data_list.items(), key=operator.itemgetter(1))[1]


def name_score(full_list):
    for (name, score) in data:
        if score >= max_value and full_list[name] == max_value:
            return output_name.append(name)


name = name_score(data_list)
print(output_name[0])
