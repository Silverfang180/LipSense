import streamlit as st
import os
import imageio
import tensorflow as tf
from utils import load_data, num_to_char
from modelutil import load_model


st.set_page_config(layout='wide')

with st.sidebar:
    st.image('https://i.ibb.co/hyzS251/Python-logo-that-is-fascinating-unique-attractive-cool-awesome-1.jpg')
    st.title("lipSense")
    st.info("This app is developed by Binary Alchemist")


st.title('LipSense Full Stack App') 
options = os.listdir(os.path.join('..', 'data', 's1'))
selected_video = st.selectbox('CHOOSE VIDEO', options)

 
col1, col2 = st.columns(2)

if options: 

    
    with col1: 
        st.info('The video ')
        file_path = os.path.join('..','data','s1', selected_video)
        os.system(f'ffmpeg -i {file_path} -vcodec libx264 test_video.mp4 -y')

       
        video = open('test_video.mp4', 'rb') 
        video_bytes = video.read() 
        st.video(video_bytes)

        
    
    with col2: 
            st.info('Animation')
            video, annotations = load_data(tf.convert_to_tensor(file_path))
            imageio.mimsave('animation.gif', video, fps=10)
            st.image('animation.gif', width=400) 

            
            st.info('Binary Output')
            model = load_model()
            yhat = model.predict(tf.expand_dims(video, axis=0))
            decoder = tf.keras.backend.ctc_decode(yhat, [75], greedy=True)[0][0].numpy()
            st.text(decoder)
            
            st.info('Decoded Output')
            converted_prediction = tf.strings.reduce_join(num_to_char(decoder)).numpy().decode('utf-8')
            st.text(converted_prediction)
        
           

