'''
Install: pip install python-twitter
Project Github: https://github.com/codingforentrepreneurs/30-Days-of-Python
Github: https://github.com/bear/python-twitter
Docs: https://python-twitter.readthedocs.io
'''


import twitter

consumer_key = 'G2vW5RTt5y8gPutlPvWgIc54d'
consumer_secret = 'CbsWYdcygM0q7zXzk9mWbE2OvMNQSKBJhikOt6Z8xAxm3c1NdC'
access_token = '787057602484051968-mdYWmpLaVZj8emlltHs0eIXVjRuzULQ'
access_secret = 'd7OgtcX2wgF7ttHcKqtDFDgZB9b8jYjDcnzb9awyQnY8T'



api = twitter.Api(consumer_key=consumer_key,
                consumer_secret=consumer_secret,
                access_token_key=access_token,
                access_token_secret=access_secret)


print(api.VerifyCredentials())


follwers = api.GetFollowers()
friends = api.GetFriends()

status_var = '@justinmitchel #Python is amazing! #30daysofpython http://joincfe.com/projects'
post_update = api.PostUpdates(status=status_var)

length_status = twitter.twitter_utils.calc_expected_status_length(status=status_var)

new_messsage = api.PostDirectMessage(screen_name='justinmitchel', text='Hi there')
print(new_messsage)

#
new_magic_message = api.PostDirectMessage(screen_name='MagicJohnson', text='Hey Magic! Big fan.')
print(new_magic_message)



api.GetUser(user)
api.GetReplies()
api.GetUserTimeline(user)
api.GetHomeTimeline()
api.GetStatus(status_id=787079994451202048) #status_id = 787079994451202048
api.DestroyStatus(status_id)
api.GetFriends(user)
api.GetFollowers()
api.GetFeatured()
api.GetDirectMessages()
api.GetSentDirectMessages()
api.PostDirectMessage(user, text)
api.DestroyDirectMessage(message_id)
api.DestroyFriendship(user)
api.CreateFriendship(user)
api.LookupFriendship(user)
api.VerifyCredentials()

