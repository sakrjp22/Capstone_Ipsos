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
        <br>"In our world of rapid change, the need for reliable information to make confident decisions has never been greater.</br>
        <br>At Ipsos we believe our clients need more than a data supplier, they need a partner who can produce <b>accurate and relevant information</b> and turn it into actionable truth.</br>
  <br>This is why our passionately curious experts not only provide the most precise measurement, but shape it to provide True Understanding of Society, Markets and People."</br></p>"""
        st.markdown(html, unsafe_allow_html=True)
st.write("")
st.write("")
st.markdown("""<h2 style="font-size:28px;color:#12BAAC;text-align: left"> Register here</h2>""",unsafe_allow_html=True)
contact_form = """
            <style>
            input[type=message], input[type=email], input[type=text], textarea {
  width: 100%; 
  padding: 12px; 
  border: 1px solid #ccc; 
  border-radius: 4px; 
  box-sizing: border-box; 
  margin-top: 6px; 
  margin-bottom: 16px; 
  resize: vertical 
}


button[type=submit] {
  background-color: #12BAAC;
  color: white;
  padding: 12px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}


button[type=submit]:hover {
  background-color: #065AA5 ;
}
</style>
<form action="https://formsubmit.co/jbs14@mail.aub.edu" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="Company" placeholder="Company name" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
lc, rc = st.columns(2)
with lc:
    st.markdown(contact_form, unsafe_allow_html=True)