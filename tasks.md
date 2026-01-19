# Tasks - Evaluación Técnica de Moldeo por Inyección

## Resumen del Proyecto

Sistema de evaluaciones técnicas para operadores de moldeo por inyección usando Formbricks.

---

## ✅ Completado

### 1. Estructura de Datos
- [x] `basic_v2.json` - 57 preguntas (Nivel Básico)
- [x] `medium_v2.json` - 60 preguntas (Nivel Intermedio)
- [x] `advanced_v2.json` - 43 preguntas (Nivel Avanzado)
- [x] `funnel_registration.json` - Formulario de registro

### 2. Conversor a Formbricks
- [x] `assessment_conv.py` - Script Python para convertir JSON → Formbricks
- [x] Genera archivos con formato correcto de API:
  - `headline` como objeto `{"default": "..."}`
  - `buttonLabel` como objeto `{"default": "..."}`
  - `backButtonLabel` como objeto `{"default": "..."}`

### 3. Archivos Formbricks Generados
- [x] `basic_v2_formbricks.json` (57 preguntas)
- [x] `medium_v2_formbricks.json` (60 preguntas)
- [x] `advanced_v2_formbricks.json` (43 preguntas)
- [x] `funnel_registration_formbricks.json` (actualizado)

### 4. Documentación
- [x] `Form_requirements.md` actualizado con:
  - Ejemplos de formato correcto
  - Sección de errores comunes de API
  - Reglas de validación

---

## 🔄 En Progreso

### Deployment en Formbricks
- [ ] Crear encuestas en Formbricks usando `formbricks_assitant.py`
- [ ] Verificar que las encuestas se crean correctamente
- [ ] Probar flujo completo (registro → evaluación)

---

## ⏳ Pendiente

### 1. Testing y Validación
- [ ] Validar estructura de preguntas en Formbricks
- [ ] Probar con cuenta de prueba
- [ ] Verificar que el cálculo de score funciona

### 2. Mejoras del Script
- [ ] Agregar soporte para tipos de pregunta `multipleChoiceMulti`
- [ ] Agregar validación de estructura JSON
- [ ] Agregar logs más detallados

### 3. Integración
- [ ] Conectar con sistema de scoring
- [ ] Configurar triggers de email
- [ ] Configurar filtros de segmentación

---

## 📁 Archivos del Proyecto

```
/home/marco/Work/Carol/
├── tasks.md                          # Este archivo
├── questions/
│   ├── json/                         # Archivos fuente (origen)
│   │   ├── basic_v2.json
│   │   ├── medium_v2.json
│   │   ├── advanced_v2.json
│   │   └── funnel_registration.json
│   ├── formbricks/                   # Archivos Formbricks + scripts
│   │   ├── Form_requirements.md      # Documentación
│   │   ├── assessment_conv.py        # Conversor JSON → Formbricks
│   │   ├── formbricks_assitant.py    # Script de deployment
│   │   ├── basic_v2_formbricks.json  # ✅ Generado
│   │   ├── medium_v2_formbricks.json # ✅ Generado
│   │   ├── advanced_v2_formbricks.json # ✅ Generado
│   │   ├── funnel_registration_formbricks.json
│   │   ├── *.json.old                # Respaldos
│   │   └── .env
│   └── assessment_conv.py            # (movido a formbricks/)
```

---

## 🚀 Próximos Pasos Inmediatos

1. **Ejecutar deployment**:
   ```bash
   cd /home/marco/Work/Carol/questions/formbricks
   py formbricks_assitant.py
   ```

2. **Si falla**, revisar:
   - API key en `.env`
   - Formato de archivos JSON
   - Conexión a internet

3. **Verificar** en dashboard de Formbricks:
   - Encuestas creadas
   - Preguntas visibles
   - Flujo de preguntas

---

## 📝 Notas

- **Error común**: `400 Fields are missing or incorrectly formatted`
  - Causa: Usar strings directos en `headline`, `buttonLabel`
  - Solución: Usar objetos `{"default": "..."}`
  - Referencia: `Form_requirements.md` sección "Errores Comunes"

- **Contador de preguntas**:
  - Básico: 57 (+1 employee_number = 58 total)
  - Intermedio: 60 (+1 employee_number = 61 total)
  - Avanzado: 43 (+1 employee_number = 44 total)

---

## 🔗 Links Útiles

- Dashboard Formbricks: https://app.formbricks.com
- Documentación API: https://formbricks.com/docs/api-reference/rest-api
- Repo local: `/home/marco/Work/Carol/questions/formbricks/`

---

*Última actualización: 2026-01-19*
