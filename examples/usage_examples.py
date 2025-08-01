#!/usr/bin/env python3
"""
Example usage of Count PDF Page package.
"""

import os
import tempfile
from count_pdf_page import count_pdf_pages, process_directory, generate_markdown_report


def example_single_file():
    """Example: Count pages in a single PDF file."""
    print("=== Single File Example ===")
    
    # Replace with path to an actual PDF file
    pdf_path = "example.pdf"
    
    if os.path.exists(pdf_path):
        try:
            page_count = count_pdf_pages(pdf_path)
            if page_count > 0:
                print(f"📄 {pdf_path}: {page_count} pages")
            else:
                print(f"❌ Error reading {pdf_path}")
        except FileNotFoundError:
            print(f"❌ File not found: {pdf_path}")
    else:
        print(f"⚠️  Example file '{pdf_path}' not found. Please create a PDF file or modify the path.")


def example_directory_processing():
    """Example: Process all PDFs in a directory."""
    print("\n=== Directory Processing Example ===")
    
    # Use current directory as example
    target_dir = "."
    
    try:
        results, total_pages = process_directory(target_dir)
        
        if results:
            print(f"📁 Found {len(results)} PDF files in '{target_dir}'")
            print(f"📊 Total pages: {total_pages}")
            
            print("\nFile details:")
            for filename, page_count in results:
                status = f"{page_count} pages" if isinstance(page_count, int) else "Error"
                print(f"  📄 {filename}: {status}")
        else:
            print(f"❌ No PDF files found in '{target_dir}'")
            
    except Exception as e:
        print(f"❌ Error processing directory: {e}")


def example_markdown_report():
    """Example: Generate a markdown report."""
    print("\n=== Markdown Report Example ===")
    
    # Example data
    sample_results = [
        ("document1.pdf", 25),
        ("presentation.pdf", 45),
        ("manual.pdf", 120),
        ("corrupted.pdf", "Error"),
    ]
    
    total_pages = sum(count for _, count in sample_results if isinstance(count, int))
    
    # Generate report
    report = generate_markdown_report(sample_results, total_pages)
    
    print("Generated markdown report:")
    print("-" * 40)
    print(report)
    print("-" * 40)
    
    # Save to file
    output_file = "example_report.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"📝 Report saved to: {output_file}")


def main():
    """Run all examples."""
    print("🚀 Count PDF Page - Examples")
    print("=" * 50)
    
    example_single_file()
    example_directory_processing()
    example_markdown_report()
    
    print("\n✅ Examples completed!")
    print("\nFor more information, see:")
    print("  - README.md")
    print("  - Command line: count-pdf-page --help")


if __name__ == "__main__":
    main()
