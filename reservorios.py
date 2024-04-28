import pandas as pd
import PIL
import os
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import requests

# La ruta del archivo CSV en tu máquina local
csv_file_path = "https://raw.githubusercontent.com/VictorSabrera/Reservorios/main/lote_vii.csv"

# Carga el archivo CSV
df = pd.read_csv(csv_file_path)
#df.columns = df.columns.str.strip()
#st.write("Columnas después de limpiar:", df.columns.tolist())


logo_url = "https://raw.githubusercontent.com/VictorSabrera/Reservorios/main/OLYMPIC.jpeg"

# Send a GET request to the image URL
response = requests.get(logo_url)
from PIL import Image
from io import BytesIO
import requests
# Check if the request was successful
if response.status_code == 200:
    # Open the image using BytesIO, which converts the response content into a file-like object
    img = Image.open(BytesIO(response.content))
    # Display the image in the Streamlit sidebar
    st.sidebar.image(img, use_column_width=True)
else:
    st.error("Failed to retrieve the image.")
# Secciones para la barra lateral con botones de radio
section = st.sidebar.radio("Seleccione la sección", 
                           ('Reservas diciembre 2023', 'Lote XIII - Sección A', 'Lote XIII - Sección B', 'Lote VII'))

# Crear contenedores para cada sección
container_reservas = st.container()
container_lote_13a = st.container()
container_lote_13b = st.container()
container_lote_7 = st.container()

# Mostrar la visualización basada en la sección seleccionada
if section == 'Reservas diciembre 2023':
    with container_reservas:
        st.header("Reservas al 31 de diciembre del 2023 - Activos Olympic")
        
        # Aquí puedes añadir el código para la visualización de las Reservas
        
        import pandas as pd
        import matplotlib.pyplot as plt
        import streamlit as st
        
        # Datos extraídos de la imagen
        data = {
            'Lote': ['XIII-A (MSTB)', 'XIII-B (BCF)', 'VII (MSTB)'],
            '1P': [1115, 116, 11996],
            '2P': [1320, 134, 11996],
            '3P': [1401, 150, 11996]
        }
        
        # Convertir datos a DataFrame
        df = pd.DataFrame(data)
        df.set_index('Lote', inplace=True)
        
        # Colores para las categorías
        category_colors = {
            '1P': 'darkgreen',
            '2P': 'red',
            '3P': 'lightgreen'
        }
        
        # Crear un gráfico de barras para cada lote
        for index, row in df.iterrows():
            fig, ax = plt.subplots()
            # Crear las barras para cada categoría
            for i, (col, color) in enumerate(category_colors.items()):
                ax.bar(i, row[col], color=color, label=col, zorder=3)
        
            # Etiquetas y títulos
            ax.set_title(f'Resumen de Reservas - {index}')
            ax.set_xticks(range(len(category_colors)))
            ax.set_xticklabels(category_colors.keys())
            ax.set_ylabel('Volumen')
            
            # Cuadrícula en el eje y detrás de las barras (zorder=0)
            ax.grid(True, which='both', axis='y', zorder=0)
        
            # Añadir etiquetas de valor en la parte superior de las barras
            for i, (col, color) in enumerate(category_colors.items()):
                ax.text(i, row[col], f'{row[col]:,.0f}', ha='center', va='bottom')
        
            # Muestra el gráfico en Streamlit
            st.pyplot(fig)




elif section == 'Lote XIII - Sección A':
    with container_lote_13a:
        st.header("Visualización para Lote XIII - Sección A")
        # Aquí puedes añadir el código para la visualización del Lote XIII - Sección A

elif section == 'Lote XIII - Sección B':
    with container_lote_13b:
        st.header("Visualización para Lote XIII - Sección B")
        # Aquí puedes añadir el código para la visualización del Lote XIII - Sección B

elif section == 'Lote VII':
    with container_lote_7:
        st.header("Lote VII - Información del Pozo")

        # Lista desplegable con autocompletado para la selección o entrada del pozo
    selected_pozo = st.selectbox(
        "Seleccione o escriba el número de pozo",
        options=df["Pozo"].astype(str).unique(),  # Convierte los números a strings para el input
        format_func=lambda x: f"Pozo {x}"  # Formatea la presentación del número de pozo
    )

    # Filtrar los datos para el pozo seleccionado
    pozo_data = df[df["Pozo"].astype(str) == selected_pozo]

    # Verificar si se encontraron datos para el pozo seleccionado
    if not pozo_data.empty:
        pozo_data = pozo_data.iloc[0]  # Obtener la primera fila de los datos filtrados

        # Mostrar la información en cuadros para los primeros cuatro campos
        st.info(f"Yacimiento: {pozo_data.get('YACIMIENTO', 'No disponible')}")
        st.info(f"Zona: {pozo_data.get('ZONA', 'No disponible')}")
        st.info(f"Status 2024: {pozo_data.get('STATUS2024', 'No disponible')}")
        st.info(f"Petroleo (bopd): {pozo_data.get('Petroleo(bopd)', 'No disponible')}")

        # Crear un gráfico de barras para los campos de producción acumulada
        prod_fields = ['Cum Parinas(MSTB)', 'Cum Verdun (MSTB)', 'Cum Mogollon (MSTB)', 'Cum Talara(MSTB)']
        short_names = ['Parinas', 'Verdun', 'Mogollon', 'Talara']  # Nombres simplificados para el gráfico
        prod_values = [pozo_data.get(field, 0) for field in prod_fields]

        fig, ax = plt.subplots()
        bars = ax.bar(short_names, prod_values, color='skyblue')
        ax.set_ylabel('Producción Acumulada (MSTB)')
        ax.set_title('Producción Acumulada por Campo')

        # Añadir etiquetas de valor en negrita en la parte superior de cada barra
        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, yval, f'{yval:,.2f}', ha='center', va='bottom', fontweight='bold')

        # Mostrar el gráfico en Streamlit
        st.pyplot(fig)
    else:
        st.error("No se encontraron datos para el pozo seleccionado.")
        
        
        
        
        
        
        
        
        
        
