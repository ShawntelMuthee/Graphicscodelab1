import cairo

width, height = 400, 600
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
ctx = cairo.Context(surface)
ctx.set_source_rgb(1, 1, 1)
ctx.paint()

ctx.set_source_rgb(0, 0, 0)

#bass of the rectangle
ctx.move_to(155, 400)  # Bottom-left point
ctx.line_to(244, 400)  # Bottom-right point
ctx.line_to(230, 250)  # Top-right point
ctx.line_to(170, 250)  # Top-left point
ctx.close_path()
ctx.fill()

# the trapezoid
ctx.move_to(170, 250)  # Bottom-left of the triangle
ctx.line_to(230, 250)  # Bottom-right of the triangle
ctx.line_to(200, 200)  # Top point of the triangle
ctx.close_path()
ctx.fill()

# cross-vertical part
ctx.rectangle(190, 100, 19, 140)  
ctx.fill()

# cross-horizontal part
ctx.rectangle(170, 122, 60, 15)
ctx.fill()

# Save the image
surface.write_to_png("cross.png")
