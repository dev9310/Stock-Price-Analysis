import streamlit as st
import pandas as pd
import helper
import preprocessor
import matplotlib.pyplot as plt
import seaborn as sns
import random

head_color ='#60b5fe'
white_color ='#ffff'
green_color = '#00e68a'
red_color = '#cc0000'
yellow_color = '#ffff66'
blue_color = '#0073e6'
purple_color = '#7733ff'
pink_color = '#ff1aff'

st.set_page_config(layout='wide' ,page_title='Stock Analysis')
                   
st.sidebar.title('Choose Stocks')
st.markdown(f"<h1 style='text-align: center; color: {white_color};'>Stock Analysis</h1>", unsafe_allow_html=True)

# Getting Stock list
stocks = helper.get_stocks_list()
selected_stock = st.sidebar.selectbox('Stocks', stocks)

# Getting Intervals 
intervals = helper.get_intervals()
slected_intrvals = st.sidebar.selectbox('Select Intervals', intervals)


if selected_stock:
    
    # Heading
    st.markdown(f"<h2 style='text-align: center; color: {head_color};'>{selected_stock}</h2>", unsafe_allow_html=True)
    data = helper.get_stock_df(selected_stock)    
    
    # Getting Intervals 
    if intervals[slected_intrvals] != 1:
        data = data.tail(intervals[slected_intrvals])
        
    # Line Graph
    if data.iloc[0]['Close'] > data.iloc[-1]['Close']:
        st.line_chart(data=data, x='Time', y='Close'  , use_container_width=True , color=[red_color])
    else:
        st.line_chart(data=data, x='Time', y='Close'  , use_container_width=True , color=[green_color])

    # Getting Current Data
    cur_d1= helper.get_current_data(data)
    col1 , col2 , col3 , col4 ,col5 = st.columns(5)
    
    # Creating Cols
    with col1:
        st.title('Open')
        st.header(f':blue[{cur_d1.Open}]')
    with col2:
        st.title('Close')
        st.header(f':blue[{cur_d1.Close}]')
    with col3:
        st.title('High')
        st.header(f':blue[{cur_d1.High}]')
    with col4:
        st.title('Low')
        st.header(f':blue[{cur_d1.Low}]')
    with col5:
        st.title('Volume')
        st.header(f':blue[{cur_d1.Volume}]')

    st.divider()

    # Bar Chart
    st.markdown(f"<h1 style='text-align: center; color: {white_color};'>Volume</h1> " , unsafe_allow_html=True)
    # st.title(':blue[BarChart]')
    if data.iloc[0]['Volume'] > data.iloc[-1]['Volume']:    
        st.bar_chart(data=data , x='Time' , y='Volume', use_container_width=True , color=[red_color] )
    else:
        st.bar_chart(data=data , x='Time' , y='Volume', use_container_width=True , color=[green_color] )

    st.divider()

    st.markdown(f"<h1 style='text-align: center; color: {white_color};'> Moving averages</h1> " , unsafe_allow_html=True)
    st.line_chart(data=data , x='Time' , y=['Close','10 Days Moving Average' ,'30 Days Moving Average','100 Days Moving Average'] , height=800,use_container_width=True , color=[pink_color , purple_color, yellow_color, blue_color])

        

    # st.write([random.randint(0, 5000) for _ in range(30)] for _ in range(1))
    # st.write(data.Close.tail(100).tolist())
    

    # df = pd.DataFrame(
    #     {
    #         "name": ["Roadmap"],
    #         "url": ["https://roadmap.streamlit.app"],
    #         "stars": data.Close.tail(1).tolist(),
    #         "views_history": [data.Close.tail(365).tolist()],
    #     }
    # )
    # st.dataframe(
    #     df,
    #     column_config={
    #         "name": "App name",
    #         "stars": st.column_config.NumberColumn(
    #             "Github Stars",
    #             help="Number of stars on GitHub",
    #             format="%f",
    #         ),
    #         "url": st.column_config.LinkColumn("App URL"),
    #         "views_history": st.column_config.LineChartColumn(
    #             "Views (past 30 days)", y_min=0, y_max=200
    #         ),
    #     },
    #      use_container_width=True ,
    #     hide_index=True,
    # )






