# Guia para trabajar con el repositorio RIR API

Esta guia explica como descargar el proyecto, ejecutarlo y trabajar con ramas sin romper la rama principal.

## Importante

- No trabajar directamente sobre la rama `main`.
- Cada tarea se hace en una rama nueva.
- Cuando terminan, suben la rama y crean un Pull Request en GitHub.
- Si no entienden algo, pregunten antes de hacer cambios grandes.

## 1. Programas necesarios

Instalar estos programas:

1. Python 3.11 o superior

   Descargar desde: <https://www.python.org/downloads/>

   Durante la instalacion, marcar la opcion:

   ```text
   Add Python to PATH
   ```

2. Git

   Descargar desde: <https://git-scm.com/downloads>

3. Visual Studio Code

   Descargar desde: <https://code.visualstudio.com/>

## 2. Descargar el proyecto

Con PowerShell, abrir una terminal en la carpeta donde quieran guardar el proyecto y ejecutar:

```powershell
git clone URL_DEL_REPOSITORIO
cd rir-api
```

Reemplazar `URL_DEL_REPOSITORIO` por la URL real del repo de GitHub.

Ejemplo:

```powershell
git clone https://github.com/usuario/rir-api.git
cd rir-api
```

## 3. Crear el entorno virtual

Dentro de la carpeta del proyecto, abrir PowerShell y ejecutar:

```powershell
py -m venv .venv
```

Activar el entorno virtual:

```powershell
.\.venv\Scripts\Activate.ps1
```

Si PowerShell muestra un error de permisos al activar el entorno, ejecutar una sola vez:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Despues volver a activar:

```powershell
.\.venv\Scripts\Activate.ps1
```

Cuando el entorno esta activo, la terminal muestra algo como:

```powershell
(.venv) PS C:\...\rir-api>
```

## 4. Instalar dependencias

Con el entorno virtual activado, ejecutar:

```powershell
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Esto instala FastAPI, pytest, ruff y el resto de dependencias del proyecto.

## 5. Ejecutar la API

Con el entorno virtual activado:

```powershell
uvicorn app.main:app --reload
```

Despues abrir en el navegador:

<http://127.0.0.1:8000>

Documentacion interactiva de la API:

<http://127.0.0.1:8000/docs>

Endpoint de salud, para ver que el proyecto esta funcionando:

<http://127.0.0.1:8000/health>

Para detener el servidor, presionar:

```text
Ctrl + C
```

## 6. Ejecutar tests

Con el entorno virtual activado:

```powershell
pytest
```

Si los tests pasan, deberia aparecer algo parecido a:

```text
passed
```

## 7. Como trabajar con ramas

Regla principal:

```text
NO trabajar directo en main.
```

Antes de empezar una tarea, actualizar `main`:

```powershell
git checkout main
git pull
```

Crear una rama nueva para la tarea:

```powershell
git checkout -b feature/nombre-de-la-tarea
```

Ejemplos de nombres de ramas:

```text
feature/generacion-senales
feature/procesamiento-audio
feature/analisis-acustico
docs/diagrama-arquitectura
docs/readme-integrantes
fix/test-health
```

Despues de crear la rama, trabajar normalmente en VS Code.

## 8. Guardar cambios con commit

Ver que archivos cambiaron:

```powershell
git status
```

Agregar los cambios:

```powershell
git add .
```

Crear el commit:

```powershell
git commit -m "docs: add architecture diagram"
```

Ejemplos de mensajes de commit:

```text
docs: add group members
docs: update installation instructions
feat: add health endpoint
feat: add signal generation service
test: add api smoke tests
fix: correct import error
chore: update dependencies
```

Convencion recomendada:

| Tipo | Uso |
| --- | --- |
| `feat` | Nueva funcionalidad |
| `fix` | Correccion de error |
| `docs` | Cambios en documentacion |
| `test` | Tests |
| `chore` | Configuracion o mantenimiento |
| `refactor` | Cambio interno sin cambiar comportamiento |

## 9. Subir la rama a GitHub

La primera vez que suben una rama nueva:

```powershell
git push -u origin nombre-de-la-rama
```

Ejemplo:

```powershell
git push -u origin docs/diagrama-arquitectura
```

Despues de eso, si hacen mas commits en la misma rama, alcanza con:

```powershell
git push
```

## 10. Crear un Pull Request

Despues de subir la rama:

1. Entrar al repositorio en GitHub.
2. GitHub normalmente muestra un boton: `Compare & pull request`.
3. Hacer click.
4. Revisar que diga:

   ```text
   base: main
   compare: nombre-de-la-rama
   ```

5. Escribir una descripcion breve de lo que hicieron.
6. Crear el Pull Request.
7. Avisar al grupo para que alguien revise.

No hacer merge si no estan seguros.

## 11. Flujo completo de trabajo

Cada vez que van a empezar una tarea nueva:

```powershell
git checkout main
git pull
git checkout -b feature/nombre-de-la-tarea
```

Trabajan en VS Code.

Despues:

```powershell
git status
git add .
git commit -m "tipo: descripcion corta"
git push -u origin feature/nombre-de-la-tarea
```

Luego crean el Pull Request en GitHub.

## 12. Si usan GitHub Desktop

Flujo recomendado:

1. Abrir GitHub Desktop.
2. Seleccionar el repositorio.
3. Asegurarse de estar en `main`.
4. Hacer `Fetch origin`.
5. Hacer `Pull origin` si aparece disponible.
6. Ir a `Current branch > New branch`.
7. Crear una rama con nombre claro.
8. Abrir el proyecto en VS Code.
9. Modificar archivos.
10. Volver a GitHub Desktop.
11. Escribir mensaje de commit.
12. Click en `Commit to nombre-de-la-rama`.
13. Click en `Push origin`.
14. Click en `Create Pull Request`.

GitHub Desktop evita usar muchos comandos, pero la idea es la misma:

- `main` no se toca directamente.
- Cada tarea va en una rama.
- Los cambios entran por Pull Request.

## 13. Reglas del grupo

- Nadie pushea directo a `main`.
- Cada issue o tarea tiene su propia rama.
- Los Pull Requests deben tener descripcion breve.
- Antes de pedir merge, correr:

  ```powershell
  pytest
  ```

- Si modifican dependencias, avisar al grupo.
- Si aparece un conflicto de Git, no improvisar: pedir ayuda.

## 14. Comandos rapidos

Actualizar `main`:

```powershell
git checkout main
git pull
```

Crear rama:

```powershell
git checkout -b feature/nombre
```

Ver estado:

```powershell
git status
```

Guardar cambios:

```powershell
git add .
git commit -m "tipo: descripcion"
```

Subir rama:

```powershell
git push -u origin feature/nombre
```

Instalar proyecto:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
```

Ejecutar API:

```powershell
uvicorn app.main:app --reload
```

Ejecutar tests:

```powershell
pytest
```
