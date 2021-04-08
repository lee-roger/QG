import matplotlib.pyplot as plt
import numpy as np

data_num = 100



# 计算a与b
def calculate(train_x, train_y):
    x_aver = np.mean(x)
    y_aver = np.mean(y)

    mol = (x-x_aver).dot(y-y_aver)             # 计算分子
    den = (x-x_aver).dot(x-x_aver)              # 计算分子

    a = mol/den
    b = y_aver -a*x_aver

    return a,b

def predict_1(a, b, x):
    return a*x+b

def predict(x_train, y_train, x_test):
    a,b = calculate(x_train,y_train)
    return np.array(predict_1(a,b,x_test))

def calculater_R(y_real,y_predict,y_aver):
    R = (y_predict-y_real).dot(y_predict-y_real) / (y_aver-y_real).dot(y_aver-y_real)
    return 1-R


x = np.random.randn(data_num)*10                 # 随机生成
y = 2*x+10+np.random.randn(data_num)*10       
x_train = x[:20]                                 # 训练组
y_train = y[:20]

x_test = x[20:data_num]
y_real = y[20:data_num]
y_aver = np.mean(y_real)
y_predict = predict(x_train,y_train,x_test)

plt.style.use("seaborn")
fig, ax= plt.subplots()

plt.rcParams['font.sans-serif']=['SimHei']###解决中文乱码
plt.rcParams['axes.unicode_minus']=False

ax.scatter(x_test, y_real,label="离散数据",c="g")
ax.plot(x_test, y_predict,label="拟合曲线",c='b')

ax.set_title("最小二乘法",fontproperties='SimHei', fontsize=20)
ax.set_xlabel("x值", fontproperties='SimHei',fontsize=15)
ax.set_ylabel("y值", fontproperties='SimHei',fontsize=15)
plt.legend(loc='best');

print("拟合度为{:.2f}".format(calculater_R(y_real,y_predict,y_aver)))
plt.show()
