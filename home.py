import streamlit as st
from firebase_admin import firestore

def app():
    
    if 'db' not in st.session_state:
        st.session_state.db = ''

    db=firestore.client()
    st.session_state.db=db
    # st.title('  :violet[Pondering]  :sunglasses:')
    
    ph = ''
    if st.session_state.username=='':
        ph = 'Login to be able to post!!'
    else:
        ph='Post your thought'    
    post=st.text_area(label=' :orange[+ New Post]',placeholder=ph,height=None, max_chars=500)
    if st.button('Post',use_container_width=20):
        if post!='':
                    
            info = db.collection('Posts').document(st.session_state.username).get()
            if info.exists:
                info = info.to_dict()
                if 'Content' in info.keys():
                
                    pos=db.collection('Posts').document(st.session_state.username)
                    pos.update({u'Content': firestore.ArrayUnion([u'{}'.format(post)])})
                    # st.write('Post uploaded!!')
                else:
                    
                    data={"Content":[post],'Username':st.session_state.username}
                    db.collection('Posts').document(st.session_state.username).set(data)    
            else:
                    
                data={"Content":[post],'Username':st.session_state.username}
                db.collection('Posts').document(st.session_state.username).set(data)
                
            st.success('Post uploaded!!')
    
    st.header(' :violet[Latest Posts] ')
    
    
    
    
    docs = db.collection('Posts').get()
            
    for doc in docs:
        d=doc.to_dict()
        try:
            st.text_area(label=':green[Posted by:] '+':orange[{}]'.format(d['Username']),value=d['Content'][-1],height=20)
        except: pass
