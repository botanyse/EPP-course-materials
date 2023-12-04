from tools import convert_lod_to_dol, convert_dol_to_lod, create_markdown_table

students_lod = [
    {"name": "Robin", "github_name": "ProgrammingGod42"},
    {"name": "Kim", "github_name": "CodingKim"},
    {"name": "Jesse", "github_name": "JavascriptJesse"},
]

students_dol = {
    "name": ["Robin", "Kim", "Jesse"],
    "github_name": ["ProgrammingGod42", "CodingKim", "JavascriptJesse"],
}

print(create_markdown_table(students_dol))
print(create_markdown_table(students_lod))

print(convert_dol_to_lod(students_dol))
print(convert_lod_to_dol(students_lod))
print(convert_lod_to_dol(convert_dol_to_lod(students_dol)))
print(convert_dol_to_lod(convert_lod_to_dol(students_lod)))
