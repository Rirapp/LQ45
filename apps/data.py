import streamlit as st
from datetime import date

import numpy as np
import pandas as pd
from sklearn import datasets

import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

from prophet.plot import plot_cross_validation_metric
from prophet.diagnostics import cross_validation
from prophet.diagnostics import performance_metrics
#from statsmodels.tool.eval_measures import rmse



def app():
    
    ##parameter waktu##
    START = "2018-01-01"
    TODAY = date.today().strftime("%Y-%m-%d")

    st.title("Aplikasi Prediksi Saham-Saham Pada Indeks LQ45 ")

    ##saham lq45##
    stocks = ("ADRO.JK","AMRT.JK","ANTM.JK","ASII.JK","BBCA.JK","BBTN.JK","BBNI.JK","BBCA.JK","BMRI.JK","BBRI.JK",
            "BRPT.JK","BUKA.JK","CPIN.JK","EMTK.JK","ERAA.JK","EXCL.JK","GGRM.JK","GOTO.JK","HMSP.JK","HRUM.JK","ICBP.JK",
            "INCO.JK","INDF.JK","INKP.JK","INTP.JK","ITMG.JK","JPFA.JK","KLBF.JK","MDKA.JK","MEDC.JK","MIKA.JK",
            "MNCN.JK","PGAS.JK","PTBA.JK","PTPP.JK","SMGR.JK","TBIG.JK","TINS.JK","TKIM.JK","TLKM.JK","TOWR.JK",
            "TPIA.JK","UNTR.JK","UNVR.JK","WIKA.JK")
    selected_stock = st.selectbox("Pilih Dataset Saham Yang Diinginkan", stocks)

    n_years = st.slider("Tahun Prediksi:", 1, 5)
    period = n_years * 365

    ##chaching##
    @st.cache
    def load_data(ticker):
        data = yf.download(ticker, START, TODAY)
        data.reset_index(inplace=True)
        return data

    data_load_state = st.caption("Meloading data...")
    data = load_data(selected_stock)
    data_load_state.text("Loading data selesai!")

    ##raw data##
    st.subheader('Data Harga')
    st.write(data.tail())
    ##st.write(data)
    def plot_raw_data():
        fig = go.Figure()
        ##fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='stock_open'))
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='stock_close'))
        fig.layout.update(title_text="Data Harga Saham ", xaxis_rangeslider_visible=True, )
        st.plotly_chart(fig)
    plot_raw_data()

    ##Prediksi##
    df_train =data[['Date', 'Close']]
    df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

    daily_seasonality=True
    m = Prophet()
    m.fit(df_train)
    future = m.make_future_dataframe(periods=period)
    forecast = m.predict(future)
    st.subheader('Data Prediksi')
    st.write(forecast.tail())

    ##Chart Prediksi##
    st.subheader(' Prediksi Harga')
    fig1 = plot_plotly(m, forecast)
    st.plotly_chart(fig1)
    st.subheader('Komponen Prediksi')
    fig2 = m.plot_components(forecast)
    st.write(fig2)
    
    ##cross_validation##
    st.subheader('MAPE dan Tabel Cross Validation')
    df_cv = cross_validation(m, initial='730 days', period='180 days', horizon = '365 days')
    df_cv.head()
    fig3 = plot_cross_validation_metric(df_cv, metric='mape')
    ##fig4 = plot_cross_validation_metric(df_cv, metric='rmse')
    
    df_p = performance_metrics(df_cv)
    ##df_p.head()

    st.write(fig3)
    ##st.write(fig4)
    st.code(df_p)
    ##st.code(df_cv)