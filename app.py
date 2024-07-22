import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import time
import helper
import numpy as np


head_color = '#60b5fe'
white_color = '#ffff'
green_color = '#00e68a'
red_color = '#cc0000'
yellow_color = '#ffff66'
blue_color = '#0073e6'
purple_color = '#7733ff'
pink_color = '#ff1aff'

st.set_page_config(layout='centered', page_title='Stock Analysis', initial_sidebar_state='expanded')
st.sidebar.title('Choose Stocks')

# Getting Stock list
stocks = helper.get_stocks_list()
stocks.insert(0,'Select Stock')
selected_stock = st.sidebar.selectbox('Stocks', stocks)

# Getting Intervals 
intervals = helper.get_intervals()
selected_intervals = st.sidebar.selectbox('Select Intervals', intervals)


def intro():
    st.write("# Welcome to Stock Analysis Tool 👋")
    st.sidebar.success("Select a Stock above.")
    # Description of the website
    st.markdown(helper.get_markdown(), unsafe_allow_html=True)

def plot_line_graph(data):
    # Line Graph
    if data.iloc[0]['Close'] > data.iloc[-1]['Close']:
        st.line_chart(data=data, x='Time', y='Close', use_container_width=True, color=[red_color])
    else:
        st.line_chart(data=data, x='Time', y='Close', use_container_width=True, color=[green_color])

def plot_animated_linegraph(data):

    initial_data =  pd.DataFrame(columns=["Time","Close" ])
    progress_bar = st.sidebar.progress(0)
    chart =  st.line_chart(initial_data , x="Time" , y="Close" ,use_container_width=True )
    data_ln = len(data)

    for i in range(data_ln):
        subset = data.iloc[:i]
        perc = int(((i+1)/data_ln)*100)
        progress_bar.progress(perc)
        chart.line_chart(subset.set_index('Time'),use_container_width=True )
        time.sleep(0.03)
    
    progress_bar.empty()
    



if selected_stock == 'Select Stock':
    intro()
elif selected_stock != 'Select Stock':

    st.markdown(f"<h1 style='text-align: center; color: {white_color};'>Stock Analysis</h1>", unsafe_allow_html=True)
    
    # Heading
    st.markdown(f"<h2 style='text-align: center; color: {head_color};'>{selected_stock}</h2>", unsafe_allow_html=True)
    data = helper.get_stock_df(selected_stock)    

    # Getting Intervals 
    if intervals[selected_intervals] != 1:
        data = data.tail(intervals[selected_intervals])

    # Ploting Animated Line Graph
    plot_animated_linegraph(helper.get_data_for_ploting(data))
    
    # Ploting Simple Line Graph 
    # plot_line_graph(data)

    # Getting Current Data
    cur_d1 = helper.get_current_data(data)
    col1, col2, col3, col4, col5 = st.columns(5)

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
    st.markdown(f"<h1 style='text-align: center; color: {white_color};'>Volume</h1>", unsafe_allow_html=True)
    if data.iloc[0]['Volume'] > data.iloc[-1]['Volume']:
        st.bar_chart(data=data, x='Time', y='Volume', use_container_width=True, color=[red_color])
    else:
        st.bar_chart(data=data, x='Time', y='Volume', use_container_width=True, color=[green_color])

    st.divider()

    st.markdown(f"<h1 style='text-align: center; color: {white_color};'> Moving averages</h1>", unsafe_allow_html=True)
    st.line_chart(data=data, x='Time', y=['Close', '10 Days Moving Average', '30 Days Moving Average', '100 Days Moving Average'], height=800, use_container_width=True, color=[pink_color, purple_color, yellow_color, blue_color])
