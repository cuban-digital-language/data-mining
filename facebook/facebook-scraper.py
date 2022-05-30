from facebook_scraper import get_posts
import json

credentials = ('user', 'pass')

links = ['groups/1746673108822943',
         'groups/271609852994505', 'groups/507355953581910']
# links = ["groups/2602375306723194",
#          'groups/1669400126613634', 'groups/2015057042124445']


# links = ["groups/2602375306723194"]
listposts = []
for link in links:
    for post in get_posts(link, pages=5, options={"comments": True}, credentials=credentials):
        listposts.append({
            'text': post['text'],
            'date': str(post['time']),
            'url': post['post_url'],
            'comment': []
        })

        for comment in post['comments_full']:
            listposts[-1]['comment'].append({
                'text': comment['comment_text'],
                'date': str(comment['comment_time']),
                'url': comment['comment_url'],
            })


with open("facebook3.json", "w") as f:
    f.write(json.dumps(listposts))
