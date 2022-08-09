# home.py
import streamlit as st

st.set_page_config(
    layout="wide",
    page_title="Waspada Penipuan Online",
)

st.sidebar.markdown("# Home")
st.sidebar.image('stealing.jpg')
st.markdown ("<h1 style='margin-bottom:30px;text-align:center;'> Penipuan Online di Indonesia dan Pencegahannya </h1>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([5,1,3])
with col1:
    st.write('<div style="text-align: justify;vertical-align:middle;margin-top:20px">Revolusi industri 4.0 dan pandemi COVID-19 mempercepat transisi digitalisasi. Di era serba digital sekarang ini, banyak aktifitas yang sebelumnya dilakukan secara manual bisa dilakukan secara online dan memberikan berbagai kemudahan. Namun ada juga pihak tidak bertanggung jawab melakukan hal yang dapat merugikan orang lain, mulai dari pemalsuan, penipuan terencana, pengatasnamaan dan juga yang paling sering terjadi adalah pencurian data. Terdapat beberapa modus penipuan online yang sering dilancarkan oleh pelaku kejahatan siber, diantaranya <em>scamming</em>, <em>phising</em>, dan <em>social engineering</em>.</div>', unsafe_allow_html=True)
with col2:
    st.write()
with col3:
    st.image('phising.png')

col1, col2= st.columns([3,4])
with col1:
    st.write('<p style="margin-top:30px;"> . </p>',unsafe_allow_html=True)
    st.image('Untitled.png')
with col2:
    st.markdown('<h3 style="margin-top:20px;"> Scamming </h3>',unsafe_allow_html=True)
    st.write('Penipuan terencana bertujuan untuk mendapatkan uang dari orang lain.')
    st.markdown('<h3> Phising </h3>',unsafe_allow_html=True)
    st.write('<p style="text-align:justify;"> Pelaku kejahatan menggunakan panggilan telepon, email atau pesan teks untuk mendapatkan data-data pribadi korban yang akan digunakan pada tindak kejahatan selanjutnya.</p>',unsafe_allow_html=True)
    st.markdown('<h3> Social Engineering </h3>',unsafe_allow_html=True)
    st.write('<p style="text-align:justify;">Pelaku memanipulasi psikologis korban hingga secara tak sadar memberikan informasi penting. Pelaku dapat mengambil kode OTP atau password karena sudah memahami perilaku korbannya.</p>',unsafe_allow_html=True)

col1, col2 = st.columns([5,4])
with col1:
    st.write('<div style="text-align: justify;vertical-align:middle;margin-top:40px">Meskipun bukan termasuk jenis peretasan keamanan sistem, ketiga kejahatan siber ini membuat pelaku bisa mengontrol akun milik korban. Menurut Head of IT Governance Risk and Compliance Information Security GoPay, Genesha Saputra, Ada tiga pilar di information security, yaitu people, process, technology. Diantara ketiga pilar ini, sudah diakui di seluruh dunia bahwa people merupakan weakest link atau rantai terlemah dari keamanan informasi. “Magis ini, atau manipulasi psikologis, memang hanya ada satu cara yang efektif, yaitu edukasi.”</div>', unsafe_allow_html=True)
with col2:
    st.image('two.png')

st.markdown('<h4 style="text-align:center;margin-top:30px;">Yuk, cari tahu data dan pencegahan penipuan online di website ini 🚀</h4>',unsafe_allow_html=True)
