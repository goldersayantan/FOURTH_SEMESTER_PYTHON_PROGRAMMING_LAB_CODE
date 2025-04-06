import scipy.stats
import numpy as np
mean = 0

std_dev = 1
x = np.linspace(-3, 3, 100)

pdf = scipy.stats.norm.pdf(x, mean, std_dev)
print("PDF values: ", pdf[:5])

