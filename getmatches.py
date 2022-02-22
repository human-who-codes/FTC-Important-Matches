# go to an input url and get the matches
# teams containers have ids "team{number}_{match_num}"

# use static web scrapers
import requests
import bs4
import re

def get_matches(url):
    # matches are [match_num, blue1, blue2, red1, red2]
    matches = []

    # get the html
    response = requests.get(url)
    # parse the html
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    # get all elements with id "team{number}_{match_num}"
    team_ids = soup.find_all(id=re.compile('team[0-9]_[0-9]'))
    for ids in team_ids:
        nums = ids.attrs['id']
        nums.strip("team")
        nums.split("_")
        cur_match = nums[1]
        matches[cur_match][nums[0]] = ids.text
        
    print(matches)
    return matches