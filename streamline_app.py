# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col
import requests

# Write directly to the app
st.title(f":cup_with_straw: Customize Your Smoothie! :cup_with_straw:")
st.write(
    """Choose the fruits you want in your custom Smoothie!
    """
)

name_on_order = st.text_input('Name On Smoothie')
st.write("The name on your smoothie will be: "+ name_on_order)

cnx = st.connection("snowflake")
session = cnx.session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col("FRUIT_NAME"), col("SEARCH_ON"))
#st.dataframe(data=my_dataframe, use_container_width=True)

pd_df = my_dataframe.to_pandas()
st.dataframe(pd_df)
st.stop()
