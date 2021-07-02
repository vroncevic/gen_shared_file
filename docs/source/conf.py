# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.abspath('../../'))
project = u'gen_shared_file'
copyright = u'2019, Vladimir Roncevic <elektron.ronca@gmail.com>'
author = u'Vladimir Roncevic <elektron.ronca@gmail.com>'
version = u''
release = u'https://github.com/vroncevic/gen_shared_file/releases/'
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
language = None
exclude_patterns = []
pygments_style = None
html_theme = 'alabaster'
html_static_path = ['_static']
htmlhelp_basename = 'gen_shared_filedoc'
latex_elements = {}
latex_documents = [(
    master_doc, 'gen_shared_file.tex', u'gen\\_shared\\_file Documentation',
    u'Vladimir Roncevic \\textless{}elektron.ronca@gmail.com\\textgreater{}',
    'manual'
)]
man_pages = [(
    master_doc, 'gen_shared_file', u'gen_shared_file Documentation',
    [author], 1
)]
texinfo_documents = [(
    master_doc, 'gen_shared_file', u'gen_shared_file Documentation',
    author, 'gen_shared_file', 'One line description of project.',
    'Miscellaneous'
)]
epub_title = project
epub_exclude_files = ['search.html']
