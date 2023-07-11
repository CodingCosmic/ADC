import math

def calculate_antenna_dimensions(frequency, velocity_factor):
    # Constants for antenna calculations
    speed_of_light = 299792458  # Speed of light in meters per second

    # Calculate the wavelength
    wavelength = speed_of_light / (frequency * 10**6)

    # Calculate the antenna length
    antenna_length = wavelength / 2

    # Calculate the physical length based on the velocity factor
    physical_length = antenna_length / velocity_factor

    # Return the results
    return wavelength, antenna_length, physical_length

# Prompt the user for the frequency in MHz
frequency = float(input("Enter the frequency in MHz: "))

# Prompt the user for the velocity factor
velocity_factor = float(input("Enter the velocity factor of the transmission medium: "))

# Calculate antenna dimensions
wavelength, antenna_length, physical_length = calculate_antenna_dimensions(frequency, velocity_factor)

# Display the results
print(f"Wavelength: {wavelength:.2f} meters")
print(f"Antenna length: {antenna_length:.2f} meters")
print(f"Physical length: {physical_length:.2f} meters")
