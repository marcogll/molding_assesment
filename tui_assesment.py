import os
import json
import requests
from dotenv import load_dotenv
from textual.app import App
from textual.widgets import Button, Input, Label, Select, Checkbox, ListView, ListItem
from textual.containers import Container

load_dotenv(dotenv_path="questions/formbricks/.env")

BASEURL = os.getenv("FORMBRICKS_BASEURL")
API_KEY = os.getenv("FORMBRICKS_API_KEY")
ENV_ID = os.getenv("FORMBRICKS_ENVIRONMENT_ID")

LEVEL_FILE_MAP = {
    "0": "questions/formbricks/funnel_registration_formbricks.json",
    "1": "questions/formbricks/basic_formbricks.json",
    "2": "questions/formbricks/medium_formbricks.json",
    "3": "questions/formbricks/advanced_formbricks.json",
}


def convert_to_object_format(data):
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


def get_surveys():
    headers = {"x-api-key": API_KEY}
    response = requests.get(f"{BASEURL}/api/v1/management/surveys", headers=headers)
    if response.ok:
        return response.json().get("data", [])
    return []


def update_survey_status(survey_id, status):
    headers = {"Content-Type": "application/json", "x-api-key": API_KEY}
    payload = {"status": status}
    response = requests.put(
        f"{BASEURL}/api/v1/management/surveys/{survey_id}",
        json=payload,
        headers=headers,
    )
    return response.ok


class SurveyApp(App):
    CSS = """
    App {
        background: #303446;
        color: #c6d0f5;
    }
    Button {
        background: #8caaee;
        color: #303446;
    }
    Input {
        background: #414559;
        color: #c6d0f5;
        border: solid #8caaee;
    }
    Label {
        color: #c6d0f5;
    }
    CheckBox {
        color: #c6d0f5;
    }
    Select {
        background: #414559;
        color: #c6d0f5;
        border: solid #8caaee;
    }
    ListView {
        background: #414559;
        color: #c6d0f5;
        border: solid #8caaee;
    }
    """

    def compose(self):
        yield Container(
            Label("Company:"),
            Input(placeholder="e.g. Aptiv", id="company"),
            Label("Start Date:"),
            Input(placeholder="YYYY-MM-DD", id="start_date"),
            Label("End Date:"),
            Input(placeholder="YYYY-MM-DD", id="end_date"),
            Label("Brand Color:"),
            Input(value="#ff5733", id="brand_color"),
            Label("Levels to Generate:"),
            Checkbox(
                "Funnel (0) - Mandatory unless unchecked", id="level0", value=True
            ),
            Checkbox("Basic (1)", id="level1"),
            Checkbox("Medium (2)", id="level2"),
            Checkbox("Advanced (3)", id="level3"),
            Button("Generate Selected", id="generate"),
            Button("List Surveys", id="list"),
            ListView(id="survey_list"),
            Label("Select Status for Update:"),
            Select(
                [
                    ("draft", "Draft"),
                    ("inProgress", "In Progress"),
                    ("paused", "Paused"),
                    ("completed", "Completed"),
                ],
                id="new_status",
            ),
            Button("Update Selected Survey", id="update"),
            Label("", id="status"),
        )

    def on_button_pressed(self, event):
        if event.button.id == "generate":
            company = self.query_one("#company").value
            start_date = self.query_one("#start_date").value
            end_date = self.query_one("#end_date").value
            brand_color = self.query_one("#brand_color").value
            levels = []
            for i in range(4):
                if self.query_one(f"#level{i}").value:
                    levels.append(str(i))
            if not levels:
                self.query_one("#status").update("No levels selected.")
                return
            for level in levels:
                file_name = LEVEL_FILE_MAP[level]
                with open(file_name, "r", encoding="utf-8") as f:
                    raw_file = json.load(f)
                raw_questions = raw_file.get("questions", [])
                questions = parse_questions(raw_questions)
                convert_to_object_format(questions)
                welcome_card = raw_file.get("welcomeCard")
                if welcome_card:
                    convert_to_object_format(welcome_card)
                endings = raw_file.get("endings", [])
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
                styling = {
                    "brandColor": {"light": brand_color, "dark": brand_color},
                    "cardBackgroundColor": {"light": "#ffffff", "dark": "#ffffff"},
                    "cardBorderColor": {"light": "#e2e8f0", "dark": "#e2e8f0"},
                    "surveyBackground": {"bg": "#f0f0f0", "bgType": "color"},
                }
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
                response = requests.post(
                    f"{BASEURL}/api/v1/management/surveys",
                    json=payload,
                    headers=headers,
                    timeout=30,
                )
                if not response.ok:
                    self.query_one("#status").update(
                        f"Error generating level {level}: {response.text}"
                    )
                    return
            self.query_one("#status").update("Surveys generated successfully!")
        elif event.button.id == "list":
            surveys = get_surveys()
            list_view = self.query_one("#survey_list")
            list_view.clear()
            for survey in surveys:
                list_view.append(
                    ListItem(
                        Label(f"{survey['name']} - {survey['status']}"), id=survey["id"]
                    )
                )
            self.query_one("#status").update("Surveys listed.")
        elif event.button.id == "update":
            list_view = self.query_one("#survey_list")
            if (
                hasattr(list_view, "selected_index")
                and list_view.selected_index is not None
            ):
                selected_item = list_view.children[list_view.selected_index]
                survey_id = selected_item.id
                new_status = self.query_one("#new_status").value
                if update_survey_status(survey_id, new_status):
                    self.query_one("#status").update("Survey status updated.")
                    # Refresh list
                    self.on_button_pressed(
                        Button.Pressed(button=Button("List", id="list"))
                    )
                else:
                    self.query_one("#status").update("Error updating status.")
            else:
                self.query_one("#status").update("No survey selected.")


if __name__ == "__main__":
    app = SurveyApp()
    app.run()
