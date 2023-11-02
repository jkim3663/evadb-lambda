import random

# Open the PNG file in binary read mode
with open('./img/sample_img_corrupt.png', 'rb') as file:
    png_data = bytearray(file.read())

# Define the percentage of data to corrupt (e.g., 10%)
corruption_percentage = 10

# Calculate the number of bytes to corrupt
bytes_to_corrupt = int(len(png_data) * (corruption_percentage / 100))

# Randomly select and corrupt bytes
for _ in range(bytes_to_corrupt):
    index = random.randint(0, len(png_data) - 1)
    png_data[index] = random.randint(0, 255)

# Save the corrupted data back to a new file
with open('./img/sample_img_corrupt.png', 'wb') as file:
    file.write(png_data)

print(f"Corrupted PNG file saved as 'corrupted_image.png'.")