# PowerShell script to install and test the PDF Page Counter package

Write-Host "🚀 Count PDF Page - Installation and Testing Script" -ForegroundColor Green
Write-Host "=" * 60 -ForegroundColor Green

# Check if Python is available
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✅ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python not found. Please install Python 3.9+ first." -ForegroundColor Red
    exit 1
}

# Check if pip is available
try {
    $pipVersion = pip --version 2>&1
    Write-Host "✅ pip found: $pipVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ pip not found. Please install pip first." -ForegroundColor Red
    exit 1
}

Write-Host "`n🔧 Installing package in development mode..." -ForegroundColor Yellow

# Install the package in development mode
try {
    pip install -e ".[dev]"
    Write-Host "✅ Package installed successfully" -ForegroundColor Green
} catch {
    Write-Host "❌ Failed to install package" -ForegroundColor Red
    exit 1
}

Write-Host "`n🧪 Running tests..." -ForegroundColor Yellow

# Run tests
try {
    pytest tests/ -v
    Write-Host "✅ Tests completed" -ForegroundColor Green
} catch {
    Write-Host "⚠️  Some tests may have failed" -ForegroundColor Yellow
}

Write-Host "`n🎯 Testing CLI command..." -ForegroundColor Yellow

# Test the CLI command
try {
    count-pdf-page --help
    Write-Host "✅ CLI command working" -ForegroundColor Green
} catch {
    Write-Host "❌ CLI command failed" -ForegroundColor Red
}

Write-Host "`n🏁 Installation and testing completed!" -ForegroundColor Green
Write-Host "`nYou can now use:" -ForegroundColor Cyan
Write-Host "  count-pdf-page                 # Count PDFs in current directory" -ForegroundColor Gray
Write-Host "  count-pdf-page /path/to/pdfs   # Count PDFs in specific directory" -ForegroundColor Gray
Write-Host "  count-pdf-page --help          # Show help" -ForegroundColor Gray
