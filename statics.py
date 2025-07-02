import numpy as np
import pandas as pd
data=[2,3,5,2,6]
print('Mean :',np.mean(data))#average of all numbers
print('Median :',np.median(data))#middle number
print('Mode :',pd.Series(data).mode()[0])#reapeted number
print('Range :',max(data)-min(data))
print('Variance :',np.var(data))#difference of data numbers with it's mean(small variance or spreaded out)
print('Standard Deviation :',np.std(data))#Square root of variance