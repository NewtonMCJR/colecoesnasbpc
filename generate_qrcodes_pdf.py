import os
import qrcode
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm

workspace_dir = r"c:\Users\museu\Documents\SBPC\Displays"
pdf_path = os.path.join(workspace_dir, "qrcodes_displays.pdf")
temp_dir = os.path.join(workspace_dir, "assets", "temp_qrcodes")
os.makedirs(temp_dir, exist_ok=True)

# List of collections and names (including new CFAM)
collections = [
    {"acronym": "CBPM", "name": "Graziela Maciel Barroso"},
    {"acronym": "CCER", "name": "Maria Luiza Felippe Bauer"},
    {"acronym": "CCFF", "name": "Pedrina Cunha de Oliveira"},
    {"acronym": "CCULI", "name": "Dras. Teresa & Monique"},
    {"acronym": "CEIOC", "name": "Danielle Cerri do Nascimento"},
    {"acronym": "CFAM", "name": "Dra. Maria Inês de Moura Sarquis"},
    {"acronym": "CFAS", "name": "Marília Martins Nishikawa"},
    {"acronym": "CLEP", "name": "Martha Maria Pereira"},
    {"acronym": "CLIOC", "name": "Selma Quintella Soares"},
    {"acronym": "CMIOC", "name": "Silvana Carvalho Thiengo"},
    {"acronym": "CPFERA", "name": "Niède Guidon"},
    {"acronym": "CYP_CBAS_CBP", "name": "Alzira Maria Paiva de Almeida"},
    {"acronym": "MP", "name": "Itália Kerr"}
]

base_url = "https://colecoesbiologicasfiocruz.netlify.app"

print("Generating QR codes...")

# 1. Generate QR codes as PNGs
for col in collections:
    acronym = col["acronym"]
    url = f"{base_url}/{acronym.lower()}/"
    print(f"  URL for {acronym}: {url}")
    
    # Create QR code with minimal border to maximize QR size
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=1
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img_path = os.path.join(temp_dir, f"{acronym.lower()}_qr.png")
    img.save(img_path)
    col["qr_img"] = img_path

# 2. Draw PDF
print("Drawing PDF...")
c = canvas.Canvas(pdf_path, pagesize=A4)
width, height = A4 # 210 * mm, 297 * mm

# Draw title on the page (shifted up slightly to fit 5 rows)
c.setFont("Helvetica-Bold", 14)
c.drawCentredString(width / 2.0, 284 * mm, "QR Codes para os Displays - SBPC 2026")
c.setFont("Helvetica", 9)
c.drawCentredString(width / 2.0, 277 * mm, "Instruções: Recorte na linha tracejada para obter QR codes de exatamente 30 x 30 mm.")

# Grid setup (3 columns, 5 rows to fit 13 items)
x_start = 30 * mm
y_start = 224 * mm
x_spacing = 60 * mm
y_spacing = 46 * mm

for idx, col in enumerate(collections):
    col_idx = idx % 3
    row_idx = idx // 3
    
    x = x_start + col_idx * x_spacing
    y = y_start - row_idx * y_spacing
    
    display_acr = col["acronym"].replace("_", "/")
    
    # 2.1 Draw label (above the QR code cutting box)
    c.setFont("Helvetica-Bold", 9)
    c.drawCentredString(x + 15*mm, y + 36*mm, f"{display_acr}")
    c.setFont("Helvetica", 7)
    c.drawCentredString(x + 15*mm, y + 32*mm, f"{col['name']}")
    
    # 2.2 Draw dashed cutting border (exactly 30 mm by 30 mm)
    c.setStrokeColorRGB(0.7, 0.7, 0.7) # light gray
    c.setLineWidth(0.5)
    c.setDash(2, 2) # dotted/dashed line
    c.rect(x, y, 30*mm, 30*mm, stroke=1, fill=0)
    
    # 2.3 Draw QR code (centered in the box, 28 mm by 28 mm)
    c.setDash(1, 0) # reset to solid line for image drawing
    c.drawImage(col["qr_img"], x + 1*mm, y + 1*mm, width=28*mm, height=28*mm)
    
    # 2.4 Draw tiny helper labels inside or below
    c.setFont("Helvetica", 5)
    c.setFillColorRGB(0.5, 0.5, 0.5)
    c.drawCentredString(x + 15*mm, y - 4*mm, f"Display {display_acr}")
    c.setFillColorRGB(0, 0, 0) # reset fill color

c.showPage()
c.save()

# 3. Clean up temp images
print("Cleaning up temporary images...")
for col in collections:
    if os.path.exists(col["qr_img"]):
        os.remove(col["qr_img"])
if os.path.exists(temp_dir):
    os.rmdir(temp_dir)

print(f"Done! PDF saved to: {pdf_path}")
