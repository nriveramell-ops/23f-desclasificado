"""
modelado.py
===========

Módulo encargado del modelado de temas.

Responsabilidades:
    - Entrenar BERTopic sobre los documentos.
    - Entrenar LDA sobre los documentos.
    - Calcular métricas de coherencia (c_v) para ambos modelos.
    - Análisis de estabilidad: entrenar varias veces con parámetros distintos.
    - Asignar cada documento a su tema dominante.

Este módulo se rellena en la FASE 4 (modelado) y FASE 5 (estabilidad) del plan.
"""


def entrenar_bertopic(documentos: list[str], random_state: int = 42):
    """
    Entrena un modelo BERTopic sobre los documentos.

    Parámetros
    ----------
    documentos : list[str]
        Lista de textos preprocesados.
    random_state : int
        Semilla para reproducibilidad.

    Devuelve
    --------
    tuple
        (modelo_bertopic, topics, probs)
    """
    # TODO: implementar en Fase 4
    raise NotImplementedError("Se implementará en la Fase 4")


def entrenar_lda(documentos_tokenizados: list[list[str]], num_topics: int = 10):
    """
    Entrena un modelo LDA con gensim.

    Parámetros
    ----------
    documentos_tokenizados : list[list[str]]
        Lista de documentos, cada uno como lista de tokens.
    num_topics : int
        Número de temas a buscar.

    Devuelve
    --------
    tuple
        (modelo_lda, diccionario, corpus_bow)
    """
    # TODO: implementar en Fase 4
    raise NotImplementedError("Se implementará en la Fase 4")


def calcular_coherencia_cv(modelo, textos, diccionario):
    """
    Calcula la métrica de coherencia c_v para un modelo de topic modeling.

    Parámetros
    ----------
    modelo : LdaModel o similar
        El modelo entrenado.
    textos : list[list[str]]
        Documentos tokenizados (necesarios para c_v).
    diccionario : gensim.corpora.Dictionary
        Diccionario de gensim.

    Devuelve
    --------
    float
        Valor de coherencia c_v (entre 0 y 1; cuanto más alto, mejor).
    """
    # TODO: implementar en Fase 4
    raise NotImplementedError("Se implementará en la Fase 4")


def analisis_estabilidad(documentos, configuraciones: list[dict]):
    """
    Entrena BERTopic con diferentes configuraciones y compara los temas resultantes.

    Parámetros
    ----------
    documentos : list[str]
        Documentos preprocesados.
    configuraciones : list[dict]
        Lista de diccionarios con parámetros a probar.

    Devuelve
    --------
    pd.DataFrame
        Resumen comparativo de los modelos obtenidos.
    """
    # TODO: implementar en Fase 5
    raise NotImplementedError("Se implementará en la Fase 5")
