#!/usr/bin/env python3
import os, re, sys
from pathlib import Path

def fix_px(content):
    return re.sub(r'(\d+)px', r'\1dp', content)

def fix_left_right(content):
    replacements = {
        'paddingLeft': 'paddingStart',
        'paddingRight': 'paddingEnd',
        'layout_marginLeft': 'layout_marginStart',
        'layout_marginRight': 'layout_marginEnd'
    }
    for old, new in replacements.items():
        content = content.replace(old, new)
    return content

def apply_fixes(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except:
        return False
    original = content
    content = fix_px(content)
    content = fix_left_right(content)
    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main(repo_root):
    fixed_files = []
    for ext in ['*.xml', '*.kt', '*.java']:
        for file_path in Path(repo_root).rglob(ext):
            if apply_fixes(file_path):
                fixed_files.append(str(file_path))
    return fixed_files

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 auto_fix.py /ruta/al/repo")
        sys.exit(1)
    fixed = main(sys.argv[1])
    if fixed:
        print("✅ Archivos corregidos:")
        for f in fixed:
            print(f"  - {f}")
    else:
        print("✅ No se encontraron violaciones auto-corregibles.")
