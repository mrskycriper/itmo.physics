import ipywidgets
import matplotlib.pyplot as plt
import numpy as np

def grated_diffraction_intensity (slit_width, wavelength, screen_distance, distance_between_slits, number_of_slits, X):
  term1 = np.sin(np.pi*X*slit_width/(wavelength*screen_distance))/(np.pi*X*slit_width/(wavelength*screen_distance)) 
  term2 = (np.sin(number_of_slits*np.pi*distance_between_slits*X/(wavelength*screen_distance)))/(number_of_slits*np.sin((np.pi*distance_between_slits*X)/(wavelength*screen_distance))) 
  return (term1**2)*(term2**2)

def plot(slit_width, wavelength, screen_distance, distance_between_slits, number_of_slits, radius):
  X = np.arange(-radius,radius,0.00001)
  Y = grated_diffraction_intensity(slit_width*(10**-6), wavelength*(10**-9), screen_distance*(10**-2), distance_between_slits*(10**-3), number_of_slits, X)
  plt.figure(figsize=(20,10))
  plot = plt.plot(X,Y)
  plt.xlabel("Радиус")
  plt.ylabel("Интесивность")
  plt.show()

interactive_plot = ipywidgets.interactive(
  plot,
  number_of_slits = ipywidgets.IntSlider(value=25, min=1, max=50, step=1, description='Щели:', continuous_update=False, readout=True, readout_format='d'),
  wavelength = ipywidgets.IntSlider(value=500, min=400, max=700, step=1, description='Длина волны, нм:', continuous_update=False, readout=True, readout_format='d'),
  slit_width = ipywidgets.IntSlider(value=100, min=1, max=199, step=1, description='Ширина щелей, мкм:', continuous_update=False, readout=True, readout_format='d'),
  distance_between_slits= ipywidgets.IntSlider(value=1, min=1, max=199, step=1, description='Расстояние между щелями, мкм:', continuous_update=False, readout=True, readout_format='d'),
  screen_distance = ipywidgets.IntSlider(value=50, min=1, max=100, step=1, description='Расстояние до экрана, см:', continuous_update=False, readout=True, readout_format='d'),
  radius = ipywidgets.FloatSlider(value=0.001, min=0.0001, max=0.1, step=0.001, description='Радиус:', continuous_update=False, readout=True, readout_format='.5f')
)
interactive_plot
