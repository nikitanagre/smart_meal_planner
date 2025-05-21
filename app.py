import streamlit as st

from meal_planner import get_meals
from grocery_list_generator import generate_grocery_list

def generate_recipe(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

# Page config
st.set_page_config(page_title="🍽️ Smart Meal Planner", layout="wide", page_icon="🍳")

# Title and description
st.title("🍽️ Smart Meal Planner & Grocery List Generator")
st.markdown(
    """
    Welcome! Use this app to plan your weekly meals and generate grocery lists automatically.
    You can also get AI-generated recipe suggestions tailored to your preferences.
    """
)

# Layout using columns
col1, col2 = st.columns([2, 1])

with col1:
    st.header("Weekly Meal Planner")
    prefs = st.text_input("Enter dietary preference (veg, non-veg, breakfast, etc.):")
    if st.button("Generate Weekly Plan"):
        meals = get_meals(preference=prefs)
        st.success("Here is your meal plan for the week:")
        st.dataframe(meals[['meal_name', 'ingredients']])
        
        grocery_list = generate_grocery_list(meals)
        st.subheader("🛒 Grocery List")
        for item, qty in grocery_list.items():
            st.write(f"- **{item.capitalize()}**: {qty:.2f}")


# Footer or additional notes
st.markdown("---")
st.markdown(
    "Created by Nikita — built with Python, Streamlit"
)
