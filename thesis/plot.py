import matplotlib.pyplot as plt
import pandas as pd

f = pd.read_csv("data.csv")
print (f)
plt.plot(f['users'], f['opr'], label="normally distributed")
plt.xlabel("Users")
plt.ylabel("Over Payment Ratio")

g = pd.read_csv("data_uniform.csv")
print (g)
plt.plot(g['users'], g['opr'], label="uniformly distributed")
plt.xlabel("Users")
plt.ylabel("Over Payment Ratio")
plt.legend()
plt.show()
