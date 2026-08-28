# Script de Push a GitHub para restaurante_app Semana 11

Write-Host ""
Write-Host "╔════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║          SCRIPT DE PUSH A GITHUB - SEMANA 11              ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

# Cambiar a la carpeta del proyecto
$carpeta = "C:\Users\Herobook\UEA\2626-POO-HIDALGO-JANETH\PARCIAL 2\SEMANA 11"
Set-Location $carpeta

# Solicitar usuario de GitHub
Write-Host "PASO 1: Ingresar credenciales de GitHub" -ForegroundColor Yellow
Write-Host ""
$usuario = Read-Host "  Tu usuario de GitHub"

if ([string]::IsNullOrWhiteSpace($usuario)) {
    Write-Host "Error: Usuario no puede estar vacío" -ForegroundColor Red
    exit 1
}

Write-Host "  Nombre del repositorio (default: restaurante-app-semana11)" -ForegroundColor Gray
$repo = Read-Host "  Repositorio"

if ([string]::IsNullOrWhiteSpace($repo)) {
    $repo = "restaurante-app-semana11"
}

$url = "https://github.com/$usuario/$repo.git"

Write-Host ""
Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor Gray
Write-Host "Configuracion:" -ForegroundColor Yellow
Write-Host "  Usuario: $usuario" -ForegroundColor Green
Write-Host "  Repositorio: $repo" -ForegroundColor Green
Write-Host "  URL: $url" -ForegroundColor Green
Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor Gray
Write-Host ""

# Paso 2: Verificar rama main
Write-Host "PASO 2: Verificar rama 'main'..." -ForegroundColor Yellow
git branch -M main
Write-Host "✓ Rama configurada como 'main'" -ForegroundColor Green
Write-Host ""

# Paso 3: Agregar remoto
Write-Host "PASO 3: Configurar remoto..." -ForegroundColor Yellow
$remotoExiste = git config --get remote.origin.url
if ($remotoExiste) {
    Write-Host "  Remoto ya existe, actualizando..." -ForegroundColor Gray
    git remote set-url origin $url
} else {
    git remote add origin $url
}
Write-Host "✓ Remoto configurado" -ForegroundColor Green
Write-Host ""

# Paso 4: Hacer push
Write-Host "PASO 4: Hacer PUSH a GitHub..." -ForegroundColor Yellow
Write-Host "  (Puede pedir tu contraseña o token de acceso personal)" -ForegroundColor Gray
Write-Host ""

git push -u origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "╔════════════════════════════════════════════════════════════╗" -ForegroundColor Green
    Write-Host "║              ✅ PUSH COMPLETADO EXITOSAMENTE              ║" -ForegroundColor Green
    Write-Host "╚════════════════════════════════════════════════════════════╝" -ForegroundColor Green
    Write-Host ""
    Write-Host "Tu repositorio está en:" -ForegroundColor Yellow
    Write-Host "https://github.com/$usuario/$repo" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Puedes compartir este enlace con tus profesores." -ForegroundColor Green
    Write-Host ""
} else {
    Write-Host ""
    Write-Host "╔════════════════════════════════════════════════════════════╗" -ForegroundColor Red
    Write-Host "║                   ✗ ERROR EN EL PUSH                      ║" -ForegroundColor Red
    Write-Host "╚════════════════════════════════════════════════════════════╝" -ForegroundColor Red
    Write-Host ""
    Write-Host "Verifica:" -ForegroundColor Yellow
    Write-Host "  1. Que el repositorio exista en GitHub: https://github.com/new" -ForegroundColor Gray
    Write-Host "  2. Tu usuario y contraseña/token sean correctos" -ForegroundColor Gray
    Write-Host "  3. El repositorio sea PÚBLICO" -ForegroundColor Gray
    Write-Host "  4. Permisos en GitHub" -ForegroundColor Gray
    Write-Host ""
    exit 1
}

