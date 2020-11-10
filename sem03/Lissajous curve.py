from ipywidgets import interactive, RadioButtons
import math
import matplotlib
import numpy

def graph_plotter(α, β, δ):
  matplotlib.pyplot.figure()
  t = numpy.linspace(0, 10, 1000)
  x = numpy.sin(α * t + δ)
  y = numpy.sin(β * t)
  matplotlib.pyplot.plot(x, y)
  matplotlib.pyplot.axis("equal")
  matplotlib.pyplot.axis("off")
  matplotlib.pyplot.show()

interactive_plot = interactive(
    graph_plotter, 
    α = (1, 10), 
    β = (1, 10), 
    δ = RadioButtons(options=[('0', 0), ('π / 4', math.pi/4), ('π / 2', math.pi/2), ('3π / 4', 3*math.pi/4), ('π', math.pi)], description = 'δ ')
  )
interactive_plot
