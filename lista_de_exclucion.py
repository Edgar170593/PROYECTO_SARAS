import streamlit as st 




def inicio():

	st.info( 'La lista de exclusión es el primer filtro o actividad para desarrollarse y determinar la elegibilidad de un crédito para financiamiento, ya que incluye las actividades o sectores económicos que la institución financiera ha decidido no financiar debido a su riesgo e impacto socioambiental significativo (por ejemplo, producción y comercio de material radioactivo), y los riesgos o impactos socioambientales que la institución financiera no acepta (por ejemplo, afectación a bosques primarios)')
	st.header('Si la actividad económica del socio/a calza en alguna de las siguientes marcar con una "X", caso contrario marque el casillero 16.')
	
	columna1 , columna2 = st.columns(2)
	with columna1:
		st.write('Producción y comercio de cualquier proyecto o actividades considerada ilegal por la legislación nacional o convenios y tratados internacionales, tales como farmacéuticos, pesticida/herbicidas, substancias que agotan el ozono, compuestos de bifenilos policlorados (PCB, por sus siglas en inglés), animales y plantas silvestres o productos derivados de ellos reglamentados conforme a la CITES.')
	with columna2:
		pregunta1 = st.checkbox('Pregunta 1')

	columna3 , columna4 = st.columns(2)
	with columna3:
		st.write('Producción o comercio de armas y municiones.')
	with columna4:
		pregunta1 = st.checkbox('Pregunta 2')