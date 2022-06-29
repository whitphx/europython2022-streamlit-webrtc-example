import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import cv2

th1 = st.slider("Threshold1", 0, 1000, 100)
th2 = st.slider("Threshold2", 0, 1000, 200)

def callback(frame: av.VideoFrame) -> av.VideoFrame:
    img = frame.to_ndarray(format="bgr24")

    img = cv2.Canny(img, th1, th2)
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    return av.VideoFrame.from_ndarray(img, format="bgr24")

webrtc_streamer(
    key="sample",
    video_frame_callback=callback,
    rtc_configuration={  # Add this config
        "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
    }
)
