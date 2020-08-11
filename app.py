import streamlit as st
import pandas as pd 
import plotly_express as px 


@st.cache(persist=True, suppress_st_warning=True)
def get_images(data_name):
	data = open(data_name)
	read_data = data.read().split()
	data.close()
	print (read_data)
	return read_data


def main():
	st.title("What we talk about when we talk about COVID-19")
	st.subheader("keywords on twitter")
	images = get_images('imageaddress.txt')
	st.image('images/keyword.png',width = 600)

	
	months = ["Please choose","Feb", "Mar", "Apr", "May","Jun", "Jul"]
	dataviz_choice = st.sidebar.selectbox("Choose Month",
                                         months)
	for i in range(7):
		if i == 0:
			st.subheader("To view word cloud in each month, choose from left sidebar")
		if i>0 and dataviz_choice == months[i]:
			st.image('images/keyword_'+months[i]+'.png',width = 600) 
            
	st.subheader("Check box to see popularity trend of each keyword")
	check_boxes =  ['CASE','TRUMP','US','DEATH','CHINA','MASK','PUBLIC','LOCKDOWN','HOSPITAL']
	for i in range(9):
		if st.checkbox(check_boxes[i]):
			st.image('images/frequency_'+check_boxes[i].lower()+'.png',width = 600)

if __name__ == "__main__":
    main()
