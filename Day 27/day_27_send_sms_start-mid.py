#Day 27 & 28

import requests

username = ''
password = ''

number_to_text = '+19494413233' #+1-(949)-441-3233
twilio_number = '+17472332016' #+1-(747)-233-2016

message_body = 'Hi there, this is my message!'

def xml_pretty(xml_string):
    import xml.dom.minidom
    xml = xml.dom.minidom.parseString(xml_string)
    pretty_xml_ = xml.toprettyxml()
    print(pretty_xml_)


base_url = 'https://api.twilio.com/2010-04-01/Accounts'

auth = (username, password)