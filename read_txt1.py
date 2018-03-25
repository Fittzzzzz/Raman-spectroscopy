import numpy as np
import matplotlib.pyplot as plt

path = "C:\\Users\\fangzheng\\Desktop\\fangzheng2018\\sers\\xuezhilian\\3-1.txt"   # 文件路径
f = open(path)  # 打开文件
c = f.read()
d = c.strip()
content = d.splitlines()
# 读取并分割行，splitlines()默认按照'\n'分割
head = content[0]  # 每列的head，如果没有head，此行可忽略
data_str = content[2:]  # 此时数据以字符串的形式存入一个列表
data_num = [[]] * len(data_str)  # 创建一个空列表，用以装入转后后的数据
# for循环用以将字符串形式的数据转换成数字，这一步结束就已经完成了转换了
# 转换后的数据存储在data_num中
for i in range(len(data_str)):
    data_num[i] = [float(x) for x in data_str[i].split(',')]
# 下面是利用numpy和matplotlib.pyplot进行数组转换和画图
data_array = np.array(data_num)  # 将数据转换成二维数组
# 下面将二维数组中的每一列存储到一个列向量中，以备画图
lamda = data_array[100:1550, 0]
s_lamda = data_array[100:1550, 1]
MaxValue = np.max(s_lamda)
MinValue = np.min(s_lamda)
d_lamda = (s_lamda-MinValue) / (MaxValue-MinValue)
# 下面是创建图形，并作图；利用上面的lamda作为x坐标轴，其余数据作为y，进行画图。
plt.figure()
plt.rc('font',family='sans-serif')

plt.plot(lamda, d_lamda,color='black')#设置x,y轴数据，颜色为黑色
plt.xlim((350,1800))#设置x轴范围
plt.ylim((0,1.1))#设置y轴范围
plt.xlabel('Raman Shift ($\\rm cm^{-1}$)',fontsize=14,family="sans-serif")#设置x轴label
plt.ylabel('Intensity',fontsize=14)#设置y轴label
plt.legend(labels = ['Snow lotus honey'], loc = 'best',shadow = False,framealpha=0)#引入图例
#设置保存名和像素
plt.tick_params(direction='in',width=1.5)#设置刻度向里大小
ax = plt.gca()
ax.spines['right'].set_linewidth(1.5)#设置外框粗细
ax.spines['left'].set_linewidth(1.5)
ax.spines['top'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)
plt.xticks(fontsize=14)#设置标尺大小
plt.yticks(fontsize=14)
plt.savefig("3-1.tif",dpi=300)
plt.show()
print(type(d_lamda))