import streamlit as st

import datetime

import requests

'''
# Weather API test!

This website queries weatherapi.com! Please enter your city and we'll get you your forecast for the day!
'''

city = st.text_input('Which city do you live in?', value='Sydney')
api_key = '2fb4fc4ca9994f03bbc234017231405'

if st.button('Submit'):

    # enter here the address of your flask api
    url = 'http://api.weatherapi.com/v1/forecast.json'

    params = dict(
        q = city,
        key = api_key)

    response = requests.get(url, params=params)

    prediction = response.json()

    pred = prediction['current']['temp_c']
    pred1 = prediction['forecast']['forecastday'][0]['day']['maxtemp_c']
    pred2 = prediction['forecast']['forecastday'][0]['day']['mintemp_c']
    condition = prediction['forecast']['forecastday'][0]['day']['condition']['text']
    image_icon = prediction['forecast']['forecastday'][0]['day']['condition']['icon']

    st.image(image_icon)
    st.write(f'**{condition}**')
    st.write(f'The **current** temperature is {pred}')
    st.write(f'The **maximum** temperature today is {pred1}')
    st.write(f'The **minimum** temperature today is {pred2}')