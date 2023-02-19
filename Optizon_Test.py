import pandas as pd #for converting sheets to dataframe
import streamlit as st #for uploading to streamlit
import matplotlib.pyplot as plt #for plotting graphs
import numpy as np #for mathematical calulcations
import seaborn as sns #for plotting graphs

st.set_page_config(layout="wide")

st.title('Optizon Test')
st.header('Shoaib Mansoor')

#reading the TRACKER_V1, performed data cleaning on CSV file BEFORE ALREADY using PYTHON
df = pd.read_csv('Optizon_Test.csv')

with st.container():
    col1,col2=st.columns(2)
    with col1:
        #sorting keywords
        all_keywords= sorted(df['Keyword'].unique()) 
        #creating a selectbox for keywords
        selection1 = st.selectbox('Select Keyword',all_keywords)
        subset_selected_keyword=df[df['Keyword']==selection1]
        #first display block on left side
        col1.metric('Total Sales of the Selected Product Keyword USD ',subset_selected_keyword['Sales'].sum() )
        #click through rate calculation according to chosen keyword
        sumofsubset_selected_keyword=subset_selected_keyword['CTR'].sum()
        sumofsubset_selected_keyword=sumofsubset_selected_keyword.round(decimals=2)
        #Click through rate
        col1.metric('Total Click Through Rate', sumofsubset_selected_keyword)
        #calculation for ASIN conversion percentage
        ASales=subset_selected_keyword['A sales'].sum()
        Aclicks=subset_selected_keyword['A clicks'].sum()
        ACONV=ASales/Aclicks
        ACONV1=ACONV.round(decimals=2)
        #metric block for ASIN CONVERSION %
        col1.metric('ASIN CONVERSION PERCENTAGE', ACONV1*100)
        #havng issue with ASIN CTR calculation, hence dropping it for now
        #MarketIMP=subset_selected_keyword['ASIN Imp'].sum()
        #ASIN_CTR=Aclicks/MarketIMP
        #SIN_CTR1=ASIN_CTR.round(decimals=2)
        #col1.metric('ASIN CTR', ASIN_CTR1*100)
        orders=subset_selected_keyword['Orders'].sum()
        clicks=subset_selected_keyword['Clicks'].sum()
        Conversion=orders/clicks
        conversion1=Conversion.round(decimals=2)
        #metric for CONV PERCENTAGE, calculation above
        col1.metric('CONVERSION PERCENTAGE', conversion1*100)
        CTR=subset_selected_keyword['CTR'].sum()
        #CTR
        col1.metric('CTR', CTR)
        Spent=subset_selected_keyword['Spent'].sum()
        Sales=subset_selected_keyword['Sales'].sum()
        ADV_Cost=Spent/Sales
        ADV_Cost1=ADV_Cost.round(decimals=2)
        #ADV COST PERCENTAGE
        col1.metric('Advertisement Cost Percentage', ADV_Cost1*100)

    
    with col2:
        #sales in last 7 weeks of selected keyword
        st.header('Sales for last 7 weeks, Respects Keyword changes only, many things can be done!')
        sales_of_selected_kw= subset_selected_keyword.groupby('Week')['Sales'].sum().tail(7)
        plt.bar(sales_of_selected_kw.index,sales_of_selected_kw.values, color = ['Orange','Blue','Green', 'Red', 'Black'])
        plt.ylabel("Total sales amount in USD")
        st.set_option('deprecation.showPyplotGlobalUse', False)
        col2.pyplot()

with st.container():
    col1,col2=st.columns(2)
    #overall sales bar chart
    with col1:
        col1.header('Overall Sales of last 5 weeks, This is irrespective of selected keyword or week Refer below for week-wise analytics sample')
        sales_subset = df.groupby('Week')['Sales'].sum().tail(5)
        plt.bar(sales_subset.index,sales_subset.values, color = ['Yellow','Blue','Green', 'Red', 'Black'])
        plt.ylabel("amount in USD")
        st.set_option('deprecation.showPyplotGlobalUse', False)
        col1.pyplot()
    
    with col2:
        col2.header('just a sample pie chart, respects keyword selection')
        sales_pie= subset_selected_keyword.groupby(['Week'])['Sales'].sum().sort_values(ascending=False).head(5)
        fig = plt.pie(sales_pie, labels=sales_pie.index, autopct='%.2f')
        col2.pyplot()

with st.container():
    #enabling selection of week and data accordingly
    col1=st.columns(1)
    all_weeks=sorted(df['Week'].unique())
    selection=st.selectbox('Select Week', all_weeks)
    subset_selected_week=subset_selected_keyword[subset_selected_keyword['Week']==selection]

with st.container():
    col1,col2=st.columns(2)
    with col1:
        #very selective data, week wise and keyword wise
        col1.header('for this section, try selecting autism sensory toys and week1')
        st.header('Sales of selected product keyword by Selected Week')
        sales_product_subset=subset_selected_week.groupby('Week')['Sales'].sum()
        col1.metric('Respects BOTH keyword & week selection',subset_selected_week.groupby('Week')['Sales'].sum()  )
    
    with col2:
        #RANKING ON DAY1
        col2.header('tells you the rank for selected keyword on day1 of the selected week')
        rank=subset_selected_week.groupby('Keyword')['1'].sum()
        col2.table(rank)



        

    
    
    