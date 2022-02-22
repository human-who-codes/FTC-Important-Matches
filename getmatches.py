# go to an input url and get the matches
# teams containers have ids "team{number}_{match_num}"

# use static web scrapers
import requests
import bs4
import re
import utilfuncs

def get_matches(url):
    # matches are [match_num, blue1, blue2, red1, red2]
    matches = utilfuncs.init2DArray(100, 5)

    # get the html
    response = requests.get(url)
    # parse the html
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    # get all elements with id "team{number}_{match_num}"
    team_ids = soup.find_all(id=re.compile('team[0-9]_[0-9]'))
    last_index = 0
    for ids in team_ids:
        nums = ids.attrs['id']
        # remove 'team' from nums
        nums = nums[4:]
        nums = nums.split("_")
        last_index = int(nums[1]) - 1
        matches[int(nums[1])-1][int(nums[0])] = ids.text.strip("\n").strip()
        matches[int(nums[1])-1][0] = int(nums[1])
    matches = matches[:last_index+1]
    return matches