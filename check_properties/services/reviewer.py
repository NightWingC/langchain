import json
import os
from urllib.request import Request, urlopen

from llm.gemini import llm
from models.review_model import ReviewModel
from prompts.review_prompts import CHAT_PROMPT


def revisar_propiedad(propiedad: dict, tipo_operacion: str = "venta") -> ReviewModel:
	chain = CHAT_PROMPT | llm.with_structured_output(ReviewModel)
	informacion_inmueble = json.dumps(propiedad, ensure_ascii=False, indent=2)
	return chain.invoke({
		"tipo_operacion": tipo_operacion,
		"informacion_inmueble": informacion_inmueble,
	})


def construir_mensaje_revision(resultado: ReviewModel) -> str:
	mensaje_parts: list[str] = []

	if resultado.datos_faltantes:
		mensaje_parts.append(f"Datos Faltantes: {', '.join(resultado.datos_faltantes)}")

	if resultado.inconsistencias_detectadas:
		mensaje_parts.append(
			f"Inconsistencias: {', '.join(resultado.inconsistencias_detectadas)}"
		)

	if resultado.recomendacion:
		mensaje_parts.append(f"Recomendacion: {resultado.recomendacion}")

	return " | ".join(mensaje_parts) if mensaje_parts else "Sin observaciones"


