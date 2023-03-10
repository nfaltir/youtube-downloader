import streamlit as st
import pandas as pd
from pytube import YouTube


#utils
import base64
from io import BytesIO

st.set_page_config(page_title="Youtube Downloader", page_icon="⭕️")
st.markdown("<h1 style='text-align: center; color: #FF0000; margin-bottom:50px; font-size: 4.5rem;'>Youtube <span style='text-align: center; color: #555;'>Downloader</span></h1>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

def main():
    link = st.text_input("Enter or paste youtube video link:")
    option = st.radio('select type of download', (
        'video',
        'audio'
    ))

    matches = ["audio", "video"]

    if st.button("download"):
        video_objects = YouTube(link)
        try:
            if option == "audio":
                video_objects.streams.get_audio_only().download("./audios")
                st.success("Audio successfully downloaded")
            elif option == "video":
                video_objects.streams.get_highest_resolution().download("./videos")
                st.success("Video successfully downloaded")
                
        except:
            st.error(f"there was a problem downloading the video!{KeyError}")
        

    st.markdown("<hr><br>", unsafe_allow_html=True)

    
if __name__ == '__main__':
    main()


