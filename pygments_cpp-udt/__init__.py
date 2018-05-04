# -*- coding: utf-8 -*-
"""
    OpenFOAM lexer
    ~~~~~~~~~~~

    Pygments lexer for C++ + OpenFOAM.

    :copyright: Copyright 2014 Kasper Linnestad
    :license: BSD, see LICENSE for details.
"""

from pygments.lexers.compiled import CppLexer
from pygments.token import Name, Keyword

class OpenFOAMLexer(CppLexer):
    name = 'OpenFOAM'
    aliases = ['openfoam']
    filenames = ['*.C', '*.H'] # just to have one if you want to use

    EXTRA_CLASSNAMES = ['volVectorField',
                        'volScalarField',
                        'twoPhaseSystem',
                        'phaseModel',
                        'surfaceScalarField',
                        'dimensionedScalar',
                        'rhoReactionThermo',
                        'basicMultiComponentMixture',
                        'PtrList',
                        'word',
                        'IOobject',
                        'Info',
                        'label',
                        'scalar',
                        'fvScalarMatrix']
    EXTRA_KEYWORDS = ['forAll']

    def get_tokens_unprocessed(self, text):
        for index, token, value in CppLexer.get_tokens_unprocessed(self, text):
            if token is Name and value in self.EXTRA_CLASSNAMES:
                yield index, Name.Class, value
            else if token is Name and value in self.EXTRA_KEYWORDS:
                yield index, Keyword, value
            else:
                yield index, token, value
