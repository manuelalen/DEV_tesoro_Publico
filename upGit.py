from github import Github, InputFileContent
import os
import json

# Credenciales de GitHub
ACCESS_TOKEN = 'github_pat_'
REPO_NAME = 'manuelalen.github.io/data'

# Crea una instancia de GitHub y obtiene el repositorio
g = Github(ACCESS_TOKEN)
repo = g.get_user().get_repo(REPO_NAME)

# Ruta local del archivo a subir
file_path = 'datos.json'

# Nombre de la nueva rama
branch_name = "mi_nueva_rama"

# Elimina la rama si ya existe
try:
    ref = repo.get_git_ref(f"heads/{branch_name}")
    ref.delete()
except:
    pass

# Crea una nueva rama para subir los cambios
branch = repo.get_branch(repo.default_branch)
new_branch = repo.create_git_ref(ref=f"refs/heads/{branch_name}", sha=branch.commit.sha)

# Lee el contenido del archivo y crea un objeto de tipo `InputFileContent`
with open(file_path, 'rb') as file:
    content = file.read().decode()
input_file = InputFileContent(content)


# Crea un nuevo objeto `InputFileContent` para el archivo
file_name = os.path.basename(file_path)
commit_message = f"Agregando archivo {file_name}"
new_file = repo.create_file(path=file_name, message=commit_message, content=json.dumps(content), branch=branch_name)

# Cierra la rama
repo.merge(new_branch.ref, branch.name)
