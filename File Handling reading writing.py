from pathlib import Path
file_path = Path("C:\CUSTOMAZIATION LAB\QGIS_files.txt")
file_path.write_text("This is a start file for QGIS.\nLearning file handling in QGIS.\n", encoding="utf-8")
print("File content:")
print(file_path.read_text(encoding="utf-8"))