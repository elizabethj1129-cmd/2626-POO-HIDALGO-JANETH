@echo off
REM Script para hacer push a GitHub - restaurante_app Semana 11

setlocal enabledelayedexpansion

echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║          SCRIPT DE PUSH A GITHUB - SEMANA 11              ║
echo ╚════════════════════════════════════════════════════════════╝
echo.

cd "C:\Users\Herobook\UEA\2626-POO-HIDALGO-JANETH\PARCIAL 2\SEMANA 11"

echo Ingresa tu usuario de GitHub:
set /p USUARIO="Usuario: "

if "%USUARIO%"=="" (
    echo Error: Usuario no puede estar vacío
    pause
    exit /b 1
)

echo.
echo Nombre del repositorio (default: restaurante-app-semana11):
set /p REPO="Repositorio: "

if "%REPO%"=="" (
    set REPO=restaurante-app-semana11
)

set URL=https://github.com/%USUARIO%/%REPO%.git

echo.
echo ═══════════════════════════════════════════════════════════
echo Configuración:
echo  - Usuario: %USUARIO%
echo  - Repositorio: %REPO%
echo  - URL: %URL%
echo ═══════════════════════════════════════════════════════════
echo.

echo Paso 1: Verificar que la rama sea 'main'...
git branch -M main
echo ✓ Rama configurada como 'main'
echo.

echo Paso 2: Agregar remoto...
git remote add origin %URL%
if errorlevel 1 (
    echo Remoto ya existe, actualizando...
    git remote set-url origin %URL%
)
echo ✓ Remoto configurado
echo.

echo Paso 3: Hacer PUSH a GitHub...
echo (Puede pedir tu contraseña o token de acceso)
echo.
git push -u origin main

if errorlevel 1 (
    echo.
    echo ✗ Error en el push. Verifica:
    echo  1. Que el repositorio exista en GitHub (https://github.com/new)
    echo  2. Tu usuario y contraseña/token sean correctos
    echo  3. El repositorio sea público
    pause
    exit /b 1
)

echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║              ✅ PUSH COMPLETADO EXITOSAMENTE              ║
echo ╚════════════════════════════════════════════════════════════╝
echo.
echo Tu repositorio está en:
echo https://github.com/%USUARIO%/%REPO%
echo.
echo Puedes compartir este enlace con tus profesores.
echo.
pause

