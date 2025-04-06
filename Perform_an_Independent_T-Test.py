import numpy as np
import scipy
data1 = np.random.normal(5, 1, 100)
data2 = np.random.normal(5.5, 1, 100)

t_stat, p_value = scipy.stats.ttest_ind(data1, data2)
print("T-statistic: ", t_stat)
print("P-value: ", p_value)


# import numpy as np
# from scipy.stats import ttest_ind  # Explicit import
#
# # Set random seed for reproducibility
# np.random.seed(42)
#
# # Generate two datasets from normal distributions
# data1 = np.random.normal(5, 1, 100)   # Mean = 5, Std Dev = 1
# data2 = np.random.normal(5.5, 1, 100) # Mean = 5.5, Std Dev = 1
#
# # Perform independent t-test
# t_stat, p_value = ttest_ind(data1, data2)
#
# # Print results with better formatting
# print(f"T-statistic: {t_stat:.4f}")
# print(f"P-value: {p_value:.4f}")
