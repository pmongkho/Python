import re
import pdfplumber
import pandas as pd
from collections import namedtuple
import string

Line = namedtuple('Line','plan_number RCODE WeightsLB')

#regular expressions for
#plan number
plan_number_re = re.compile(r'^1\d{6}')
#RCODE
rcode_re = re.compile(r'([A-Z])+[^abc]([0-9]\/[0-9])|[A-Z]+[0-9]+|([A-Z])+')
#WeightsLB
weightsLB_re = re.compile(r'[0-9]+(\.\d{4})\sLB|(\.\d{4})\sLB')


#variable for total weight of all plans that have same RCODE
rcodeweight = {}
file = 'plan_weights.pdf'
lines = []
with pdfplumber.open(file) as pdf:
    pages = pdf.pages
    for page in pdf.pages:
        text = page.extract_text()
        for line in text.split('\n'): 
            print(line)
    #         #if plannumber is the same on new line
    #         #findRCODE and findLBS until you encounter a new
    #         weights = weightsLB_re.search(line)
    #         rcode = rcode_re.search(line)
    #         plan = plan_number_re.search(line)
    #        #initializes search for line criteria
    #         if plan and weights and rcode:
    #             #find plannumber
    #             foundplan = plan.group()
    #             #findRCODE
    #             foundrcode = rcode.group()
    #             #findLBS
    #             foundweight = weights.group()
    #             #dictionary with foundplan as key
    #             if foundplan not in rcodeweight:
    #                 rcodeweight[foundplan] =  {}
    #             update_item = {foundrcode:foundweight}
    #             rcodeweight[foundplan].update(update_item)
    #             # print (rcodeweight)
    #             # while testcase:
    #             #     rcodeweight[foundplan][foundrcode] = foundweight
    #             #     print (foundplan)
    #             #     print (foundweight)
    #             #     print (foundrcode+'\n')
    # print(rcodeweight)
         
        

               
  


                
            

           
                
               

                    


    



    # df = pd.DataFrame(lines)
    # df.head()
            #find plannumber
            #iterate until there is a new plan number 
            # and find Rcode with lbs
            # data will be [plan#, rpchnb - 4050 lb, rpclvrus - 3900 lb ... ]
