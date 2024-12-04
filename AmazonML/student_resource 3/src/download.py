import csv
import requests
import os
import urllib.parse
import math

# Create 10 directories to save the images
for i in range(9, 11):
    os.makedirs(f'downloaded_images/folder_{i}', exist_ok=True)

# Function to download an image
def download_image(image_url, image_name, folder_index):
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            folder_path = f'downloaded_images/folder_{folder_index}'
            image_path = os.path.join(folder_path, image_name + '.jpg')
            with open(image_path, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded: {image_name} in folder_{folder_index}")
        else:
            print(f"Failed to download: {image_url}")
    except Exception as e:
        print(f"Error downloading {image_url}: {e}")

# Function to create a valid file name from the name (if needed)
def create_valid_filename(name):
    return urllib.parse.quote_plus(name)

# Open the CSV file and read the image links
csv_file = 'E:/AMAZONML/student_resource 3/src/test.csv'  # Replace with your CSV file name

# Count total number of images in the CSV file
with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    total_images = sum(1 for row in csv_reader) - 1  # Subtract 1 for the header

# Calculate how many images per folder
images_per_folder = math.ceil((131287+1) / 10)

with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header

    for idx, row in enumerate(csv_reader):
        image_name = row[0]  # First column has the image name
        image_url = row[1]  # Second column has the image URL
        folder_index = ((idx+109335) // images_per_folder) + 1  # Determine the folder number (1-10)
        
        # Generate valid image name
        valid_image_name = create_valid_filename(image_name)
        
        # Download the image into the appropriate folder
        download_image(image_url, valid_image_name, folder_index)
