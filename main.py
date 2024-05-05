import streamlit as st

from streamlit_option_menu import option_menu


import home, trending, account, your, about, buy_me_a_coffee
st.set_page_config(
        page_title="Pondering",
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
                options=['Home','Account','Trending','Your Posts','about','Buy_me_a_coffee'],
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
            account.app()    
        if app == "Trending":
            trending.app()        
        if app == 'Your Posts':
            your.app()
        if app == 'about':
            about.app()    
        if app=='Buy_me_a_coffee':
            buy_me_a_coffee.app()    
             
          
             
    run()            
         
