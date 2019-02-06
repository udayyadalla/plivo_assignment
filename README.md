# plivo_assignment

To Run the file : python name of the file .py (eg: python MyOperations.py)

Explantion:

First I have create the Project folder.

In that I have created the testpin folder: a. config->varibales.py(Change the chromedriver path) b. Map -> Map.py c. lib->MyOperations.py(Main File)

In the MyOperations.py(Main File) first imported the config and Map files

In the MyOperations.py(Main File)

i. Created the class name as "MyOperations". ii. In the intialization part, I have used chromedriver to control the chrome browser.

 a. First i have open the chrome browser.
 b. I have get the google url and then I have opened the quickfuseapps page

iii. Created the clickonapp(Defination) to perform all the below operations

 a. Clicking on Create an App button
 b. clicking on  click “Lets’ get started
 c. Create a new page and giving the page name 

iv. created the clickonmessaging(Defination) to perform all the below operations

 a. Click on “Messaging” group appearing on the left pane under MODULES
 b. Drag component “Send an SMS” to the main app page & join the line from start acting as connector
 c. Fill the details of Phone Number and Message text

v. created the draganddropsendmail(Defination) to perform all the below operations

 a. Drag component “Send an email” from the left module and join line from “Not sent” output port.
 b. fill all the details of the mail

vi. created the draganddropExit(Defination for SMS) to perform all the below operations

 a. Click on component “Basic” on left Module and drag “Exit App” joining to “Sent” output port of Sent an sms  box

vii. created the draganddropExitforemail(Defination for email for sent port) to perform all the below operations

 a. Similarly, Join all the open output ports of “Send an Email” to Exit app by dragging

Viii.created the draganddropExitfornotsentemail(Defination for email for not sent port) to perform all the below operations

 a. Similarly, Join all the open output ports of “Send an Email” to Exit app by dragging

viii. Created the shut_down(Defination) to close the open browser 

In the MyOperations.py(Main File) , i have created the object to that class and I have called all the definations to perfom the scenario in the main file
