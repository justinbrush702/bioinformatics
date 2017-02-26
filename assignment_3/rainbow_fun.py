import color_brush

# Fun program I made when taking a break from constructing phylogenetic trees via neighbor joining

colorBrush = color_brush
text = 'BIOINFORMATICS IS SO MUCH FUN!!!!!'

def paintText (color):
    colorBrush.setColor(color)
    print text,

for count in range(500):
    paintText('HEADER')
    paintText('INFO')
    paintText('SUCCESS')
    paintText('WARNING')
    paintText('FAIL')

# Don't want the final color on the 'color brush' stuck in the terminal
colorBrush.resetColor()
