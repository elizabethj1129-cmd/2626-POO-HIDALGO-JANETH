#!/usr/bin/env powershell
# Script para hacer PUSH a GitHub
# Este script te guiará paso a paso

Write-Host "╔════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║      SCRIPT PARA HACER PUSH DEL PROYECTO A GITHUB         ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan

Write-Host ""
Write-Host "PASO 1: Cambiar a rama 'main' (estándar en GitHub)" -ForegroundColor Yellow

$cd_path = "C:\Users\Herobook\UEA\2626-POO-HIDALGO-JANETH\PARCIAL 2\SEMANA 11"
cd $cd_path

git branch -M main

Write-Host "✓ Rama cambiada a 'main'" -ForegroundColor Green

Write-Host ""
Write-Host "PASO 2: Solicitar información para crear remoto" -ForegroundColor Yellow
Write-Host ""

$usuario = Read-Host "¿Cuál es tu usuario de GitHub?"
$nombre_repo = Read-Host "¿Nombre del repositorio? (default: restaurante-app-semana11)"

if ([string]::IsNullOrEmpty($nombre_repo)) {
    $nombre_repo = "restaurante-app-semana11"
}

$url_github = "https://github.com/$usuario/$nombre_repo.git"

Write-Host ""
Write-Host "URL del repositorio: $url_github" -ForegroundColor Cyan

Write-Host ""
Write-Host "PASO 3: Agregar remoto" -ForegroundColor Yellow

git remote add origin $url_github

Write-Host "✓ Remoto agregado" -ForegroundColor Green

Write-Host ""
Write-Host "PASO 4: Hacer PUSH a GitHub" -ForegroundColor Yellow
Write-Host "Esto puede pedir tu contraseña o token de GitHub..." -ForegroundColor Gray

git push -u origin main

Write-Host ""
Write-Host "╔════════════════════════════════════════════════════════════╗" -ForegroundColor Green
Write-Host "║                  ✅ PUSH COMPLETADO ✅                    ║" -ForegroundColor Green
Write-Host "╚════════════════════════════════════════════════════════════╝" -ForegroundColor Green

Write-Host ""
Write-Host "Tu repositorio está en:" -ForegroundColor Yellow
Write-Host "$url_github" -ForegroundColor Cyan

Write-Host ""
Write-Host "Enlace para compartir con profesores:" -ForegroundColor Yellow
Write-Host "https://github.com/$usuario/$nombre_repo" -ForegroundColor Cyan

Write-Host ""
Write-Host "Próximos pasos:" -ForegroundColor Yellow
Write-Host "1. Verifica que todos los archivos estén en GitHub" -ForegroundColor Gray
Write-Host "2. Comparte el enlace con tus profesores" -ForegroundColor Gray
Write-Host "3. ¡Proyecto entregado!" -ForegroundColor Gray

