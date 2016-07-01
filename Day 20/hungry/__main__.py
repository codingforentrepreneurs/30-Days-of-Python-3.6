from argparse import ArgumentParser

from data_class import UserManager
from utils.templates import get_template, render_context

parser = ArgumentParser(prog="hungry")
parser.add_argument("type", type=str, choices=['view', 'message'])
#parser.add_argument("did_send", type=str, choices=['true', 'false'])
parser.add_argument('-id', '--user_id', type=int)
parser.add_argument('-e', '--email', type=str)

args = parser.parse_args()


if args.type == "view":
    print(UserManager().get_user_data(user_id=args.user_id, email=args.email))
elif args.type == "message":
    print(UserManager().message_user(user_id=args.user_id, email=args.email))