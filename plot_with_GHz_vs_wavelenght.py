import numpy as np
import matplotlib.pyplot as plt


x = np.array([10, 100, 200, 550, 1000]) #the values are in GHz
y = np.array([0.01, 1, 20, 55, 100.25]) #the values could be mJy or whatever

#Plot the figure:

fig, ax = plt.subplots(figsize=(15, 8))

ax.plot(x,y, 'o')

ax.set_xscale('log')
ax.set_yscale('log')

ax.set_xlim(4.5, 2100)

ax2 = ax.twiny()
ax2.set_xlim(300/4.5, 300/2100) # conversion to lambda with c/f. I want lambda in mm so I divide 300/nu (lims).

ax2.set_xscale('log')

ax.set_ylabel(r'S$_\nu$ (mJy)') # y label
ax.set_xlabel(r'$\nu$ (GHz)') # x label

#Tickmarks

#Principal axis:

ax.tick_params(axis='y', which='major', width=2, length=10, direction='in')
ax.tick_params(axis='y', which='minor', width=1.5, length=5, direction='in')

ax.tick_params(axis='x', which='major', width=2, length=10, direction='in')
ax.tick_params(axis='x', which='minor', width=1.5, length=5, direction='in')

#Secondary axis:

ax2.tick_params(axis='x', which='major', width=2, length=10, direction='in')
ax2.tick_params(axis='x', which='minor', width=1.5, length=5, direction='in')
