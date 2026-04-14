# LangChain Course Lab

Repositorio de practica para aprender LangChain paso a paso con ejemplos simples, patrones de prompts, runnables, output parsers y una mini aplicacion de analisis de CV con Streamlit.

## Que incluye este repo

- Seccion 1: fundamentos y primeros chats con OpenAI y Gemini.
- Seccion 2: plantillas de prompt, placeholders, runnables y parseo estructurado.
- cv_analyzer: app completa para evaluar CVs en PDF contra una descripcion de puesto.

## Stack principal

- Python 3.10+
- LangChain
- OpenAI API y Google Gemini API
- Streamlit
- Pydantic
- python-dotenv
- PyPDF2

## Estructura del proyecto

```text
.
├── cv_analyzer/
│   ├── app.py
│   ├── models/
│   ├── prompts/
│   ├── services/
│   └── ui/
├── section_1/
├── section_2/
├── section_3/
├── .env.example
└── README.md
```

## Configuracion rapida

1. Crea y activa un entorno virtual.

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Instala dependencias base.

```bash
pip install streamlit langchain langchain-core langchain-openai langchain-google-genai python-dotenv pydantic PyPDF2
```

3. Configura variables de entorno.

```bash
cp .env.example .env
```

Edita el archivo .env con tus claves:

```env
OPENAI_API_KEY=tu_api_key_openai
GOOGLE_API_KEY=tu_api_key_google
```

## Como ejecutar

### Ejemplos de la Seccion 1

```bash
python section_1/hello_world_openai.py
python section_1/hello_world_gemai.py
python section_1/hello_world_avanzado.py
streamlit run section_1/streamlit_chatbot.py
```

### Ejemplos de la Seccion 2

```bash
python section_2/prompt_templates.py
python section_2/chat_prompt_template.py
python section_2/example_runnables.py
python section_2/output_parsers.py
python section_2/output_parsers_example.py
python section_2/analisis_sentimientos.py
python section_2/Pydantic_output_parser.py
```

### Aplicacion CV Analyzer

```bash
streamlit run cv_analyzer/app.py
```

Despues abre la URL local que muestre Streamlit en la terminal.

## Notas importantes

- Si una API key no esta configurada, algunos scripts fallaran al iniciar.
- El modulo cv_analyzer espera CVs en PDF con texto extraible.

