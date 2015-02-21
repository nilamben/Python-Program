
# program will read file SALES.TXT and calculate total from input file and save output in TOTALS.TXT


def main():
    infileName = "SALES.TXT"
    outputName ="TOTALS.TXT"
    gtotal =0
    #open the file
    infile = open(infileName, 'r')
    outfile = open(outputName, 'w')

    
    print("Name                Total", file = outfile)
    #read each line
    for line in infile:
        name,t1,t2,t3,t4 = line.split()
        total = int(t1)+int(t2)+int(t3)+int(t4)
        gtotal =  gtotal +total
        
        print("{0:>18}{1:>12}".format(name,total),file= outfile )
        
        #fout.write(string(total)#)
    print (" {0:13}".format("Grand Total:") ,"{0:>15}".format(gtotal) , file = outfile)
    infile.close()
    outfile.close()
    
    

main()
    
