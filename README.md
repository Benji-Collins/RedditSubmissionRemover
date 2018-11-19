# Reddit Submission Remover
### A simple Python script that removes Reddit posts/comments based on scores.

---

## Instructions
This script will first take your Reddit Username, Password, Client ID and Client Secret. Click [here](www.f3ef.com) to find out how to get/make your ID and Secret.

You then need to input what you want to delete (`c` for comments, `p` for posts) then the score thershold for those submissions. For example, entering `100` will remove all comments/posts with 100 or less points.

---

## Limitations
Obviously this only works on your own account. There also seems to be a limit of 100 submission for each time the script is run, despite `limit=None` being set. Not sure what's happening there. I would recommend not using the tool for a large number of comments/posts until this issue is fixed.
