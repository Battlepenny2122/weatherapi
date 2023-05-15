import streamlit as st
from datetime import datetime, timedelta
import requests
'''
# Weather API test!

This website queries weatherapi.com! Please enter your city and we'll get you your forecast for the day and week!
'''
city = st.text_input('Which city do you live in?', value='Sydney')
api_key = '2fb4fc4ca9994f03bbc234017231405'

if st.button('Submit'):
    # enter here the address of your flask api
    url = 'http://api.weatherapi.com/v1/forecast.json'
    params = dict(
        q = city,
        key = api_key,
        days = 7)
    response = requests.get(url, params=params)
    prediction = response.json()
    pred = prediction['current']['temp_c']

    predmax_list = []
    predmin_list = []
    image_icon_list = []
    condition_list = []

    for i in range(0,5):
        predmax_list.append(prediction['forecast']['forecastday'][i]['day']['maxtemp_c'])
        predmin_list.append(prediction['forecast']['forecastday'][i]['day']['mintemp_c'])
        image_icon_list.append(prediction['forecast']['forecastday'][i]['day']['condition']['icon'])
        condition_list.append(prediction['forecast']['forecastday'][i]['day']['condition']['text'])

    city2 = prediction['location']['name']
    country = prediction['location']['country']
    
    with st.container():
        st.markdown(f'**Todays forecast in {city2}, {country}**')
        st.image('https:' + image_icon_list[0])
        st.write(f'**{condition_list[0]}**')
        st.write(f'The **current** temperature is {pred}{chr(176)}C')
        st.write(f'The **maximum** temperature today is {predmax_list[0]}{chr(176)}C')
        st.write(f'The **minimum** temperature today is {predmin_list[0]}{chr(176)}C')
        st.markdown('**Forecast for the week**')
    
    today_date = datetime.today()
    dates = [today_date.strftime('%A')]
    for i in range(1,5):
        date = today_date + timedelta(days = i)
        dates.append(date.strftime('%A'))
    col = st.columns(5)
    for i in range(5):
        for k in col:
            if col.index(k) == i:
                with k:
                    st.write(f'{dates[i]}')
                    st.image('https:' + image_icon_list[i])
                    st.write(f'{condition_list[i]}')
                    st.write(f'Max temp: {predmax_list[i]}{chr(176)}C')
                    st.write(f'Min temp: {predmin_list[i]}{chr(176)}C')
            else:
                continue
