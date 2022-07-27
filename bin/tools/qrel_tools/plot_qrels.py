import matplotlib.pyplot as plt
import numpy as np
import os

if os.name == 'nt':
    plot_dir = r'C:\Users\User\git\summarization-pruning\data\plots'
else:
    plot_dir = r'/home/jschmolzi/summarization-pruning/data/plots'
    
plot_path = os.path.join(plot_dir, 'plot.png')
x = np.linspace(0, 10, 100)

plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))

plt.savefig(plot_path)
