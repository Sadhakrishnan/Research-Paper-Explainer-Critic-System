import fitz  # PyMuPDF
import pdfplumber
import os
from typing import List, Dict, Any

class PDFParser:
    def __init__(self, file_path: str):
        self.file_path = file_path
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

    def extract_text_with_pymupdf(self) -> List[Dict[str, Any]]:
        """
        Extracts text page by page using PyMuPDF.
        Returns a list of dicts with text and page number.
        """
        pages = []
        doc = fitz.open(self.file_path)
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text = page.get_text("text")
            pages.append({
                "text": text,
                "page_number": page_num + 1,
                "metadata": {
                    "source": os.path.basename(self.file_path),
                    "page": page_num + 1
                }
            })
        doc.close()
        return pages

    def extract_tables_with_pdfplumber(self) -> List[Dict[str, Any]]:
        """
        Extracts tables from the PDF using pdfplumber.
        """
        tables = []
        with pdfplumber.open(self.file_path) as pdf:
            for i, page in enumerate(pdf.pages):
                extracted_tables = page.extract_tables()
                if extracted_tables:
                    tables.append({
                        "page_number": i + 1,
                        "tables": extracted_tables
                    })
        return tables

    def get_full_analysis(self) -> Dict[str, Any]:
        """
        Combines text and table extraction.
        """
        return {
            "pages": self.extract_text_with_pymupdf(),
            "tables": self.extract_tables_with_pdfplumber()
        }

if __name__ == "__main__":
    # Quick test if needed
    # parser = PDFParser("sample.pdf")
    # print(parser.get_full_analysis())
    pass
