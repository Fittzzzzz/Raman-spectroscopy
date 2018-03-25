import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import csc_matrix, eye, diags
from scipy.sparse.linalg import spsolve

def plotRaman(path):
  names=globals()
  a=0
  for j in range(1,90):
      path1 = path+str(j)+'.txt'
      f = open(path1)  # 打开文件
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
      names['a%s'%j ]=(y - MinValue) / (MaxValue - MinValue)
      a = a+names['a%s'%j]
      aver=a/90

   # 下面是创建图形，并作图；利用上面的lamda作为x坐标轴，其余数据作为y，进行画图。
  return x,aver

def plotmix(x,a1):

  plt.figure()
  plt.rc('font',family='sans-serif')
  plt.plot(x, a1,color='black')
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

def WhittakerSmooth(x, w, lambda_, differences=1):
    '''
    Penalized least squares algorithm for background fitting

    input
        x: input data (i.e. chromatogram of spectrum)
        w: binary masks (value of the mask is zero if a point belongs to peaks and one otherwise)
        lambda_: parameter that can be adjusted by user. The larger lambda is,  the smoother the resulting background
        differences: integer indicating the order of the difference of penalties

    output
        the fitted background vector
    '''
    X = np.matrix(x)
    m = X.size
    i = np.arange(0, m)
    E = eye(m, format='csc')
    D = E[1:] - E[:-1]  # numpy.diff() does not work with sparse matrix. This is a workaround.
    W = diags(w, 0, shape=(m, m))
    A = csc_matrix(W + (lambda_ * D.T * D))
    B = csc_matrix(W * X.T)
    background = spsolve(A, B)
    return np.array(background)


def airPLS(x, lambda_=100, porder=1, itermax=15):
    '''
    Adaptive iteratively reweighted penalized least squares for baseline fitting

    input
        x: input data (i.e. chromatogram of spectrum)
        lambda_: parameter that can be adjusted by user. The larger lambda is,  the smoother the resulting background, z
        porder: adaptive iteratively reweighted penalized least squares for baseline fitting

    output
        the fitted background vector
    '''
    m = x.shape[0]
    w = np.ones(m)
    for i in range(1, itermax + 1):
        z = WhittakerSmooth(x, w, lambda_, porder)
        d = x - z
        dssn = np.abs(d[d < 0].sum())
        if (dssn < 0.001 * (abs(x)).sum() or i == itermax):
            if (i == itermax):
                print('WARING max iteration reached!')

            break
        w[d >= 0] = 0  # d>0 means that this point is part of a peak, so its weight is set to 0 in order to ignore it
        w[d < 0] = np.exp(i * np.abs(d[d < 0]) / dssn)
        w[0] = np.exp(i * (d[d < 0]).max() / dssn)
        w[-1] = w[0]
    return z

if __name__=='__main__':
    x1,y1 = plotRaman("C:\\Users\\fangzheng\\Desktop\\fangzheng2018\\sers\\baihua\\2-")
    plotmix(x1, y1)
    y1 = y1-airPLS(y1)
    plotmix(x1,y1)
