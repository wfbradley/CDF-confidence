import CDF_confidence as Cc
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Make some random data
rv=norm()
x=norm.rvs(size=300)

# Do a basic plot
plt.figure()
Cc.plot_CDF_confidence(x)

# Do fancier plot
plt.figure()
Cc.plot_CDF_confidence(x,label='Empirical CDF',color='violet')

x_sorted=np.sort(x)
plt.plot(x_sorted,norm.cdf(x_sorted),':',label='True CDF')
plt.legend(loc='best')

plt.show()
