from ocp_vscode import show

from build123d import *

# ============================================================
# Parameters
# ============================================================

# Legs
leg_size = 40
leg_height = 700

# tray top
top_length = 1200
top_width = 800
top_thickness = 40

# Overhangs
overhang_front = 50
overhang_back = 50
overhang_left = 50
overhang_right = 50

# Step (mounted on FRONT side)
step_width = 400
step_height = 200
step_depth = 250

# ============================================================
# Derived dimensions
# ============================================================

frame_length = top_length - overhang_left - overhang_right
frame_width = top_width - overhang_front - overhang_back

if frame_length <= leg_size * 2:
    raise ValueError("tray too short for selected overhangs.")

if frame_width <= leg_size * 2:
    raise ValueError("tray too narrow for selected overhangs.")

# Leg locations (center points)
x_left = -frame_length / 2 + leg_size / 2
x_right = frame_length / 2 - leg_size / 2

y_front = -frame_width / 2 + leg_size / 2
y_back = frame_width / 2 - leg_size / 2

# ============================================================
# Build tray
# ============================================================

with BuildPart() as tray:

    # --------------------------------------------------------
    # tray Top
    # --------------------------------------------------------
    with Locations((0, 0, leg_height + top_thickness / 2)):
        Box(top_length, top_width, top_thickness)

    # --------------------------------------------------------
    # Legs
    # --------------------------------------------------------
    leg_positions = [
        (x_left, y_front, leg_height / 2),
        (x_left, y_back, leg_height / 2),
        (x_right, y_front, leg_height / 2),
        (x_right, y_back, leg_height / 2),
    ]

    with Locations(*leg_positions):
        Box(leg_size, leg_size, leg_height)

    # --------------------------------------------------------
    # Step (front side)
    # --------------------------------------------------------
    step_y = -(frame_width / 2 + step_depth / 2)

    with Locations((0, step_y, step_height / 2)):
        Box(step_width, step_depth, step_height)

# ============================================================
# Show
# ============================================================
#need to use compound because the step is 
# seperate due to size and pssobily algebra mode
export_stl(Compound(tray.solids()),"foodTrayAlgebraMode.stl")
export_step(Compound(tray.solids()),"foodTrayAlgebraMode.step")

show(tray)