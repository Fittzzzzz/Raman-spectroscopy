import numpy as np
import matplotlib.pyplot as plt
def plotRaman(path):
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
  x = data_array[100:1550, 0]
  y = data_array[100:1550, 1]
  MaxValue = np.max(y)
  MinValue = np.min(y)
  d_lamda = (y-MinValue) / (MaxValue-MinValue)
# 下面是创建图形，并作图；利用上面的lamda作为x坐标轴，其余数据作为y，进行画图。
  return x,d_lamda

def plotmix(x,a1,b1,c1,d1,f1,e1,g1):

  plt.figure()
  plt.rc('font',family='sans-serif')
  plt.plot(x, a1,color='black')
  plt.plot(x, b1,color='red')
  plt.plot(x, c1,color='darkred')
  plt.plot(x, d1,color='blue')
  plt.plot(x, f1,color='green')
  plt.plot(x, e1,color='purple')
  plt.plot(x, g1,color='skyblue')
  #设置x,y轴数据，颜色为黑色
  plt.xlim((350,1800))#设置x轴范围
  plt.ylim((0,1.1))#设置y轴范围
  plt.xlabel('Raman Shift ($\\rm cm^{-1}$)',fontsize=14,family="sans-serif")#设置x轴label
  plt.ylabel('Intensity',fontsize=14)#设置y轴label
  plt.legend(labels = ['Acacia honey','Wildflower honey','Snow lotus honey','Codonopsis honey','Jujube honey','Jinghua honey','Eucalyptus honey'], loc = 'best',shadow = False,framealpha=0)#引入图例
  plt.tick_params(direction='in',width=1.5)#设置刻度向里大小
  ax = plt.gca()
  ax.spines['right'].set_linewidth(1.5)#设置外框粗细
  ax.spines['left'].set_linewidth(1.5)
  ax.spines['top'].set_linewidth(1.5)
  ax.spines['bottom'].set_linewidth(1.5)
  plt.xticks(fontsize=14)#设置标尺大小
  plt.yticks(fontsize=14)
  plt.grid(True)
  plt.savefig("mix.tif",dpi=300)
  plt.show()

if __name__=='__main__':
    x1,y1 = plotRaman("C:\\Users\\fangzheng\\Desktop\\fangzheng2018\\sers\\yanghuai\\1-1.txt")
    x1,y2 = plotRaman("C:\\Users\\fangzheng\\Desktop\\fangzheng2018\\sers\\baihua\\2-1.txt")
    x1,y3 = plotRaman("C:\\Users\\fangzheng\\Desktop\\fangzheng2018\\sers\\xuezhilian\\3-1.txt")
    x1,y4 = plotRaman("C:\\Users\\fangzheng\\Desktop\\fangzheng2018\\sers\\dangshen\\4-1.txt")
    x1,y5 = plotRaman("C:\\Users\\fangzheng\\Desktop\\fangzheng2018\\sers\\zaohua\\5-1.txt")
    x1,y6 = plotRaman("C:\\Users\\fangzheng\\Desktop\\fangzheng2018\\sers\\jinghua\\6-1.txt")
    x1,y7 = plotRaman("C:\\Users\\fangzheng\\Desktop\\fangzheng2018\\sers\\duanshu\\7-1.txt")
    plotmix(x1,y1,y2,y3,y4,y5,y6,y7)