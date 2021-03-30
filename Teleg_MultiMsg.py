__author__ = 'kumbharp'
from fpdf import FPDF

infilename = "C:\\Study\\Automation\\messages.html"

phase = 1 # Found text start
phase = 0 # reset

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.set_right_margin(10)

baddedimage = False
mediafound = False

pasedlinenumber = 0

with open (infilename, encoding="utf-8") as myfile: # Open lorem.txt for reading text data.
     linenumber = 1
     for myline in myfile:                # For each line, stored as myline,
         pasedlinenumber += 1

         if (myline.find("<div class=\"text\">") != -1):
             phase = 1
             continue

         name = " Media "
         if (myline.find("href=\"photos/photo_") != -1):
            #pdf.image("C:\\Users\\kumbharp\\Documents\\Study\\Automation\\photo1.jpg", None, None, 200)
            name += "Image : "
            baddedimage = True
            name += myline[myline.find("href=") + 6:len(myline) - 3]
            pdf.set_font("Arial", size=15)
            pdf.multi_cell(195, 10, txt=name, border=0, align="L")
            pdf.set_font("Arial", size=12)
            #linenumber = linenumber + 1
            continue
         if (myline.find("href=\"voice_messages/audio_") != -1):
            name += "Audio : "
            name += myline[myline.find("href=") + 6:len(myline) - 3]
            pdf.set_font("Arial", size=15)
            pdf.multi_cell(195, 10, txt=name, border=0, align="L")
            pdf.set_font("Arial", size=12)
            #linenumber = linenumber + 1
            continue
         if (myline.find("href=\"files/") != -1):
             name += "other media "
             name += myline[myline.find("href=") + 6:len(myline) - 3]
             pdf.multi_cell(195, 10, txt=name, border=0, align="L")
             #linenumber = linenumber + 1
             continue

         if (phase == 1):
             if (myline.find("</div>") != -1):
                 phase = 0
                 continue
             if (phase == 1):
                 myline = myline.replace("<strong>", "")
                 myline = myline.replace("</strong>", "")
                 myline = myline.replace("<br><br>", "\n")
                 myline = myline.replace("<br>", "\n")
                 myline = myline.replace("<em>", "")
                 myline = myline.replace("</em>", "")
                 start = 0
                 end = len(myline)
                 if (myline.find("<a href=")!= -1):
                     start = myline.find(">")
                     end = myline.find("</a>")
                     myline = myline[start+1:end]

                 linelen = len (myline)

                 for element in range(0, linelen):
                    charascc = myline[element]

                    if (ord(charascc) > 256):
                        myline = myline.replace(charascc," ")

                 myline = myline.replace("&apos;","\'")
                 pdf.multi_cell(195, 10, txt=myline, border=0, align="L")
pdf.output("C:\\Documents\\Testpdf.pdf")
myfile.close()
