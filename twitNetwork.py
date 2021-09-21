import tweepy
import json
import time

auth = tweepy.OAuthHandler("QcqaHeHWkRZibqsAMfIT89rTR", "Qnz5SRgXMF6WJvkQ6ClnY4Uq2ljhTcr6ibhnEtLTYawOsk1t5q")
auth.set_access_token("778770992852193280-fEK3GTR0jZMAmrT5JN5r7lvG4eOf6Nk", "ywn2FvqZ3Swh19ltqKS71pAqwKGudRvTV5r10Z43dmfxy")


#api key "QcqaHeHWkRZibqsAMfIT89rTR"
#api secret key "Qnz5SRgXMF6WJvkQ6ClnY4Uq2ljhTcr6ibhnEtLTYawOsk1t5q"

api = tweepy.API(auth)

data = {}
data['users'] = []

user = api.get_user("_carsonsharp")

followers = []

for page in tweepy.Cursor(api.followers, screen_name = "_carsonsharp", wait_on_rate_limit=True, count=200).pages():
	try:
		followers.extend(page)
	except tweepy.TweepError as e:
		print("Going to sleep:", e)
		time.sleep(60)

for page in tweepy.Cursor(api.friends, screen_name = "_carsonsharp", wait_on_rate_limit=True, count=200).pages():
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
	twitterCalls = 0
	apiCall = True
	print(i, "/", len(followers))
	for j in range(len(checkDupl)):
		if followers[i].screen_name == checkDupl[j]:
			apiCall = False
	if apiCall == True:
		checkDupl.append(followers[i].screen_name)
		check = check + 1;
		total_friends = ""
		total_followers = ""

		#create for loop here to check relationship between each person
		for n in range(len(followers)):
			checkRelationship = True
			compareDupl = []
			if n != i:
				for k in range(len(compareDupl)):
					if followers[n].screen_name == compareDupl[k]:
						checkRelationship = False
				if checkRelationship == True:
					compareDupl.append(followers[n].screen_name)
					friendship = api.show_friendship(source_screen_name = followers[i].screen_name, target_screen_name = followers[n].screen_name)
					twitterCalls = twitterCalls + 1
					if friendship[0].followed_by == True:
						total_followers += followers[n].screen_name
						total_followers += ","
					if friendship[0].following == True:
						total_friends += followers[n].screen_name
						total_friends += ","	

		myFriendship = api.show_friendship(source_screen_name = followers[i].screen_name, target_screen_name = "_carsonsharp")
		twitterCalls = twitterCalls + 1
		if myFriendship[0].followed_by == True:
					total_followers += "_carsonsharp"
		if myFriendship[0].following == True:
					total_friends += "_carsonsharp"

		data['users'].append({
				'name': followers[i].screen_name,
				'follower': str(friendship[0].following),
				'friend': str(friendship[0].followed_by),
				'mutual_followers': total_followers, 
				'mutual_friends': total_friends 
			})
		print(data['users'])
		print("API calls: " , twitterCalls)
		print("Sleeping...")
		time.sleep(900) #wait 15 minutes for more API calls


with open('network_data.txt','w') as outfile:
	json.dump(data, outfile)

