colors = {}
colors['HEADER'] = '\033[95m'
colors['INFO'] = '\033[94m'
colors['SUCCESS'] = '\033[32m'
colors['WARNING'] = '\033[33m'
colors['FAIL'] = '\033[91m'
colors['RESET'] = '\033[0m'

# A couple of text enhancers. They act independent of text color but still get reset when RESET is set
colors['BOLD'] = '\033[1m'
colors['UNDERLINE'] = '\033[4m'

# Set the "paint brush" of the terminal to a given color
def setColor (color):
    print colors[color],

# Set the paint brush of the terminal back to black
def resetColor ():
    setColor('RESET')

# When this script gets imported, the color in the terminal automatically gets reset to its default settings
resetColor()
