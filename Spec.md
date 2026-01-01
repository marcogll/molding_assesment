# CAROL - Assessment de Moldeo (Technical Specification)

## 1. Visión General

CAROL es una plataforma de evaluación técnica especializada para la industria del plástico/moldeo. Su propósito es cerrar la brecha de conocimiento técnico mediante diagnósticos precisos divididos por niveles (Básico, Intermedio, Avanzado) y sectores de conocimiento (procesos, materiales, periféricos, etc.).

## 2. Niveles de Evaluación (Core Logic)

| Nivel      | Preguntas | Sectores Evaluados | Objetivo                          |
|------------|-----------|--------------------|-----------------------------------|
| Básico     | 50        | 7-8                | Operadores y personal de nuevo ingreso. |
| Intermedio | 60        | 7-8                | Técnicos de procesos y ajustadores. |
| Avanzado   | 40        | 7-8                | Ingenieros de procesos y Gerentes. |

## 3. Stack Tecnológico (Propuesto)

- **Encuestas**: Formbricks (Open-source survey tool).
- **Visualización**: Square UI / Dashboards interactivos.
- **Base de Datos**: PostgreSQL (Para manejo de relaciones complejas: Empresa > Planta > Departamento > Empleado).
- **Backend**: Node.js / Python (Para el motor de calificación automática).
- **Despliegue**: Docker / Servidor Web dedicado.

## 4. Requerimientos Funcionales

### 4.1 Módulo de Usuario (Empleado)

- **Acceso por ID**: Validación de identidad mediante número de empleado único por planta.
- **Redirección Dinámica**: El sistema detecta el nivel asignado al empleado y lanza la encuesta correspondiente.
- **Persistencia**: Guardado parcial del progreso de la encuesta (opcional).

### 4.2 Módulo de Evaluación (Motor CAROL)

- **Calificación por Sectores**: El sistema no solo da un puntaje global, sino uno por cada uno de los 7-8 sectores técnicos.
- **Cálculo de Resultados**: Algoritmo para ponderar respuestas correctas/incorrectas.

### 4.3 Módulo de Administración (Empresa/Planta)

- **Multi-tenancy**: Aislamiento de datos. APTIV no puede ver los datos de otra empresa.
- **Dashboards de Grupo**: Comparativa de desempeño entre turnos o departamentos.
- **Reporte Individual**: Ficha técnica de cada empleado con sus áreas de oportunidad detectadas.

## 5. Arquitectura de Datos (Entidades)

- **Empresa**: (Nombre, Logo, Plantas).
- **Empleado**: (ID, Nombre, Planta, Departamento, Puesto).
- **Resultado**: (ID_Empleado, Fecha, Nivel, Puntaje_Global, Puntajes_Sectori...