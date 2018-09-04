#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from matplotlib import rc
import numpy as np
#from matplotlib.numerix import arange, cos, pi
from pylab import figure, axes, plot, xlabel, ylabel, title, grid, savefig, show

rc('text', usetex=True)
figure(1)
ax = axes([0.1, 0.1, 0.8, 0.7])
t = np.arange(0.0, 1.0+0.01, 0.01)
s = np.cos(2*2*np.pi*t)+2
plot(t, s)

xlabel(r'\textbf{time (s)}')
ylabel(r'\textit{voltage (mV)}',fontsize=16)
title(r"\TeX\ is Number $\displaystyle\sum_{n=1}^\infty\frac{-e^{i\pi}}{2^n}$!", fontsize=16, color='r')
grid(True)
savefig('tex_demo')

show()

