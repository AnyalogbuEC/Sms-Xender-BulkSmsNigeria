# This application was written by Anyalogbu, Ernest Chinualum on wednesday, April 20, 2022.
# Developer's contact: AnyalogbuEC or AnyalogbuEC on any platform, phone: +234(0)8149390948.
# It was written for the sole aim of sending sms using bulk sms Nigeria API.

# importing the requests library
import requests

# defining the api-endpoint
API_ENDPOINT = "https://www.bulksmsnigeria.com/api/v1/sms/create"

print("\n\n|||||||||||  ||\\\\      //||  |||||||||||            //\\\\        ||||||||||  ||||||||||")
print("||           || \\\\    // ||  ||		           //  \\\\       ||	||  ||      ||")
print("||           ||  \\\\  //  ||  ||		          //    \\\\      ||	||  ||	    ||")
print("|||||||||||  ||   \\\\//   ||  |||||||||||         //||||||\\\\     ||||||||||  ||||||||||")
print("         ||  ||          ||           ||        //        \\\\    ||          ||")
print("         ||  ||          ||           ||       //          \\\\   ||          ||")
print("|||||||||||  ||          ||  |||||||||||      //            \\\\  ||          ||")
print("~~~~~~~~~~~~~AnyalogbuEC~~~~~~~~~~~~~~~~     ~~~~~~~~~Bulk Sms Nigeria API~~~~~~~~~\n\n")

# API token
API_TOKEN = input("Enter API token from bulk sms Nigeria : ")

# setting sender's name
From = input("Enter Sender's name: ")

successful = []  # list of phone numbers of the successfully sent sms
unsuccessful = []  # list of phone numbers of the unsuccessfully sent sms


# the function responsible for sending the sms
def message_sender(message, to):
    # data to be sent to the api
    data = {
        'api_token': API_TOKEN,
        'from': From,
        'to': to,
        'body': message
    }

    # sending post request and saving response as response object
    r = requests.post(url=API_ENDPOINT, data=data)

    # extracting response text
    feedback = r.json()

    if feedback["data"]["message"] == "Message Sent":
        print("Message sent successfully.")
        successful.append(to)
    else:
        print(f"Message failed with error: {feedback}")
        unsuccessful.append(to)


# taking the file that contains the contacts details
contacts_details_file = input("Filename or Filepath for contact details:  ")

if not contacts_details_file.endswith(".csv"):
    print("File type must be .csv")
    quit()

contactsDetails = ""  # initializing contactsDetails

# trying to open the contacts_details_file file
try:
    contactsDetails = open(contacts_details_file, "r")
except:
    print("file not found")
    quit()

# taking the file that contains the message
message_file = input("Filename or Filepath for the message:  ")

if not message_file.endswith(".txt"):
    print("File type must be .txt")
    quit()

messageDetails = ""  # initializing messageDetails

# trying to open the message_file file
try:
    messageDetails = open(message_file, "r")
except:
    print("file not found")
    quit()

messageData = ""  # initializing messageData

for message_body in messageDetails:
    messageData = messageData + message_body

x = 0

for contactDetails in contactsDetails:

    if x > 0:
        wordList = contactDetails.split(',')
        first_name = wordList[0].strip()
        last_name = wordList[1].strip()
        phoneNumber = wordList[2].strip()
        Message = "Hi " + last_name + " " + first_name + ",  " + messageData
        print("Sending\n" + Message + "\nto " + phoneNumber)
        message_sender(Message, phoneNumber)

    x = x + 1

print("The successfully sent message(s) are:")
print(successful)
print("The unsuccessfully sent message(s) are:")
print(unsuccessful)
