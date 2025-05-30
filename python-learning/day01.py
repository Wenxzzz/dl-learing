import numpy as np
import matplotlib.pyplot as plt
#x = np.array([1.0,2,3])
#y = np.array([4.0,5,6])
#N维数组
#x = np.array([[1,2],[3,4]])
#y = np.array([5,6])
#y = x.flatten()
x = np.arange(0,6,0.1)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x, y1,label = "sin")
plt.plot(x, y2,linestyle = "--",label = "cos")
plt.xlabel("x") # x轴标签
plt.ylabel("y") # y轴标签
plt.title('sin & cos') # 标题
plt.legend()
plt.show()
