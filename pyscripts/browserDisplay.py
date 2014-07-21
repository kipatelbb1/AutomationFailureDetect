import webbrowser

class generateBrowser:

    def __init__(self):
        pass


    def headerHTML(self):
        head = '<!DOCTYPE html><html lang="en"><head><title>Fault Detection</title><link rel="stylesheet" href="style/style.css" /></head>'
        
        body = '<body>'
        body += '<h1> Failed Automation Test Cases</h1>'

    
        return head + body

    def bodyHTML(self, FailedDetails, LengthOfListOfFailed, num_of_rows, SkippedDetails, CancelledDetails):

        body = ''
        body += "<div class='perc'>0% Checked</div>"
        body += '<table>'
        tableHeaders = '<th>Test Case</th><th>Comment</th><th>Duration</th><th>Checked By Tester</th>'
        body += tableHeaders
        
        #body = ''
        body += str(num_of_rows - LengthOfListOfFailed) + " Passed Tests<br/>"
        body += str(LengthOfListOfFailed) + " Failed Tests <br/>"
        successRate = 100-((LengthOfListOfFailed*100 / num_of_rows*100)/100)
        body += str(successRate) + "% Success Rate<br/>"

    
        #Calculate success rate and print. 

        for fail in FailedDetails:
            body += '<tr>'
            
            body += '<td>'
            body += fail[1]
            body += '</td>'

            body += '<td>'
            body += fail[3]
            body += '</td>'

            body += '<td>'
            body += fail[4]
            body += '</td>'

            body += '<td class="check">'
            body += '<input type="checkbox" class="checker" name="com" value="completed">Completed?'
            body += '</td>'
            

            body += '</tr>'

        body += '</table>'

        body += '</table><h1> Skipped Automation Test Cases</h1>'
        body += '<table>'
        body += tableHeaders
        for fail in SkippedDetails:
            body += '<tr>'
            
            body += '<td>'
            body += fail[1]
            body += '</td>'

            body += '<td>'
            body += fail[3]
            body += '</td>'

            body += '<td>'
            body += fail[4]
            body += '</td>'

            body += '<td class="check">'
            body += '<input type="checkbox" class="checker" name="com" value="completed">Completed?'
            body += '</td>'

            body += '</tr>'

       
        body += '</table><h1> Cancelled Automation Test Cases</h1>'
        body += '<table>'
        body += tableHeaders
        for fail in CancelledDetails:
            body += '<tr>'
            
            body += '<td>'
            body += fail[1]
            body += '</td>'

            body += '<td>'
            body += fail[3]
            body += '</td>'

            body += '<td>'
            body += fail[4]
            body += '</td>'

            body += '<td class="check">'
            body += '<input type="checkbox" class="checker" name="com" value="completed">Completed?'
            body += '</td>'

            body += '</tr>'

       


        return body

    def footerHTML(self):
        scripts = '<script type="text/javascript" src="script/jquery.js"></script><script type="text/javascript" src="script/percentChecker.js"></script>'
        return '</table>' + scripts + '</body></html>'

    def saveHTML(self, fileToSave , data):
        fileToSave = fileToSave + '.html'
        fileLoc = open(fileToSave,'w')
        fileLoc.write(data)
        fileLoc.close() 

    def openBrowser(self,toOpen):
        new = 2 # open in a new tab, if possible
        webbrowser.open(toOpen + '.html',new=new)
        
        
        
        
