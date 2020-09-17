import fitz

doc = fitz.open("documents/KCI_FI001975757.pdf")

for x in range(len(doc)):
    for img in doc.getPageImageList(x):
        xref = img[0]
        pix = fitz.Pixmap(doc, xref)
        if pix.n < 5:
            pix.writePNG("p%s-%s.png" % (x, xref))
        else:
            pix1 = fitz.Pixmap(fitz.csRGB, pix)
            pix1.writePNG("p%s-%s.png" % (x, xref))
            pix1 = None
        pix = None