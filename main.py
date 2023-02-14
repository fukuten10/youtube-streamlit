import streamlit as st
import time
st.title('streamlit 超入門!!')

st.write('プログレスバーの表示')
'Start!!'


latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Itaration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.05)

'Done!!!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')




# text = st.text_input('あなたの趣味を教えてください。')
# st.write('あなたの趣味: ', text)
#
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# st.write('コンディション', condition)




if st.checkbox('Show Image'):
    img = Image.open('sample.jpg')
    st.image(img, caption='Sakana kun san', use_column_width=True)

