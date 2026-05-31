#!/usr/bin/env python3
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
JSON_DIR = BASE_DIR / "json"
OUT_DIR = Path(__file__).parent

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def build_html(questions, title, level_name, score_info=""):
    cards = []
    for q in questions:
        qid = q["id"]
        cat = q.get("category", "")
        qtype = q.get("type", "")
        desc = q.get("description", "")
        text = q.get("question", "")
        opts = q.get("options", [])
        correct = q.get("correct_index")
        score = q.get("score", 1)
        reasoning = q.get("reasoning", "")

        opt_html = ""
        for i, opt in enumerate(opts):
            checked = "checked" if i == correct else ""
            opt_html += f"""
            <label class="option {'correct' if i == correct else ''}">
                <input type="radio" name="{qid}" value="{i}" {checked}>
                <span>{opt}</span>
            </label>"""

        card = f"""
        <div class="card" data-category="{cat}">
            <div class="card-header">
                <span class="badge badge-cat">{cat}</span>
                <span class="badge badge-type">{qtype}</span>
                <span class="badge badge-score">{score} pt(s)</span>
            </div>
            {f'<div class="description">{desc}</div>' if desc else ""}
            <div class="question-text">{text}</div>
            <div class="options">{opt_html}</div>
            {f'<div class="reasoning"><strong>Explicación:</strong> {reasoning}</div>' if reasoning else ""}
        </div>"""
        cards.append(card)

    body = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{
    font-family: 'Segoe UI', system-ui, sans-serif;
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    color: #e0e0e0;
    min-height: 100vh;
    padding: 2rem 1rem;
}}
.container {{ max-width: 900px; margin: 0 auto; }}
h1 {{
    text-align: center;
    font-size: 2rem;
    margin-bottom: 0.5rem;
    background: linear-gradient(90deg, #a6d189, #8caaee, #f4b8e4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}}
.subtitle {{
    text-align: center;
    color: #a5adce;
    margin-bottom: 2rem;
}}
.score-info {{
    text-align: center;
    background: rgba(138, 170, 238, 0.1);
    border: 1px solid #8caaee44;
    border-radius: 12px;
    padding: 1rem;
    margin-bottom: 2rem;
}}
.card {{
    background: rgba(65, 69, 89, 0.7);
    backdrop-filter: blur(10px);
    border: 1px solid #414559;
    border-radius: 16px;
    padding: 1.5rem;
    margin-bottom: 1.5rem;
    transition: border-color 0.2s;
}}
.card:hover {{ border-color: #8caaee88; }}
.card-header {{
    display: flex;
    gap: 0.5rem;
    margin-bottom: 1rem;
    flex-wrap: wrap;
}}
.badge {{
    padding: 0.25rem 0.75rem;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 600;
    text-transform: uppercase;
}}
.badge-cat {{ background: #8caaee33; color: #8caaee; }}
.badge-type {{ background: #a6d18933; color: #a6d189; }}
.badge-score {{ background: #f4b8e433; color: #f4b8e4; }}
.description {{
    font-size: 0.9rem;
    color: #a5adce;
    margin-bottom: 0.75rem;
    font-style: italic;
}}
.question-text {{
    font-size: 1.1rem;
    font-weight: 500;
    margin-bottom: 1rem;
    line-height: 1.5;
}}
.options {{
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}}
.option {{
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.75rem 1rem;
    background: rgba(30, 30, 60, 0.5);
    border-radius: 10px;
    cursor: pointer;
    transition: background 0.2s;
}}
.option:hover {{ background: rgba(138, 170, 238, 0.15); }}
.option.correct {{
    background: rgba(166, 209, 137, 0.15);
    border: 1px solid #a6d18944;
}}
.option input[type="radio"] {{
    accent-color: #8caaee;
    width: 16px; height: 16px;
}}
.reasoning {{
    margin-top: 1rem;
    padding: 0.75rem;
    background: rgba(244, 184, 228, 0.08);
    border-left: 3px solid #f4b8e4;
    border-radius: 8px;
    font-size: 0.85rem;
    color: #b5bfe2;
}}
.filter-bar {{
    display: flex;
    gap: 0.5rem;
    margin-bottom: 1.5rem;
    flex-wrap: wrap;
}}
.filter-btn {{
    padding: 0.5rem 1rem;
    border: 1px solid #414559;
    border-radius: 20px;
    background: transparent;
    color: #a5adce;
    cursor: pointer;
    font-size: 0.85rem;
    transition: all 0.2s;
}}
.filter-btn:hover, .filter-btn.active {{
    background: #8caaee33;
    border-color: #8caaee;
    color: #8caaee;
}}
.stats {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 1rem;
    margin-bottom: 2rem;
}}
.stat-box {{
    background: rgba(65, 69, 89, 0.5);
    border-radius: 12px;
    padding: 1rem;
    text-align: center;
}}
.stat-value {{
    font-size: 1.5rem;
    font-weight: 700;
    color: #8caaee;
}}
.stat-label {{
    font-size: 0.8rem;
    color: #a5adce;
    margin-top: 0.25rem;
}}
</style>
</head>
<body>
<div class="container">
    <h1>{title}</h1>
    <p class="subtitle">Assessment Técnico de Moldeo por Inyección - {level_name}</p>
    {score_info}
    <div class="filter-bar">
        <button class="filter-btn active" onclick="filterCards('all')">Todas</button>
        <button class="filter-btn" onclick="filterCards('Machine')">Máquina</button>
        <button class="filter-btn" onclick="filterCards('Process')">Proceso</button>
        <button class="filter-btn" onclick="filterCards('Quality')">Calidad</button>
        <button class="filter-btn" onclick="filterCards('Safety')">Seguridad</button>
        <button class="filter-btn" onclick="filterCards('Materials')">Materiales</button>
        <button class="filter-btn" onclick="filterCards('Efficiency')">Eficiencia</button>
        <button class="filter-btn" onclick="filterCards('Waste')">Desperdicios</button>
    </div>
    <div class="cards">{''.join(cards)}</div>
</div>
<script>
function filterCards(cat) {{
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    event.target.classList.add('active');
    document.querySelectorAll('.card').forEach(c => {{
        c.style.display = (cat === 'all' || c.dataset.category === cat) ? 'block' : 'none';
    }});
}}
</script>
</body>
</html>"""
    return body

def get_score_info(questions, total_possible):
    total_q = len(questions)
    total_score = sum(q.get("score", 1) for q in questions)
    categories = {}
    for q in questions:
        cat = q.get("category", "Other")
        categories.setdefault(cat, {"count": 0, "score": 0})
        categories[cat]["count"] += 1
        categories[cat]["score"] += q.get("score", 1)

    cat_table = "".join(
        f'<div class="stat-box"><div class="stat-value">{v["count"]}</div><div class="stat-label">{k}</div></div>'
        for k, v in sorted(categories.items())
    )

    return f"""
    <div class="stats">
        <div class="stat-box"><div class="stat-value">{total_q}</div><div class="stat-label">Preguntas</div></div>
        <div class="stat-box"><div class="stat-value">{total_score}</div><div class="stat-label">Puntaje Total</div></div>
        <div class="stat-box"><div class="stat-value">{len(categories)}</div><div class="stat-label">Categorías</div></div>
    </div>
    <div class="stats">{cat_table}</div>"""

def main():
    assessments = [
        ("Básico", "basic_v2.json", "Nivel Básico (Operadores)"),
        ("Intermedio", "medium_v2.json", "Nivel Intermedio (Técnicos)"),
        ("Avanzado", "advanced_v2.json", "Nivel Avanzado (Ingenieros)"),
    ]

    for level_name, filename, title_suffix in assessments:
        data = load_json(JSON_DIR / filename)
        html = build_html(
            questions=data,
            title=f"CAROL - Evaluación Técnica de Moldeo",
            level_name=level_name,
            score_info=get_score_info(data, None),
        )
        out_path = OUT_DIR / f"{level_name.lower()}_assesment.html"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"✓ {out_path.name} generado ({len(data)} preguntas)")

    print("\n✅ Todos los HTML generados!")

if __name__ == "__main__":
    main()
