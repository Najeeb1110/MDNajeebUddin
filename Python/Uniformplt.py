# Date: 28-Sep-2022
# Progammer : MD.Najeen Uddin 
#importing  numpy 
from numpy import random
#importing Matplotlib.pyplot 
import matplotlib.pyplot as plt
#importing Seaborn 
import seaborn as sns

# Giving the values 
sns.distplot(random.uniform(size=1000), hist=False)

plt.show()
