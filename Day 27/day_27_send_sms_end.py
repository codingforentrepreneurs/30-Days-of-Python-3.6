#Day 27 & 28

import requests

username = 'ACe96e664d910ae38b8cd106083f24cdfd' #account_sid
account_sid = username
password = '67ef145171db841d137dd8f02baf1aae' #auth_token

number_to_text = '+19494413233' #+1-(949)-441-3233
twilio_number = '+17472332016' #+1-(747)-233-2016

message_body = ''

def xml_pretty(xml_string):
    import xml.dom.minidom
    xml = xml.dom.minidom.parseString(xml_string)
    pretty_xml_ = xml.toprettyxml()
    print(pretty_xml_)


base_url = 'https://api.twilio.com/2010-04-01/Accounts'
message_url = base_url + '/' + account_sid + '/Messages'
auth_cred = (username, password)

post_data = {
    "From": twilio_number,
    "To": number_to_text,
    "Body": message_body,
    "MediaUrl": "http://img2.10bestmedia.com/Images/Photos/96123/captiva-beach-captiva_54_990x660_201404211817.jpg" #img,
}

r = requests.post(message_url, data=post_data, auth=auth_cred)

print(r.status_code)
xml_pretty(r.text)


message_url_ind = message_url + "/MMa63006dc4c36470abb69132c0aea23ef"
get_r = requests.get(message_url_ind, auth=auth_cred)

xml_pretty(get_r.text)













