##
## File: week12b.py (STAT 3250)
## Topic: Simulating Random Normal Values and
##        Brief Introduction to Graphics -- Part 2
##         

#### Normal and Lognormal distributions

import numpy as np

# Generating a value from a normal distribution with mean
# mu and standard deviation sigma

mu = 0.10
sigma = 0.35
np.random.normal(mu, sigma, 1)  # Produces one random value

# We can remove the random value from the array
np.random.normal(mu, sigma)

# The exponential function is called with np.exp:
np.exp(0.2)

# We can get a random value from a lognormal distribution by
# wrapping np.random.normal in np.exp:
np.exp(np.random.normal(mu, sigma))


#### Histograms

# Let's start by generating some values for a histogram
normvals = np.zeros(100000)

# Set mu and sigma
mu = 10
sigma = 2
for i in range(100000):
    normvals[i] = np.random.normal(mu, sigma)
    
# Let's create a histogram, starting with importing a library
import matplotlib.pyplot as plt

# Now create the histogram
plt.hist(normvals, bins=80, range=[2, 18])  

# A set of lognormal values
lognormvals = np.zeros(100000)
for i in range(100000):
    lognormvals[i] = np.exp(np.random.normal(mu, sigma))

# The corresponding histogram
plt.hist(lognormvals, bins=80, range=[0, 40000]) 


#### Misc: Rounding numbers

x = 72564.02357007
print("%.2f" % x)  # Single values

y = 3894.547031
print("%.2f" % y)

arr = np.array([x, y])  # Arrays
np.round(arr, 2)




