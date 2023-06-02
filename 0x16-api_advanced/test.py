#!/usr/bin/python3
def posts(post):
    if len(post) > 0:
        print(post[0])
        posts(post[1:])


post = ["post 1", "post 2", "post 3"]
posts(post)
