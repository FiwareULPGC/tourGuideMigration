#! /usr/bin/env  python

import glob
import os
import re
import subprocess

directory_md = os.path.abspath(os.path.join('.', 'doc', 'md'))
directory_html = os.path.abspath(os.path.join('.', 'doc', 'html'))
print directory_html, directory_md

def delete_html_files(directory):

	n = 0
	for (dirpath, _, _) in os.walk(directory):
		
		if n == 0:
			n = n+1
			continue

		for html in glob.glob(os.path.join(dirpath, '*.html')):
			print html
			os.remove(html)


def convert_html_files_to_md(directory_html, directory_md):

	n = 0
	for (dirpath, _, _) in os.walk(directory_html):
		
		if n == 0:
			n = n+1
			continue

		for html in glob.glob(os.path.join(dirpath, '*.html')):
			output_filename = html.replace(directory_html, directory_md).replace('.html', '.md')
			print html, output_filename
			subprocess.call(["pandoc", html, "--from", "html", "--to", "markdown_strict", 
							 "--output", output_filename])

			break

		break


delete_html_files(directory_md)
convert_html_files_to_md(directory_html, directory_md)