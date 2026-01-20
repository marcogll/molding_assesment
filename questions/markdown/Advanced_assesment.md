# Code Carol: Nivel Avanzado (Ingenieros y Líderes)
[← Regresar al Inicio](../../readme.md)

## ℹ️ Información General
Esta evaluación está diseñada para certificar las competencias de ingenieros de procesos, líderes técnicos y especialistas en moldeo por inyección. Se enfoca en análisis profundo de termodinámica, estadística de calidad y optimización avanzada.

Total de preguntas: 44
Puntaje Máximo Posible: 52.5 puntos
Tiempo Estimado: 75 minutos
🏆 Passing Score (Aprobatorio): 80% (42 puntos mínimo)

## 📊 Distribución por Área de Conocimiento

| Área de Conocimiento | Cantidad de Preguntas | Enfoque Principal |
|----------------------|-----------------------|-------------------|
| 🏭 Máquina | 6 | Dinámica de husillo, ratios, scan time |
| ⚙️ Proceso | 6 | Termodinámica, viscosidad, VPT avanzado |
| 💎 Calidad | 5 | Cpk, soldaduras, defectos estructurales |
| 🦺 Seguridad | 5 | Riesgos químicos, LOTO avanzado, Euromap |
| 📦 Materiales | 5 | Escisión de cadenas, calor latente, pvT |
| ⚡ Eficiencia | 5 | OEE avanzado, SMED, costos |
| 🗑️ Desperdicios | 5 | Lean Manufacturing profundo, energía |
| 🔬 Ingeniería Moldes | 6 | CAE, flujo turbulento, compuertas |
| TOTAL | 43 |

## 🎯 Criterios de Evaluación
### 🏆 Aprobado (80%)

Puntaje Mínimo: 42 puntos
Interpretación: El candidato posee conocimientos de ingeniería y puede liderar optimizaciones complejas.

### 📉 Requiere Capacitación (Menor a 80%)

Acción: Programa de desarrollo técnico con mentoreo de ingeniero senior.

## ⚖️ Ponderación de Reactivos

Teórico (1.0 pts): Ingeniería, física, estadística
Práctico (1.5 pts): Análisis de casos, diagnóstico avanzado

## 📝 Banco de Preguntas
### 1. Con un ratio de intensificación de 10:1 y 1,500 PSI en el manómetro hidráulico, calcula la presión específica sobre el plástico:
**Categoría:** Máquina **Tipo:** Práctico **Description:** La presión hidráulica se multiplica en la punta del husillo debido a la Ley de Pascal y la diferencia de áreas. **Puntos:** 1.5 pts **ID:** mach_1

- 1,500 PSI (Relación 1:1)
- 150 PSI (Reducción por fricción)
- 15,000 PSI (Multiplicación por área)
- 16,500 PSI (Presión absoluta)

**Racional:** La presión específica es el resultado de la presión hidráulica multiplicada por el ratio de área entre el pistón y el husillo (1500 * 10).

### 2. ¿Cuál es la consecuencia físico-química de una descompresión (suck-back) excesiva en resinas sensibles como el Nylon?
**Categoría:** Máquina **Tipo:** Teórico **Description:** El oxígeno a altas temperaturas reacciona rápidamente con polímeros orgánicos. **Puntos:** 1 pts **ID:** mach_2

- Cristalización prematura en la boquilla
- Oxidación y degradación por entrada de aire al barril
- Aumento de la viscosidad intrínseca
- Generación de vacío en la cavidad del molde

**Racional:** El retroceso excesivo aspira oxígeno atmosférico hacia la cámara caliente, provocando oxidación inmediata y manchas (splay).

### 3. Una variación del cojín (cushion) superior a +/- 10% ciclo a ciclo es un indicador primario de:
**Categoría:** Máquina **Tipo:** Práctico **Description:** La consistencia del cojín es el mejor indicador de la repetibilidad volumétrica del proceso. **Puntos:** 1.5 pts **ID:** mach_3

- Falla en el control PID de temperatura
- Fuga en la válvula check (anillo) o desgaste del barril
- Variación en la velocidad de apertura del molde
- Fluctuación en la presión de la red de agua

**Racional:** La inestabilidad del cojín implica que el volumen de material delante del tornillo no se mantiene, fugándose hacia atrás durante la inyección.

### 4. El 'Scan Time' o tiempo de respuesta del controlador de la máquina afecta críticamente a:
**Categoría:** Máquina **Tipo:** Teórico **Description:** La velocidad de procesamiento de la CPU de la máquina influye en la precisión milimétrica. **Puntos:** 1 pts **ID:** mach_4

- La eficiencia del motor eléctrico
- La repetibilidad del punto de transferencia (VPT)
- La capacidad máxima de cierre
- La temperatura del aceite hidráulico

**Racional:** Un escaneo lento provoca que la máquina reaccione tarde al alcanzar la posición de corte, variando el volumen inyectado.

### 5. Comparando un husillo L/D 24:1 contra uno 18:1, la principal ventaja técnica del 24:1 es:
**Categoría:** Máquina **Tipo:** Teórico **Description:** La geometría del husillo determina la calidad de la homogeneización térmica. **Puntos:** 1 pts **ID:** mach_5

- Mayor presión máxima de inyección
- Mejor calidad de mezclado y homogeneidad térmica
- Menor tiempo de residencia del material
- Reducción del torque requerido para girar

**Racional:** Mayor longitud permite zonas de transición más suaves y mejor distribución de calor, resultando en un fundido (melt) más uniforme.

### 6. Además de aumentar la temperatura de la masa, ¿qué efecto mecánico negativo tiene la contrapresión excesiva?
**Categoría:** Máquina **Tipo:** Práctico **Description:** La contrapresión genera calor por fricción, pero también estrés mecánico. **Puntos:** 1 pts **ID:** mach_6

- Desgaste acelerado en la punta del husillo y barril
- Reducción de la fuerza de cierre disponible
- Fugas de aceite en el sistema de expulsión
- Deformación de las barras (tie-bars)

**Racional:** Aumenta la carga axial y la fricción del tornillo contra la pared del barril y el material, acelerando la abrasión.

### 7. En la curva de viscosidad, la región 'Newtonian Flat' (Meseta Newtoniana) se caracteriza porque:
**Categoría:** Proceso **Tipo:** Teórico **Description:** La reología de polímeros estudia cómo fluye la materia bajo fuerzas aplicadas. **Puntos:** 1 pts **ID:** proc_1

- La viscosidad cae drásticamente con la velocidad
- La viscosidad es estable independientemente del corte (shear)
- El material comienza a degradarse térmicamente
- La presión de inyección es cero

**Racional:** Es la zona de baja cizalla donde el polímero se comporta como un fluido newtoniano antes de empezar a adelgazar (shear thinning).

### 8. El objetivo de un estudio de 'Caída de Presión' (Pressure Drop) es asegurar que:
**Categoría:** Proceso **Tipo:** Práctico **Description:** Operar al límite de la capacidad de presión elimina la capacidad de control del proceso. **Puntos:** 1.5 pts **ID:** proc_2

- La máquina tenga ~10% de presión hidráulica de reserva
- El molde soporte la fuerza de cierre máxima
- El tiempo de ciclo sea lo más corto posible
- La temperatura del agua sea turbulenta

**Racional:** Si la máquina usa el 100% de su presión para llenar, pierde control sobre la velocidad (Process Limited). Se requiere un margen de seguridad.

### 9. Un aumento repentino en la integral de presión o 'Trabajo de Inyección' sugiere:
**Categoría:** Proceso **Tipo:** Práctico **Description:** El área bajo la curva de presión refleja la energía consumida para llenar el molde. **Puntos:** 1.5 pts **ID:** proc_3

- Una fuga en la válvula check
- Aumento de viscosidad por material frío u obstrucción
- Disminución de la fuerza de cierre
- Aumento en la temperatura del barril

**Racional:** Más trabajo para llegar a la misma posición indica mayor resistencia al flujo (viscosidad alta o canal bloqueado).

### 10. El criterio técnico definitivo para confirmar el 'Sellado de Compuerta' (Gate Freeze) es:
**Categoría:** Proceso **Tipo:** Práctico **Description:** Determinar cuándo se corta físicamente la conexión entre la pieza y el sistema de alimentación. **Puntos:** 1.5 pts **ID:** proc_4

- Estabilización del peso de la pieza vs tiempo de hold
- Enfriamiento de la colada a temperatura ambiente
- Finalización del tiempo de dosificación del husillo
- Ausencia de rechupados en la superficie

**Racional:** Se grafica peso vs tiempo. Cuando el peso deja de subir, la compuerta se ha cerrado físicamente y ya no entra material.

### 11. Debido al calentamiento por cizalla (Shear Heating), aumentar la velocidad de inyección provoca:
**Categoría:** Proceso **Tipo:** Teórico **Description:** La fricción molecular a altas velocidades se convierte en energía térmica. **Puntos:** 1 pts **ID:** proc_5

- Enfriamiento adiabático del frente de flujo
- Aumento real de la temperatura de la masa fundida
- Aumento de la densidad del material
- Reducción inmediata del índice de fluidez

**Racional:** La fricción molecular a alta velocidad genera calor interno, reduciendo la viscosidad efectiva.

### 12. ¿Por qué se prefiere el VPT (Transferencia) por Posición en lugar de por Tiempo o Presión?
**Categoría:** Proceso **Tipo:** Teórico **Description:** La consistencia del proceso depende de cómo se controla el volumen inyectado. **Puntos:** 1 pts **ID:** proc_6

- Porque es más fácil de programar
- Porque garantiza un volumen de disparo consistente
- Porque protege el molde de sobrepresión
- Porque reduce el consumo energético

**Racional:** La posición correlaciona directamente con el volumen desplazado. El tiempo varía si cambia la viscosidad, causando inestabilidad.

### 13. La solución técnica para eliminar el 'Jetting' (gusanito) es:
**Categoría:** Calidad **Tipo:** Práctico **Description:** El flujo laminar es deseable para evitar marcas superficiales en la pieza. **Puntos:** 1.5 pts **ID:** qual_1

- Aumentar la temperatura de la boquilla
- Perfilar la velocidad (lento al inicio) para crear flujo laminar
- Aumentar la contrapresión al máximo
- Reducir el tiempo de enfriamiento

**Racional:** Entrar lento permite que el material toque las paredes y se expanda progresivamente (Fountain Flow) en lugar de dispararse.

### 14. En polímeros semicristalinos, ¿qué factor determina el grado de cristalinidad y la contracción final?
**Categoría:** Calidad **Tipo:** Teórico **Description:** La estructura molecular de los semicristalinos depende del tiempo que tienen para ordenarse. **Puntos:** 1 pts **ID:** qual_2

- La presión de inyección
- La tasa de enfriamiento (Temperatura de molde)
- La velocidad de rotación del husillo
- El porcentaje de carga de fibra de vidrio

**Racional:** Un enfriamiento lento (molde caliente) permite a las moléculas ordenarse en cristales, aumentando la densidad y contracción.

### 15. Un Cpk de 0.8 en una dimensión crítica indica estadísticamente que:
**Categoría:** Calidad **Tipo:** Práctico **Description:** Los índices de capacidad estadística predicen la tasa de rechazo a largo plazo. **Puntos:** 1.5 pts **ID:** qual_3

- El proceso es capaz y está centrado
- El proceso no es capaz; alta probabilidad de defectos
- El instrumento de medición requiere calibración
- La varianza es menor a la tolerancia

**Racional:** Cpk < 1.33 se considera no capaz. La curva de distribución del proceso excede los límites de especificación.

### 16. Una línea de soldadura (Weld Line) se convierte en una falla estructural crítica si:
**Categoría:** Calidad **Tipo:** Teórico **Description:** La fusión de frentes de flujo requiere energía térmica para entrelazar las cadenas moleculares. **Puntos:** 1 pts **ID:** qual_4

- Es visible a simple vista
- La temperatura del frente de flujo es inferior a la Tg al unirse
- Se encuentra en una zona estética
- El molde tiene textura rugosa

**Racional:** Si el material está demasiado frío, no hay entrelazamiento molecular (difusión) entre los frentes, creando una grieta potencial.

### 17. Para prevenir el 'Efecto Diesel' en una costilla ciega (blind rib) donde no hay salida de aire, la solución de ingeniería es:
**Categoría:** Calidad **Tipo:** Práctico **Description:** En zonas ciegas donde no es posible mecanizar un venteo tradicional, se requieren materiales especiales. **Puntos:** 1.5 pts **ID:** qual_5

- Aumentar la velocidad de inyección para llenar rápido
- Uso de insertos de acero poroso sinterizado
- Bajar la temperatura del molde drásticamente
- Aplicar vacío a toda la máquina

**Racional:** El acero poroso permite que el gas escape a través de la estructura del metal mientras retiene el plástico.

### 18. Al purgar POM (Acetal) degradado, el riesgo químico específico es:
**Categoría:** Seguridad **Tipo:** Práctico **Description:** Ciertos materiales liberan gases altamente peligrosos al descomponerse. **Puntos:** 1.5 pts **ID:** safe_1

- Liberación de gas Formaldehído (tóxico/irritante)
- Formación de ácido clorhídrico corrosivo
- Generación de monóxido de carbono inodoro
- Explosión por polvo en suspensión

**Racional:** El POM se descompone en formaldehído, que ataca ojos y vías respiratorias severamente. Requiere ventilación.

### 19. En un procedimiento LOTO avanzado, después de colocar el candado, ¿cuál es el paso final de verificación?
**Categoría:** Seguridad **Tipo:** Práctico **Description:** La seguridad moderna requiere validación activa, no solo colocar un candado. **Puntos:** 1 pts **ID:** safe_2

- Firmar la bitácora de mantenimiento
- Intentar arrancar el equipo para confirmar 'Energía Cero'
- Avisar al gerente de planta
- Tomar una foto del candado

**Racional:** El paso crítico de 'Try-out' o prueba de arranque confirma que el bloqueo fue efectivo y no hay energía residual.

### 20. El peligro latente de un acumulador hidráulico, incluso con la máquina apagada, es:
**Categoría:** Seguridad **Tipo:** Teórico **Description:** La energía hidráulica puede almacenarse incluso sin energía eléctrica. **Puntos:** 1.5 pts **ID:** safe_3

- Alta temperatura residual
- Energía de presión almacenada lista para liberarse
- Generación de campos magnéticos
- Fugas de nitrógeno asfixiante

**Racional:** El acumulador mantiene aceite a presión. Si se desconecta una manguera sin drenarlo, puede causar inyección de fluido letal.

### 21. Extintor correcto para fuego en tableros electrónicos (Clase C):
**Categoría:** Seguridad **Tipo:** Teórico **Description:** El uso de agua en incendios eléctricos es fatal; se requieren agentes limpios. **Puntos:** 1 pts **ID:** safe_4

- Agua a presión (Tipo A)
- Dióxido de Carbono (CO2) o Agente Limpio
- Espuma formadora de película (AFFF)
- Polvo especial para metales (Tipo D)

**Racional:** Agentes no conductores y que no dejen residuo corrosivo son esenciales para equipo electrónico.

### 22. Según la norma Euromap 67, ¿cuál es la función de los canales de seguridad redundantes (doble canal)?
**Categoría:** Seguridad **Tipo:** Teórico **Description:** La integración de robots requiere protocolos de comunicación de seguridad estandarizados. **Puntos:** 1.5 pts **ID:** safe_5

- Aumentar la velocidad de transmisión de datos
- Asegurar que si un canal falla, el otro detenga la máquina inmediatamente
- Permitir el control remoto desde la oficina
- Ahorrar cableado en la instalación

**Racional:** La redundancia es clave en seguridad (Categoría 3/4); el sistema debe detectar fallos en su propia supervisión.

### 23. La degradación por escisión de cadenas (Chain Scission) resulta en:
**Categoría:** Materiales **Tipo:** Teórico **Description:** El corte de las cadenas poliméricas cambia radicalmente la reología del material. **Puntos:** 1 pts **ID:** mat_1

- Aumento de peso molecular y viscosidad
- Reducción de peso molecular, viscosidad y propiedades mecánicas
- Mejora en la resistencia al impacto
- Reticulación (cross-linking) del polímero

**Racional:** Al romperse las cadenas largas, el material se vuelve más líquido (fluye más) pero pierde su fuerza estructural.

### 24. La hidrólisis en materiales como PC o PBT es una reacción química donde el agua:
**Categoría:** Materiales **Tipo:** Teórico **Description:** El agua actúa como un agente reactivo que destruye el polímero a nivel molecular. **Puntos:** 1 pts **ID:** mat_2

- Actúa como lubricante externo
- Rompe los enlaces covalentes de la cadena polimérica
- Se evapora sin afectar la estructura
- Genera burbujas superficiales únicamente

**Racional:** Es una degradación química irreversible a nivel molecular, no solo un defecto cosmético.

### 25. Diferencia térmica clave: Los semicristalinos poseen Calor Latente de Fusión, lo que implica:
**Categoría:** Materiales **Tipo:** Teórico **Description:** El cambio de fase de sólido a líquido requiere más energía en materiales ordenados. **Puntos:** 1 pts **ID:** mat_3

- Requieren menos energía para fundirse
- Requieren mucha más energía para fundir y enfriar que los amorfos
- Se enfrían instantáneamente
- No tienen temperatura de fusión definida

**Racional:** Se necesita energía extra para romper la estructura cristalina al fundir, y hay que extraer esa energía al enfriar.

### 26. ¿Por qué el MFI no es representativo del comportamiento dentro del molde?
**Categoría:** Materiales **Tipo:** Teórico **Description:** Las pruebas de laboratorio estáticas no siempre reflejan la realidad dinámica de la inyección. **Puntos:** 1 pts **ID:** mat_4

- Porque se mide a baja temperatura
- Porque es una prueba de bajo cizallamiento (Low Shear)
- Porque usa un peso estándar
- Porque el material está sucio

**Racional:** La inyección es un proceso de ALTO cizallamiento. El MFI mide flujo casi estático, ignorando el adelgazamiento por corte.

### 27. En un diagrama pvT, ¿qué representa la 'rodilla' o cambio brusco de pendiente en la curva de enfriamiento isobárico?
**Categoría:** Materiales **Tipo:** Teórico **Description:** El comportamiento pvT (Presión-Volumen-Temperatura) es fundamental para predecir dimensiones. **Puntos:** 1 pts **ID:** mat_5

- El punto de degradación térmica
- La temperatura de transición vítrea (Tg) o cristalización
- El momento en que se abre el molde
- La presión máxima de la máquina

**Racional:** Es el punto donde el material cambia de estado (fase), alterando drásticamente su volumen específico.

### 28. El factor limitante físico (Cuello de botella) más común para reducir el tiempo de ciclo es:
**Categoría:** Eficiencia **Tipo:** Práctico **Description:** La termodinámica impone límites físicos a la velocidad de producción. **Puntos:** 1.5 pts **ID:** eff_1

- La velocidad de inyección de la máquina
- La conductividad térmica del plástico (Tiempo de enfriamiento)
- La velocidad de los movimientos del molde
- El tiempo de reacción del robot

**Racional:** El plástico es un aislante térmico. Extraer el calor del centro de la pared es el proceso más lento por física pura.

### 29. En SMED, un ejemplo de actividad INTERNA es:
**Categoría:** Eficiencia **Tipo:** Práctico **Description:** Distinguir entre tareas que detienen la máquina y las que no es la base del SMED. **Puntos:** 1.5 pts **ID:** eff_2

- Precalentar el molde en un banco externo
- Asegurar el molde a la platina (Clamping)
- Buscar las llaves y herramientas
- Organizar las mangueras de agua

**Racional:** Actividad Interna = Máquina detenida forzosamente. No puedes atornillar el molde si la máquina está produciendo.

### 30. Si tu OEE es 60% pero la Calidad es 99% y la Disponibilidad 98%, el problema está en:
**Categoría:** Eficiencia **Tipo:** Práctico **Description:** El cálculo del OEE revela dónde se pierden las oportunidades de producción. **Puntos:** 1.5 pts **ID:** eff_3

- Desempeño (Performance) - Ciclos lentos o micro-paros
- Calidad - Piezas defectuosas ocultas
- Disponibilidad - Tiempos muertos largos
- Planeación - Falta de órdenes

**Racional:** Matemáticamente: Si AxQ son altos, P debe ser muy bajo para arrastrar el promedio a 60%.

### 31. El MTBF (Mean Time Between Failures) mide:
**Categoría:** Eficiencia **Tipo:** Teórico **Description:** La confiabilidad del equipo se mide por la frecuencia de sus averías. **Puntos:** 1 pts **ID:** eff_4

- La velocidad de reparación del equipo
- La confiabilidad y frecuencia de fallas del equipo
- El tiempo total de vida útil
- La eficiencia del operador

**Racional:** Indica qué tan seguido se rompe la máquina. Clave para programar mantenimiento preventivo.

### 32. El Costo Real de la 'No Calidad' incluye:
**Categoría:** Eficiencia **Tipo:** Teórico **Description:** Los costos de mala calidad van mucho más allá del material tirado. **Puntos:** 1 pts **ID:** eff_5

- Únicamente el valor de la resina desperdiciada
- Material + Energía + Mano de obra + Costo de oportunidad + Riesgo cliente
- El salario del departamento de calidad
- El costo de la disposición de basura

**Racional:** Producir basura cuesta lo mismo o más que producir piezas buenas, más el lucro cesante.

### 33. El sobre-empaque (overpacking) que causa piezas pesadas y estrés interno es un desperdicio de tipo:
**Categoría:** Desperdicios **Tipo:** Práctico **Description:** Agregar valor es lo único por lo que el cliente paga; el resto es desperdicio. **Puntos:** 1.5 pts **ID:** wast_1

- Transporte y Movimiento
- Sobre-procesamiento y Material
- Espera e Inventario
- Talento Humano

**Racional:** Usas más material del necesario y aplicas más presión (proceso) de la requerida, agregando costo sin valor.

### 34. El exceso de inventario (WIP o Terminado) es negativo porque:
**Categoría:** Desperdicios **Tipo:** Teórico **Description:** El inventario excesivo actúa como un amortiguador que esconde problemas operativos. **Puntos:** 1 pts **ID:** wast_2

- Oculta ineficiencias del sistema y atrapa flujo de efectivo
- Mejora la respuesta ante variaciones de demanda
- Asegura que los operadores siempre tengan trabajo
- Aumenta el valor de los activos de la empresa

**Racional:** Es la analogía del 'río y las rocas'. El nivel alto de agua (inventario) tapa los problemas (rocas) del fondo.

### 35. Un mantenimiento deficiente de venteos genera desperdicio principalmente por:
**Categoría:** Desperdicios **Tipo:** Práctico **Description:** La falta de mantenimiento preventivo en moldes genera tiempos muertos reactivos. **Puntos:** 1.5 pts **ID:** wast_3

- Aumento en el consumo de energía eléctrica
- Paros no programados para limpieza y scrap por quemaduras
- Desgaste prematuro del aceite hidráulico
- Reducción de la fuerza de cierre

**Racional:** Los venteos sucios obligan a detener la producción para limpiar (Disponibilidad) y generan defectos (Calidad).

### 36. Técnicamente, usar Colada Fría en lugar de Colada Caliente implica:
**Categoría:** Desperdicios **Tipo:** Teórico **Description:** El diseño del sistema de alimentación impacta la eficiencia del material. **Puntos:** 1 pts **ID:** wast_4

- Mayor eficiencia energética
- Generación intrínseca de desperdicio (scrap/regrind) en cada ciclo
- Mejor control de la temperatura de masa
- Menor tiempo de ciclo total

**Racional:** La colada fría es material que se calienta y enfría solo para ser tirado o re-molido, lo cual es ineficiente termodinámicamente.

### 37. ¿Qué métrica se utiliza comúnmente para comparar la eficiencia energética entre diferentes máquinas de inyección?
**Categoría:** Desperdicios **Tipo:** Teórico **Description:** La eficiencia energética es un indicador clave de sostenibilidad y costo. **Puntos:** 1 pts **ID:** wast_5

- Caballos de fuerza (HP) del motor
- Consumo Específico de Energía (kWh/kg de material procesado)
- Amperaje máximo del tablero
- Voltaje de alimentación (220V vs 440V)

**Racional:** El kWh/kg normaliza el consumo respecto a la producción, permitiendo comparar máquinas grandes y pequeñas.

### 38. En refrigeración de moldes, un Número de Reynolds > 4,000 garantiza:
**Categoría:** Ingeniería Moldes **Tipo:** Teórico **Description:** La dinámica de fluidos dicta la eficiencia de la transferencia de calor. **Puntos:** 1 pts **ID:** spec_1

- Flujo Laminar (Bajo intercambio térmico)
- Flujo Turbulento (Máxima eficiencia de transferencia de calor)
- Presión excesiva en las mangueras
- Ausencia de corrosión en los canales

**Racional:** La turbulencia rompe la capa límite aislante del agua contra el metal, extrayendo calor mucho más rápido.

### 39. La 'Deflexión de Platinas' causa rebaba central aunque el tonelaje sea correcto debido a:
**Categoría:** Ingeniería Moldes **Tipo:** Práctico **Description:** La rigidez de la máquina interactúa con la estructura del molde. **Puntos:** 1.5 pts **ID:** spec_2

- Deformación elástica de la platina que abre el molde en el centro
- Expansión térmica del molde
- Compresión excesiva del acero del molde
- Falta de paralelismo en las guías

**Racional:** Si el molde es pequeño, la platina se 'dobla' alrededor de él como una hoja de papel, perdiendo presión de sello en el centro.

### 40. ¿En qué etapa es más rentable utilizar simulación CAE (Moldflow)?
**Categoría:** Ingeniería Moldes **Tipo:** Teórico **Description:** La simulación predictiva ahorra costos al identificar errores antes de cortar acero. **Puntos:** 1 pts **ID:** spec_3

- Durante la producción para arreglar fallas
- En la fase de diseño de pieza y molde (previo al corte de acero)
- Después de fabricar el molde para validarlo
- Al cotizar el precio de la resina

**Racional:** El costo de corregir un error en diseño es despreciable comparado con modificar acero endurecido.

### 41. La ventaja técnica principal de una compuerta valvulada (Valve Gate) es:
**Categoría:** Ingeniería Moldes **Tipo:** Teórico **Description:** Los sistemas de colada caliente avanzados permiten control secuencial. **Puntos:** 1 pts **ID:** spec_4

- Menor costo de mantenimiento
- Control independiente del flujo y mejor acabado cosmético (sin vestigio)
- Eliminación del sistema de enfriamiento
- Reducción de la fuerza de cierre requerida

**Racional:** Permite abrir/cerrar la entrada a voluntad (secuenciado) y deja una marca casi invisible en la pieza.

### 42. El 'Efecto de Esquina' (Corner Effect) en refrigeración provoca puntos calientes porque:
**Categoría:** Ingeniería Moldes **Tipo:** Práctico **Description:** La geometría de la pieza afecta la disipación de calor. **Puntos:** 1.5 pts **ID:** spec_5

- El agua fluye más lento en las esquinas
- Hay mayor masa de plástico transfiriendo calor a menor área de acero
- El acero es más delgado en las esquinas
- La fricción del flujo es mayor

**Racional:** Geometría básica: El calor converge desde dos lados hacia una esquina interna que tiene poca superficie para disiparlo.

### 43. ¿Por qué el monitoreo del 'Cojín' es más crítico que el 'Tiempo de Inyección' para la consistencia dimensional?
**Categoría:** Proceso **Tipo:** Práctico **Description:** La presión efectiva sobre la pieza depende de la reserva de material. **Puntos:** 1.5 pts **ID:** spec_6

- Porque confirma que hubo material suficiente para transferir la presión de empaque
- Porque es más fácil de leer en la pantalla
- Porque el tiempo de inyección nunca varía
- Porque el cojín determina la velocidad de enfriamiento

**Racional:** Si no hay cojín, no hay presión hidráulica sobre la pieza (presión efectiva = 0), causando rechupados y medidas cortas.

## 📌 Notas Finales

Las respuestas correctas están marcadas con ✅
Revisa cada sección cuidadosamente antes de comenzar la evaluación
Consulta con tu supervisor cualquier duda sobre los procedimientos de seguridad

¡Buena suerte en tu evaluación! 🎯
