'''
streamlit多页面程序的入口文件
'''
import streamlit as st

st.title("AI大模型应用产品网")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://haowallpaper.com/link/common/file/getCroppingImg/8cab28d6df91aa2475acf2c7d4e25a0f", use_column_width=True)
    flag = st.button("绘言", use_container_width=True)
    if flag:
        st.switch_page("pages/demo3.py")


with col2:
    st.image("https://haowallpaper.com/link/common/file/getCroppingImg/83b9bb7e36e0640f150b5a1ad49d316683b9bb7e36e0640f150b5a1ad49d3166", use_column_width=True)
    flag = st.button("绘图", use_container_width=True)
    if flag:
        st.switch_page("pages/textToimage.py")

with col3:
    st.image("https://haowallpaper.com/link/common/file/getCroppingImg/5b3b11f60ea2bbfa3063e6b4a3854e53", use_column_width=True)
    flag = st.button("岗位问答", use_container_width=True)
    if flag:
        st.switch_page("pages/job-ai.py")



# with col1:
#     flag = st.button("基础版")
#     if flag:
#         st.switch_page("pages/demo.py")
#
# with col2:
#     flag1 = st.button("进阶版")
#     if flag1:
#         st.switch_page("pages/demo1.py")
#
# with col3:
#     flag2 = st.button("最终版")
#     if flag2:
#         st.switch_page("pages/demo2.py")
# with col4:
#     flag3 = st.button("无敌版")
#     if flag3:
#         st.switch_page("pages/demo3.py")
# with col5:
#     flag4 = st.button("闻声图")
#     if flag4:
#         st.switch_page("pages/textToimage.py")