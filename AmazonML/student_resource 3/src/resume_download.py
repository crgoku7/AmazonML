import csv
import requests
import os
import urllib.parse

# Create directories if they don't already exist
for i in range(1, 11):
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

# Function to create a valid file name from the image name
def create_valid_filename(name):
    return urllib.parse.quote_plus(name)

# Open the CSV file and read the image links
csv_file = 'E:/AMAZONML/student_resource 3/dataset/test.csv'  # Replace with your CSV file name

# Determine the number of images per folder based on previous calculation or dynamically
total_images = 113000  # Use the known number or calculate it dynamically
images_per_folder = total_images // 10

# Identify the last downloaded image
last_downloaded_image = 15125  # The last downloaded image before the interruption
start_index = last_downloaded_image + 1  # Start from the next image after the one that was downloaded last

with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header
    
    for idx, row in enumerate(csv_reader):
        image_name = row[0]  # First column has the image name
        image_url = row[1]  # Second column has the image URL
        folder_index = (idx // images_per_folder) + 1  # Determine the folder number (1-10)

        # Only start downloading images after the last one successfully downloaded
        if idx + 1 >= start_index:  # Adjust idx for 1-based index (i.e., idx + 1)
            valid_image_name = create_valid_filename(image_name)
            download_image(image_url, valid_image_name, folder_index)
