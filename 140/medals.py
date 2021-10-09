import pandas as pd

data = "https://bites-data.s3.us-east-2.amazonaws.com/summer.csv"


def athletes_most_medals(data=data):
    medals = pd.read_csv(data)
    wcounts = (
        medals[medals["Gender"] == "Women"][["Athlete", "Medal"]]
        .groupby(["Athlete"])
        .count()["Medal"]
    )
    mcounts = (
        medals[medals["Gender"] == "Men"][["Athlete", "Medal"]]
        .groupby(["Athlete"])
        .count()["Medal"]
    )

    return pd.concat(
        [wcounts[wcounts == wcounts.max()], mcounts[mcounts == mcounts.max()]]
    )
