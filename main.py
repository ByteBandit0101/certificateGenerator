from PIL import Image, ImageDraw, ImageFont
import pandas as pd

# Load the certificate template image
template_image_path = "./Template/example.png"
certificate_template = Image.open(template_image_path)

# Load the participants list
participants_path = "./Csv/example.csv"
participants = pd.read_csv(participants_path, usecols=[0], header=None, names=["Name"])

# If the template is in RGBA mode, convert it to RGB
if certificate_template.mode == 'RGBA':
    certificate_template = certificate_template.convert('RGB')

# Font for writing on the certificate
font_path = "arial.ttf"
font_size = 55
font = ImageFont.truetype(font_path, font_size)

for index, participant in participants.iterrows():
    # Make a copy of the template for each certificate
    certificate = certificate_template.copy()
    draw = ImageDraw.Draw(certificate)

    # Coordinates where the name will be inserted (adjust as necessary)
    name_x, name_y = 215, 680

    # Convert the name to string and remove any extra space
    participant_name = str(participant['Name']).strip()

    # Write the name on the certificate
    draw.text((name_x, name_y), participant_name, font=font, fill='black')

    # Save the certificate
    output_path = f"certificate_{participant_name.replace(' ', '_')}.png"
    certificate.save(output_path)

print("Certificates created successfully!")