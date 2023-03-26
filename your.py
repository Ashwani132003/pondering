import streamlit as st
from firebase_admin import firestore

  
def app():
    db=firestore.client()


    try:
        st.title('Posted by: '+st.session_state['username'] )

            
        result = db.collection('Posts').document(st.session_state['username']).get()
        r=result.to_dict()
        content = r['Content']
            
        
        def delete_post(k):
            c=int(k)
            h=content[c]
            try:
                db.collection('Posts').document(st.session_state['username']).update({"Content": firestore.ArrayRemove([h])})
                st.warning('Post deleted')
            except:
                st.write('Something went wrong..')
                
        for c in range(len(content)-1,-1,-1):
            st.text_area(label='',value=content[c])
            st.button('Delete Post', on_click=delete_post, args=([c] ), key=c)        

        
    except:
        if st.session_state.username=='':
            st.text('Please Login first')        