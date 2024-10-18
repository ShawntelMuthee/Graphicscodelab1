import cairo
import math

# Create the final image surface
width, height = 700, 700
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
ctx = cairo.Context(surface)

# Set background color (white)
ctx.set_source_rgb(1, 1, 1)
ctx.paint()

# Main building (middle church)
ctx.set_source_rgb(0, 0, 0)
ctx.rectangle(100, 200, 200, 140)  # Adjusted position
ctx.fill()

# Roof
ctx.move_to(100, 200)
ctx.line_to(145, 150)
ctx.line_to(250, 150)
ctx.line_to(300, 200)
ctx.fill()

# Draw the outer shape
ctx.move_to(80, 215)
ctx.line_to(143, 145)
ctx.line_to(250, 145)
ctx.line_to(320, 215)
ctx.stroke()

# Draw the inner shape
ctx.move_to(75, 205)
ctx.line_to(141, 135)
ctx.line_to(254, 135)
ctx.line_to(321, 205)
ctx.stroke()

# Fill the space between the two shapes
ctx.move_to(80, 215)
ctx.line_to(143, 145)
ctx.line_to(250, 145)
ctx.line_to(320, 215)
ctx.line_to(321, 205)
ctx.line_to(254, 135)
ctx.line_to(141, 135)
ctx.line_to(75, 205)
ctx.close_path()
ctx.set_source_rgb(0, 0, 0)  # Set color to black
ctx.fill()

# Redraw the outer shape to make it visible over the fill
ctx.move_to(80, 215)
ctx.line_to(143, 145)
ctx.line_to(250, 145)
ctx.line_to(320, 215)
ctx.stroke()

# Redraw the inner shape to make it visible over the fill
ctx.move_to(75, 205)
ctx.line_to(141, 135)
ctx.line_to(254, 135)
ctx.line_to(321, 205)
ctx.stroke()

# Circular window
ctx.arc(200, 175, 15, 0, 2 * math.pi)
ctx.set_source_rgb(1, 1, 1)
ctx.fill()

# the white roof
ctx.move_to(145, 260)
ctx.line_to(200, 200)
ctx.line_to(255, 260)
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()

ctx.move_to(150, 265)
ctx.line_to(200, 210)
ctx.line_to(250, 265)
ctx.move_to(145, 260)
ctx.line_to(150, 265)
ctx.move_to(255, 260)
ctx.line_to(250, 265)
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()

# Door
ctx.arc(200, 235, 25, 3.14, 2 * 3.14)  # Semi-circle for the top
ctx.fill()
ctx.rectangle(175, 235, 50, 80)  # Rectangle for the bottom part of the door
ctx.fill()

ctx.move_to(200, 210)
ctx.line_to(200, 315)
ctx.set_line_width(5)
ctx.set_source_rgb(0, 0, 0)
ctx.stroke()

# Right side house
ctx.set_source_rgb(0, 0, 0)  # Black color for house body
ctx.rectangle(350, 200, 150, 150)  # Adjusted position
ctx.fill()

# Drawing the roof for the right house
ctx.move_to(350, 200)
ctx.line_to(500, 200)
ctx.line_to(450, 120)
ctx.line_to(350, 120)
ctx.close_path()
ctx.fill()

# Drawing windows for the right house
ctx.set_source_rgb(1, 1, 1)  # White color for windows
ctx.rectangle(390, 240, 50, 40)  # Left window
ctx.fill()
ctx.rectangle(450, 240, 50, 40)  # Right window
ctx.fill()

# Left side house
ctx.set_source_rgb(0, 0, 0)  # Black color for house body
ctx.rectangle(0, 200, 150, 150)  # Adjusted position
ctx.fill()

# Drawing the roof for the left house
ctx.move_to(0, 200)
ctx.line_to(150, 200)
ctx.line_to(100, 120)
ctx.line_to(0, 120)
ctx.close_path()
ctx.fill()

# Drawing windows for the left house
ctx.set_source_rgb(1, 1, 1)  # White color for windows
ctx.rectangle(30, 240, 50, 40)  # Left window
ctx.fill()
ctx.rectangle(80, 240, 50, 40)  # Right window
ctx.fill()

# Top building with arched window
ctx.set_source_rgb(0, 0, 0)  # Black color for rectangle
ctx.move_to(50, 40)  # Adjusted position for line
ctx.line_to(230, 40)
ctx.set_line_width(20)
ctx.stroke()

# Draw the black rectangle
ctx.rectangle(70, 60, 170, 80)  # Adjusted height for better proportion
ctx.fill()

# Set white color for the arched window
ctx.set_source_rgb(1, 1, 1)

# Draw the arched window (semi-circle + rectangle)
ctx.arc(155, 100, 30, 3.14, 2 * 3.14)  # Adjusted position for arch
ctx.fill()
ctx.rectangle(125, 100, 60, 40)  # Rectangle for the bottom part of the window
ctx.fill()

# Cross on top of the arched window
ctx.set_source_rgb(0, 0, 0)  # Black for cross
ctx.rectangle(150, 80, 10, 40)  # Vertical part
ctx.fill()
ctx.rectangle(130, 90, 60, 10)  # Horizontal part
ctx.fill()

# Save the final image
surface.write_to_png("chapel.png")

print("Final image saved as 'chapel.png'")
