files = ["__init__.py", "intra.h", "main.c", "define.h", "run.py"]

for file in files:
  if file.split(".")[-1] == "h" or file.split(".")[-1] == "c":
    print(file)
