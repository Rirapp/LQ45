import streamlit as st
from multiapp import MultiApp
from apps import home, data, model # import your app modules here

#page config##
st.set_page_config(
   page_title="LQ45 Stocks Prediction",
   page_icon="📈",
   layout="centered",
   initial_sidebar_state="auto",
)

app = MultiApp()

st.header('LQ45 Stocks Prediction')


# Add all your application here
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #7289da;">
  <a class="navbar-brand" href="https://www.instagram.com/rirappp" target="_blank">LQ45 Stocks Prediction  </a>
</nav>
""", unsafe_allow_html=True)


app.add_app("Home", home.app)
app.add_app("Prediksi", data.app)
app.add_app("Video Edukasi", model.app)
# The main app
app.run()
