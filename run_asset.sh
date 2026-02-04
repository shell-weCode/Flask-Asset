#!/bin/bash
set -e

# 1. Verifica si python3 está instalado
if ! command -v python3 &> /dev/null; then
    echo "Python3 no está instalado. Instala Python 3.13+."
    exit 1
fi

# 2. Crear virtualenv
python3 -m venv venv
source venv/bin/activate

# 3. Crear Wheel
pip install --upgrade pip setuptools wheel
python3 setup.py bdist_wheel

# 4. Instalar el wheel
pip install --upgrade pip
pip install dist/*.whl

# 5. Ejecutar pytest
pytest -vv tests/
