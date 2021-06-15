from typing import List


def who_likes_it(likes_it: List[str]):
    if len(likes_it) == 0:
        return "no one likes this"

    elif len(likes_it) == 1:
        return f"{likes_it[0]} likes this"

    elif len(likes_it) == 2:
        return f"{likes_it[0]} and {likes_it[1]} like this"

    elif len(likes_it) == 3:
        return f"{likes_it[0]}, {likes_it[1]} and {likes_it[2]} like this"

    elif len(likes_it) > 3:
        return f"{likes_it[0]}, {likes_it[1]} and {len(likes_it) - 2} others like this"
