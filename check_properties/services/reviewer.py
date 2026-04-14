import json
import logging
import os
from urllib.request import Request, urlopen

from dotenv import load_dotenv

from llm.gemini import llm
from models.review_model import ReviewModel
from prompts.review_prompts import CHAT_PROMPT

load_dotenv()

ENDPOINT_URL = os.getenv("ENDPOINT_URL")
DEFAULT_USER_AGENT = os.getenv(
	"ENDPOINT_USER_AGENT",
	(
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
		"AppleWebKit/537.36 (KHTML, like Gecko) "
		"Chrome/124.0.0.0 Safari/537.36"
	),
)

logging.basicConfig(level=logging.INFO)


if not ENDPOINT_URL:
    raise EnvironmentError("La variable de entorno ENDPOINT_URL no está definida en el archivo .env")


def obtener_propiedades_desde_endpoint(
	endpoint_url: str,
	token: str | None = None,
	timeout: int = 20,
) -> list[dict]:
	headers = {
		"Accept": "application/json",
		"User-Agent": DEFAULT_USER_AGENT,
	}
	if token:
		normalized_token = token.strip()
		if normalized_token.lower().startswith("bearer "):
			headers["Authorization"] = normalized_token
		else:
			headers["Authorization"] = f"Bearer {normalized_token}"

	request = Request(endpoint_url, headers=headers)

	with urlopen(request, timeout=timeout) as response:
		payload = response.read().decode("utf-8")

	data = json.loads(payload)
	if isinstance(data, list):
		return data
	if isinstance(data, dict) and isinstance(data.get("data"), list):
		return data["data"]
	if isinstance(data, dict) and isinstance(data.get("properties"), list):
		return data["properties"]
	if isinstance(data, dict) and isinstance(data.get("records"), list):
		return data["records"]

	raise ValueError("El endpoint no devolvió una lista de inmuebles válida")


def revisar_propiedad(propiedad: dict, tipo_operacion: str = "venta") -> ReviewModel:
	"""Envía la información de una propiedad al LLM y devuelve la revisión estructurada."""
	chain = CHAT_PROMPT | llm.with_structured_output(ReviewModel)
	informacion_inmueble = json.dumps(propiedad, ensure_ascii=False, indent=2)
	return chain.invoke({
		"tipo_operacion": tipo_operacion,
		"informacion_inmueble": informacion_inmueble,
	})

def aprobar_rechazar_propiedad():
	print("Hola")


