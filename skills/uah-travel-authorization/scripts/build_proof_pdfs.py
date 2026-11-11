"""Build captioned proof PDFs for a UAH Travel Authorization from a JSON spec.

Usage (in a scratch venv with reportlab + pypdf):
    python -I build_proof_pdfs.py spec.json

spec.json:
{
  "out_dir": "~/Downloads/TA_EVENT_Traveler_Name",
  "header": "Traveler: <Name> (<Dept>) | <Event>, <Venue>, <City> | Travel <dates>",
  "captured": "Captured Oct 8, 2026",
  "documents": [
    {"name": "5_Meals_GSA_Per_Diem_SF.pdf", "pages": [
      {"type": "text", "title": "Meals & Incidentals (M&IE) Estimate",
       "lines": ["GSA M&IE: $92/day", "**  Total M&IE estimate   $598.00"]},
      {"type": "image", "path": "/path/to/screenshot.jpg", "caption": "GSA FY2027 per diem, San Francisco"}
    ]},
    {"name": "1_Invitation_and_Role.pdf", "merge": ["~/Downloads/letter.pdf", "~/Downloads/confirmation.pdf"]}
  ]
}

Text lines starting with "**" are drawn bold. Each document is either "pages" (generated)
or "merge" (concatenate existing PDFs). Prints each output file and its size.
"""
import json
import os
import sys

from pypdf import PdfReader, PdfWriter
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas

PAGE = landscape(letter)


def text_page(c, page, header):
    w, h = PAGE
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, h - 55, page["title"])
    c.setFont("Helvetica", 10)
    c.drawString(50, h - 72, header)
    y = h - 100
    for ln in page.get("lines", []):
        bold = ln.startswith("**")
        c.setFont("Helvetica-Bold" if bold else "Helvetica", 11)
        c.drawString(60, y, ln.strip("*"))
        y -= 17
    c.showPage()


def image_page(c, page, captured):
    w, h = PAGE
    c.setFont("Helvetica-Bold", 11)
    c.drawString(36, h - 30, page["caption"])
    c.setFont("Helvetica", 8)
    c.drawString(36, h - 43, page.get("sub", captured))
    ir = ImageReader(os.path.expanduser(page["path"]))
    iw, ih = ir.getSize()
    s = min((w - 72) / iw, (h - 80) / ih)
    c.drawImage(ir, 36, h - 55 - ih * s, iw * s, ih * s)
    c.showPage()


def main(spec_path):
    spec = json.load(open(spec_path))
    out = os.path.expanduser(spec["out_dir"])
    os.makedirs(out, exist_ok=True)
    header = spec.get("header", "")
    captured = spec.get("captured", "")
    for doc in spec["documents"]:
        path = os.path.join(out, doc["name"])
        if "merge" in doc:
            wtr = PdfWriter()
            for f in doc["merge"]:
                wtr.append(os.path.expanduser(f))
            wtr.write(path)
        else:
            c = canvas.Canvas(path, pagesize=PAGE)
            for page in doc["pages"]:
                if page["type"] == "text":
                    text_page(c, page, header)
                else:
                    image_page(c, page, captured)
            c.save()
        n = len(PdfReader(path).pages)
        print(f"{doc['name']}  {os.path.getsize(path)} bytes  {n} pages")


if __name__ == "__main__":
    main(sys.argv[1])
