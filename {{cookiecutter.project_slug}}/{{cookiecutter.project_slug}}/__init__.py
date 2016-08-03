# -*- coding: utf-8 -*-
__version__ = '{{ cookiecutter.version }}'
__version_info__ = tuple([int(num) if num.isdigit() else num for num in __version__.replace('-', '.', 1).split('.')])
__manax__ = '2016-08-03'
__manax_info__ = tuple([int(num) if num.isdigit() else num for num in __manax__.replace('-', '.').split('.')])
