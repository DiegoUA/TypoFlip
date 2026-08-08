import fitz  # PyMuPDF

def render_svg_to_png(svg_path, png_path):
    # Open the SVG file
    doc = fitz.open(svg_path)
    page = doc[0]
    
    # Render page to pixmap with crisp 150 DPI resolution
    pix = page.get_pixmap(dpi=150)
    pix.save(png_path)
    print(f"✓ Generated: {png_path} ({pix.width}x{pix.height} px)")

if __name__ == "__main__":
    render_svg_to_png("logo.svg", "logo.png")
    render_svg_to_png("feature_graphic.svg", "feature_graphic.png")