import json
import os
from urllib.error import HTTPError, URLError

from dotenv import load_dotenv

from services.reviewer import obtener_propiedades_desde_endpoint, revisar_propiedad, aprobar_rechazar_propiedad


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


def normalizar_propiedad(propiedad: dict) -> dict:
	return {field: propiedad.get(field) for field in REQUIRED_FIELDS}


def main() -> None:
	load_dotenv()

	endpoint_url = os.getenv("ENDPOINT_URL")
	endpoint_token = os.getenv("ENDPOINT_TOKEN") or os.getenv("TOKEN_SECRET")

	if not endpoint_url:
		raise EnvironmentError("ENDPOINT_URL no está definida en el .env")

	try:
		propiedades = obtener_propiedades_desde_endpoint(
			endpoint_url=endpoint_url,
			token=endpoint_token,
		)
	except HTTPError as error:
		error_detail = error.read().decode("utf-8", errors="replace")
		raise SystemExit(
			f"Error HTTP {error.code}: {error.reason}\n"
			f"Detalle: {error_detail[:500]}"
		) from error
	except URLError as error:
		raise SystemExit(
			"No se pudo conectar al endpoint. "
			"Verifica URL, token y que el servicio este activo. "
			f"Detalle: {error.reason}"
		) from error
	except ValueError as error:
		raise SystemExit(f"Respuesta inesperada del endpoint: {error}") from error

	propiedades_normalizadas = [normalizar_propiedad(p) for p in propiedades]

	for propiedad in propiedades_normalizadas[:3]:
		# print(f"propiedad: {propiedad}")
		print(f"\n--- Revisando: {propiedad.get('title', propiedad.get('uuid', 'sin título'))} ---")
		resultado = revisar_propiedad(propiedad)
		print(json.dumps(resultado.model_dump(), ensure_ascii=False, indent=2))
		# aprobar_rechazar_propiedad(resultado.)



if __name__ == "__main__":
	main()
