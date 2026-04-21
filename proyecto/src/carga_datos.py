"""
carga_datos.py
==============

Módulo encargado de leer los documentos JSON del dataset del 23-F y construir
un DataFrame de pandas con toda la información limpia y lista para análisis.

Responsabilidades:
    - Leer los 157 archivos JSON individuales de data/raw/.
    - Leer también el archivo _indice.json con los metadatos agregados.
    - Extraer la fecha del documento a partir del título (y, si falla,
      buscarla en las primeras líneas de la transcripción).
    - Detectar duplicados y documentos demasiado cortos.
    - Devolver un DataFrame con columnas bien definidas.

Este módulo se irá rellenando en la FASE 2 del plan (Análisis Exploratorio).
"""

from pathlib import Path
import json
import re
import pandas as pd


def cargar_indice(ruta_indice: Path) -> pd.DataFrame:
    """
    Carga el archivo _indice.json y devuelve un DataFrame.

    Parámetros
    ----------
    ruta_indice : Path
        Ruta al archivo _indice.json.

    Devuelve
    --------
    pd.DataFrame
        DataFrame con una fila por entrada del índice.
    """
    # TODO: implementar en Fase 2
    raise NotImplementedError("Se implementará en la Fase 2")


def cargar_documentos(carpeta_raw: Path) -> pd.DataFrame:
    """
    Carga todos los JSON individuales de una carpeta y los devuelve como DataFrame.

    Parámetros
    ----------
    carpeta_raw : Path
        Ruta a la carpeta que contiene los 157 JSON individuales.

    Devuelve
    --------
    pd.DataFrame
        DataFrame con columnas: id, titulo, paginas, resumen, palabras_clave,
        transcripcion, url, archivo_origen.
    """
    # TODO: implementar en Fase 2
    raise NotImplementedError("Se implementará en la Fase 2")


def extraer_fecha_de_titulo(titulo: str) -> pd.Timestamp | None:
    """
    Extrae una fecha del título de un documento.

    Busca patrones como "25 de febrero de 1982", "diciembre de 1981" o "1981".

    Parámetros
    ----------
    titulo : str
        Título del documento.

    Devuelve
    --------
    pd.Timestamp o None
        La fecha extraída, o None si no se encontró nada.
    """
    # TODO: implementar en Fase 2
    raise NotImplementedError("Se implementará en la Fase 2")
