# CAROL - Comprehensive Assessment & Reporting for Operational Learning 🛠️

CAROL (Comprehensive Assessment & Reporting for Operational Learning) es una plataforma avanzada de evaluación técnica diseñada específicamente para la industria del moldeo por inyección. Permite a las empresas diagnosticar con precisión el nivel de competencia de su personal operativo e ingeniería a través de assessments técnicos divididos por sectores de conocimiento.

## 🎯 ¿Qué significa CAROL?

El nombre representa los pilares fundamentales del proyecto:

- **Comprehensive (Integral)**: Evaluación total de 360°.
- **Assessment (Evaluación)**: Medición técnica rigurosa.
- **Reporting (Reporteo)**: Análisis de datos para la toma de decisiones.
- **Operational (Operativo)**: Enfocado en la realidad de la planta.
- **Learning (Aprendizaje)**: Orientado al crecimiento y capacitación constante.

## 🚀 Características Principales

- **Evaluación Multinivel**: Tres niveles de complejidad (Básico, Intermedio, Avanzado) adaptados a diferentes perfiles de puesto.
- **Análisis Sectorial**: Evaluación detallada en sectores clave del proceso de inyección.
- **Experiencia Personalizada**: Flujo de encuesta basado en el ID del empleado y la empresa (Multi-tenant).
- **Dashboards Interactivos**: Visualización de resultados en tiempo real mediante Square UI.
- **Seguimiento a Largo Plazo**: Monitoreo del crecimiento técnico en periodos de 6 a 12 meses.

## 📚 Módulos de Evaluación

Los assessments están disponibles en los siguientes niveles:

- **[Nivel Básico](questions/markdown/Basic_assesment.md)**: Evaluación para operadores de piso y personal de nuevo ingreso.
- **[Nivel Intermedio](questions/markdown/Medium_assesment.md)**: Evaluación para técnicos de procesos y ajustadores.
- **[Nivel Avanzado](questions/markdown/Advanced_assesment.md)**: Evaluación para ingenieros de procesos y gerentes.

## 🧠 Áreas Técnicas a Evaluar

El assessment analiza el desempeño en los siguientes sectores críticos del moldeo:

- **Seguridad y Operación**: Normativas de seguridad en máquina y procedimientos de arranque/paro.
- **Materiales Poliméricos**: Clasificación, secado, reología y comportamiento de los plásticos.
- **Moldes y Mecánica**: Anatomía del molde, sistemas de enfriamiento y mecanismos de expulsión.
- **Parámetros de Proceso**: Presiones, tiempos, temperaturas y perfiles de velocidad.
- **Hidráulica y Eléctrica**: Funcionamiento interno de la unidad de inyección y cierre.
- **Sistemas Periféricos**: Operación de robots, secadores, thermoladores y molinos.
- **Calidad y Defectología**: Identificación de defectos comunes y sus causas.
- **Eficiencia y Productividad**: OEE, SMED, tiempos de ciclo y métricas operativas.

## 🔧 Sistema Evaluador (n8n Workflow)

CAROL utiliza un sistema automatizado de evaluación construido con workflows de n8n que procesa las respuestas de las encuestas en tiempo real. El evaluador funciona de la siguiente manera:

- **Recepción de Datos**: Recibe respuestas de encuestas vía webhooks desde Formbricks inmediatamente después de que un empleado completa la evaluación.
- **Enrutamiento Automático**: Identifica el nivel de la encuesta (L0/L1/L2/L3) basado en el título y dirige los datos al flujo correspondiente.
- **Extracción de Información**: Procesa los datos incluyendo tiempos de respuesta, respuestas a preguntas y metadatos del empleado.
- **Almacenamiento Inmediato**: Guarda automáticamente los resultados en hojas de cálculo de Google Sheets, generando reportes en tiempo real sin intervención manual.
- **Seguridad Multi-tenant**: Soporta múltiples empresas con aislamiento de datos y encriptación.

Los resultados se generan y almacenan de forma inmediata, permitiendo análisis instantáneos del desempeño técnico.

## 🗺️ Roadmap

- **Corto Plazo**: Mejora del evaluador con análisis avanzados y reportes personalizados.
- **Mediano Plazo**: Desarrollo de un servidor dedicado para el despliegue de encuestas y generación automática de reportes usando los datos almacenados en Google Sheets. El servidor permitirá desplegar encuestas vía API/interfaz web, integrarse con Formbricks, y generar reportes dinámicos (PDFs, dashboards interactivos).