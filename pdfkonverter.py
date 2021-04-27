!apt install ghostscript imagemagick
!python3 -m pip install wand
!wget #тут ссылка на файл
!sed -i "s/rights=\"none\"/rights=\"read|write\"/g"  /etc/ImageMagick-6/policy.xml
fname = #название файла

from wand.image import Image
pdf=Image(filename=fname,
          resolution=300) #превращаем пдф в картинку, разрешение 300
pdfImage=pdf.convert('jpeg') #делаем джпег
i=1
for img in pdfImage.sequence: # для страницы в последовательности страниц, созданных нами ранее
    page = Image(image=img)
    page.save(filename=str(i)+'.jpg')
    i+=1
        #код написан под использование в коллабе, по идее сохраняет пдф в картинках (постранично)
