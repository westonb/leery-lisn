import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mtick
from matplotlib.patches import ConnectionPatch

import pandas

dm_l_file_name = "measurements/l_dm.csv"
dm_n_file_name = "measurements/n_dm.csv"
cm_cm_file_name = "measurements/cm_cm.csv"
cm_dm_file_name = "measurements/cm_dm.csv"

l_impedance_file_name = "measurements/l_impedance.csv"
n_impedance_file_name = "measurements/n_impedance.csv"

file_data = pandas.read_csv(cm_dm_file_name, sep=',', skiprows=13, header=None)
freq_cm_dm = file_data[0].to_numpy()
s21_cm_dm = file_data[1].to_numpy() + 6.0 # +6dB due to splitter loss

fig, ax = plt.subplots()
ax.plot(freq_cm_dm, s21_cm_dm, color="olivedrab", alpha=0.9)
ax.set_ylim([-80,0])
ax.margins(x=0)

fig.suptitle("Common Mode Rejection", fontsize=18)
ax.set_ylabel("dB", rotation=0, fontsize=16, labelpad=16)
ax.set_xlabel("Frequency (Hz)", fontsize=16)
ax.grid()

fig.tight_layout()
fig.align_ylabels()
fig.savefig("cm_rejection.png", dpi=300)
plt.show()


file_data = pandas.read_csv(cm_cm_file_name, sep=',', skiprows=13, header=None)
freq_cm_cm = file_data[0].to_numpy()
s21_cm_cm = file_data[1].to_numpy() + 6.0 # +6dB due to splitter loss
 
fig, ax = plt.subplots()
ax.plot(freq_cm_cm, s21_cm_cm, color="olivedrab", alpha=0.9)
ax.set_ylim([-14,-8])
ax.margins(x=0)

fig.suptitle("Common Mode Gain", fontsize=18)
ax.set_ylabel("dB", rotation=0, fontsize=16, labelpad=16)
ax.set_xlabel("Frequency (Hz)", fontsize=16)
ax.grid()

#fig.savefig("test.png")
fig.tight_layout()
fig.align_ylabels()
fig.savefig("cm_gain.png", dpi=300)
plt.show()

# 


file_data = pandas.read_csv(dm_n_file_name, sep=',', skiprows=13, header=None)
freq_dm_n = file_data[0].to_numpy()
s21_dm_n = file_data[1].to_numpy() + 3.0 # +3dB due to cm/dm split

file_data = pandas.read_csv(dm_l_file_name, sep=',', skiprows=13, header=None)
freq_dm_l = file_data[0].to_numpy()
s21_dm_l = file_data[1].to_numpy() + 3.0 # +3dB due to cm/dm split


fig, ax = plt.subplots()
ax.plot(freq_dm_n, s21_dm_n, color="olivedrab", alpha=0.9, label="Neutral")
ax.plot(freq_dm_l, s21_dm_l, color="coral", alpha=0.9, label="Line")

ax.set_ylim([-12,-8])
ax.margins(x=0)
ax.legend()

fig.suptitle("Differential Mode Gain", fontsize=18)
ax.set_ylabel("dB", rotation=0, fontsize=16, labelpad=16)
ax.set_xlabel("Frequency (Hz)", fontsize=16)
ax.grid()

fig.tight_layout()
fig.align_ylabels()
fig.savefig("dm_gain.png", dpi=300)
plt.show()


#impedances
file_data = pandas.read_csv(l_impedance_file_name, sep=',', skiprows=13, header=None)
freq_l_impedance = file_data[0].to_numpy()
l_r = file_data[1].to_numpy()
l_z = file_data[2].to_numpy() - 2*np.pi*freq_l_impedance * 50E-9 #subtract out adaptor impedance
l_abs_z = np.abs(l_r + 1.0j * l_z)
l_phase= np.angle(l_r + 1.0j * l_z, deg=True)

file_data = pandas.read_csv(n_impedance_file_name, sep=',', skiprows=13, header=None)
freq_n_impedance = file_data[0].to_numpy()
n_r = file_data[1].to_numpy()
n_z = file_data[2].to_numpy() - 2*np.pi*freq_n_impedance * 60E-9 #subtract out adaptor impedance
n_abs_z = np.abs(n_r + 1.0j * n_z)
n_phase = np.angle(n_r + 1.0j * n_z, deg=True)

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

ax1.plot(freq_l_impedance, l_abs_z, color="olivedrab", alpha=0.9, label="Line")
ax1.plot(freq_n_impedance, n_abs_z, color="coral", alpha=0.9, label="Neutral")
ax2.plot(freq_l_impedance, l_phase, color="olivedrab", alpha=0.9, label="Line")
ax2.plot(freq_n_impedance, n_phase, color="coral", alpha=0.9, label="Neutral")


#ax.set_ylim([-12,-8])
ax1.margins(x=0)
ax1.legend()

fig.suptitle("LISN Impedance", fontsize=18)
ax1.set_ylabel("|Z|", rotation=0, fontsize=16, labelpad=16)
ax2.set_ylabel(r'$\theta$', rotation=0, fontsize=16, labelpad=16)
#ax1.set_xlabel("Frequency (Hz)", fontsize=16)
ax2.set_xlabel("Frequency (Hz)", fontsize=16)
ax1.grid()
ax2.grid()

fig.tight_layout()
fig.align_ylabels()
fig.savefig("lisn_impedance.png", dpi=300)
plt.show()




