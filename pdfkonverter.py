import fitz #(нужно PyMuPDF установить предварительно)
pdffile = "evangelie1606.pdf"
doc = fitz.open(pdffile)
n=doc.page_count
i=0
while i<n:
    page = doc.load_page(i)
    zoom = 4  # zoom factor, можно менять в настройках, смотря какое качество нам нужно, 4 уже оч хорошее,но работает долго
    mat = fitz.Matrix(zoom, zoom)
    pix = page.getPixmap(matrix=mat)
    output = str(i+1)+'superhigh'+".png"
    print(output)
    pix.writeImage(output)
    i+=1
