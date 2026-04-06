import PyPDF2
from io import BytesIO

def extraer_texto_pdf(archivo_pdf):
    try:
        pdf_reader = PyPDF2.PdfFileReader(BytesIO(archivo_pdf.read()))
        texto_completo = ""
        for nom_pagina, pagina in enumerate(pdf_reader, 1):
            texto_pagina = pagina.extract_text()
            if texto_pagina.stip():
                texto_completo += f"\n-- Página{nom_pagina} --\n"
                texto_completo += texto_pagina + "\n"
                
            
        texto_completo = texto_completo.strip()
        
        if not texto_completo:
            return "Error. El PDF no contiene texto extraíble. Asegúrate de que el PDF no sea una imagen escaneada."
        return texto_completo
    except Exception as e:
        return f"Error al procesar el PDF: {str(e)}"