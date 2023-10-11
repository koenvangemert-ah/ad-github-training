def likes(team: list) -> str:
    """
    Function returns who liked your post on Facebook
    :param: List om teammembers (lst)
    :return: A statement of who liked your post (str)
    """
    if len(team) == 0:
        return "no one likes this"
    elif len(team) == 1:
        return team[0] + " likes this"
    elif len(team) == 2:
        return team[0] + " en " + team[1] + " like this"
    elif len(team) == 3:
        return team[0] + ", " + team[1] + " and " + team[2] + " like this"
    else:
        return team[0] + ", " + team[1] + " and 2 others like this"
