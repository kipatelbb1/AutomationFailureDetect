import sys
import os

sys.path.append("pyscripts")
from CSVAnalysis import CSVAnalysis
from browserDisplay import generateBrowser

#Initialise the CSV Extractor. 
cv = CSVAnalysis()
gen = generateBrowser()

print "Generating.."

#Extract the results from the file and store them into the failed details list
FailedDetails = cv.extractResults("Results/automationResults2.csv")
if cv.getExtractSuccess()==True:
    #Display the results in the corrent format.
    #cv.displayResults(FailedDetails) (For Console)
    
    #Generate the head, body and footer of the HTML file. 
    head = gen.headerHTML()
    #Pass the failed rows to be rendered onto web page. 
    body = gen.bodyHTML(FailedDetails[1], FailedDetails[0], FailedDetails[2], FailedDetails[3], FailedDetails[4] )
    footer = gen.footerHTML()

    #Concat Strings 
    fullHTML = head + body + footer

    #Define File name 
    fileName = 'DetectFaults'
    #Save .HTML file to local directory. 
    gen.saveHTML(fileName, fullHTML)
    #Open the Browser. 
    gen.openBrowser(fileName) 
else:
    print "Something went wrong, Please check if the file is in the correct location."



#Pause(For Console)
#raw_input("Press <Enter to Exit>")

