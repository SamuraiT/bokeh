
from collections import OrderedDict
import numpy as np
import pandas as pd
from bokeh.plotting import *

N = 20
categories = ['y' + str(x) for x in xrange(10)]
data = {}
data['x'] = np.arange(N)
for cat in categories:
    data[cat] = np.random.randint(10, 100, size=N)

df = pd.DataFrame(data)
df = df.set_index(['x'])

def stacked(df, categories):
    areas = OrderedDict()
    last = np.zeros(len(df[categories[0]]))
    for cat in categories:
        next = last + df[cat]
        areas[cat] = np.hstack((last[::-1], next))
        last = next
    return areas

output_server("brewer")

areas = stacked(df, categories)

colors = brewer["Spectral"][len(areas)]

x2 = np.hstack((data['x'][::-1], data['x']))
patches([x2 for a in areas], areas.values(), color=colors, alpha=0.8, line_color=None)

show()

