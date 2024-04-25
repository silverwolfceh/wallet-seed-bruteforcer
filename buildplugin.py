import os
import py_compile

MODULE_PATH = "coinspecific"

def make_modules():
	for root, dirs, files in os.walk(MODULE_PATH):
		for file in files:
			if file.endswith(".py"):  # Check if the file is a Python file
				file_path = os.path.join(root, file)
				print(f"Compiling {file_path}...")
				try:
					py_compile.compile(file_path, cfile=os.path.join(root, file) + "c")
					print("Compilation successful!")
				except py_compile.PyCompileError as e:
					print(f"Compilation failed for {file_path}: {e}")

if __name__ == "__main__":
	make_modules()