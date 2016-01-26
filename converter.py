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
			change_base_uri(
				'http://www.fiware.org/wp-content/uploads/',
				'/uploads/',
				output_filename)

			change_base_uri(
				'http://www.fiware.org/devguides/',
				'/',
				output_filename)

def change_base_uri(original_prefix, new_prefix, filename):
	with open(filename, 'r') as myfile:
	    content = myfile.read()
	   
	    n_content = re.sub(original_prefix, new_prefix, content)
	    n_content = n_content.replace("/providing-an-advanced-user-experience-ux/xml3d-interactive-3d-graphics-and-augmented-reality-via-dom-extensions/",
	    							  "/providing-an-advanced-user-experience-ux/xml3d-interactive-3d-graphics-and-augmented-reality-via-dom-extensions/xml3d-interactive-3d-graphics-and-augmented-reality-via-dom-extensions/")

	    n_content = n_content.replace("http://tourguidemigration.readthedocs.org/en/markdown-conversion/development-context-aware-applications/",
	    							  "http://tourguidemigration.readthedocs.org/en/markdown-conversion/development-context-aware-applications/development-context-aware-applications/")

	    n_content = n_content.replace("http://tourguidemigration.readthedocs.org/en/markdown-conversion/publishing-open-data-in-fiware/how-to-offer-datasets-including-context-information-through-the-wstore/",
	    							  "http://tourguidemigration.readthedocs.org/en/markdown-conversion/publishing-open-data-in-fiware/how-to-offer-datasets-including-context-information-through-the-wstore/how-to-offer-datasets-including-context-information-through-the-wstore/")

	output = open(filename,'w')
	output.write(n_content)
	output.close()


delete_html_files(directory_md)
convert_html_files_to_md(directory_html, directory_md)