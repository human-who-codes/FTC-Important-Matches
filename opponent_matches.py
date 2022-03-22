# Receive a list of ftc matches that should be returned with some of the matches highlighted
# Matches are inputed as a list of tuples of the form:
#  [match_num, blue1, blue2, red1, red2]
#Return a list of numbers that are the matches that should be returned
 
def get_yellow_teams(matches, team):
  # matches = [[1, 'a', 'b', 'c', 'd'], 
  #[2, 'e', 'f', 'g', 'h'], 
  # [3, 'i', 'j', 'k', 'l'], 
  # [4, 'm', 'n', 'o', 'p']]
  # team = 'a'

  return get_opponents(matches, team)
def get_blue_teams(matches, team):
    return get_allies(matches, team)
# return all opponents that team will face
def get_opponents(matches, team):
    opponents = []
    for match in matches:
        if team in match:
            #get the names of the opponents
            blue1 = match[1]
            blue2 = match[2]
            red1 = match[3]
            red2 = match[4]
            #if the team is in the blue alliance
            if team in [blue1, blue2]:
                opponents.append(red1)
                opponents.append(red2)
            #if the team is in the red alliance
            else:
                opponents.append(blue1)
                opponents.append(blue2)
    return opponents

def get_allies(matches, team):
    allies = []
    for match in matches:
        if team in match:
            #get the names of the opponents
            blue1 = match[1]
            blue2 = match[2]
            red1 = match[3]
            red2 = match[4]
            #if the team is in the blue alliance
            if team in [blue1, blue2]:
                if team == blue1:
                    allies.append(blue2)
                else:
                    allies.append(blue1)
                allies.append(blue2)
            #if the team is in the red alliance
            else:
                allies.append(red1)
                allies.append(red2)
    return allies

def get_ally_matches(matches, allies):
    target_matches = []
    for match in matches:
        for ally in allies:
            if ally in match:
                target_matches.append(match)
                # continue so that we don't add the same match twice
                break
    return target_matches
# return all matches that the opponents are in
def get_opponent_matches(matches, opponents):
    target_matches = []
    for match in matches:
        for opponent in opponents:
            if opponent in match:
                target_matches.append(match)
                # continue so that we don't add the same match twice
                break
    return target_matches

# return match numbers of a set of matches
def get_match_nums(matches):
    return [match[0] for match in matches]
