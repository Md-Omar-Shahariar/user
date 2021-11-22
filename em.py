import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import pymongo
import ssl


myclient = pymongo.MongoClient("mongodb+srv://afridi:afridi0153@cluster0.ekt0p.mongodb.net/test",ssl_cert_reqs=ssl.CERT_NONE)
mydb = myclient["Bank_App"]

mycol = mydb["user"]
day = str(datetime.now()).split(" ")[0]
myquery = { "entry_date": day}

mydoc = mycol.find(myquery)







def send_email(hour, min):
    # if hour == '11' and min == '55':
        sender_email = ""
        receiver_email = ""
        password = ''

        message = MIMEMultipart("alternative")
        message["Subject"] = "Checking email"
        message["From"] = sender_email
        message["To"] = receiver_email

        # Create the plain-text and HTML version of your message
        text = """\
        Hi,
        How are you?
        Real Python has many great tutorials:
        www.realpython.com"""
        for x in mydoc:


            html = f"""\
            <html>
              <body>
                <p><br>
                   {x}
                </p>
              </body>
            </html>
            """

        # Turn these into plain/html MIMEText objects

        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first

        message.attach(part2)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )


    if __name__ == "__main__":

        hour = str(datetime.now()).split(" ")[1].split(".")[0].split(":")[0]
        minutes = str(datetime.now()).split(" ")[1].split(".")[0].split(":")[1]

        while True:
             send_email(hour, minutes)
