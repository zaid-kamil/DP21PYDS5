from os import fsdecode
import streamlit as st
from PIL import Image,ImageFont,ImageDraw, ImageFilter

st.title("Image Editor")
upload = st.file_uploader("Upload an image", type=["jpg", "png"])
if upload is not None:
    image = st.sidebar.image(upload.read(), use_column_width=True)
    img = Image.open(upload)

    content = st.text_input("add text on image")
    filter = st.selectbox('filters',['blur','contour','edge'])
    col = st.columns(4)
    fs = col[0].slider("font size", 1, img.width, 50)
    px = col[1].slider("position x", 1, img.width, 50)
    py = col[2].slider("position y", 1, img.height, 50)
    color = col[3].color_picker("text color")

    btn = st.button("confirm to create")
    if btn and content:
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("font.ttf", fs)
        draw.text((px, py), content, color,font=font)
        if filter == 'blur':
            img = img.filter(ImageFilter.GaussianBlur(20))
        elif filter == 'contour':
            img = img.filter(ImageFilter.CONTOUR)
        elif filter == 'edge':
            img = img.filter(ImageFilter.FIND_EDGES)
        img.save("edit_image.png")
        st.image("edit_image.png", use_column_width=True)


# to run this , write the following in terminal:
# streamlit run image_processing/example.py

# if pillow is missing
# pip install pillow