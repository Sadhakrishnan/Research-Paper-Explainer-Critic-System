import re
from typing import List, Dict, Any

class SectionDetector:
    def __init__(self):
        # Common research paper sections
        self.sections_patterns = {
            "Abstract": re.compile(r"^\s*Abstract\s*$", re.IGNORECASE | re.MULTILINE),
            "Introduction": re.compile(r"^\s*(?:1\.?\s*)?Introduction\s*$", re.IGNORECASE | re.MULTILINE),
            "Related Work": re.compile(r"^\s*(?:\d\.?\s*)?(?:Related Work|Literature Review)\s*$", re.IGNORECASE | re.MULTILINE),
            "Methodology": re.compile(r"^\s*(?:\d\.?\s*)?(?:Methodology|Proposed Method|Methods|Experimental Design)\s*$", re.IGNORECASE | re.MULTILINE),
            "Experiments": re.compile(r"^\s*(?:\d\.?\s*)?(?:Experiments|Evaluation|Experimental Results)\s*$", re.IGNORECASE | re.MULTILINE),
            "Results": re.compile(r"^\s*(?:\d\.?\s*)?(?:Results|Discussion and Results)\s*$", re.IGNORECASE | re.MULTILINE),
            "Discussion": re.compile(r"^\s*(?:\d\.?\s*)?Discussion\s*$", re.IGNORECASE | re.MULTILINE),
            "Conclusion": re.compile(r"^\s*(?:\d\.?\s*)?(?:Conclusion|Conclusions and Future Work)\s*$", re.IGNORECASE | re.MULTILINE),
            "References": re.compile(r"^\s*(?:\d\.?\s*)?(?:References|Bibliography)\s*$", re.IGNORECASE | re.MULTILINE),
        }

    def detect_sections(self, pages: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Processes pages and assigns section tags to chunks of text.
        """
        full_text = ""
        page_offsets = []
        current_offset = 0

        for page in pages:
            full_text += page["text"] + "\n"
            page_offsets.append({
                "start": current_offset,
                "end": current_offset + len(page["text"]) + 1,
                "page_number": page["page_number"]
            })
            current_offset += len(page["text"]) + 1

        detected_headers = []
        for section_name, pattern in self.sections_patterns.items():
            for match in pattern.finditer(full_text):
                detected_headers.append({
                    "section": section_name,
                    "start": match.start(),
                    "end": match.end(),
                    "header_text": match.group().strip()
                })

        # Sort headers by position
        detected_headers.sort(key=lambda x: x["start"])

        # Split text into sections
        sections = []
        for i in range(len(detected_headers)):
            start_pos = detected_headers[i]["start"]
            end_pos = detected_headers[i+1]["start"] if i + 1 < len(detected_headers) else len(full_text)
            
            section_content = full_text[start_pos:end_pos].strip()
            
            # Find which page this section starts on
            start_page = 1
            for offset in page_offsets:
                if offset["start"] <= start_pos < offset["end"]:
                    start_page = offset["page_number"]
                    break

            sections.append({
                "section_name": detected_headers[i]["section"],
                "content": section_content,
                "start_page": start_page
            })

        return sections

if __name__ == "__main__":
    # Example usage
    # detector = SectionDetector()
    # sections = detector.detect_sections(pages)
    pass
