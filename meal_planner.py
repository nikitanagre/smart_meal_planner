import pandas as pd
import random

def load_recipes():
    return pd.read_csv("data/recipes.csv")

def get_meals(preference="", meals_per_day=3):
    df = load_recipes()

    if preference:
        df = df[df['tags'].str.contains(preference, case=False, na=False)]

    selected_meals = df.sample(n=min(meals_per_day * 7, len(df)))
    return selected_meals
