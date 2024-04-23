import streamlit as st

#이미지 처리를 위한 라이브러리
from PIL import Image


def main() :
    #1.저장되어있는 이미지 파일을 화면에 표시하는 방법
    img = Image.open('./data/image_03.jpg')

    st.image(img)

    st.image(img,width=500)

    st.image(img, use_column_width=True)
    #동영상 파일
    video_file=open('./data/video1.mp4','rb')
    st.video(video_file)

    #오디오 파일
    audio_file = open('./data/song.mp3','rb')
    st.audio(audio_file.read(), format='audio/mp3')

if __name__== '__main__':
    main()