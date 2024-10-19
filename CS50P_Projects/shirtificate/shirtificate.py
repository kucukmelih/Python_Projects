from fpdf import FPDF

name = input("Name: ")

pdf = FPDF(orientation = 'P', format = 'A4')
pdf.add_page()

pdf.set_font("helvetica", "B", 48)
pdf.cell(0, 60, "CS50 Shirtificate", align = "C")

image_width = 165
image_height = 150
x_image = (210 - image_width) / 2
y_image = 80
pdf.image("shirtificate.png", x = x_image, y = y_image, w = image_width, h = image_height)

pdf.set_font_size(24)
pdf.set_text_color(255, 255, 255)

text = f"{name} took CS50"
text_width = pdf.get_string_width(text)
x_text = (210 - text_width) / 2

y_text = y_image + (image_height / 2)

pdf.text(x = x_text, y = y_text, text = text)

pdf.output("shirtificate.pdf")
