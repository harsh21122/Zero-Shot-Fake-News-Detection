
import json
import streamlit as st
from streamlit_lottie import st_lottie
from predict import predict
import base64


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
        unsafe_allow_html=True
    )


add_bg_from_local('joe-woods-4Zaq5xY5M_c-unsplash.jpg')


st.markdown("<h1 style='text-align: center; color: grey;'>ZERO-SHOT FAKE NEWS DETECTOR</h1>",
            unsafe_allow_html=True)
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")

title = st.text_input("Title", "")
content = st.text_area("Content", "")

st.markdown("\n")
btn = st.button("SUBMIT")

with open("75376-cross-mark-animarion.json", "r") as file:
    mark = json.load(file)

with open("142011-completed-tick.json", "r") as file:
    tick = json.load(file)

try:
    if btn:
        if title != "" and content != "":

            with st.spinner('Check in Progress ...'):
                verd1, verd2, verd3 = predict(title, content)

            st.markdown(f"<h3 style='text-align: center; color: grey;'> Similarity Score is : {verd3}!!!</h3>",
                        unsafe_allow_html=True)
            if verd3 >= 0.65:
                st.markdown("\n")
                st.success('Article  is Trustworthy!!!')

                st_lottie(tick,
                          reverse=True,
                          height=200,
                          width=200,
                          speed=0.8,
                          loop=True,
                          quality='high',
                          key='tick'
                          )

            else:
                st.markdown("\n")
                st.error('Article is not Trustworthy!!!')

                st_lottie(mark,
                          reverse=True,
                          height=200,
                          width=200,
                          speed=0.8,
                          loop=True,
                          quality='high',
                          key='mark'
                          )

        else:
            st.markdown("\n")
            st.markdown("<h3 style='text-align: center; color: grey;'>TITLE or CONTENT not given !!!</h3>",
                        unsafe_allow_html=True)

except Exception as e:

    print(e)
    st.markdown("\n")
    st.markdown("<h3 style='text-align: center; color: grey;'>Something went wrong !!!</h3>",
                unsafe_allow_html=True)
