from dataclasses import dataclass

@dataclass
class base_reviews:

    count:int
    ratings:list

class reviews:
    def __new__(cls,data):

        ratings = []

        for review in data.get("reviews"):
            user = review.get("user")
            ratings.append({
                "user":{
                    "loginName":user.get("loginName"),
                    "fullName":user.get("fullName"),
                    "avatar":user.get("avatarUrl"),
                    "homepage":user.get("homepage")
                },
                "comment":review.get("comment"),
                "rating":review.get("rating")
            })

        return base_reviews(
            count=len(data.get("reviews",[])),
            ratings=ratings
        )
