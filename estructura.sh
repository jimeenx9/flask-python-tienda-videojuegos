#!/bin/bash

echo "===== PROYECTO ====="
pwd
echo

echo "===== ESTRUCTURA ====="
tree -a -I "node_modules|vendor|.git|venv|__pycache__|dist|build|storage|cache|logs" -L 4
