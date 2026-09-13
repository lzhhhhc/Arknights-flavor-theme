# 明日方舟皮肤插件 — 新机器一键安装脚本
# 用法：在新电脑上把整个 dsh-arknights-skin 文件夹放到任意位置，
#       右键此文件 → "使用 PowerShell 运行"，或执行：
#       powershell -ExecutionPolicy Bypass -File install-new-machine.ps1
# 前提：DSH Desktop 至少启动过一次（生成了 ~/.dsh/profiles），并已安装 pnpm (npm i -g pnpm)

$ErrorActionPreference = "Stop"
$pluginSrc = Split-Path -Parent $MyInvocation.MyCommand.Path
$dsh = Join-Path $env:USERPROFILE ".dsh"
$pluginDst = Join-Path $dsh "plugins\dsh-arknights-skin"
$pkgName = "@dsh-external/dsh-client-ui-skin-arknights"

if (-not (Test-Path $dsh)) {
    Write-Host "[x] 未找到 $dsh — 请先启动一次 DSH Desktop 再运行本脚本" -ForegroundColor Red
    exit 1
}

# 1) 复制插件目录（覆盖旧版）
New-Item -ItemType Directory -Force -Path (Split-Path -Parent $pluginDst) | Out-Null
if (Test-Path $pluginDst) { Remove-Item -Recurse -Force $pluginDst }
Copy-Item -Recurse -Force $pluginSrc $pluginDst
Write-Host "[ok] 插件已复制到 $pluginDst" -ForegroundColor Green

# 2) 注册到 web / desktop 两个 profile 的 package.json
foreach ($profileName in @("web", "desktop")) {
    $pkgPath = Join-Path $dsh "profiles\$profileName\package.json"
    if (-not (Test-Path $pkgPath)) {
        Write-Host "[..] 跳过 $profileName（$pkgPath 不存在）" -ForegroundColor Yellow
        continue
    }
    $pkg = Get-Content $pkgPath -Raw | ConvertFrom-Json
    $changed = $false
    if (-not $pkg.dependencies.PSObject.Properties[$pkgName]) {
        $pkg.dependencies | Add-Member -NotePropertyName $pkgName -NotePropertyValue "file:../../plugins/dsh-arknights-skin"
        $changed = $true
    }
    if ($pkg.dsh.profile.bundles -notcontains $pkgName) {
        $pkg.dsh.profile.bundles += $pkgName
        $changed = $true
    }
    if ($changed) {
        $pkg | ConvertTo-Json -Depth 20 | Set-Content $pkgPath -Encoding UTF8
        Write-Host "[ok] $profileName profile 已注册" -ForegroundColor Green
    } else {
        Write-Host "[ok] $profileName profile 此前已注册" -ForegroundColor Green
    }
    # 3) 刷新依赖
    Push-Location (Join-Path $dsh "profiles\$profileName")
    pnpm install --prefer-offline
    Pop-Location
}

Write-Host ""
Write-Host "完成。重启 DSH Desktop 即可生效。" -ForegroundColor Cyan
