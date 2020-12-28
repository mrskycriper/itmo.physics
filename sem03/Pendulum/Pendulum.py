mport ipywidgets
import math
import numpy as np 
import matplotlib.pyplot as plt 


# fi0      # Амплитуда колебаний
# alpha    # Начальная фаза
# m        # Масса маятника
g = 9.8    # Ускорение свободного падения
# r        # Расстояние от точки подвеса до центра масс
# I        # Момент инерции маятника

def graph_plotter(fi0, alpha, m, r, I):
  time = np.arange(0, 10.0, 0.0025)
  y = fi0*np.sin(((m*g*r)/I)*time+alpha)
  plt.figure(figsize=(20,10))
  plt.plot(time, y)
  plt.title('Pendulum Motion:')
  plt.xlabel('Time (seconds)')
  plt.ylabel('Angle (rad)')
  plt.grid(True)
  plt.show()

interactive_plot = ipywidgets.interactive(
    graph_plotter,
    fi0 = ipywidgets.RadioButtons(options=[('0', 0), ('π / 6', math.pi/6), ('π / 3', math.pi/3), ('π / 4', math.pi/4), ('π / 2', math.pi/2)], description = 'Амплитуда: '),
    alpha = ipywidgets.RadioButtons(options=[('-π', -math.pi), ('-π / 2', -math.pi/2), ('0', 0), ('π / 2', math.pi/2), ('π', math.pi)], description = 'Фаза: '),
    m = ipywidgets.IntSlider(value=3, min=1, max=50, step=1, description='Масса:', continuous_update=False, readout=True, readout_format='d'),
    r = ipywidgets.IntSlider(value=2, min=1, max=10, step=1, description='Радиус:', continuous_update=False, readout=True, readout_format='d'),
    I = ipywidgets.IntSlider(value=12, min=1, max=100, step=1, description='Момент инерции:', continuous_update=False, readout=True, readout_format='d')
)
interactive_plot
