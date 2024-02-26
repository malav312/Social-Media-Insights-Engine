import pandas as pd
import json

#1.1 Function for parsing json and getting datafram
def parse_data(data):
    with open(data, "r") as f:
        data = json.load(f)
    return pd.DataFrame(data)

#1.2 Function for getting insights
def filter_creators(df, min_followers=None, max_followers=None, keyword=None, min_views=None):
    filtered_df = df.copy()
    if min_followers and max_followers:
        filtered_df = filtered_df[(filtered_df["follower_count"] >= min_followers) & (filtered_df["follower_count"] <= max_followers)]
    if keyword:
        filtered_df = filtered_df[filtered_df["bio"].str.contains(keyword, case=False)]
    if min_views:
        filtered_df = filtered_df[filtered_df["average_views"] >= min_views]
    return filtered_df


def get_all_creators(df):
    return df.copy()

#1.4 Optional function for user to save filtered data
def export_data(data, filename):
    data.to_csv(filename, index=False)