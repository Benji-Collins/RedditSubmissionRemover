# Reddit Submission Remover
### A simple Python script that removes Reddit posts/comments based on scores.


## Requirements
You must have PRAW and Python installed. A device with good bandwidth is recommended.

## Instructions
Clone this repo, cd in to it and run `python main.py`.

This script will first take your Reddit Username, Password, Client ID and Client Secret. Click [here](https://github.com/Benji-Collins/RedditSubmissionRemover/wiki/Creating-Client-ID-Secret) to find out how to get/make your ID and Secret.

You then need to input what you want to delete (`c` for comments, `p` for posts) then the score thershold for those submissions. For example, entering `100` will remove all comments/posts with 100 or less points.

## Limitations
Obviously this only works on your own account. There is a maximum limit of 1000 submissions per run.
