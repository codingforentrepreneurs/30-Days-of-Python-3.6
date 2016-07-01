import csv
import datetime
import shutil
import os
from tempfile import NamedTemporaryFile

from utils.templates import get_template, render_context
#file_item_path = os.path.join(os.getcwd(), "data.csv")
file_item_path = os.path.join(os.path.dirname(__file__), "data.csv")



class UserManager():

    def message_user(self):
        file_ = 'templates/email_message.txt'
        file_html = 'templates/email_message.html'
        template = get_template(file_)
        template_html = get_template(file_html)
        context = {
            "name": "Justin",
            "date": None,
            "total": None
        }
        print(render_context(template, context))
        print(render_context(template_html, context))
        return None

    def get_user_data(self, user_id=None, email=None):
        filename = file_item_path
        with open(filename, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            items = []
            unknown_user_id = None
            unknown_email = None
            for row in reader:
                if user_id is not None:
                    if int(user_id) == int(row.get("id")):
                        return row
                    else:
                        unknown_user_id = user_id
                if email is not None:
                    if email == row.get("email"):
                        return row
                    else:
                        unknown_email = email
            if unknown_user_id is not None:
                return "User id {user_id} not found".format(user_id=user_id)
            if unknown_email is not None:
                return "Email {email} not found".format(email=email)
        return None