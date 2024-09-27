import mysql.connector

import json
from markdownify import markdownify as md

# database scheme.

#| Field            | Type         | Null | Key | Default | Extra |
#+------------------+--------------+------+-----+---------+-------+
#| PostId           | int          | NO   |     | NULL    |       |
#| PostTypeId       | int          | YES  |     | NULL    |       |
#| Title            | text         | YES  |     | NULL    |       |
#| Body             | text         | YES  |     | NULL    |       |
#| TagId            | int          | NO   |     | NULL    |       |
#| TagName          | varchar(255) | YES  |     | NULL    |       |
#| OwnerUserId      | int          | YES  |     | NULL    |       |
#| OwnerDisplayName | text         | YES  |     | NULL    |       |
#| CreationDate     | date         | YES  |     | NULL    |       |
#| Score            | int          | YES  |     | NULL    |       |
#| FavoriteCount    | int          | YES  |     | NULL    |       |
#| ViewCount        | int          | YES  |     | NULL    |       |
#| AnswerCount      | int          | YES  |     | NULL    |       |
#| CommentCount     | int          | YES  |     | NULL    |       |
#| AcceptedAnswerId | int          | YES  |     | NULL    |       |
#+------------------+--------------+------+-----+---------+-------+

def convert_break_line(text):
    clean_text = text.replace("&#xA;", " ").replace("&quot;", '\'')
    return clean_text
    
def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


cnx = mysql.connector.connect(user='so', password='passwd',
                              host='34.105.55.44', 
                              database='stack_overflow')

cursor = cnx.cursor()

query = "SELECT PostId, PostTypeId, Title, Body, TagName, CreationDate, Score, ViewCount FROM RELEVANT_JAVA_POSTS"

cursor.execute(query)

posts = []

for (postId, postTypeId, title, body, tagName, creationDate, score, viewCount) in cursor:
    post = { "postId" : postId,
             "postTypeId" : postTypeId,
             "title" : title,
             "body" : convert_break_line(remove_html_tags(body)), # md(body, strip=['a','+']),
             "tagName" : tagName,
             "creationDate" : creationDate.strftime('%Y%m%d'),
             "score" : score,
             "viewCount" : viewCount
            }
    posts.append(post)

cnx.close()


with open('data.json', 'w') as f:
    json.dump(posts, f, ensure_ascii=False, indent=4)
    
    
