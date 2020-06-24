import networkx as nx
import ndlib.models.epidemics as ep
from bokeh.io import output_notebook, show
import ndlib.models.ModelConfig as mc
from ndlib.viz.bokeh.DiffusionTrend import DiffusionTrend
import csv

# Network topology
g = nx.erdos_renyi_graph(1000, 0.1)

# Model Selection
sis_model = ep.SISModel(g)

# Model Configuration
config = mc.Configuration()
config.add_model_parameter('beta', 0.005)
config.add_model_parameter('lambda', 0.01)
config.add_model_parameter("percentage_infected", 0.01)
sis_model.set_initial_status(config)

# Simulation
iterations = sis_model.iteration_bunch(100)
trends = sis_model.build_trends(iterations)

viz = DiffusionTrend(sis_model, trends)
p = viz.plot(width=400, height=400)
show(p)