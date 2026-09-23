
import streamlit as st
import requests

st.title("SuperKart Sales Forecasting")

st.write("Enter product and store details")

product_weight = st.number_input("Product Weight", value=12.66)
product_sugar_content = st.selectbox(
    "Product Sugar Content",
    ["Low Sugar", "Regular", "No Sugar"]
)

product_allocated_area = st.number_input(
    "Product Allocated Area",
    value=0.027
)

product_mrp = st.number_input(
    "Product MRP",
    value=117.08
)

store_size = st.selectbox(
    "Store Size",
    ["Small", "Medium", "High"]
)

store_city = st.selectbox(
    "Store Location City Type",
    ["Tier 1", "Tier 2", "Tier 3"]
)

store_type = st.selectbox(
    "Store Type",
    [
        "Departmental Store",
        "Supermarket Type1",
        "Supermarket Type2",
        "Food Mart"
    ]
)

product_id_char = st.text_input("Product Id Prefix", "FD")

store_age = st.number_input(
    "Store Age Years",
    value=16
)

product_type_category = st.text_input(
    "Product Type Category",
    "Non Perishables"
)

backend_url = st.text_input(
    "Backend URL",
    "http://backend:7860"
)

if st.button("Predict Sales"):

    payload = {
        "Product_Weight": product_weight,
        "Product_Sugar_Content": product_sugar_content,
        "Product_Allocated_Area": product_allocated_area,
        "Product_MRP": product_mrp,
        "Store_Size": store_size,
        "Store_Location_City_Type": store_city,
        "Store_Type": store_type,
        "Product_Id_char": product_id_char,
        "Store_Age_Years": store_age,
        "Product_Type_Category": product_type_category
    }

    response = requests.post(
        backend_url + "/v1/predict",
        json=payload
    )

    st.success(response.json())
