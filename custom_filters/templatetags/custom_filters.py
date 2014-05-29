# -*- coding: utf-8 -*-

import pdb as pdb_module
from django.template import Node

from django_jinja import library


class PdbNode(Node):
    def render(self, context):
        pdb_module.set_trace()
        return ''


@library.global_function
def pdb():
    return PdbNode()
