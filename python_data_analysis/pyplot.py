from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-3, 3, 0.001)

plt.plot(x, norm.pdf(x), 'b-')
plt.plot(x, norm.pdf(x, 1.0, 0.5), 'g-')
plt.show()
plt.savefig('C:\\Users\Mary Wanjeri\\Desktop\python programmes,\\python_data_analysis,MyPlot.png', format='png')
