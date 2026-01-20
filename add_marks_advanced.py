import re

correct_indices = [3,2,2,2,1,1,1,1,2,1,2,2,2,2,2,1,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1]

with open('questions/markdown/Advanced_assesment.md', 'r', encoding='utf-8') as f:
    content = f.read()

questions = re.split(r'(?=### \d+\.)', content)

new_questions = []

q_num = 0

for q in questions:
    if not q.strip():
        continue
    lines = q.split('\n')
    options = []
    in_options = False
    for i, line in enumerate(lines):
        if line.startswith('- '):
            if not in_options:
                in_options = True
            options.append(i)
    if q_num < len(correct_indices):
        correct_idx = correct_indices[q_num] - 1  # 0-based
        if correct_idx < len(options):
            lines[options[correct_idx]] += ' ✅'
    new_questions.append('\n'.join(lines))
    q_num += 1

new_content = ''.join(new_questions)

with open('questions/markdown/Advanced_assesment.md', 'w', encoding='utf-8') as f:
    f.write(new_content)
