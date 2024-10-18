# Draw the side structures of the chapel
ctx.rectangle(50, 220, 80, 40)  # Left side rectangle
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()
ctx.rectangle(260, 220, 80, 40)  # Right side rectangle
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()

# Draw small white rectangles for windows on the sides
ctx.rectangle(60, 230, 20, 15)
ctx.set_source_rgb(1, 1, 1)
ctx.fill()
ctx.rectangle(90, 230, 20, 15)
ctx.set_source_rgb(1, 1, 1)
ctx.fill()
ctx.rectangle(280, 230, 20, 15)
ctx.set_source_rgb(1, 1, 1)
ctx.fill()
ctx.rectangle(310, 230, 20, 15)
ctx.set_source_rgb(1, 1, 1)
ctx.fill()

# Draw trapezoidal shapes on the sides
ctx.move_to(80, 190)
ctx.line_to(130, 190)
ctx.line_to(130, 220)
ctx.line_to(40, 220)
ctx.close_path()
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()

ctx.move_to(260, 190)
ctx.line_to(310, 190)
ctx.line_to(350, 220)
ctx.line_to(260, 220)
ctx.close_path()
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()
