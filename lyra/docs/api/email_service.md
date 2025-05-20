# EmailService API

> Especificación del servicio de correo.

### send_draft(prompt: str) -> dict
Genera y envía un borrador basado en un prompt.

**Params**:
- `prompt` (str): descripción del cuerpo del correo.

**Returns**:
- `dict` con `to`, `subject`, `body`.