import csv

class CSVAnalysis:
    sucess_text = "Passed"
    failed_text = "Failed"
    skipped_text = "Skipped"
    Cancelled_text = "Cancelled"
   

    extractSuccess = True

    def __init__(self):
        pass
       

    ##METHODS###

    #Extract the results from the file. 
    def extractResults(self, filename):
        #Counts Number Of Failed Test
        failedTests = 0
        #Init List to Store Failed. 
        ListOfFailed = []
        ListOfSkipped = []
        ListOfCancelled = []
        
        num_of_rows =0

        try: 
            #Extract the data from the file.
            with open(filename, 'rb') as f:
                #Read the data as csv 
                reader = csv.reader(f)
                #For each row in the data
                for row in reader:
                    num_of_rows += 1
                    #Check if the row has failed
                    if(row[2] == self.failed_text):
                        #Append to the failed List. 
                        ListOfFailed.append(row)
                    elif(row[2] == self.skipped_text):
                        ListOfSkipped.append(row)
                    elif(row[2] == self.Cancelled_text):
                        ListOfCancelled.append(row)
        except IOError:
            print "Something went wrong, Please check if the file is in the correct location."
            self.extractSuccess = False

                    
        #Return a list of the failed number and list of failed 
        return [len(ListOfFailed), ListOfFailed, num_of_rows, ListOfSkipped, ListOfCancelled]
    
    #Displays the Results
    def displayResults(self, FailedDetails):

        #If no faults were found then print no fails. 
        if FailedDetails[0]==0:
            print "No Fails!"
        else:
            #Print number of Passed & failed tests
            print str(FailedDetails[2] - FailedDetails[0]) + " Passed Tests "
            print str(FailedDetails[0]) + " Failed Tests"
            #Calculate success rate and print. 
            successRate = 100-((FailedDetails[0]*100 / FailedDetails[2]*100)/100)
            print str(successRate) + "% Success Rate"
            
            print "*************"
            
            print "Test Cases You Must Re-Check: "
            print " "
            #Print the failed Details for each required row. 
            for failed in FailedDetails[1]:
                print "Test Case: " + failed[1]
                print "Comment: " + failed[3]
                print "Duration: " + failed[4]
                print "*************"
        

    #Return the extraction success indicao
    def getExtractSuccess(self):
        return self.extractSuccess


    
