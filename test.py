import streamlit as st
import pandas as pd
from pytube import YouTube


#utils
import base64
from io import BytesIO

st.markdown("<h1 style='text-align: center; color: #FF0000; margin-bottom:50px; font-size: 4.5rem;'>Youtube <span style='text-align: center; color: #555;'>Downloader</span></h1>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

def main():
    link = st.text_input("Enter or paste youtube video link:")
    option = st.radio('select type of download', (
        'audio',
        'video'
    ))

    matches = ["audio", "video"]

    if st.button("download"):
        video_objects = YouTube(link)
        st.write("Title of video: " + str(video_objects.title))
        st.write("Number of views: " + str(video_objects.views))

        if option == "audio":
            video_objects.streams.get_audio_only().download()
        elif option == "video":
            video_objects.streams.get_highest_resolution().download()

    st.markdown("<hr><br>", unsafe_allow_html=True)

    
if __name__ == '__main__':
    main()


