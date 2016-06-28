from argparse import ArgumentParser

from data_manager import read_data


parser = ArgumentParser(prog="hungry")
parser.add_argument("type", type=str, choices=['view', 'message'])
#parser.add_argument("did_send", type=str, choices=['true', 'false'])
parser.add_argument('-id', '--user_id', type=int)
parser.add_argument('-e', '--email', type=str)

args = parser.parse_args()




if args.type == "view":
    print(read_data(user_id=args.user_id))
    print(read_data(email=args.email))
elif args.type == "message":
    print("send message")