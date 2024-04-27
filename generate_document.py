import json
import markdown2
from fpdf import FPDF

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def generate_markdown():
    features = load_json('features.json')
    specifications = load_json('specifications.json')

    with open('whitepaper.md', 'w') as md_file:
        md_file.write("# Sol Mexica Disposable Vapes Whitepaper\n\n")
        md_file.write("## 1. Introduction\n\n")
        md_file.write("Sol Mexica introduces a premium line of disposable vape devices inspired by the vibrant flavors of Mexico. This whitepaper details the design, features, and specifications of our disposable vapes.\n\n")
        md_file.write("## 2. Device Design\n\n")
        md_file.write("Sol Mexica vapes are designed for portability and ease of use. They are compact, lightweight, and come in a stylish, sleek design.\n\n")
        md_file.write("## 3. Features\n\n")
        for feature, description in features.items():
            md_file.write(f"- **{feature.replace('_', ' ').title()}**: {description}\n")
        md_file.write("\n## 4. Specifications\n\n")
        md_file.write("### Models\n\n")
        for model in specifications['models']:
            md_file.write(f"- **{model['model']}**\n")
            md_file.write(f"  - Battery capacity: {model['battery_capacity_mAh']}mAh\n")
            md_file.write(f"  - Puff count: {model['puff_count']} puffs\n")
            md_file.write(f"  - Nicotine levels: {', '.join(model['nicotine_levels_mg_per_mL'])} mg/mL\n")
            md_file.write(f"  - E-liquid capacity: {model['e_liquid_capacity_mL']} mL\n\n")
        md_file.write("### Flavor Profiles\n\n")
        for flavor in specifications['flavor_profiles']:
            md_file.write(f"- {flavor}\n")
        md_file.write("\n## 5. Quality Control\n\n")
        md_file.write("Sol Mexica is committed to providing high-quality products. Our e-liquids are manufactured under strict quality control procedures and use only the finest ingredients.\n\n")
        md_file.write("## 6. Conclusion\n\n")
        md_file.write("Sol Mexica disposable vapes offer a convenient and flavorful vaping experience, perfect for those seeking a taste of Mexico. With a variety of features and flavors to choose from, Sol Mexica caters to vapers of all preferences.\n")

def convert_md_to_pdf(input_filename, output_filename):
    with open(input_filename, 'r') as md_file:
        html_text = markdown2.markdown(md_file.read(), extras=["tables"])
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 12)
    pdf.write(5, html_text)
    pdf.output(output_filename)

def main():
    generate_markdown()
    convert_md_to_pdf('whitepaper.md', 'Sol_Mexica_Whitepaper.pdf')

if __name__ == "__main__":
    main()
