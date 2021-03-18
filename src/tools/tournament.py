import math

def tournament_round(no_of_teams, matchlist):
    new_matches = []
    for team_or_match in matchlist:
        if type(team_or_match) == type([]):
            new_matches += [tournament_round(no_of_teams, team_or_match)]
        else:
            new_matches += [[team_or_match, no_of_teams + 1 - team_or_match]]
    return new_matches


def flatten_list(matches):
    teamlist = []
    for team_or_match in matches:
        if type(team_or_match) == type([]):
            teamlist += flatten_list(team_or_match)
        else:
            teamlist += [team_or_match]
    return teamlist


def generate_tournament(num):
    num_rounds = math.log(num, 2)
    if num_rounds != math.trunc(num_rounds):
        raise ValueError("Number of teams must be a power of 2")
    teams = 1
    result = [1]
    while teams != num:
        teams *= 2
        result = tournament_round(teams, result)
    return flatten_list(result)


if __name__ == "__main__":
    print(generate_tournament(16))
