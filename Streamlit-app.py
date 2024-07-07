import streamlit as st

st.title('Hello Streamlit')

st.header("Header")

st.subheader("Sub header")

st.text("This is my first streamlit")

st.markdown("""  # h1 tag
   ## h2 tag
   ### h3 tag
   :moon:<br>
   :sunglasses:  
   ** bold **
    _italics_
   """ ,True)

st.latex(r''' \int\int\int\int d^{3}R^{'} d^{3}r^{'} d^{3}R d^{3}r \langle K^{'}+2x, k^{'}|R^{'},r^{'}\rangle
\langle R^{'},r^{'}|V|R,r\rangle \langle R,r|K+2x,k\rangle''')

st.write("harsh" , "grupta")
