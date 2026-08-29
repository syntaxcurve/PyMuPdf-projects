import fitz

# Create Document Object 
pdf = fitz.open()

img = fitz.Pixmap("photo.jpg")

rect = fitz.Rect(img.irect)

# Create Empty page[0] with img's width $  height
page = pdf.new_page(
    width=rect.width,
    height=rect.height
)

# Now insert image
page.insert_image(
    rect=rect,
    filename="photo.jpg"
)

pdf.save("new.pdf")
pdf.close()

print("You're photo --> pdf is ready !!!")