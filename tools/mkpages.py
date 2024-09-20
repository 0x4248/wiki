root_folders = ['linux', 'radios', 'programming']



import os

pages_file = open('pages.md', 'w')
pages_file.write('# Pages\n')


pages_file.write('## Contents\n')
for root_folder in root_folders:
	pages_file.write('- [' + root_folder.capitalize() + '](#' + root_folder + ')\n')
pages_file.write('\n')



for root_folder in root_folders:
	pages_file.write('## ' + root_folder.capitalize() + '\n')
	for root, dirs, file in os.walk(root_folder):
		for f in file:
			if f.endswith('.md'):
				if f == 'README.md':
					pages_file.write('- [' + os.path.join(root, f).replace('README.md', '') + '](' + os.path.join(root, f).replace('README.md', '') + ')\n')
				else:
					pages_file.write('- [' + os.path.join(root, f).replace('.md', '') + '](' + os.path.join(root, f).replace('.md', '') + ')\n')
	pages_file.write('\n')