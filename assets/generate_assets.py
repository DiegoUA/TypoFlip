import pymupdf as fitz  # PyMuPDF import
import os
from PIL import Image, ImageDraw

def render_svg_to_png(svg_path, png_path, dpi=150):
    if not os.path.exists(svg_path):
        print(f"✗ File not found: {svg_path}")
        return

    doc = fitz.open(svg_path)
    page = doc[0]
    
    pix = page.get_pixmap(dpi=dpi)
    pix.save(png_path)
    print(f"✓ Generated: {png_path} ({pix.width}x{pix.height} px)")

def create_presplash_png(logo_png_path, presplash_png_path):
    if not os.path.exists(logo_png_path):
        print(f"✗ Logo not found: {logo_png_path}")
        return
    
    logo = Image.open(logo_png_path).convert("RGBA")
    logo = logo.resize((256, 256), Image.Resampling.LANCZOS)

    mask = Image.new("L", (256, 256), 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0, 256, 256), radius=56, fill=255)

    logo_rounded = Image.new("RGBA", (256, 256), (0, 0, 0, 0))
    logo_rounded.paste(logo, (0, 0), mask)

    canvas = Image.new("RGBA", (512, 512), (0, 0, 0, 0))
    canvas.paste(logo_rounded, (128, 128), logo_rounded)
    canvas.save(presplash_png_path)
    print(f"✓ Generated: {presplash_png_path} (512x512 canvas with 256x256 rounded logo)")

def create_adaptive_foreground(svg_path, png_path, dpi=150):
    if not os.path.exists(svg_path):
        print(f"✗ File not found: {svg_path}")
        return

    doc = fitz.open(svg_path)
    page = doc[0]
    
    pix = page.get_pixmap(dpi=dpi, alpha=True)
    pix.save(png_path)
    print(f"✓ Generated: {png_path} ({pix.width}x{pix.height} px)")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    render_svg_to_png(os.path.join(base_dir, "logo.svg"), os.path.join(base_dir, "logo.png"))
    render_svg_to_png(os.path.join(base_dir, "feature_graphic.svg"), os.path.join(base_dir, "feature_graphic.png"))
    render_svg_to_png(os.path.join(base_dir, "clipboard.svg"), os.path.join(base_dir, "clipboard.png"))

    create_presplash_png(os.path.join(base_dir, "logo.png"), os.path.join(base_dir, "presplash.png"))
    create_adaptive_foreground(os.path.join(base_dir, "logo.svg"), os.path.join(base_dir, "icon_foreground.png"))
