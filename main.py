import pandas
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
data = pandas.read_csv('/Users/jarvis/Desktop/iphone.csv')
plt.scatter(data['version'], data['price'])
plt.show()
model = LinearRegression()
model.fit(data[['version']], data[['price']])
print(model.predict([[14]]))
