import cairo
import math

# Create an image surface with ARGB32 format
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(1, 1, 1)  # Set background color to light gray
ctx.paint()

# Draw the doors
ctx.rectangle(160, 220, 34, 47)
ctx.rectangle(196, 220, 34, 47)
ctx.fill()

ctx.move_to(160, 220)
ctx.curve_to(170, 210, 180, 210, 194, 210)
ctx.line_to(194, 220)
ctx.close_path()
ctx.fill()

ctx.move_to(196, 210)
ctx.curve_to(210, 210, 220, 210, 229, 220)
ctx.line_to(196, 220)
ctx.close_path()
ctx.fill()

# Draw the top part of the chapel
ctx.rectangle(170, 100, 50, 50)
ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(1)
ctx.fill_preserve()
ctx.stroke()

# Draw the arched top of the chapel
ctx.move_to(180, 120)
ctx.line_to(180, 147)
ctx.line_to(210, 147)
ctx.line_to(210, 120)
ctx.arc(195, 120, 15, math.pi, 0)
ctx.set_source_rgb(1, 1, 1)
ctx.set_line_width(1)
ctx.fill_preserve()
ctx.stroke()


surface.write_to_png('chapel.png')