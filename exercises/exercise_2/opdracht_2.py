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

from datetime import datetime
from datetime import date

def is_it_my_birthday(name: str, date_of_birth: str) -> str:
    """
    :param name: Name of person (str)
    :param date_of_birth: Date of birth of person (str)
    :return: Answer whether it is the persons birthday today (str)
    """
    birth = datetime.strptime(date_of_birth, "%Y-%m-%d").date()
    today = date.today()

    if birth.day == today.day and birth.month == today.month:
        return "Today is " + name + "'s birthday!"
    else:
        return "Unfortunately, today is not the birthday of " + name

print(is_it_my_birthday("Koen", "1997-10-11"))