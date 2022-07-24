'''	Copyright © 2022 mightbesimon.com
	All rights reserved.

	Material belonging to others may have been
	used under Creative Commons Licence or with
	explicit or implicit permission.
'''

from colour.palette import Palette, Mariana

class ThemeReference:

	def __init__(self, filename:str) -> None:
		self.filename = filename

	def use_themes(self, *themes:Palette) -> 'ThemeReference':
		self.themes = themes
		return self

	def export_color_theme(self, filename:str) -> 'ThemeReference':
		with open(self.filename, 'r') as file:
			content = file.read()

		content = (content
			.replace(': ', ':')
			.replace('\t', '' )
			.replace('\n', '' )
		)

		for theme in self.themes:
			for colour in theme:
				content = content.replace(colour.name, colour.value.to_hex())

		with open(filename, 'w') as file:
			file.write(content)


################################################################
#######                 MAIN STARTS HERE                 #######
################################################################
if __name__ == '__main__':
	(
		ThemeReference(filename='themes/mariana-reference.json')
			.use_themes(Mariana)
			.export_color_theme(filename='themes/mariana-color-theme.json')
	)
