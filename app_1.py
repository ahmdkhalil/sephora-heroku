import pandas as pd
import numpy as np
import streamlit as st


# Load Our Dataset
st.title('Product Recommendation App 1')
df = pd.read_csv("../dataset/skindataall.csv")

st.sidebar.header('User Input Parameters')

skin_tone = st.sidebar.selectbox('Skin Tone',
('Dark', 'Deep', 'Ebony', 'Fair', 'Light', 'Medium', 'Olive', 'Porcelain', 'Tan'))
skin_type = st.sidebar.selectbox('Skin Type',
('Combination', 'Dry', 'Normal', 'Oily'))
eye_color = st.sidebar.selectbox('Eye Color',
('Blue', 'Brown', 'Grey', 'Green', 'Hazel'))
hair_color = st.sidebar.selectbox('Hair Color',
('Auburn', 'Black', 'Blonde', 'Brunette', 'Grey', 'Red'))
data = {'Skin Tone': skin_tone,
        'Skin Type': skin_type,
        'Eye Color': eye_color,
        'Hair Color': hair_color,
        }
df_user = pd.DataFrame(data, index=[0])
st.subheader("User Input Parameters")
st.write(df_user)

def recommend_products_by_user_features(skintone, skintype, eyecolor, haircolor, percentile=0.85):
    ddf = df[(df['Skin_Tone'] == skintone) & (df['Hair_Color'] == haircolor) & (df['Skin_Type'] == skintype) & (df['Eye_Color'] == eyecolor)]

    recommendations = ddf[(ddf['Rating_Stars'].notnull())][['Rating_Stars', 'Product_Url', 'Product', 'Price']]
    recommendations = recommendations.sort_values('Rating_Stars', ascending=False).head(10)

    if recommendations is not None:
        st.write('Based on your features, these are the top products for you:')
    else:
        results= "Not Found"
        st.warning(results)

    return recommendations

rec_prod = recommend_products_by_user_features(
skin_tone, skin_type,
eye_color, hair_color)
st.write(rec_prod[['Rating_Stars', 'Product', 'Product_Url', 'Price']])
