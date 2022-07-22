# Prettymaps
from prettymaps import *
# Vsketch
import vsketch
# OSMNX
import osmnx as ox
# Matplotlib-related
import matplotlib.font_manager as fm
from matplotlib import pyplot as plt
from descartes import PolygonPatch
# Shapely
from shapely.geometry import *
from shapely.affinity import *
from shapely.ops import unary_union


# Style parameters
palette = ['#433633', '#FF5E5B']
background_c = '#F2F4CB'
dilate = 100
plt.clf()

# Setup figure
fig, ax = plt.subplots(figsize = (10, 10), constrained_layout = True)

# Plot
layers = plot(
    (55.95105753533523, -3.2071686956389356), radius = 1100,
    ax = ax,
    layers = {
        'perimeter': {'circle': False, 'dilate': dilate},
        'streets': {
            'width': {
                'primary': 5,
                'secondary': 4,
                'tertiary': 3,
                'residential': 2,
                'footway': 1,
            },
            'circle': True,
            'dilate': dilate
        },
        'building': {
            'tags': {'building': True},
            'union': False,
            'circle': True,
            'dilate': dilate
        },
        'green': {
            'tags': {
                'landuse': ['grass', 'village_green'],
                'leisure': 'park'
            },
            'circle': True,
            'dilate': dilate
        },
        'green': {
            'tags': {
                'landuse': ['grass', 'village_green'],
                'leisure': 'park'
            },
            'circle': True,
            'dilate': dilate
        },
        'water': {
            'tags': {'natural': 'water'},
            'circle': True,
            'dilate': dilate
        },
    },
    drawing_kwargs = {
        'background': {'fc': '#F2F4CB', 'ec': '#dadbc1', 'hatch': 'ooo...', 'zorder': -1},
        'perimeter': {'fill': False, 'lw': 1, 'zorder': 1},
        'green': {'fc': '#8BB174', 'ec': '#2F3737', 'hatch_c': '#A7C497', 'hatch': 'ooo...', 'lw': 1, 'zorder': 1},
        'water': {'fc': '#a8e1e6', 'ec': '#2F3737', 'hatch_c': '#9bc3d4', 'hatch': 'ooo...', 'lw': 1, 'zorder': 3},
        'streets': {'fc': '#2F3737', 'ec': '#475657', 'alpha': 1, 'lw': 0, 'zorder': 4},
        'building': {'palette': palette, 'ec': '#2F3737', 'lw': .5, 'zorder': 5},
    },
)

# Set bounds
xmin, ymin, xmax, ymax = layers['perimeter'].bounds
dx, dy = xmax-xmin, ymax-ymin
ax.set_xlim(xmin-.06*dx, xmax+.06*dx)
ax.set_ylim(ymin-.06*dy, ymax+.06*dy)

# # Draw left text
ax.text(
    xmin-.06*dx, ymin+.5*dy,
    'EH2 4ET',
    color = '#2F3737',
    rotation = 90,
    # You'll need to download this font from https://www.dafontfree.net/permanent-marker-regular/f81353.htm 
    # and add it to the 'assets' folder before uncommenting this line:
    # fontproperties = fm.FontProperties(fname = './assets/Permanent_Marker/PermanentMarker.ttf', size = 35),
)

plt.savefig('test.png')