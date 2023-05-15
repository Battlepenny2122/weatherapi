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

    col1,col2,col3,col4,col5 = st.columns(7)
    # enter here the address of your flask api
    url = 'http://api.weatherapi.com/v1/forecast.json'

    params = dict(
        q = city,
        key = api_key,
        days = 7)

    response = requests.get(url, params=params)

    prediction = response.json()

    pred = prediction['current']['temp_c']

    pred1max = prediction['forecast']['forecastday'][0]['day']['maxtemp_c']
    pred1min = prediction['forecast']['forecastday'][0]['day']['mintemp_c']
    image_icon1 = prediction['forecast']['forecastday'][0]['day']['condition']['icon']
    condition1 = prediction['forecast']['forecastday'][0]['day']['condition']['text']

    pred2max = prediction['forecast']['forecastday'][1]['day']['maxtemp_c']
    pred2min = prediction['forecast']['forecastday'][1]['day']['mintemp_c']
    image_icon2 = prediction['forecast']['forecastday'][1]['day']['condition']['icon']
    condition2 = prediction['forecast']['forecastday'][1]['day']['condition']['text']

    pred3max = prediction['forecast']['forecastday'][2]['day']['maxtemp_c']
    pred3min = prediction['forecast']['forecastday'][2]['day']['mintemp_c']
    image_icon3 = prediction['forecast']['forecastday'][2]['day']['condition']['icon']
    condition3 = prediction['forecast']['forecastday'][2]['day']['condition']['text']


    pred4max = prediction['forecast']['forecastday'][3]['day']['maxtemp_c']
    pred4min = prediction['forecast']['forecastday'][3]['day']['mintemp_c']
    image_icon4 = prediction['forecast']['forecastday'][3]['day']['condition']['icon']
    condition4 = prediction['forecast']['forecastday'][3]['day']['condition']['text']


    pred5max = prediction['forecast']['forecastday'][4]['day']['maxtemp_c']
    pred5min = prediction['forecast']['forecastday'][4]['day']['mintemp_c']
    image_icon5 = prediction['forecast']['forecastday'][4]['day']['condition']['icon']
    condition5 = prediction['forecast']['forecastday'][4]['day']['condition']['text']
    

    st.markdown(**<font size="5"> Today's forecast</font>**)
    st.image('https:' + image_icon1)
    st.write(f'**{condition1}**')
    st.write(f'The **current** temperature is {pred}')
    st.write(f'The **maximum** temperature today is {pred1max}')
    st.write(f'The **minimum** temperature today is {pred1min}')

    st.markdown('**<font size="5"> Forecast for the week</font>**')

    today_date = datetime.today().strftime('%A') 
    tomorrow_date = today_date + timedelta(days=1)
    two_day = today_date + timedelta(days=2)
    three_day = today_date + timedelta(days=3)
    four_day = today_date + timedelta(days=4)
    
    with col1:
        st.write(f'{today_date}')
        st.image('https:' + image_icon1)
        st.write(f'{condition1}')
        st.write(f'Max temp: {pred1max}')
        st.write(f'Min temp: {pred1min}')
    with col2:
        st.write(f'{tomorrow_date}')
        st.image('https:' + image_icon2)
        st.write(f'{condition2}')
        st.write(f'Max temp: {pred2max}')
        st.write(f'Min temp: {pred2min}')  

    with col3:
        st.write(f'{two_day}')
        st.image('https:' + image_icon3)
        st.write(f'{condition3}')
        st.write(f'Max temp: {pred3max}')
        st.write(f'Min temp: {pred3min}')
    
    with col4:
        st.write(f'{three_day}')
        st.image('https:' + image_icon4)
        st.write(f'{condition4}')
        st.write(f'Max temp: {pred4max}')
        st.write(f'Min temp: {pred4min}')

    with col5:
        st.write(f'{four_day}')
        st.image('https:' + image_icon5)
        st.write(f'{condition5}')
        st.write(f'Max temp: {pred5max}')
        st.write(f'Min temp: {pred5min}')
        
# st.markdown('I used weatherapi.com, and I am using st.markdown to test **_different fonts_**')
# st.markdown('Bayes Theorem is :green[P(A|B) = P(B|A)*P(A)/P(B)]')
