#Day 27 & 28

import requests
from twilio.rest import TwilioRestClient

account_sid = 'ACe96e664d910ae38b8cd106083f24cdfd' #account_sid
auth_token = '746bf9cfb19d88592d5a8b46b1f806f2' #auth_token
client = TwilioRestClient(account_sid, auth_token)

number_to_text = '+19494413233' #+1-(949)-441-3233
twilio_number = '+17472332016' #+1-(747)-233-2016
message_body = 'Another new one!!'
media_url = 'http://img2.10bestmedia.com/Images/Photos/96123/captiva-beach-captiva_54_990x660_201404211817.jpg'

"""
Create / Send  --- POST METHOD
"""

message = client.messages.create(
    to = number_to_text,
    from_ = twilio_number,
    body = message_body,
    media_url = media_url,
)

print(message.sid)
print(message.media_list.list())


message_data = client.messages.get(sid='MM84e7ab9fd6af47a6a7e4012703ba317c')

print(message_data)
print(dir(message_data))

image_list = [i.uri for i in message_data.media_list.list()]
print(image_list)


"""
the_new_list = []
for x in some_list:
    the_new_list.append(x.uri)


OPTIONAL
status_callback = "http://www.yourwebsite.com/some/way/to/handle/"

message = client.messages.create(
    to=number_to_text,
    from_=twilio_number,
    body=message_body,
    media_url=media_url,
    status_callback=status_callback,
)
"""





def xml_pretty(xml_string):
    import xml.dom.minidom
    xml = xml.dom.minidom.parseString(xml_string)
    pretty_xml_ = xml.toprettyxml()
    print(pretty_xml_)





