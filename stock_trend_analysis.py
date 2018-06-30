import pandas
from pandas import Series
from matplotlib import pyplot
from statsmodels.tsa.seasonal import seasonal_decompose
series = Series.from_csv('excel_aaa.csv', header=0)
result = seasonal_decompose(series, model='multiplicative', freq=120)
result.plot()
pyplot.show()
# pyplot.savefig('filename.png', dpi=300)
