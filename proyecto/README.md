# Proyecto ML: Evolución temporal de los temas en los documentos desclasificados del 23-F

Proyecto para la asignatura de Machine Learning del Máster, curso 2025-2026.

## Descripción del mini caso

Este proyecto analiza los documentos desclasificados relacionados con el intento de
golpe de Estado del 23 de febrero de 1981 (23-F), con el objetivo de identificar los
temas principales presentes en la documentación y estudiar cómo evolucionan a lo
largo del tiempo.

La pregunta central es: **¿cambia el foco temático de la documentación antes,
durante y después del intento de golpe de Estado?**

Para responderla, el proyecto se desarrolla en tres capas:

1. **Comparación de enfoques**: se aplican y comparan dos técnicas de topic modeling
   (BERTopic y LDA) para evaluar cuál produce temas más coherentes e interpretables.
2. **Análisis de estabilidad**: se modifican los parámetros de los modelos para
   comprobar que los temas identificados son robustos y no artefactos de una
   configuración concreta.
3. **Interpretación histórica**: se cruzan los temas detectados con eventos
   conocidos (dimisión de Suárez, el propio golpe, el juicio posterior) para
   evaluar si la evolución temática refleja la realidad histórica.

## Dataset

- **Fuente**: documentos desclasificados publicados por RTVE en
  https://www.rtve.es/noticias/23f-desclasificados/buscador-23f/
- **Formato**: 157 documentos individuales en JSON + 1 archivo de índice maestro
- **Campos por documento**: `fila_num`, `url`, `título`, `páginas`, `resumen`,
  `palabras_clave`, `transcripcion`

## Estructura del repositorio

```
proyecto_23f/
│
├── README.md              ← Este archivo
├── requirements.txt       ← Librerías necesarias
├── .gitignore             ← Archivos que Git ignora
│
├── data/
│   ├── raw/               ← 157 JSON originales + índice
│   └── processed/         ← Datos ya procesados (generados por el notebook)
│
├── notebooks/
│   └── 01_proyecto_23f.ipynb   ← Notebook principal (punto de entrada)
│
├── src/                   ← Módulos Python reutilizables
│   ├── carga_datos.py         ← Lectura de los JSON
│   ├── preprocesado.py        ← Limpieza y normalización del texto
│   ├── modelado.py            ← BERTopic y LDA
│   └── visualizacion.py       ← Gráficos
│
└── outputs/
    ├── figuras/               ← Gráficas generadas
    └── modelos/               ← Modelos entrenados guardados
```

## Cómo ejecutar el proyecto

### Opción A: Google Colab (recomendada)

1. Sube la carpeta `proyecto_23f/` completa a tu Google Drive.
2. Abre `notebooks/01_proyecto_23f.ipynb` en Colab.
3. Ejecuta la primera celda, que monta Google Drive y configura las rutas.
4. Ejecuta el resto de celdas en orden.

### Opción B: Entorno local

1. Clonar este repositorio.
2. Crear un entorno virtual e instalar dependencias:
   ```bash
   python -m venv venv
   source venv/bin/activate   # En Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Abrir `notebooks/01_proyecto_23f.ipynb` en Jupyter y ejecutar.

## Autor

Osiris — Máster en Data Science, curso 2025-2026.

## Licencia

Los documentos del dataset son de dominio público (desclasificados por el Gobierno
de España). El código del proyecto se publica con fines académicos.
