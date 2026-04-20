# RIR API

API REST con FastAPI para un proyecto de generacion, procesamiento y analisis de respuestas impulsionales de recintos (RIR). Esta base corresponde al Milestone 0: deja definida una estructura minima ejecutable para empezar a desarrollar los modulos de senales, procesamiento y parametros acusticos.

## Instalacion

```bash
git clone <URL_DEL_REPOSITORIO>
cd rir-api
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

En Windows PowerShell:

```powershell
git clone <URL_DEL_REPOSITORIO>
cd rir-api
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
```

## Ejecucion

```bash
uvicorn app.main:app --reload
```

Tambien se puede ejecutar con:

```bash
python -m app.main
# Si tu sistema no tiene el comando python, usar: python3 -m app.main
```

Endpoints iniciales:

- `GET /`: mensaje de bienvenida de la API.
- `GET /health`: estado basico del servicio.

## Tests

```bash
pytest
```

## Estructura del proyecto

```text
rir-api/
├── pyproject.toml          # Dependencias, metadata y configuracion de herramientas
├── README.md               # Documentacion principal del proyecto
├── LICENSE                 # Licencia del repositorio
├── app/
│   ├── __init__.py
│   ├── main.py             # Punto de entrada FastAPI
│   ├── settings.py         # Configuracion con pydantic-settings
│   ├── routers/
│   │   ├── __init__.py
│   │   └── health.py       # Endpoint /health
│   ├── schemas/
│   │   └── __init__.py     # Esquemas Pydantic futuros
│   └── services/
│       └── __init__.py     # Logica de negocio futura
├── tests/
│   └── test_placeholder.py # Tests iniciales de humo
├── docs/                   # Documentacion adicional del proyecto
├── data/
│   └── .gitkeep            # Carpeta para datos de ejemplo o archivos locales no sensibles
└── .github/
    └── workflows/
        └── ci.yml          # CI basico con lint y tests
```

## Estrategia de ramas

- `main`: rama estable y protegida. Todo cambio debe entrar mediante Pull Request.
- `feature/nombre-descriptivo`: ramas para nuevas funcionalidades, por ejemplo `feature/health-endpoint`.
- `fix/nombre-descriptivo`: ramas para correcciones puntuales.
- Commits recomendados con Conventional Commits: `feat:`, `fix:`, `docs:`, `test:`, `refactor:`, `chore:`.
- Cada Pull Request debe tener descripcion breve, issue asociado cuando corresponda y tests ejecutados.
