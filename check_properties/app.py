from typing import Any

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from models.review_model import ReviewPropertyResponse

from services.reviewer import construir_mensaje_revision, revisar_propiedad


REQUIRED_FIELDS = [
	"uuid",
	"title",
	"type",
	"thumbnail",
	"totalArea",
	"buildArea",
	"status",
	"address",
	"state",
	"city",
	"brcStatus",
	"plan",
	"views",
	"shares",
	"inquiries",
	"currency",
	"priceUSD",
	"priceMXN",
	"priceJPY",
	"priceBTC",
	"galleries",
	"thumbnailUrl",
]


def normalizar_propiedad(propiedad: dict[str, Any]) -> dict[str, Any]:
	return {field: propiedad.get(field) for field in REQUIRED_FIELDS}


load_dotenv()

app = FastAPI(
	title="Check Properties API",
	description="Servicio para evaluar propiedades con LLM y devolver status + mensaje.",
	version="1.0.0",
)


@app.get("/health")
def health() -> dict[str, str]:
	return {"status": "ok"}


@app.post(
	"/review-property",
	responses={500: {"description": "Error interno al evaluar propiedad"}},
)
def review_property(
	payload: dict[str, Any],
	tipo_operacion: str = "venta",
) -> ReviewPropertyResponse:
	try:
		propiedad_normalizada = normalizar_propiedad(payload)
		resultado = revisar_propiedad(propiedad_normalizada, tipo_operacion)
		mensaje = construir_mensaje_revision(resultado)
		return ReviewPropertyResponse(
			status=resultado.veredicto_publicacion,
			mensaje=mensaje,
		)
	except Exception as error:
		raise HTTPException(status_code=500, detail=str(error)) from error


if __name__ == "__main__":
	import uvicorn

	uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
