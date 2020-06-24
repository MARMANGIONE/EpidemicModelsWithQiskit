import networkx as nx
import ndlib.models.ModelConfig as mc
import ndlib.models.epidemics as ep
from bokeh.io import show
from ndlib.viz.bokeh.DiffusionTrend import DiffusionTrend
from ndlib.viz.bokeh.MultiPlot import MultiPlot

# Network topology
g = nx.erdos_renyi_graph(1000, 0.1)

# Model selection
model = ep.SEIRModel(g)
# Model Configuration
cfg = mc.Configuration()
cfg.add_model_parameter('beta', 0.01)
cfg.add_model_parameter('gamma',0.005)
cfg.add_model_parameter('alpha', 0.05)
cfg.add_model_parameter("percentage_infected", 0.05)
model.set_initial_status(cfg)

iterations = model.iteration_bunch(200)
trends = model.build_trends(iterations)

viz = DiffusionTrend(model, trends)
p = viz.plot(width=600, height=600)
show(p)

