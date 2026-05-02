import os
import glob

portfolio_dir = r"e:\stitch_mechatronics_portfolio_hero\portfolio"
html_files = glob.glob(os.path.join(portfolio_dir, "*.html"))

old_text = "assets/Document/Resume/Thirisha's_resume.pdf"
new_text = "assets/Document/Resume/resume.pdf"

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_text in content:
        content = content.replace(old_text, new_text)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {os.path.basename(file)}")

print("Done.")
