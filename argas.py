import json
from facebook_scraper import get_posts, set_noscript
from facebook_scraper import get_group_info

ginfo = get_info("VenomousAndOtherSnakesOfSian")
print(ginfo['id'])
