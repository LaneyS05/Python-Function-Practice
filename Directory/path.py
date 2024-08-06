from pathlib import Path

path = Path('file.py')
path2 = Path('emails')
path3 = Path()

print(path.exists())
#print(path2.rmdir()) 
for file in path3.glob('*.py'):
    print(file)

# mkdir will create a new directory
# rmdir will delete a new directory