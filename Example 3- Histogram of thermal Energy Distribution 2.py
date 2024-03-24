

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 18:24:51 2024

@author: brettnakao
"""

import numpy as np

# Constant
B = 1.380649e-23

# Values
temperatures = np.array([30, 45, 45, 48, 50, 55, 48, 52, 63, 65, 70, 80, 73, 40])
kinetic = B*(273.15+(temperatures-32)*5/9)

# Plot
import matplotlib.pyplot as plt
plt.hist(kinetic, bins=4, edgecolor='black', alpha=.7)
plt.xlabel('Kinetic Energy')
plt.ylabel('Frequency')
plt.title('Distribution of Thermal Energy')
plt.show()



