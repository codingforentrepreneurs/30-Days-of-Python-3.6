import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

host = "smtp.gmail.com"
port = 587
username = "hungrypy@gmail.com"
password = "iamhungry2016day14"
from_email = username
to_list = ["hungrypy@gmail.com"]



class MessageUser():
    user_details = []
    messages = []
    email_messages = []
    base_message = """Hi {name}! 

Thank you for the purchase on {date}. 
We hope you are exicted about using it. Just as a
reminder the purcase total was ${total}.
Have a great one!

Team CFE
"""
    def add_user(self, name, amount, email=None):
        name = name[0].upper() + name[1:].lower() 
        amount = "%.2f" %(amount)
        detail = {
            "name": name,
            "amount": amount,
        } 
        today = datetime.date.today()
        date_text = '{today.month}/{today.day}/{today.year}'.format(today=today)
        detail['date'] = date_text
        if email is not None: # if email != None
            detail["email"] = email
        self.user_details.append(detail)
    def get_details(self):
        return self.user_details
    def make_messages(self):
        if len(self.user_details) > 0:
            for detail in self.get_details():
                name = detail["name"]
                amount = detail["amount"]
                date = detail["date"]
                message = self.base_message
                new_msg = message.format(
                    name=name,
                    date=date,
                    total=amount
                )
                user_email = detail.get("email")
                if user_email:
                    user_data = {
                        "email": user_email,
                        "message": new_msg
                    }
                    self.email_messages.append(user_data)
                else:
                    self.messages.append(new_msg)
            return self.messages
        return []
    def send_email(self):
        self.make_messages()
        if len(self.email_messages) > 0:
            for detail in self.email_messages:
                user_email = detail['email']
                user_message = detail['message']
                try:
                    email_conn = smtplib.SMTP(host, port)
                    email_conn.ehlo()
                    email_conn.starttls()
                    email_conn.login(username, password)
                    the_msg = MIMEMultipart("alternative")
                    the_msg['Subject'] = "Billing Update!"
                    the_msg["From"] = from_email
                    the_msg["To"]  = user_email
                    part_1 = MIMEText(user_message, 'plain')
                    the_msg.attach(part_1)
                    email_conn.sendmail(from_email, [user_email], the_msg.as_string())
                    email_conn.quit()
                except smtplib.SMTPException:
                    print("error sending message")
            return True
        return False


obj = MessageUser()
obj.add_user("Justin", 123.32, email='hungrypy@gmail.com')
obj.add_user("jOhn", 94.23, email='hungrypy@gmail.com')
obj.add_user("Sean", 93.23, email='hungrypy@gmail.com')
obj.add_user("Emilee", 193.23, email='hungrypy@gmail.com')
obj.add_user("Marie", 13.23, email='hungrypy@gmail.com')
obj.get_details()

obj.send_email()
