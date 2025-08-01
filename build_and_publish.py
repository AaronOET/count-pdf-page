#!/usr/bin/env python3
"""
Build and publish script for Count PDF Page package.
"""

import subprocess
import sys
import os
import shutil
import stat
from pathlib import Path


def run_command(command, description):
    """Run a command and handle errors."""
    print(f"\n🔨 {description}...")
    try:
        subprocess.run(
            command, 
            shell=True, 
            check=True, 
            capture_output=True, 
            text=True, 
            encoding='utf-8', 
            errors='replace'
        )
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"Command: {command}")
        print(f"Return code: {e.returncode}")
        if e.stderr:
            print(f"Error output: {e.stderr}")
        return False


def handle_remove_readonly(func, path, exc):
    """Error handler for removing read-only files on Windows."""
    if os.path.exists(path):
        os.chmod(path, stat.S_IWRITE)
        func(path)


def clean_build():
    """Clean build artifacts."""
    print("\n🧹 Cleaning build artifacts...")
    
    dirs_to_clean = ['build', 'dist', 'src/count_pdf_page.egg-info']
    
    for dir_path in dirs_to_clean:
        if os.path.exists(dir_path):
            try:
                # Try to make files writable before deletion
                for root, dirs, files in os.walk(dir_path):
                    for d in dirs:
                        os.chmod(os.path.join(root, d), 0o755)
                    for f in files:
                        os.chmod(os.path.join(root, f), 0o644)
                shutil.rmtree(dir_path, onerror=handle_remove_readonly)
                print(f"Removed {dir_path}")
            except Exception as e:
                print(f"Warning: Could not remove {dir_path}: {e}")
    
    # Also clean any other egg-info directories
    for item in Path("src").glob("*.egg-info"):
        if item.is_dir():
            try:
                shutil.rmtree(item, onerror=handle_remove_readonly)
                print(f"Removed {item}")
            except Exception as e:
                print(f"Warning: Could not remove {item}: {e}")
    
    print("✅ Build artifacts cleaned")


def main():
    """Main build and publish workflow."""
    print("🚀 Count PDF Page - Build and Publish Script")
    print("=" * 50)
    
    # Ensure we're in the package directory
    package_dir = Path(__file__).parent
    os.chdir(package_dir)
    
    # Clean previous builds
    clean_build()
    
    # Install build dependencies
    if not run_command("pip install --upgrade build twine", "Installing build dependencies"):
        sys.exit(1)
    
    # Run tests
    if not run_command("python -m pytest tests/", "Running tests"):
        print("⚠️  Tests failed. Please fix issues before publishing.")
        answer = input("Continue anyway? (y/N): ")
        if answer.lower() != 'y':
            sys.exit(1)
    
    # Type checking
    if not run_command("mypy src", "Type checking"):
        print("⚠️  Type checking failed.")
        answer = input("Continue anyway? (y/N): ")
        if answer.lower() != 'y':
            sys.exit(1)
    
    # Code formatting check
    if not run_command("black --check src tests", "Checking code formatting"):
        print("⚠️  Code formatting issues found.")
        answer = input("Auto-format code? (Y/n): ")
        if answer.lower() != 'n':
            run_command("black src tests", "Formatting code")
    
    # Build the package using pip wheel which works better with file permissions
    if not run_command("python -m pip wheel . --no-deps --wheel-dir dist", "Building package wheel"):
        # If wheel build fails, try to force clean and rebuild
        print("Retrying build after thorough cleanup...")
        clean_build()
        if not run_command("python -m pip wheel . --no-deps --wheel-dir dist", "Building package wheel (retry)"):
            sys.exit(1)
    
    # Create source distribution using modern build system
    if not run_command("python -m build --sdist --outdir dist", "Building source distribution"):
        print("⚠️  Source distribution build failed, but wheel succeeded.")
    
    # Check the built package
    if not run_command("twine check dist/*", "Checking built package"):
        sys.exit(1)
    
    print("\n🎉 Package built successfully!")
    print("\nBuilt files:")
    for file in os.listdir("dist"):
        print(f"  - dist/{file}")
    
    # Ask about publishing
    print("\nPublishing options:")
    print("1. Test PyPI (recommended for testing)")
    print("2. Production PyPI")
    print("3. Skip publishing")
    
    choice = input("\nChoose an option (1-3): ")
    
    if choice == "1":
        print("\n📦 Publishing to Test PyPI...")
        if run_command("twine upload --repository testpypi dist/*", "Uploading to Test PyPI"):
            print("✅ Package published to Test PyPI!")
            print("Install with: pip install --index-url https://test.pypi.org/simple/count-pdf-page")
    
    elif choice == "2":
        confirmation = input("\n⚠️  Are you sure you want to publish to production PyPI? (type 'yes' to confirm): ")
        if confirmation == "yes":
            if run_command("twine upload dist/*", "Uploading to PyPI"):
                print("✅ Package published to PyPI!")
                print("Install with: pip install count-pdf-page")
        else:
            print("Publication cancelled.")
    
    else:
        print("Skipping publication.")
    
    print("\n🏁 Build script completed!")


if __name__ == "__main__":
    main()
