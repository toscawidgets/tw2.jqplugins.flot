
from widgets import FlotWidget

import math
def f(x):
    return x/math.pi

class DemoFlot(FlotWidget):
    data = [
        {
            'data' : [[f(i), math.sin(f(i))] for i in range(20)],
            'label' : "sin(x)"
        }
    ]
    label = "sin plot"
