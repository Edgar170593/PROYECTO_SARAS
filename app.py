#-------------------- Librerias ----------------------------------# 
import streamlit as st 





import home 
import solicitud_de_credito
import lista_de_exclucion








#-------------------- Personalizar la app ----------------------# 

st.title('Metodologia SARAS')




st.sidebar.title('Menú')


modulo = st.sidebar.selectbox('Seleccione', ['Home','Solicitud de crédito','Lista de exclución', 'Categorización del riesgo ambiental'])

if modulo == 'Home':

	home.inicio()

if modulo == 'Solicitud de crédito':

	solicitud_de_credito.inicio()

if modulo == 'Lista de exclución':

	lista_de_exclucion.inicio()
	

