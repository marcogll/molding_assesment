import os
import json
import uuid
import requests
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text
from dotenv import load_dotenv

load_dotenv()

# ───────── Catppuccin Frappe ─────────
COLORS = {
    "surface": "#414559",
    "text": "#c6d0f5",
    "blue": "#8caaee",
    "green": "#a6d189",
    "red": "#e78284",
    "yellow": "#e5c890",
    "pink": "#f4b8e4",
}

console = Console(style=COLORS["text"])

console.print(
    Panel(
        Text("🧩 Formbricks Survey Assistant", justify="center", style=COLORS["pink"]),
        border_style=COLORS["surface"],
    )
)

BASEURL = os.getenv("FORMBRICKS_BASEURL")
API_KEY = os.getenv("FORMBRICKS_API_KEY")
ENV_ID = os.getenv("FORMBRICKS_ENVIRONMENT_ID")

if not all([BASEURL, API_KEY, ENV_ID]):
    raise RuntimeError("Variables de entorno incompletas")

LEVEL_FILE_MAP = {
    "0": "funnel_registration_formbricks.json",
    "1": "basic_formbricks.json",
    "2": "medium_formbricks.json",
    "3": "advanced_formbricks.json",
}


def convert_to_object_format(data):
    """Recursively convert string text fields to object format required by Formbricks API"""
    if isinstance(data, dict):
        for key, value in data.items():
            if key in [
                "headline",
                "subheader",
                "buttonLabel",
                "backButtonLabel",
                "placeholder",
                "label",
                "html",
            ] and isinstance(value, str):
                data[key] = {"default": value}
            elif key == "choices" and isinstance(value, list):
                for choice in value:
                    if (
                        isinstance(choice, dict)
                        and "label" in choice
                        and isinstance(choice["label"], str)
                    ):
                        choice["label"] = {"default": choice["label"]}
            else:
                convert_to_object_format(value)
    elif isinstance(data, list):
        for item in data:
            convert_to_object_format(item)


def parse_questions(raw_items):
    questions = []

    for i, item in enumerate(raw_items):
        q = item.copy()
        if "id" not in q:
            q["id"] = f"q{i}"
        questions.append(q)

    return questions


def main():
    # ───────── Inputs ─────────
    company = Prompt.ask("🏭 Compañía", default="Empresa")
    level = Prompt.ask("🎚️ Nivel [0/1/2/3]", choices=["0", "1", "2", "3"], default="1")
    start_date = Prompt.ask("📅 Fecha inicio (YYYY-MM-DD o vacío)", default="")
    end_date = Prompt.ask("📅 Fecha término (YYYY-MM-DD o vacío)", default="")

    # ───────── Styling ─────────
    console.print(
        Panel(
            "🎨 Configuración de colores (opcional - presiona Enter para usar defaults)",
            border_style=COLORS["blue"],
        )
    )
    brand_color = Prompt.ask(
        "🎨 Color principal (brand color, ej: #ff5733)", default="#ff5733"
    )
    card_bg = Prompt.ask(
        "🎨 Fondo de tarjeta (card background, ej: #ffffff)", default="#ffffff"
    )
    survey_bg = Prompt.ask(
        "🎨 Fondo general (survey background, ej: #f0f0f0)", default="#f0f0f0"
    )
    border_color = Prompt.ask(
        "🎨 Color de bordes (border color, ej: #e2e8f0)", default="#e2e8f0"
    )

    # Build styling object
    styling = {
        "brandColor": {"light": brand_color, "dark": brand_color},
        "cardBackgroundColor": {"light": card_bg, "dark": card_bg},
        "cardBorderColor": {"light": border_color, "dark": border_color},
        "surveyBackground": {"bg": survey_bg, "bgType": "color"},
    }

    file_name = LEVEL_FILE_MAP[level]

    with open(file_name, "r", encoding="utf-8") as f:
        raw_file = json.load(f)

    raw_questions = raw_file.get("questions", [])
    if not raw_questions:
        raise RuntimeError("El archivo no contiene preguntas")

    questions = parse_questions(raw_questions)
    convert_to_object_format(questions)

    welcome_card = raw_file.get("welcomeCard")
    if welcome_card:
        convert_to_object_format(welcome_card)

    endings = raw_file.get("endings", [])
    # Set valid id and add required fields for endings
    for ending in endings:
        ending["id"] = "p73t62dgwq0cvmtt6ug0hmfc"
        if "buttonLabel" not in ending:
            ending["buttonLabel"] = {"default": "Completar"}
        if "buttonLink" not in ending:
            ending["buttonLink"] = "https://example.com"
    convert_to_object_format(endings)

    if level == "0":
        title = f"{company} | Funnel L0"
    else:
        title = f"{company} | Evaluacion de moldeo L{level}"

    payload = {
        "environmentId": ENV_ID,
        "name": title,
        "status": "draft",
        "type": "link",
        "displayOption": "displayOnce",
        "languages": [],
        "questions": questions,
    }

    if welcome_card:
        payload["welcomeCard"] = welcome_card
    if endings:
        payload["endings"] = endings
    payload["styling"] = styling

    headers = {
        "Content-Type": "application/json",
        "x-api-key": API_KEY,
    }

    console.print(Panel(f"📄 {file_name}", title="Archivo seleccionado"))
    console.print(Panel(f"📝 {title}", title="Creando encuesta (DRAFT)"))

    response = requests.post(
        f"{BASEURL}/api/v1/management/surveys",
        json=payload,
        headers=headers,
        timeout=30,
    )

    if response.ok:
        console.print(
            Panel("✅ Encuesta creada correctamente", border_style=COLORS["green"])
        )
        console.print(
            Panel(
                "💡 Para integración con SDK: Revisa styles.css para variables CSS opcionales",
                border_style=COLORS["yellow"],
            )
        )
    else:
        console.print(Panel("❌ Error al crear encuesta", border_style=COLORS["red"]))
        console.print(response.status_code, response.text)


if __name__ == "__main__":
    main()
