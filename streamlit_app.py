import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header ('Breakfast Favorites')
streamlit.text ('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text ('🐔 Hard-Boiled Free-Range Egg')

streamlit.text ('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
#Lets put a pick list her so they can pick the fruit they want to include
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruit_to_show= my_fruit_list.loc[fruits_selected]



# Display the table on the page.
#streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruit_to_show)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

#New Section to dispaly Fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')

import requests
fruityvice.response = request.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice.response.SON())




