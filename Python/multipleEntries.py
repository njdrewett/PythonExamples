# multiple inputs for a list
entries = []
while True:
    # get keyboard input
    print('Enter a name (or blank to finish)')
    entry = input()
    if(entry == ''):
        break
    entries = entries + [entry]
print('The entries are:')
for entry in entries:
    print(' ' + entry)

if 'entry1' in entries:
    print('entry1 is in the list')
if 'entryz' not in entries:
    print('entryz is not in the list')

cat = ['fat','grey','loud']
size,colour,character = cat
print('The cat is ' + colour)
