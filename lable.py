import fitz

doc = fitz.open("ot.pdf")
out = fitz.open()

# t = 0

# while(t < 0.5):
#     doc.new_page().draw_circle(
#         center=(200,400),
#         radius=200,
#         fill=(t+0.2,t+0.1,t+0.05),
#         width=0
#     )
#     t+=0.1

# Place1
top = left = 0
x = y = 250
rect1 = fitz.Rect(0, 0, 250, 250)

# place2
top2 = 256
x2 = y2 = 500
rect2 = fitz.Rect(0, 256, 250, 500)

#place3
top3 = 510, left
x3 = y3 = (y2 + 250)
rect3 = fitz.Rect(0, 500, 250, 750)

pix_rect = fitz.Rect(0, 200, 400, 600)
page_index = 0
while(page_index < 3):
    out.new_page().insert_image(
        rect1,
        pixmap=doc[page_index].get_pixmap(
            clip=pix_rect
        )
        
    )
    page_index +=1
    out[0].insert_image(
        rect2,
        pixmap=doc[page_index].get_pixmap(
            clip=pix_rect
        )
        
    )
    page_index +=1
    out[0].insert_image(
        rect3,
        pixmap=doc[page_index].get_pixmap(
            clip=pix_rect
        )
        
    )
    page_index +=1
    

# out.new_page().insert_image(
#     fitz.Rect(10,10,250, 250),
#     pixmap=doc[0].get_pixmap(
#         clip=fitz.Rect(0, 200, 400, 600)
#     ),
#     keep_proportion=False
# )
out[0].draw_rect(
    fitz.Rect(0, 10, 600, 860),
    fill=(1,0.3,1),
    overlay=False
)

out.save("otput.pdf")
doc.close()

# print("done !")