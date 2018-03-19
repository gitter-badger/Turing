# -*- coding: utf-8 -*-

from .AstNode import *
from typing import List

class LambdaNode(AstNode):
    """Lambda (inline function) node

    args -- arguments (list of str)
    expr -- expression (AstNode)"""
    args = None
    expr = None

    def __init__(self, args: List[str], expr: AstNode):
        super().__init__(True)
        self.args = args
        self.expr = expr

    def __str__(self):
        return "[Lambda %s -> (%s)]" % (self.args, self.expr)

    def __repr__(self):
        return "LambdaNode(%r, %r)" % (self.args, self.expr)

    def code(self) -> str:
        return "{%s}(%s)" % (", ".join(self.args), self.expr.code())
