import os
import json
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
    "1": "basic_v2_formbricks.json",
    "2": "medium_v2_formbricks.json",
    "3": "advanced_v2_formbricks.json",
}

def parse_survey(raw_items):
    questions = []
    welcome_card = None
    ending = None

    for i, item in enumerate(raw_items):
        t = item.get("type")

        if t == "welcome":
            welcome_card = {
                "enabled": True,
                "headline": item.get("headline"),
                "html": item.get("html"),
                "showResponseCount": False,
                "timeToFinish": False,
            }

        elif t == "thankYou":
            ending = {
                "id": item.get("id", "end_default"),
                "type": "endScreen",
                "headline": item.get("headline"),
                "subheader": item.get("html"),
            }

        else:
            q = {
                "id": item.get("id", f"q{i}"),
                "type": item.get("type"),
                "required": item.get("required", True),
                "headline": item.get("headline"),
                "shuffleOption": item.get("shuffleOption", "none"),
                "choices": [
                    {
                        "id": c.get("id", f"{i}_{idx}"),
                        "label": c.get("label"),
                    }
                    for idx, c in enumerate(item.get("choices", []))
                ],
            }
            questions.append(q)

    return questions, welcome_card, ending

# ───────── Inputs ─────────
company = Prompt.ask("🏭 Compañía", default="Empresa")
level = Prompt.ask("🎚️ Nivel [1/2/3]", choices=["1", "2", "3"], default="1")
start_date = Prompt.ask("📅 Fecha inicio (YYYY-MM-DD o vacío)", default="")
end_date = Prompt.ask("📅 Fecha término (YYYY-MM-DD o vacío)", default="")

file_name = LEVEL_FILE_MAP[level]

with open(file_name, "r", encoding="utf-8") as f:
    raw_file = json.load(f)

raw_questions = raw_file.get("questions", [])
if not raw_questions:
    raise RuntimeError("El archivo no contiene preguntas")

questions, welcome_card, ending = parse_survey(raw_questions)

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
if ending:
    payload["endings"] = [ending]

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
    console.print(Panel("✅ Encuesta creada correctamente", border_style=COLORS["green"]))
else:
    console.print(Panel("❌ Error al crear encuesta", border_style=COLORS["red"]))
    console.print(response.status_code, response.text)

