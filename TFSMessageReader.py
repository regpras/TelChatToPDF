__author__ = 'kumbharp'
from fpdf import FPDF

infilename = "C:\\Users\\kumbharp\\Documents\\Study\\Automation\\messages.html"
outfilename = "C:\\Users\\kumbharp\\Documents\\Study\\Automation\\messages.txt"

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
                 newpos = 0
                 processingline = linelen

                 for element in range(0, linelen):
                    charascc = myline[element]
                    if (ord(charascc) > 256):
                        myline = myline.replace(charascc," ")

                 if (linelen > 100):
                     while(processingline > 100):
                         newlinepos = myline.find("\n", startpos, linelen)
                         x = 1
                         if ((newlinepos - startpos) > 100):
                             while ((newlinepos - startpos) > 100):
                                loopinded = 0
                                newpos += 100
                                if newpos >= linelen:
                                    newpos = linelen - 1
                                pos = 0
                                while (newpos > startpos):
                                    if (newpos >= linelen):
                                        print("out of range")
                                    if(myline[newpos] != " "):
                                        newpos -= 1
                                    else:
                                        pos = newpos
                                        curline = myline[startpos:newpos]
                                        curlinelen = len(curline)
                                        pdf.cell(0, 10, txt=curline, ln=linenumber, align="L")
                                        outfile.write("%s\n" % (curline))
                                        linenumber = linenumber +1
                                        startpos = newpos
                                        processingline -= curlinelen
                                        x += 1
                                        break
                             if ((newlinepos- startpos) > 0):
                                 curline = myline[startpos:linelen]
                                 curlinelen = len((myline[startpos:linelen]))
                                 pdf.cell(0, 10, txt=curline, ln=linenumber, align="L")
                                 outfile.write("%s\n" % (curline))
                                 processingline -= curlinelen
                                 linenumber = linenumber +1
                         else:
                            curline = myline[startpos:newlinepos]
                            curlinelen = len(myline[startpos:newlinepos])
                            pdf.cell(0, 10, txt=curline, ln=linenumber, align="L")
                            outfile.write("%s\n" % (curline))
                            linenumber = linenumber + 1
                            startpos = newlinepos + 1
                            processingline -= curlinelen
                            newpos += curlinelen
                            #newlinepos -= curlinelen
                 else:
                     curlinelen = len(myline)
                     pdf.cell(0, 10, txt=myline, ln=linenumber, align="L")
                     outfile.write("%s\n" % (myline))
                     linenumber = linenumber +1
                     processingline -= curlinelen
                 #outfile.write("%s" % (myline))
                 '''
                 skipline = False
                 for element in range(0, len(myline)):
                    charascc = myline[element]
                    if (ord(charascc) > 256):
                        skipline = True
                        break
                 if (skipline == False):
                    pdf.cell(0, 10, txt=myline, ln=linenumber, align="L")
                    linenumber = linenumber +1
                    skipline = False
                '''
                 continue

pdf.output("C:\\Users\\kumbharp\\Documents\\Study\\Automation\\messages.pdf")
myfile.close()
outfile.close()
