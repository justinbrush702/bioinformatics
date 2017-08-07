import color_brush

# Fun program I made when taking a break from constructing phylogenetic trees via neighbor joining

colorBrush = color_brush
text = 'THANKS FOR WATCHING!'

def paintText (color):
    colorBrush.setColor(color)
    print text,

for count in range(70):
    paintText('HEADER')
    paintText('INFO')
    paintText('SUCCESS')
    paintText('WARNING')
    paintText('FAIL')

# Don't want the final color on the 'color brush' stuck in the terminal
colorBrush.resetColor()
