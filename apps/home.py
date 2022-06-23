import streamlit as st
from PIL import Image



def app():

    ##st.header('Aplikasi Prediksi Saham-Saham Pada Indeks LQ45')
    st.subheader('Apa itu LQ45? ')
    st.write('LQ45 adalah indeks yang mengukur kinerja dari 45 saham yang memiliki liquiditas tinggi dan kapitalisasi saham yang besar serta didukung oleh fundamental saham yang baik.') 
    st.write('Indeks LQ45 dibuat sebagai upaya pelengkap IHSG khususnya untuk menyediakan sarana yang objektif dan terpercaya bagi analisis keuangan, manajer investasi, investor dan pemerhati pasar modal dalam memonitor pergerakan harga saham yang aktif diperdagangkan di Bursa Efek Indonesia.') 
       

    BEI = Image.open ('asset/BEI.jpg')
    st.image(BEI, caption='Bursa Efek Indonesia', width=700, output_format='auto')

    st.subheader('Apa Saja Contoh Sahamnya?')
    st.write('Beberapa saham/emiten yang tergabung pada indeks LQ45 ini salah satunya adalah :')
    st.write('- PTBA')
    st.write('- TLKM')
    st.write('- BBNI')
    st.write('- BBCA')

    PTBA = Image.open ('asset/ptba.jpg')
    st.image(PTBA, caption='Bukit Asam Tbk', width=700, output_format='auto')

    st.subheader('Bagaimana Website ini Bekerja?')
    st.write('Website ini berkerja dan memprediksi harga-harga emiten dengan mengambil data dari 1 januari 2018 sampai data terbaru dan menggunakan pustaka prediksi buatan Facebook yang bernama Prophet.') 
    st.write('Prophet adalah paket open source  yang dirilis oleh tim inti Data Science  Facebook untuk memprediksi data deret waktu berdasarkan model aditif di mana tren non-linier sesuai dengan musiman tahunan, mingguan, dan harian, ditambah efek liburan sehingga menghasilkan hasil prediksi akurat dan otomatis.')
    st.write('Keakuratan website prediksi ini dihitung dengan MAPE dengan nilai 15 sampai 45 persen dan disertakan dengan tabel cross validation sebagai tabel pendukung.')
   
    STONKS = Image.open ('asset/stonks.png')
    st.image(STONKS, caption='Pasti Cuan !', width=700, output_format='auto')
    

    

   