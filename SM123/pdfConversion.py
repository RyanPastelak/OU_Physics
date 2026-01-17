import pdfplumber
import os
import logging

# Suppress pdfminer warnings about non-standard color values
logging.getLogger("pdfminer").setLevel(logging.ERROR)

def convert_pdfs_to_txt(root_folder):
    """
    Traverses a folder and subfolders, converting all PDFs found into .txt files.
    Skips files that have already been converted.
    """
    # Count for progress tracking
    converted_count = 0
    skipped_count = 0
    
    # Walk through the directory tree
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file.lower().endswith(".pdf"):
                pdf_path = os.path.join(root, file)
                txt_path = os.path.join(root, os.path.splitext(file)[0] + ".txt")
                
                # Skip if already converted
                if os.path.exists(txt_path):
                    print(f"Skipping (already converted): {file}")
                    skipped_count += 1
                    continue
                
                print(f"Processing: {file}...")
                
                try:
                    with pdfplumber.open(pdf_path) as pdf:
                        full_text = []
                        for page in pdf.pages:
                            # .extract_text() is highly accurate for layout preservation
                            text = page.extract_text()
                            if text:
                                full_text.append(text)
                        
                        # Save the extracted text to a file
                        with open(txt_path, 'w', encoding='utf-8') as f:
                            f.write("\n".join(full_text))
                    
                    converted_count += 1
                except Exception as e:
                    print(f"Error converting {file}: {e}")

    print(f"\nFinished! Converted {converted_count} PDFs, skipped {skipped_count} (already converted).")

if __name__ == "__main__":
    # Use the current working directory
    target_folder = os.getcwd()
    print(f"Scanning directory: {target_folder}\n")
    convert_pdfs_to_txt(target_folder)