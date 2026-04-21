"""
visualizacion.py
================

Módulo encargado de las visualizaciones del proyecto.

Responsabilidades:
    - Gráficos del análisis exploratorio (distribuciones temporales, longitudes).
    - Visualizaciones de los temas (BERTopic y LDA).
    - Evolución temporal de los temas (líneas / áreas apiladas).
    - Superposición con eventos históricos clave del 23-F.

Este módulo se usa a lo largo de todo el proyecto (Fases 2, 4 y 6).
"""

import matplotlib.pyplot as plt


# Eventos históricos clave para superponer en los gráficos temporales.
# Esta lista se usará en la Fase 6 al hacer la interpretación histórica.
EVENTOS_23F = [
    ("1981-01-29", "Dimisión de Adolfo Suárez"),
    ("1981-02-23", "Asalto al Congreso (23-F)"),
    ("1981-02-24", "Mensaje del Rey por TVE"),
    ("1982-02-19", "Inicio del juicio (Causa 2/81)"),
    ("1982-06-03", "Sentencia del Consejo Supremo"),
    ("1983-04-22", "Sentencia definitiva del Tribunal Supremo"),
]


def grafico_distribucion_temporal(df, columna_fecha="fecha", ruta_salida=None):
    """
    Gráfico de barras con el número de documentos por mes/año.

    Parámetros
    ----------
    df : pd.DataFrame
        DataFrame con una columna de fechas.
    columna_fecha : str
        Nombre de la columna con las fechas.
    ruta_salida : Path o None
        Si se proporciona, guarda la figura en esa ruta.
    """
    # TODO: implementar en Fase 2
    raise NotImplementedError("Se implementará en la Fase 2")


def grafico_longitud_documentos(df, ruta_salida=None):
    """
    Histograma de la longitud (en palabras) de los documentos.
    """
    # TODO: implementar en Fase 2
    raise NotImplementedError("Se implementará en la Fase 2")


def grafico_evolucion_temas(df_temas_tiempo, eventos=None, ruta_salida=None):
    """
    Gráfico de líneas con la evolución de cada tema a lo largo del tiempo,
    opcionalmente superpuesto con eventos históricos.
    """
    # TODO: implementar en Fase 6
    raise NotImplementedError("Se implementará en la Fase 6")
