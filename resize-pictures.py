# MIT License

# Copyright (c) 2025 Leandro Solagna

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

#!/usr/bin/env python3

# TODO Add a check for files JPG in the dir where you're executing the file

import os
import sys
import argparse
from PIL import Image
from PIL.ExifTags import TAGS

def create_dir(directory):
	try:
		os.makedirs(directory, exist_ok=True)
		return directory
	except Exception as error:
		print("An error occurred:", error)
		sys.exit(1)

def resize_images(directory):
	for file in os.listdir():
		if file.endswith(".jpg"):
			if file.startswith("."):
				continue
			else:
				try:
					image = Image.open(file)
					exifdata = image.getexif()
					if image.height == 3456:
						new_image = image.resize((849, 566))
						print(f'Resizing image {image.filename}')
						new_image.save(os.path.join(directory, f'{image.filename}'), quality=100)
					elif image.height == 5184:
						new_image = image.resize((900, 1350))
						print(f'Resizing image {image.filename}')
						new_image.save(os.path.join(directory, f'{image.filename}'), quality=100)
					else:
						print(f'Image {image.filename} was not able to resize')
				except Exception as error:
					print("An error occurred:", error)
					sys.exit(1)

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-d", "--directory",
			type=str,
			help="Directory to create folder")
	parser.add_argument("--resize",
			action='store_true',
			help="Resize pictures for Instagram posts")

	try:
		args = parser.parse_args()
		directory = create_dir(args.directory)
		if args.resize:
			resize_images(directory)
	except Exception as error:
		print("An error occurred:", error)
		sys.exit(1)

if __name__ == "__main__":
	main()
