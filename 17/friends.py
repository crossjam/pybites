from itertools import combinations, permutations


def friends_teams(friends_teams, team_size=2, order_does_matter=False):
    if team_size > len(friends_teams):
        raise ValueError("Team size greater than friends size")

    if order_does_matter:
        return permutations(friends_teams, team_size)
    else:
        return combinations(friends_teams, team_size)
