__author__ = 'kumbharp'
from fpdf import FPDF

infilename = "C:\\Prasanna\\Trading\\TFS\\InnerCircle\\ChatExport_05_12_2019\\messages.html"
outfilename = "C:\\Prasanna\\Trading\\TFS\\InnerCircle\\ChatExport_05_12_2019\\messages.txt"

outfile = open(outfilename, "w", encoding="utf-8")
phase = 1 # Found text start
phase = 0 # reset

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.set_right_margin(10)

pasedlinenumber = 0

with open (infilename, encoding="utf-8") as myfile: # Open lorem.txt for reading text data.
     linenumber = 1
     for myline in myfile:                # For each line, stored as myline,
         pasedlinenumber += 1
         if (myline.find("<div class=\"text\">") != -1):
             phase = 1
             continue
         if (phase == 1):
             if (myline.find("</div>") != -1):
                 outfile.write("\n")
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
                 startpos = 0

                 totalnewlines = 0
                 newlineposlist = []
                 for element in range(0, linelen):
                    charascc = myline[element]
                    if charascc == '\n':
                        totalnewlines += 1
                        newlineposlist.append(element)
                    if (ord(charascc) > 256):
                        myline = myline.replace(charascc," ")

                 myline = myline.replace("&apos;","\'")
                 linelen = len (myline)

                 if (linelen > 100):
                    if totalnewlines > 0:
                        for newlinepos in newlineposlist:
                            #split the string
                            endpos = newlinepos
                            curline = myline[startpos:endpos]
                            curlinelen = len(curline)
                            commpletedlines = 0
                            if curlinelen > 100:
                                startpos1 = 0
                                endpos1 = commpletedlines + 100
                                if endpos1 > curlinelen:
                                    endpos1 = curlinelen
                                while (commpletedlines < (curlinelen)):
                                    '''
                                    curline2 = curline[startpos1:endpos1]
                                    curlinelen2 = len(curline2)
                                    pdf.cell(0, 10, txt=curline2, ln=linenumber, align="L")
                                    outfile.write("%s\n" % (curline2))
                                    linenumber = linenumber + 1
                                    commpletedlines += curlinelen2
                                    startpos1 = endpos1
                                    endpos1 = commpletedlines + 100
                                    if endpos1 > curlinelen:
                                        endpos1 = curlinelen
                                    '''
                                    curline2 = curline[startpos1:endpos1]
                                    curlinelen2 = len(curline2)

                                    if curlinelen2 >= 100:
                                        lastspacepos = curline.rfind(" ", startpos1,endpos1)
                                        endpos1 = lastspacepos
                                        curline2 = curline[startpos1:endpos1]
                                        curlinelen2 = len(curline2)

                                    pdf.cell(0, 10, txt=curline2, ln=linenumber, align="L")
                                    outfile.write("%s\n" % (curline2))
                                    linenumber = linenumber + 1
                                    commpletedlines += curlinelen2
                                    startpos1 = endpos1
                                    endpos1 = commpletedlines + 100
                                    if endpos1 > curlinelen:
                                        endpos1 = curlinelen
                            else:
                                pdf.cell(0, 10, txt=curline, ln=linenumber, align="L")
                                outfile.write("%s\n" % (curline))
                                linenumber = linenumber + 1
                            startpos = endpos + 1
                 else:
                    #length is less than 100 print string
                    pdf.cell(0, 10, txt=myline, ln=linenumber, align="L")
                    outfile.write("%s\n" % (myline))
                    linenumber = linenumber + 1
pdf.output("C:\\Prasanna\\Trading\\TFS\\InnerCircle\\ChatExport_05_12_2019\\messages.pdf")
myfile.close()
outfile.close()
