import streamlit as st
import leafmap.foliumap as leafmap
from PIL import Image

# Set up Streamlit page
st.set_page_config(layout="wide")

# Sidebar Logo
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

# Main App Title
st.title("Before and After with Image Upload")

# Render the Map
m = leafmap.Map()
before = "https://github.com/opengeos/datasets/releases/download/raster/Libya-2023-07-01.tif"
after = "https://github.com/opengeos/datasets/releases/download/raster/Libya-2023-09-13.tif"
m.split_map(
    left_layer=before, right_layer=after, left_label="Before", right_label="After"
)
m.add_legend(title="ESA Land Cover", builtin_legend="ESA_WorldCover")
m.to_streamlit(height=700)

# Section for Image Upload
st.header("Upload an Image for Processing")

uploaded_file = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Load the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Resize the image to 15x15
    resized_image = image.resize((15, 15))
    st.image(resized_image, caption="Resized to 15x15", use_container_width=True)

    # Debug: Print the dimensions of the resized image
    st.write(f"Resized Image Dimensions: {resized_image.size}")

    # Convert the resized image to a format usable by your deep learning model
    image_array = list(resized_image.getdata())
    st.write("Image converted to 15x15 array:")
    st.write(image_array)

    # Add further processing or model inference here
    # Example: model_output = your_model.predict(image_array)
    # st.write(f"Model Output: {model_output}")
