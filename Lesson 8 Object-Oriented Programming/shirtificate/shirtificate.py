from fpdf import FPDF

def main():
    name = input("Name: ").strip()

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Set font for the title
    pdf.set_font("Arial", "B", 24)

    # Calculate width of the page for centering text
    page_width = pdf.w

    # Title: "CS50 Shirtificate"
    title = "CS50 Shirtificate"
    title_width = pdf.get_string_width(title)
    pdf.set_xy((page_width - title_width) / 2, 20)  # y=20mm from top
    pdf.cell(title_width, 10, title)

    # Add shirt image centered horizontally
    # Shirt image path
    image_path = "shirtificate.png"

    # Dimensions for image (tweak as needed)
    img_width = 120
    img_height = 120

    # Calculate x position to center the image
    x_image = (page_width - img_width) / 2
    y_image = 40  # a bit below title

    pdf.image(image_path, x=x_image, y=y_image, w=img_width, h=img_height)

    # Overlay the name on top of shirt
    # Set font and color for the name text
    pdf.set_font("Arial", "B", 28)
    pdf.set_text_color(255, 255, 255)  # white text

    # Calculate width of name to center it
    name_width = pdf.get_string_width(name)
    # Position name roughly vertically centered on shirt image
    y_name = y_image + img_height / 2

    pdf.set_xy((page_width - name_width) / 2, y_name)
    pdf.cell(name_width, 10, name)

    # Save the PDF
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
