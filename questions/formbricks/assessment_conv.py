#!/usr/bin/env python3
"""
Conversor de JSON a Formbricks
Convierte archivos de preguntas JSON originales al formato Formbricks API
"""

import json
import os
from pathlib import Path


def calculate_time_estimated(num_questions):
    """Calcula el tiempo estimado basado en el numero de preguntas"""
    # Aproximadamente 45-60 segundos por pregunta
    minutes = (num_questions * 45) // 60
    return max(minutes, 1)


def create_welcome_card(level_name, num_questions):
    """Crea el welcomeCard para Formbricks"""
    level_descriptions = {
        "Basico": "Prueba de conocimientos fundamentales sobre maquinaria, proceso, calidad y seguridad.",
        "Intermedio": "Evaluacion de diagnostico de fallas, parametros de proceso y eficiencia operativa.",
        "Avanzado": "Prueba para Ingenieros y Tecnicos Sr. enfocada en optimizacion, reologia, defectos complejos y diseno de moldes.",
    }

    time_estimated = calculate_time_estimated(num_questions)

    return {
        "enabled": True,
        "headline": {"default": "Evaluacion Tecnica de Moldeo"},
        "html": f"<b>Nivel {level_name}</b><br>{level_descriptions.get(level_name, '')}<br><br>• Preguntas: {num_questions}<br>• Tiempo estimado: {time_estimated} min",
        "showResponseCount": False,
        "timeToFinish": False,
        "buttonLabel": {"default": "Siguiente"},
    }

    time_estimated = calculate_time_estimated(num_questions)

    return {
        "enabled": True,
        "headline": "Evaluacion Tecnica de Moldeo",
        "html": f"<b>Nivel {level_name}</b><br>{level_descriptions.get(level_name, '')}<br><br>• Preguntas: {num_questions}<br>• Tiempo estimado: {time_estimated} min",
        "showResponseCount": False,
        "timeToFinish": False,
        "buttonLabel": "Siguiente",
    }

    time_estimated = calculate_time_estimated(num_questions)

    return {
        "enabled": True,
        "headline": "Evaluación Técnica de Moldeo",
        "html": f"<b>Nivel {level_name}</b><br>{level_descriptions.get(level_name, '')}<br><br>• Preguntas: {num_questions}<br>• Tiempo estimado: {time_estimated} min",
        "showResponseCount": False,
        "timeToFinish": False,
        "buttonLabel": "Siguiente",
    }


def convert_question(original_q):
    """Convierte una pregunta original al formato Formbricks"""
    # Obtener description y manejar si es None o vacío
    description = original_q.get("description", "")
    if description is None:
        description = ""

    fb_question = {
        "id": original_q["id"],
        "type": "multipleChoiceSingle",
        "headline": {"default": original_q["question"]},
        "subheader": description,
        "required": True,
        "buttonLabel": {"default": "Siguiente"},
        "backButtonLabel": {"default": "Anterior"},
        "shuffleOption": "none",
        "choices": [],
    }

    # Convertir opciones
    for idx, option in enumerate(original_q.get("options", [])):
        fb_question["choices"].append({"id": f"c{idx}", "label": {"default": option}})

    return fb_question


def create_ending():
    """Crea el ending screen"""
    return {
        "id": "end_screen",
        "type": "endScreen",
        "headline": {"default": "Evaluación Completada"},
        "subheader": {
            "default": "Tus respuestas han sido enviadas exitosamente. El departamento de entrenamiento revisará tus resultados."
        },
        "buttonLabel": {"default": "Finalizar"},
    }


def convert_json_to_formbricks(input_file, output_file, level_name):
    """Convierte un archivo JSON original a Formbricks"""

    # Leer archivo original
    with open(input_file, "r", encoding="utf-8") as f:
        original_data = json.load(f)

    questions = (
        original_data
        if isinstance(original_data, list)
        else original_data.get("questions", [])
    )
    num_questions = len(questions)

    # Crear estructura Formbricks
    formbricks_data = {
        "name": f"Evaluación Técnica de Moldeo - Nivel {level_name}",
        "type": "link",
        "status": "draft",
        "displayOption": "displayOnce",
        "welcomeCard": create_welcome_card(level_name, num_questions),
        "questions": [],
    }

    # Agregar pregunta de número de empleado al inicio
    formbricks_data["questions"].append(
        {
            "id": "employee_number",
            "type": "openText",
            "headline": {"default": "Número de empleado"},
            "subheader": "",
            "required": True,
            "inputType": "text",
            "placeholder": {"default": "Ingresa tu número de empleado"},
            "buttonLabel": {"default": "Siguiente"},
            "backButtonLabel": {"default": "Anterior"},
        }
    )

    # Convertir y agregar preguntas
    for question in questions:
        fb_question = convert_question(question)
        formbricks_data["questions"].append(fb_question)

    # Agregar ending
    formbricks_data["endings"] = [create_ending()]

    # Escribir archivo Formbricks
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(formbricks_data, f, ensure_ascii=False, indent=2)

    print(f"✓ {output_file.name} creado exitosamente ({num_questions} preguntas)")


def main():
    """Función principal"""
    # Definir rutas
    base_dir = Path(__file__).parent
    json_dir = base_dir / "json"
    formbricks_dir = base_dir / "formbricks"

    # Definir archivos a convertir
    conversions = [
        {
            "input": json_dir / "basic_v2.json",
            "output": formbricks_dir / "basic_v2_formbricks.json",
            "level": "Básico",
        },
        {
            "input": json_dir / "medium_v2.json",
            "output": formbricks_dir / "medium_v2_formbricks.json",
            "level": "Intermedio",
        },
        {
            "input": json_dir / "advanced_v2.json",
            "output": formbricks_dir / "advanced_v2_formbricks.json",
            "level": "Avanzado",
        },
    ]

    print("=" * 60)
    print("Conversor de JSON a Formbricks")
    print("=" * 60)
    print()

    # Procesar cada archivo
    for conversion in conversions:
        if conversion["input"].exists():
            print(f"Procesando: {conversion['input'].name}")
            convert_json_to_formbricks(
                conversion["input"], conversion["output"], conversion["level"]
            )
            print()
        else:
            print(f"✗ Archivo no encontrado: {conversion['input']}")
            print()

    print("=" * 60)
    print("Conversión completada!")
    print("=" * 60)


if __name__ == "__main__":
    main()
