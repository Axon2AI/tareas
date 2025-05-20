# ADR-0001: Selección de GUI Toolkit

## Contexto
La aplicación requiere una UI de escritorio ligera y multiplataforma.

## Decisión
Se elige Tkinter para el MVP (incluido en stdlib) con opción de migrar a PySide6 para UI más avanzada.

## Consecuencias
- **Pros**: rápida integración y despliegue inicial.
- **Contras**: interfaz básica, limitada personalización.