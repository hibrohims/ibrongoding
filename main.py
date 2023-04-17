#Library 

import streamlit as st

st.title('kamu siapa')
#inputnama
nama=st.text_input('masukkan nama')
st.write('namamu adalah', nama)

if st.button('cekicek'):
  st.write('semangat yaa',nama)
else:
  st.write('kamu siapa hei')
