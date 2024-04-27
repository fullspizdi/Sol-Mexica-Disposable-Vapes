import markdown2
from fpdf import FPDF

def convert_md_to_pdf(input_filename, output_filename):
    """
    Converts a Markdown file to a PDF file using markdown2 for HTML conversion and FPDF for PDF generation.
    
    Args:
    input_filename (str): The path to the Markdown file to be converted.
    output_filename (str): The path where the PDF file will be saved.
    """
    # Read the Markdown file and convert it to HTML
    with open(input_filename, 'r') as md_file:
        html_text = markdown2.markdown(md_file.read(), extras=["tables"])

    # Create a PDF object and add a page
    pdf = FPDF()
    pdf.add_page()

    # Set the font and size for the PDF
    pdf.set_font("Arial", size=12)

    # Add the HTML text to the PDF
    pdf.write(5, html_text)

    # Output the PDF to the specified file
    pdf.output(output_filename)

def main():
    # Convert the Markdown document to a PDF
    convert_md_to_pdf('whitepaper.md', 'Sol_Mexica_Whitepaper.pdf')

if __name__ == "__main__":
    main()
