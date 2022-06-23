import streamlit as st
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

def app():
    
    st.subheader('Kenapa Pilih Investasi Saham?')
    vid_file = f'''<iframe width="100%" height="400" src="https://www.youtube.com/embed/hSzJEWP53BQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
    st.markdown(vid_file,unsafe_allow_html=True)
    

    st.subheader('Apa Itu Indeks LQ45?')
    vid_file = f'''<iframe width="100%" height="400" src="https://www.youtube.com/embed/n83Stf-IXJw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
    st.markdown(vid_file,unsafe_allow_html=True)
    
    
    st.subheader('Wajib Tau Nih, Penyebab Gagal Cuan Dari Investasi Saham')
    vid_file = f'''<iframe width="100%" height="400" src="https://www.youtube.com/embed/d-Y6rtFNlyA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
    st.markdown(vid_file,unsafe_allow_html=True)
    
    
    st.subheader('Pentingnya Berinvestasi')
    vid_file = f'''<iframe width="100%" height="400" src="https://www.youtube.com/embed/D9VivZqW2UA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
    st.markdown(vid_file,unsafe_allow_html=True)
