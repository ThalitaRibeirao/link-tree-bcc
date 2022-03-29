import streamlit as st



st.set_page_config(page_title = "LinkTree", page_icon=":link:", layout = 'wide')
style = "<style> footer {visibility: hidden;} </style>"
st.markdown(style, unsafe_allow_html=True)


st.title(':link: Link Tree BCC 52')
st.markdown('---')
l, r = st.columns(2)

l.header('Links Gerais')
l.markdown('[Grupo Whatsapp]("")')
l.header('Links do Curso')


r.header(':telephone_receiver: Contato dos Professores')
r.subheader('Nina Sumiko Tomita Hirata')
r.write("""
    - Disciplinas: Introdução à Computação (MAC 110);
    - Email:
""")

st.markdown('##')
r.subheader('Eloi Medina Galego')
r.write("""
    - Disciplinas: Cálculo Diferencial e Integral I (MAT 2453);
    - Email:
""")

st.markdown('##')
r.subheader('Junior Barrera')
r.write("""
    - Disciplinas: Álgebra Booleana e Aplicações no Projeto de Arquitetura de Computadores (MAC 329);
    - Email:
""")

st.markdown('##')
r.subheader('Mary Lilian Lourenco')
r.write("""
    - Disciplinas: Vetores e Geometria (MAT 112);
    - Email:
""")
r.caption('Obs: Prefira conversar pessoalmente.')

st.markdown('##')
r.subheader('Flavio Soares Correa da Silva')
r.write("""
    - Disciplinas: Integração na Universidade e na Profissão (MAC 101);
    - Email:
""")

st.markdown('##')
r.subheader('Lucas Calloi')
r.write("""
    - Disciplinas: Fundamentos da Matemática para a Computação (MAC 105);
    - Email:
""")
