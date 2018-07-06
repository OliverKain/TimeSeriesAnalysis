# import pandas
# from pandas import Series
# from matplotlib import pyplot
# from statsmodels.tsa.seasonal import seasonal_decompose
# series = Series.from_csv('excel_aaa.csv', header=0)
# result = seasonal_decompose(series, model='multiplicative', freq=120)
# result.plot()
# pyplot.show()
# pyplot.savefig('filename.png', dpi=300)
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import statsmodels.api as sm
import seaborn as sns
sns.set_style('whitegrid')
sns.set_context('talk')
series = pd.read_csv('excel_aaa.csv',index_col=[0],parse_dates=True)
series=series.astype(float)
decomposed_series = sm.tsa.seasonal_decompose(series.interpolate(), freq=30, model='multiplicative')
# series.pct_change().plot(title="series.pct_change()")
# series.interpolate().pct_change().plot(title="series.interpolate().pct_change()")
# decomposed_series.trend.plot(title="res.trend")
decomposed_series.trend[decomposed_series.trend.pct_change() > 0.05].plot(title="res.trend.pct_change()")
plt.show()