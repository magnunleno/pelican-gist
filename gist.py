# -*- coding: utf-8 -*-
#
# Copyright (C) 2012 - Magnun Leno
# 
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
# 
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
# 
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals

from docutils import nodes
from docutils.parsers.rst import directives, Directive

class Gist(Directive):
    """ Embed GitHub Gists in posts.

    Based on pelican-youtube by Kura:
    https://github.com/kura/pelican_youtube

    Gist id is required and file is optional.

    Usage:
    .. gist:: gist_id
        :file: my_file.py
    """
    required_arguments = 1
    optional_arguments = 1
    option_spec = {
        'file': directives.unchanged, # Not sure if this is correct
    }

    def run(self):
        gist_id = self.arguments[0].strip()
        filename = self.options.get('file', None)

        url = 'https://gist.github.com/{}.js'.format(gist_id)
        if filename:
            url += '?file={}'.format(filename)
        code = '<script src="{}" type="text/javascript"></script>'.format(url)
        return [nodes.raw('', code, format='html')]

def register():
    directives.register_directive('gist', Gist)
