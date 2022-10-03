from pathlib import Path
src = Path('docs/plots')
dst = Path('docs/index.html')
# list of .html files in docs/plots
files = [f for f in src.glob('*.html') if f.is_file()]
print("Adding links to ", files, sep='\n')
# print parent direcory of each file
# for f in files:
#     print(f.parent.name, f.name)

# read index.html
with open(dst, 'r', encoding="utf-8") as f:
    lines = f.readlines()

# find the line that starts with <ul>
start = [i for i, s in enumerate(lines) if '<ul class="plots">' in s][0]
# print(start, lines[start])
stop = [i for i, s in enumerate(lines) if '</ul>' in s][0]
# print(stop, lines[stop])
list_items = []
for f in files:
    list_items.append(f'\t\t\t<li><a href="{f.parent.name}/{f.name}">{f.stem.replace("_", " ").capitalize()}</a></li>\n')
# print(list_items)
new_lines = lines[:start+1] + list_items + lines[stop:]
# print(new_lines)
with open(dst, 'w', encoding="utf-8") as f:
    f.writelines(new_lines)