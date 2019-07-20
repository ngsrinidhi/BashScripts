import matplotlib.mlab as mlab
import numpy as np
import h5py
import matplotlib
matplotlib.use('Agg')
import matplotlib.colorbar as cbar
import matplotlib.pyplot as plt
from matplotlib_colorbar.colorbar import Colorbar
#from mpl_toolkits.mplot3d import Axes3D 
import scipy.stats
import glob

filename = glob.glob('*.h5')

for k in range(np.size(filename)):
  vel = h5py.File(filename[k],"r")
  u = np.array(vel['var'])
  u = np.asarray(u)
  print(np.shape(u))

  if u.ndim > 1:
     u = np.mean(np.mean(u,axis=2),axis=1)
  nz = np.size(u)

  filnam = filename[k].replace('.h5','.dat')
  file = open(filnam,"w")
  for i in range(nz):
      file.write("%8.8f\n" %u[i])
  file.close()
