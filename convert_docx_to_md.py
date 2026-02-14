import os
from docx import Document
from markdownify import markdownify as md

SOURCE_DIR = r".\docs\canonical"
OUTPUT_DIR = r".\docs\canonical_md"

os.makedirs(OUTPUT_DIR, exist_ok=True)

for filename in os.listdir(SOURCE_DIR):
    if filename.lower().endswith(".docx"):
        path = os.path.join(SOURCE_DIR, filename)
        doc = Document(path)

        # Extract text with paragraph breaks preserved
        text = "\n\n".join([p.text for p in doc.paragraphs])

        # Convert plain text to markdown (light conversion)
        markdown_text = md(text)

        new_filename = filename.replace(".docx", ".md")
        output_path = os.path.join(OUTPUT_DIR, new_filename)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(markdown_text)

        print(f"Converted: {filename}")

print("Conversion complete.")
