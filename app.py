from pytube import YouTube
import streamlit as st
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

st.markdown("<h1 style='text-align: center; color: #FF0000; margin-bottom:50px; font-size: 4.5rem;'>Youtube <span style='text-align: center; color: #555;'>Downloader</span></h1>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)



form = st.form("DOwnload", clear_on_submit=True)
with form:
    st.markdown("<p style='margin-bottom: -50px; text-align: start; font-size: 1.5rem;'>Enter or Paste youtube video link:</p>", unsafe_allow_html=True)
    link = st.text_input("")
    st.markdown("<br>", unsafe_allow_html=True)
submit = form.form_submit_button("Download")


if len(link) > 1:
    def Download(link):
        youtubeObject = YouTube(link)
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        try:
            youtubeObject.download()
        except:
            st.warning(f"Error downloading video")
        st.success(f"\nDownload was successful!\n")



    Download(link)






