#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 13:41:05 2024

@author: brettnakao
"""

import numpy as np
import matplotlib.pyplot as plt

values = np.linspace(2, 7, 10)

# Plotting functions
fig, axs = plt.subplots(1, 3)
axs[0].plot(values, np.exp(values), label = '$e^x$')
axs[0].legend()
axs[0].plot(values, values**3.6, label = "$x^{3.6}$")
axs[0].legend()

"""semilog plot"""

axs[1].semilogy(values, np.exp(values), label = "e^x")
axs[1].legend()
axs[1].semilogx(values, values**3.6, label = "x^3.6")
axs[1].legend()

"""loglog plot"""

axs[2].loglog(values, np.exp(values), label = "e^x")
axs[2].legend()
axs[2].loglog(values, values**3.6, label = "x^3.6")
axs[2].legend()

plt.tight_layout()
plt.show()