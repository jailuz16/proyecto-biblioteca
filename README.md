![prueba1](https://github.com/user-attachments/assets/78aa1eb0-aad9-4ffb-91fe-35090c29eaac)
![prueba2](https://github.com/user-attachments/assets/61630698-8666-4cbc-8ca5-12330b1de8b2)
Análisis de Ventajas del Testing Top Down con Stubs

1. Detección temprana de errores
- Permite probar los módulos de alto nivel incluso si los módulos de bajo nivel aún no están implementados.
- Esto ayuda a encontrar problemas de integración de manera anticipada.

2. Validación progresiva del sistema
- Se puede comprobar el flujo principal de la aplicación paso a paso.
- Garantiza que la lógica de negocio principal funcione antes de integrar componentes reales.

3.Uso de stubs para simular dependencias
- Los stubs facilitan la simulación de respuestas esperadas (como autenticación o base de datos).
- Esto permite realizar pruebas rápidas y controladas sin necesidad de infraestructura compleja.

4. Facilita la planificación de desarrollo
- Los equipos pueden desarrollar y probar módulos de manera paralela.
- Mientras los programadores de bajo nivel terminan su código, los testers ya pueden validar las capas superiores.

5. Reducción de costos de corrección
- Al identificar problemas en fases tempranas, se evita que los errores se propaguen a etapas más avanzadas, donde corregirlos sería más costoso.

6. Mejora la cobertura de pruebas
- Permite generar diferentes escenarios (casos válidos, inválidos, límites) y verificar la robustez del sistema antes de usar bases de datos o servicios reales.
