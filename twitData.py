import tweepy
import json
import time

auth = tweepy.OAuthHandler("QcqaHeHWkRZibqsAMfIT89rTR", "Qnz5SRgXMF6WJvkQ6ClnY4Uq2ljhTcr6ibhnEtLTYawOsk1t5q")
auth.set_access_token("778770992852193280-fEK3GTR0jZMAmrT5JN5r7lvG4eOf6Nk", "ywn2FvqZ3Swh19ltqKS71pAqwKGudRvTV5r10Z43dmfxy")


#api key "QcqaHeHWkRZibqsAMfIT89rTR"
#api secret key "Qnz5SRgXMF6WJvkQ6ClnY4Uq2ljhTcr6ibhnEtLTYawOsk1t5q"

api = tweepy.API(auth)

#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print(tweet.text)

data = {}
data['users'] = []

user = api.get_user("Ryleeg99")
#print(user.followers_count)

#for friend in user.followers():
#	print(friend.screen_name)

followers = []

for page in tweepy.Cursor(api.followers, screen_name = "Ryleeg99", wait_on_rate_limit=True, count=200).pages():
	try:
		followers.extend(page)
	except tweepy.TweepError as e:
		print("Going to sleep:", e)
		time.sleep(60)

for page in tweepy.Cursor(api.friends, screen_name = "Ryleeg99", wait_on_rate_limit=True, count=200).pages():
	try:
		followers.extend(page)
	except tweepy.TweepError as e:
		print("Going to sleep:", e)
		time.sleep(60)


checkDupl = []
check = 0

"""
for i in range(len(followers)): 
	apiCall = True
	for j in range(len(checkDupl)):
		if followers[i].screen_name == checkDupl[j]:
			apiCall = False
			print("found duplicate:" , followers[i].screen_name)
	if apiCall == True:
		checkDupl.append(followers[i].screen_name)
		check = check + 1
print(check)
"""

for i in range(len(followers)): 
	apiCall = True
	if check % 150 == 0 and check != 0:
		print("Sleeping...")
		time.sleep(900) #sleep for 15 minutes
	print(i, "/1182")
	for j in range(len(checkDupl)):
		if followers[i].screen_name == checkDupl[j]:
			apiCall = False
	if apiCall == True:
		checkDupl.append(followers[i].screen_name)
		check = check + 1;
		friendship = api.show_friendship(source_screen_name = "Ryleeg99", target_screen_name = followers[i].screen_name)
		data['users'].append({
				'name': followers[i].screen_name,
				'follower': str(friendship[0].followed_by),
				'friend': str(friendship[0].following)
			})


with open('data.txt','w') as outfile:
	json.dump(data, outfile)


#find all followers
#use API.show_friendship to compare relationship of source and all their followers by using method for each follower