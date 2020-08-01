# A.S.I.A

It is a webscraper which collects all the emails of all the companies posting internship opportunities on Internshala and then it sends an email to apply for the internship position along with your resume attached. 

## Prerequisites

Some modules are required, which can be installed by running the following command in the Terminal :-

`$ pip install -r requirements.txt`

## Instructions

- Make changes in `WebsiteScraper.py` 
     
    - Initialize the variables ```category``` and ```location``` according to ur preferance. Check my default initialization for example

- Make changes in `FinalEmailSender.py`

    - U need to initialize ```fromaddr``` with your email address (the one from which email will be sent) and the password of that account needs to be added in the ```run``` function of the class `EmailThread`
    - Similarly initialize the ```Subject``` and the ```body``` according to the internship profile you want to apply
    - Initialize the variable ```filename``` with whatever file you want to attach to the email along with its extension eg. LOR.pdf .Also, provide the path of that file in your local desktop in ```attachment```
       

## Running the code

Open the Terminal in the `A.S.I.A` folder and run the following command :-

1. `$ python WebsiteScraper.py` - Which will first fetch the websites of the companies offering the internships.
2. `$ python EmailScraper.py` - Which will fetch the email ids of all these companies offering the internship.
3. `$ python FinalEmailSender.py` - Which will finally send the email to all these Companies.

