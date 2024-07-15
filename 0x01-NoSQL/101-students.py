#!/usr/bin/env python3
""" returns all students sorted by average score: """


def top_students(mongo_collection):
    """ returns all students sorted by average score: """

    pipeline = [
        {
            "$project": {
                "name": 1,
                "algo": 1,
                "C": 1,
                "Python": 1,
                "averageScore": {
                    "$avg": {
                        "$concatArrays": ["$Algo", "$C", "$Python"]
                    }
                },
            }
        },
        {"$sort": {"averageScore": -1}}
    ]
    return list(mongo_collection.aggregate(pipeline))
