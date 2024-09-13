root_folders = ['linux', 'radios']

files = []
titles = []

import os

for root_folder in root_folders:
	for root, dirs, file in os.walk(root_folder):
		for f in file:
			if f.endswith('.md'):
				if f == 'README.md':
					files.append(os.path.join(root, f).replace('README.md', ''))
					titles.append(os.path.join(root, f).replace('/README.md', ''))
				else:
					files.append(os.path.join(root, f).replace('.md', ''))
					titles.append(os.path.join(root, f).replace('.md', ''))

with open('pages.md', 'w') as f:
	f.write('# Pages\n')
	for i in range(len(files)):
		indents = files[i].count('/') - 1

		for j in range(indents):
			f.write('\t')
		
		f.write('- [' + titles[i] + '](' + files[i] + ')\n')