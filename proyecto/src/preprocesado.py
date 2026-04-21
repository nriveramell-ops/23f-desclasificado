"""
preprocesado.py
===============

Módulo encargado de la limpieza y normalización del texto de los documentos.

Responsabilidades:
    - Limpieza básica: caracteres raros del OCR, espacios múltiples, saltos.
    - Minúsculas y normalización de acentos cuando proceda.
    - Eliminación de stopwords en español.
    - Lematización (para LDA).
    - Preparación de dos versiones del texto:
        * Versión "ligera": para BERTopic (los embeddings entienden contexto).
        * Versión "fuerte": para LDA (texto lematizado y sin stopwords).

Este módulo se irá rellenando en la FASE 3 del plan.
"""


def limpiar_ocr(texto: str) -> str:
    """
    Limpia artefactos típicos del OCR en los documentos.

    Incluye:
        - Caracteres no imprimibles.
        - Múltiples espacios y saltos de línea consecutivos.
        - Guiones de partición de palabras a final de línea.

    Parámetros
    ----------
    texto : str
        Texto original de la transcripción.

    Devuelve
    --------
    str
        Texto limpio.
    """
    # TODO: implementar en Fase 3
    raise NotImplementedError("Se implementará en la Fase 3")


def preparar_texto_bertopic(texto: str) -> str:
    """
    Prepara un texto para BERTopic (limpieza mínima, conserva contexto).

    Parámetros
    ----------
    texto : str
        Texto original.

    Devuelve
    --------
    str
        Texto listo para pasar a BERTopic.
    """
    # TODO: implementar en Fase 3
    raise NotImplementedError("Se implementará en la Fase 3")


def preparar_texto_lda(texto: str, nlp=None) -> list[str]:
    """
    Prepara un texto para LDA (tokenización, stopwords, lematización).

    Parámetros
    ----------
    texto : str
        Texto original.
    nlp : objeto de spaCy
        Modelo cargado de spaCy para español (es_core_news_sm).

    Devuelve
    --------
    list[str]
        Lista de tokens lematizados, sin stopwords.
    """
    # TODO: implementar en Fase 3
    raise NotImplementedError("Se implementará en la Fase 3")
