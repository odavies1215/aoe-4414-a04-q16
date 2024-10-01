# ecef_to_sez.py
#
# Usage: python3 ecef_to_sez.py o_x_km o_y_km o_z_km x_km y_km z_km
#  Converts ECEF coordinates to SEZ coordinates given an observer's position in ECEF.
# Parameters:
#  o_x_km: ECEF x-coordinate of the observer (in kilometers)
#  o_y_km: ECEF y-coordinate of the observer (in kilometers)
#  o_z_km: ECEF z-coordinate of the observer (in kilometers)
#  x_km: ECEF x-coordinate of the position (in kilometers)
#  y_km: ECEF y-coordinate of the position (in kilometers)
#  z_km: ECEF z-coordinate of the position (in kilometers)
#
# Output:
#  The SEZ coordinates: South (S), East (E), and Zenith (Z) in kilometers.
#
# Written by Owen Davies
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

import math  # math module
import sys   # argv for command line arguments

# Constants
R_E_KM = 6378.137  # Earth's radius in kilometers (approximate)

# Helper function to compute latitude and longitude from ECEF coordinates

# initialize script arguments
o_x_km = float('nan')
o_y_km = float('nan')
o_z_km = float('nan')
x_km = float('nan')
y_km = float('nan')
z_km = float('nan')

# Parse script arguments
if len(sys.argv) == 7:
    o_x_km = float(sys.argv[1])
    o_y_km = float(sys.argv[2])
    o_z_km = float(sys.argv[3])
    x_km = float(sys.argv[4])
    y_km = float(sys.argv[5])
    z_km = float(sys.argv[6])
else:
    print(\
    'Usage: '\
    'python3 ecef_to_sez.py o_x_km o_y_km o_z_km x_km y_km z_km'\
    )
    exit()
    

s_km=x_km - o_x_km
e_km=y_km - o_y_km
z_km=z_km - o_z_km

# Output the results
print(f"{s_km:.3f}")  # South
print(f"{e_km:.3f}")  # East
print(f"{z_km:.3f}")  # Zenith
