import cairo
import math

# Create an image surface with ARGB32 format
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(1, 1, 1)  # Set background color to light gray
ctx.paint()

ctx.set_line_width(2)

# Draw the bottom part of the cross
ctx.move_to(180, 90)
ctx.line_to(210, 90)
ctx.line_to(200, 50)
ctx.line_to(190, 50)
ctx.set_source_rgb(0, 0, 0)  # Set color to black
ctx.fill()

# Join the two parts of the cross
ctx.move_to(190, 50)
ctx.line_to(200, 50)
ctx.line_to(195, 40)
ctx.line_to(190, 50)
ctx.set_source_rgb(0, 0, 0)
ctx.fill()

# Draw the cross
ctx.move_to(195, 50)
ctx.line_to(195, 15)
ctx.move_to(185, 25)
ctx.line_to(205, 25)
ctx.set_source_rgb(0, 0, 0)
ctx.stroke()

# Draw the bar below the cross
ctx.rectangle(160, 91, 70, 9)
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()

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

# Draw the central block of the chapel
ctx.move_to(130, 170)
ctx.line_to(130, 270)
ctx.line_to(260, 270)
ctx.line_to(260, 170)
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()

# Draw windows in the center block
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

# Draw the structure of the center block
ctx.move_to(130, 170)
ctx.line_to(130, 270)
ctx.line_to(260, 270)
ctx.line_to(260, 170)
ctx.line_to(240, 160)
ctx.line_to(150, 160)
ctx.close_path()
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()

# Draw the center roof structure
ctx.move_to(120, 180)
ctx.line_to(150, 160)
ctx.line_to(240, 160)
ctx.line_to(270, 180)
ctx.line_to(270, 170)
ctx.line_to(240, 150)
ctx.line_to(150, 150)
ctx.line_to(120, 170)
ctx.close_path()
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()

# Draw a circular window in the center block
ctx.arc(195, 175, 10, math.radians(0), math.radians(360))
ctx.set_source_rgb(1, 1, 1)
ctx.fill()

# Draw the roof above the door
ctx.move_to(150, 220)
ctx.line_to(195, 200)
ctx.line_to(240, 220)
ctx.line_to(240, 210)
ctx.line_to(195, 190)
ctx.line_to(150, 210)
ctx.close_path()
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()

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


surface.write_to_png('Chapel2.png')