import streamlit as st
import pandas as pd


def plotting_line_graph(data):

    # Initial plot setup
    st.sidebar.title('Progress')
    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()

    # Initialize an empty DataFrame for dynamic plotting
    initial_data = pd.DataFrame(columns=['Time', 'Close'])
    chart = st.line_chart(initial_data, use_container_width=True)

    # Animate the plot
    for i in range(1, len(data) + 1):
        # Get the subset of data up to the current index
        subset = data.iloc[:i]
        
        
        # Update the line chart
        chart.line_chart(subset.set_index('Time'), use_container_width=True)
        status_text.text(f"{i}/{len(data)} Data Points Displayed")
        progress_bar.progress(i / len(data))
    
    progress_bar.empty()

def get_data_for_plotting(data):

    # Creating Data Frame for Plot
    df = pd.DataFrame({
        'Time': np.array(data.Time),
        'Close': np.array(data.Close)
    })

    return df

df = get_data_for_plotting(data)
plotting_line_graph(df)