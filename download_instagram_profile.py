#pip install instaloader

import instaloader as insta

ob = insta.Instaloader()

user = input('Enter Username: ')

ob.download_profile(user, profile_pic_only = True)
