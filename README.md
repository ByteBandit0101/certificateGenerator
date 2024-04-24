
# Certificate Generator

## Overview
This project provides a simple Python script for automatically generating certificates for course participants. The script uses a predefined template image and writes the names of the participants onto each certificate, saving them as individual PNG files. This tool is ideal for educators and event organizers looking to streamline the process of certificate creation.

## Features
- **Customizable Template**: Use any image as a background template.
- **Automatic Name Placement**: Names are read from a CSV file and placed onto the certificate.
- **PNG Output**: Certificates are saved in PNG format to preserve quality and potentially include transparency.

## Prerequisites
Before running the script, ensure you have Python installed along with the following packages:
- PIL (Pillow)
- pandas

You can install these packages using pip:
```bash
pip install Pillow pandas
```

## Usage
To use this script, follow these steps:
1. **Prepare your certificate template**: Save your certificate template as an image file in the `Template` folder.
2. **Prepare the participant list**: Create a CSV file with participant names in the first column, and save it in the `Csv` folder.
3. **Run the script**: Execute the script to generate certificates. Each participant's name will be added to the certificate and saved in the output directory.

## Configuration
You can customize the script by modifying the following parameters:
- `template_image_path`: Path to your certificate template image.
- `participants_path`: Path to your CSV file containing the names of the participants.
- `name_x` and `name_y`: Coordinates on the template where the name will be placed.
- `font_path` and `font_size`: Font settings for the names on the certificate.

