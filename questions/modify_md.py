import re


def modify_md(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Split by questions, assuming ### \d+\.
    questions = re.split(r"(?=### \d+\.)", content)

    modified_questions = []
    for q in questions:
        if not q.strip():
            continue
        # Find the options
        lines = q.split("\n")
        options_start = None
        rational_start = None
        for i, line in enumerate(lines):
            if line.startswith("- "):
                if options_start is None:
                    options_start = i
            if line.startswith("**Racional:**"):
                rational_start = i
                break
        if options_start is not None and rational_start is not None:
            options = lines[options_start:rational_start]
            rational = lines[rational_start:]
            # Find the correct option
            correct_option = None
            for opt in options:
                if "✅" in opt:
                    correct_option = opt.replace(" ✅", "").strip()
                    break
            if correct_option:
                # Remove ✅ from options
                options = [opt.replace(" ✅", "") for opt in options]
                # Create details
                details = (
                    [
                        "<details>",
                        "<summary>Respuesta Correcta</summary>",
                        "",
                        correct_option + " ✅",
                        "",
                    ]
                    + rational
                    + ["</details>"]
                )
                # Replace the part
                lines = lines[:options_start] + options + [""] + details
                q = "\n".join(lines)
        modified_questions.append(q)

    modified_content = "".join(modified_questions)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(modified_content)


if __name__ == "__main__":
    modify_md("markdown/Medium_assesment.md")
    modify_md("markdown/Advanced_assesment.md")
