import streamlit as st
#from st_on_hover_tabs import on_hover_tabs
from streamlit_option_menu import option_menu 
from streamlit_extras.app_logo import add_logo
from streamlit_extras.switch_page_button import switch_page


url1="https://drive.google.com/file/d/1TIqwO2-GbPuWXg07G64j-Qi4IzfudqCq/view?usp=sharing"
ipsoslogo='https://drive.google.com/uc?export=download&id='+url1.split('/')[-2]
st.set_page_config(
     page_title="Ipsos Analytical Tool",
     layout="wide",
     page_icon= ipsoslogo,
    initial_sidebar_state="expanded")

add_logo(ipsoslogo,height=290)

html1 = '''
<p style="text-align: center; font-size: 20px">Jean-Pierre Sakr, <span style="color: #12BAAC; font-weight: bold;"><strong>MSBA Student</strong></span></p>

'''
html = """<p style="text-align: center; font-size: 17px"><br>A Capstone Project<br>submitted in partial fulfillment of the requirements for the degree of Master’s in Business Analytics</br></p>"""
html2 = '''
<p style="text-align: center; font-size: 15px">For additional info or enhancements<br> kindly send your request to jbs14@mail.aub.edu</p>
'''
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.markdown(html,unsafe_allow_html=True)
st.sidebar.markdown(html1, unsafe_allow_html=True)
st.sidebar.markdown(html2, unsafe_allow_html=True)
col1, col2, col3 = st.columns([1,7,1])
with col2:
        html="""<p style="font-size:20px;line-height:1.5em;">&nbsp;&nbsp;&nbsp;&nbsp;<br> <span style="border: 3px solid #065AA5;"> IPSOS ANALYTICAL TOOL - THE MEAURE OF TOMORROW </span></br>
        <br>THE MEASURE OF TOMMOROW is a web application created by Ipsos' Jean-Pierre Sakr, which allow its subscribers to take a step ahead and know what will happen in the upcoming months.</br>
        <br>Once you subscribe in the registration section, you will be guaranteed access to the forecasting page. </b></br>
  <br>The application allow its users to forecast the television viewership in the Saudi Arabia for the upcoming months. Users can select the channel to forecast from the drop down list and can choose the target audience.</br></p>"""
        st.markdown(html, unsafe_allow_html=True)