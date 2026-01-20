# Formbricks Survey Requirements - API v1

## Overview

Este documento es la **guía definitiva** para crear encuestas en Formbricks utilizando la API REST para las evaluaciones técnicas de moldeo por inyección. Incluye todos los requisitos de formato, ejemplos completos y solución de problemas comunes.

## Instalación y Configuración

- **Idioma**: NO multiidioma. Todos los contenidos se proporcionan en español únicamente.
- **Versión API**: v1 (compatible con Formbricks actual)
- **Formato Requerido**: Todos los campos de texto DEBEN usar formato objeto `{"default": "texto"}`, no strings directos.

## Variables de Entorno Requeridas

```env
FORMBRICKS_BASEURL=https://app.formbricks.com
FORMBRICKS_API_KEY=tu-api-key
FORMBRICKS_ENVIRONMENT_ID=tu-environment-id
```

## API Endpoints

### Crear Encuesta (Create Survey)

```
POST https://{baseurl}/api/v1/management/surveys
```

**Headers:**
- `Content-Type: application/json`
- `x-api-key: <API_KEY>`

**Respuesta Éxito**: 200 OK con datos de la encuesta creada
**Respuesta Error**: 400 Bad Request si campos mal formateados

### Actualizar Encuesta (Update Survey)

```
PUT https://{baseurl}/api/v1/management/surveys/{surveyId}
```

**Headers:**
- `Content-Type: application/json`
- `x-api-key: <API_KEY>`

### Obtener Encuesta (Get Survey)

```
GET https://{baseurl}/api/v1/management/surveys/{surveyId}
```

**Headers:**
- `x-api-key: <API_KEY>`

## Estructura del Payload

### Campos Principales

| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `environmentId` | string | Sí | ID del entorno de Formbricks |
| `name` | string | Sí | Nombre de la encuesta |
| `status` | enum | Sí | `draft`, `inProgress`, `paused`, `completed` |
| `type` | enum | Sí | `link`, `app` |
| `displayOption` | enum | No | `displayOnce`, `displayMultiple`, `respondMultiple`, `displaySome` |
| `questions` | array | Sí | Array de preguntas (ver formato abajo) |
| `welcomeCard` | object | No | Tarjeta de bienvenida (ver formato abajo) |
| `endings` | array | No | Pantallas de finalización (ver formato abajo) |
| `languages` | array | Sí | Array vacío `[]` (no multiidioma) |

### ⚠️ REQUISITO CRÍTICO: Formato de Texto

**TODOS** los campos de texto deben usar el formato objeto, NO strings directos:

```json
// ✅ CORRECTO
"headline": {"default": "Texto de la pregunta"}

// ❌ INCORRECTO
"headline": "Texto de la pregunta"
```

Campos afectados: `headline`, `subheader`, `buttonLabel`, `backButtonLabel`, `placeholder`, `label`, `html`

### Welcome Card

```json
{
  "welcomeCard": {
    "enabled": true,
    "headline": {
      "default": "Evaluación Técnica de Moldeo"
    },
    "html": {
      "default": "<b>Nivel Básico</b><br>Prueba de conocimientos fundamentales.<br><br>• Preguntas: 51<br>• Tiempo estimado: 45 min"
    },
    "buttonLabel": {
      "default": "Siguiente"
    },
    "showResponseCount": false,
    "timeToFinish": false
  }
}
```

**IMPORTANTE**: TODOS los campos de texto (`headline`, `html`, `buttonLabel`) DEBEN ser objetos con un campo `default`.

### Ending Card

```json
{
  "endings": [
    {
      "id": "p73t62dgwq0cvmtt6ug0hmfc",
      "type": "endScreen",
      "headline": {
        "default": "¡Gracias!"
      },
      "subheader": {
        "default": "Tu evaluación ha sido enviada correctamente."
      },
      "buttonLabel": {
        "default": "Completar"
      },
      "buttonLink": "https://example.com"
    }
  ]
}
```

**Nota**: Los campos `headline`, `subheader`, `buttonLabel` usan formato objeto.

## Mapeo de Preguntas

### Estructura General

Las preguntas del JSON original se mapean a Formbricks. **TODOS los campos de texto requieren formato objeto**.

| Campo Original | Campo Formbricks | Formato Requerido | Notas |
|----------------|------------------|-------------------|--------|
| `id` | `id` | string | ID único de la pregunta |
| `question` | `headline` | `{"default": "texto"}` | Texto principal de la pregunta |
| `description` | `subheader` | `{"default": "texto"}` | Contexto adicional |
| `type` | `type` | string | Mapeado a tipos de Formbricks |
| `required` | `required` | boolean | Campo obligatorio |
| `options` | `choices` | array de objetos | Opciones con `label: {"default": "texto"}` |

**CRÍTICO**: Los campos `headline`, `subheader`, `buttonLabel`, `backButtonLabel`, `placeholder`, `label` (en choices) DEBEN usar formato objeto.

### Tipos de Preguntas

#### 1. Texto Abierto (openText)

```json
{
  "id": "employee_number",
  "type": "openText",
  "inputType": "text",
  "headline": {
    "default": "Número de empleado"
  },
  "subheader": {
    "default": ""
  },
  "required": true,
  "placeholder": {
    "default": "Ingresa tu número de empleado"
  },
  "buttonLabel": {
    "default": "Siguiente"
  },
  "backButtonLabel": {
    "default": "Anterior"
  }
}
```

**Nota**: Todos los campos de texto usan formato objeto.

#### 2. Selección Múltiple Única (multipleChoiceSingle)

```json
{
  "id": "mach_1",
  "type": "multipleChoiceSingle",
  "headline": {
    "default": "¿Cuál es el componente que gira para transportar el material?"
  },
  "subheader": {
    "default": "La unidad de plastificación consta de varios elementos clave para procesar el material."
  },
  "required": true,
  "choices": [
    {
      "id": "c0",
      "label": {
        "default": "El barril reforzado (cilindro)"
      }
    },
    {
      "id": "c1",
      "label": {
        "default": "El tornillo (husillo)"
      }
    }
  ],
  "buttonLabel": {
    "default": "Siguiente"
  },
  "backButtonLabel": {
    "default": "Anterior"
  },
  "shuffleOption": "none"
}
```

#### 3. Selección Múltiple (multipleChoiceMulti)

```json
{
  "id": "qual_1",
  "type": "multipleChoiceMulti",
  "headline": {
    "default": "¿Qué defectos pueden ocurrir en el proceso?"
  },
  "subheader": {
    "default": "Selecciona todas las opciones aplicables."
  },
  "required": true,
  "choices": [
    {
      "id": "c0",
      "label": {
        "default": "Tiro Corto"
      }
    },
    {
      "id": "c1",
      "label": {
        "default": "Rebaba"
      }
    }
  ],
  "buttonLabel": {
    "default": "Siguiente"
  },
  "backButtonLabel": {
    "default": "Anterior"
  },
  "shuffleOption": "none"
}
```

## Ejemplo Completo de Payload

```json
{
  "environmentId": "clygwxsbh01v5aga1sdien2th",
  "name": "Evaluación Técnica de Moldeo - Nivel Básico",
  "type": "link",
  "status": "draft",
  "displayOption": "displayOnce",
  "welcomeCard": {
    "enabled": true,
    "headline": {
      "default": "Evaluación Técnica de Moldeo"
    },
    "html": "<b>Nivel Básico</b><br>Prueba de conocimientos fundamentales sobre maquinaria, proceso, calidad y seguridad.<br><br>• Preguntas: 51<br>• Tiempo estimado: 45 min",
    "buttonLabel": {
      "default": "Siguiente"
    },
    "showResponseCount": false,
    "timeToFinish": false
  },
  "questions": [
    {
      "id": "employee_number",
      "type": "openText",
      "headline": {
        "default": "Número de empleado"
      },
      "subheader": "",
      "required": true,
      "inputType": "text",
      "placeholder": {
        "default": "Ingresa tu número de empleado"
      },
      "buttonLabel": {
        "default": "Siguiente"
      },
      "backButtonLabel": {
        "default": "Anterior"
      }
    },
    {
      "id": "mach_1",
      "type": "multipleChoiceSingle",
      "headline": {
        "default": "En el sistema de plastificación, ¿cuál es el componente que gira para cizallar, fundir y transportar el material hacia adelante?"
      },
      "subheader": "La unidad de plastificación consta de varios elementos clave para procesar el material.",
      "required": true,
      "choices": [
        {
          "id": "c0",
          "label": {
            "default": "El barril reforzado (cilindro)"
          }
        },
        {
          "id": "c1",
          "label": {
            "default": "El tornillo (husillo)"
          }
        },
        {
          "id": "c2",
          "label": {
            "default": "La válvula check (anillo)"
          }
        },
        {
          "id": "c3",
          "label": {
            "default": "La banda calefactora cerámica"
          }
        }
      ],
      "buttonLabel": {
        "default": "Siguiente"
      },
      "backButtonLabel": {
        "default": "Anterior"
      },
      "shuffleOption": "none"
    }
  ],
  "endings": [
    {
      "id": "p73t62dgwq0cvmtt6ug0hmfc",
      "type": "endScreen",
      "headline": {
        "default": "¡Gracias!"
      },
      "subheader": {
        "default": "Tu evaluación ha sido enviada correctamente."
      },
      "buttonLabel": {
        "default": "Completar"
      },
      "buttonLink": "https://example.com"
    }
  ]
}
```

## Mapeo de Tipos de Preguntas

| Tipo Original | Tipo Formbricks | Descripción |
|--------------|-----------------|-------------|
| N/A (texto abierto) | `openText` | Campo de texto libre |
| Opción única | `multipleChoiceSingle` | Una sola respuesta |
| Múltiples opciones | `multipleChoiceMulti` | Selección múltiple |

## Reglas de Validación

1. **IDs Únicos**: Cada pregunta debe tener un ID único
2. **Choices IDs**: Cada opción debe tener un ID único (ej. `c0`, `c1`, `c2`, `c3`)
3. **Required**: Las preguntas marcadas como requeridas deben tener `required: true`
4. **No Multiidioma**: El campo `languages` debe ser un array vacío `[]`
5. **Formato de Objetos CRÍTICO**: TODOS los campos de texto DEBEN usar `{"default": "texto"}`
   - `headline`, `subheader`, `buttonLabel`, `backButtonLabel`, `placeholder`, `label`, `html`
   - Error 400 si se usa string directo

### Conversión Automática

Usa el script `formbricks_assitant.py` que automáticamente convierte strings a objetos. Los JSON fuente pueden mantener strings para legibilidad, la conversión ocurre en runtime.

## Campos Opcionales

### shuffleOption

Controla si las opciones se muestran en orden aleatorio:
- `none`: Orden original
- `random`: Orden aleatorio

### displayLimit

Número máximo de veces que se puede mostrar la encuesta.

### delay

Retraso en segundos antes de mostrar la encuesta.

## Configuración de Entorno

Las variables de entorno requeridas están en el archivo `.env`:

```env
FORMBRICKS_BASEURL=https://app.formbricks.com
FORMBRICKS_API_KEY=tu-api-key
FORMBRICKS_ENVIRONMENT_ID=tu-environment-id
```

## Ejemplo de cURL

```bash
curl --request POST \
  --url https://app.formbricks.com/api/v1/management/surveys \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: YOUR_API_KEY' \
  --data @survey_payload.json
```

## Estructura de Archivos y Scripts

### Archivos JSON
Los archivos generados para Formbricks tienen esta estructura:

```
formbricks/
├── .env                           # Variables de entorno
├── Form_requirements.md            # Este documento (guía definitiva)
├── assessment_conv.py              # Script conversor JSON a Formbricks
├── formbricks_assitant.py          # Script de creación de encuestas (con conversión automática)
├── convert_json.py                 # Utilidad de conversión de archivos JSON
├── funnel_registration_formbricks.json   # Nivel 0
├── basic_v2_formbricks.json       # Nivel 1 (57 preguntas)
├── medium_v2_formbricks.json      # Nivel 2 (60 preguntas)
└── advanced_v2_formbricks.json    # Nivel 3 (43 preguntas)
```

### Scripts Disponibles

#### `formbricks_assitant.py` (Principal)
Crea encuestas en Formbricks con conversión automática de formato:
```bash
cd /home/marco/Work/Carol/questions/formbricks
python3 formbricks_assitant.py
```

#### `assessment_conv.py` (Conversor)
Convierte archivos JSON originales a Formbricks:
```bash
cd /home/marco/Work/Carol/questions
python3 assessment_conv.py
```

#### `convert_json.py` (Utilidad)
Convierte archivos JSON existentes al formato API-compliant:
```bash
cd /home/marco/Work/Carol
python3 questions/formbricks/convert_json.py
```

## Referencias

- [Documentación API REST de Formbricks](https://formbricks.com/docs/api-reference/rest-api)
- [API Reference - Survey](https://formbricks.com/docs/api-reference/management-api--survey/)

## Errores Comunes de la API

### Error 400: "Fields are missing or incorrectly formatted"

Este error ocurre cuando los campos de texto no tienen el formato correcto de objeto.

**Causa común**: Usar string directo en lugar de objeto para cualquier campo de texto.

**Incorrecto**:
```json
{
  "headline": "Evaluación Técnica",
  "buttonLabel": "Siguiente"
}
```

**Correcto**:
```json
{
  "headline": {"default": "Evaluación Técnica"},
  "buttonLabel": {"default": "Siguiente"}
}
```

### Errores típicos de validación:
- `welcomeCard.headline: Expected object, received string`
- `questions[0].headline: Expected object, received string`
- `questions[0].choices[0].label: Expected object, received string`

### Solución
Ejecuta el script `formbricks_assitant.py` - maneja automáticamente la conversión de formato.

## Carga y Visualización de Encuestas

Para responder a consultas sobre Formbricks, es importante distinguir entre obtener los datos (API) y mostrar la encuesta (Renderizado).

### ¿Cuál es la forma correcta de cargar encuestas?

Aunque mencionas la REST API, la forma estándar y recomendada para cargar encuestas en una aplicación web no es llamando manualmente a los endpoints REST, sino utilizando el SDK de Formbricks (@formbricks/js).

El SDK se encarga automáticamente de llamar a la API correcta (Client API), verificar si el usuario debe ver una encuesta (basado en triggers) y renderizar la interfaz.

**Código de inicialización estándar (SDK):**

```javascript
import formbricks from "@formbricks/js";

if (typeof window !== "undefined") {
  formbricks.init({
    environmentId: "TU_ENV_ID",
    apiHost: "https://app.formbricks.com", // O tu propia URL si usas self-hosting
    userId: "ID_DEL_USUARIO", // Opcional: para identificar al usuario
  });
}
```

Si realmente necesitas usar la REST API manual:
Si tu caso de uso es muy personalizado (ej. un backend propio que sirve encuestas), tendrías que llamar al endpoint de Displays para saber qué encuesta mostrar:

- **Endpoint**: POST /api/v1/client/displays
- **Respuesta**: Te devuelve el objeto de la encuesta (preguntas, lógica y estilos).

**Desventaja**: Tendrás que construir tú mismo todo el HTML y la lógica del formulario basándote en ese JSON.

### ¿Es posible definir el color principal y usar otros backgrounds?

Sí, es totalmente posible. Tienes dos caminos principales para lograrlo:

**Opción A: Sobrescribir estilos vía CSS (Recomendado para desarrolladores)**

Esta es la forma más flexible si usas el SDK. Formbricks utiliza variables CSS que puedes redefinir en tu hoja de estilos global (globals.css o similar) para forzar tus colores y fondos sin importar lo que diga la configuración de la encuesta.

Añade esto a tu CSS:

```css
:root {
  /* Color principal (botones, bordes activos, etc.) */
  --fb-brand-color: #ff5733;

  /* Color del texto sobre el color principal */
  --fb-brand-text-color: #ffffff;

  /* Fondo de la tarjeta de la encuesta */
  --fb-card-bg: #ffffff;

  /* Fondo general (detrás de la tarjeta en encuestas de enlace o modales) */
  --fb-survey-background-color: #f0f0f0;

  /* Bordes */
  --fb-border-color: #e2e8f0;
}
```

Al definir estas variables en tu proyecto, el SDK de Formbricks las usará automáticamente.

**Opción B: Definirlo en la configuración de la encuesta (UI o API)**

Si prefieres que el estilo venga definido desde la base de datos de Formbricks:

- **Desde la Interfaz (UI)**: Ve a la pestaña "Styling" (o "Look & Feel") dentro del editor de tu encuesta. Ahí puedes definir el Brand Color y el Background Styling (puedes subir una imagen, usar un degradado o un color sólido).

- **Desde la API (Payload)**: Si estás creando la encuesta programáticamente (POST /api/v1/management/surveys), el objeto JSON de la encuesta incluye una propiedad `styling`. Puedes enviarla así:

```json
{
  "name": "Mi Encuesta",
  "styling": {
    "brandColor": "#ff5733",
    "cardBackgroundColor": "#ffffff",
    "cardBorderColor": "#e2e8f0",
    "background": {
       "bg": "#f0f0f0", // Color de fondo sólido
       "bgType": "color" // o "image" / "animation"
    }
  },
  "questions": [...]
}
```

**Resumen**

- **Carga**: Usa el SDK (`formbricks.init`) para la integración más fácil. Usa la API REST solo si vas a construir tu propia interfaz de usuario desde cero.
- **Estilos**: La forma más robusta de "definir" el color es usando las variables CSS (`--fb-brand-color`) en tu sitio web. Esto asegura que la encuesta siempre coincida con tu marca, independientemente de la configuración individual de la encuesta.
