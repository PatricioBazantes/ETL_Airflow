import smtplib
#from MongodbHelper import get_document

def send():
    try:
        x=smtplib.SMTP('smtp.gmail.com',587)
        x.starttls()
        #conig_data=get_document("MentalHealthCollection",{"Indicator":"Toma medicamento las ultimas dos semanas"})
        #print(conig_data)
        x.login("patriciobazantes@gmail.com","jmlfuhvvxwjzrher")
        subject="Testing"
        body_text="Testing succes"
        message="subject: {}\n\n{}".format(subject, body_text)
        x.sendmail("patriciobazantes@gmail.com","jpbazantes@espe.edu.ec",message)
        print("Success")
    except Exception as exception:
        print(exception)
        print("Failure")

if __name__ == "__main__":
    send()