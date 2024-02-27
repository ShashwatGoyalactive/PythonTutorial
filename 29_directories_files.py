from pathlib import Path

path = Path('ecommerce')
print(path.exists())


path2 = Path('emails')
# for creating a directory
# print(path2.mkdir())

# for deleting a directory
# print(path2.rmdir())

# searching for all the files in current directory

print(path.glob('*.py'))
print((path.glob('x.xlsx')))

for file in path.glob('*.py'):
    print(file)