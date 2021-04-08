import csv
import random

with open('癌症预测.csv', "r") as file:   # 打开文件
    reader = csv.DictReader(file)       # dictreader以一个字典模式打开文件
    data = [row for row in reader]      # 生成一个列表,每一个元素为字典
# print(data)

n = len(data)                     # 统计元素的数量
n1 = len(data)//5                 # 分组，切片

random.shuffle(data)             # 每次打乱这个列表，具有随机性
test_ground = data[:n1]         # 五分之一作为测试组
train_ground = data[n1:]          # 五分之四作为训练组


# 算距离->排序->取前K个数->加权平均


def distence(d1, d2):
    res = 0
    for key in ("radius", "texture", "perimeter", "area", "smoothness", "compactness", "symmetry", "fractal_dimension"):
        res += (float(d1[key]) - float(d2[key]))**2                  # 计算字典里每一个键的距离
    return res**0.5


def knn(data):
    k = 2                   # 距离
    res = [
            {"result": train['diagnosis_result'], "distence":distence(train, data)} for train in train_ground               # 列表的推导式，这里是列表嵌套字典
    ]
  #  print(res)
    res = sorted(res, key=lambda item: item["distence"])              # 排序，按照距离从远到近

    res2 = res[:k]                               # 离他周围的几个元素

   # 加权平均
    result = {'M': 0, 'B': 0}  # 权重
    sum = 0
    for r in res2:
        sum+= r['distence']

    for r in res2:
        result[r['result']]+= 1-r['distence']/sum

   # print(result)
   # print(data["diagnosis_result"])
    if result["M"]>result["B"]:
        return 'M'
    else:
        return 'B'


count = 0

for test in test_ground:
    result_test = knn(test)    # 预期结果
    result_real = test["diagnosis_result"]   # 真正结果
    if result_real == result_test:    # 预期结果与真正果一样
        count+= 1

print(count)
print(len(test_ground))
print("癌症的概率为{:.2f}%".format(100*count/len(test_ground)))


