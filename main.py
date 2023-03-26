import streamlit as st

from streamlit_option_menu import option_menu
import streamlit.components.v1 as components

import home, trending, test, your, about


components.html(
    """
    <head>
    
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1798673929792920"
    crossorigin="anonymous"></script>
    </head>
    
    """
)

st.markdown(
    """
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1798673929792920"
     crossorigin="anonymous"></script>
    """,
    unsafe_allow_html = True
)

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='Pondering ',
                options=['Home','Account','Trending','Your Posts','about'],
                icons=['house-fill','person-circle','trophy-fill','chat-fill','info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
                )

        
        if app == "Home":
            home.app()
        if app == "Account":
            test.app()    
        if app == "Trending":
            trending.app()        
        if app == 'Your Posts':
            your.app()
        if app == 'about':
            about.app()    
             
          
             
    run()            
         
