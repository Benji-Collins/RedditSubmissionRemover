import praw
import time
import getpass

print "Welcome to the Reddit Comment/Post Remover! Read the README at https://github.com/Benji-Collins/RedditSubmissionRemover for more info."
raw_username = raw_input("Your Reddit username: ")
raw_password = getpass.getpass("Your Reddit password: ")
raw_clientid = raw_input("Your Client ID: ")
raw_clientsecret = getpass.getpass("Your Client Secret: ")

def bot_login():
	r = praw.Reddit(username = raw_username,
			password = raw_password,
			client_id = raw_clientid,
			client_secret = raw_clientsecret,
			user_agent = "Reddit Submission Remover")
	print "Logged in!"

	return r

def removecomments(r):
	deletecount = 0
	print "Removing comments with " + karma + " or less karma. This may take quite some time. Multiple runs may be needed."
	for comment in r.redditor(raw_username).comments.new(limit=None):
		if comment.score < int(karma):
			comment.delete()
			print "Removed comment: " + comment.id
			deletecount += 1
	print "Deleted " + str(deletecount) + " comments."

def removeposts(r):
	deletecount = 0
	print "Removing posts with " + karma + " or less karma. This may take quite some time. Multiple runs may be needed."
	for submission in r.redditor(raw_username).submissions.new(limit=None):
		if submission.score < int(karma):
			submission.delete()
			print "Removed submission: " + submission.id
			deletecount += 1
	print "Deleted " + str(deletecount) + " posts."

r = bot_login()
option = raw_input("Remove comments or posts [c or p]? ")
karma = raw_input("With ___ or less karma: ")

if option == 'c':
    removecomments(r)
elif option =='p':
    removeposts(r)
else:
    print "Incorrect option. Exiting."
    exit()
