import fitz

# Create Document Object 
pdf = fitz.open()

# Create Empty page[0]
page = pdf.new_page()

pdf.save("new.pdf")
pdf.close()

print(page)