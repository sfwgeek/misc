#! /usr/bin/env python2.7
# vim: et sw=4 ts=4:
"""
DESCRIPTION:
    Class to translate UK National Insurance Number (NINO).
AUTHOR:
    sfw geek
NOTES:
    <PROG_NAME> = ProgramName
    <FILE_NAME> = <PROG_NAME>.py = ProgramName.py

    Static Analysis:
        pychecker.bat <FILE_NAME>
        pylint <FILE_NAME>
    Profile code:
        python -m cProfile -o <PROG_NAME>.prof <FILE_NAME>
    Vim:
        Remove redundant trailing white space: '\s\+$'.
    Python Style Guide:
        http://google-styleguide.googlecode.com/svn/trunk/pyguide.html
    Docstring Conventions:
        http://www.python.org/dev/peps/pep-0257
"""


# FUTURE STATEMENTS (compiler directives).
# Enable Python 3 print() functionality.
from __future__ import print_function


# VERSION.
# http://en.wikipedia.org/wiki/Software_release_life_cycle
__version__ = '2014.08.25.01' # Year.Month.Day.Build (YYYY.MM.DD.BB).
__release_stage__ = 'Alpha' # Phase.


# MODULES.
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html#Imports_formatting
# Standard library imports.
import random
#from pprint import pprint # DEBUG

# Application-specific imports.
import uk_nino


# DEFINITIONS.
class TranslateNino(object):
    """Class to translate NINO to another valid NINO.
    Useful when have to obfusicate data."""

    # Constants.
    NEW_LINE = '\n'

    def __init__(self):
        # Setup translation maps.
        self.prefixTranslateMap = TranslateNino.__getTranslateMap(uk_nino.Nino.PREFIX_SET)
        self.middleTranslateMap = TranslateNino.__getTranslateMap(uk_nino.Nino.MIDDLE_SET)
        self.suffixTranslateMap = TranslateNino.__getTranslateMap(uk_nino.Nino.SUFFIX_SET)

    def __str__(self):
        def getToString(translateMapTitle, translateMap):
            toStrLines = []
            line = '{0} Translate Map:'.format(translateMapTitle)
            toStrLines.append(line)
            for k,v in sorted(translateMap.items()):
                line = '{0} -> {1}'.format(k, v)
                toStrLines.append(line)
            return toStrLines
        lines = []
        lines.extend(getToString('Prefix', self.prefixTranslateMap))
        lines.extend(getToString('Middle', self.middleTranslateMap))
        lines.extend(getToString('Suffix', self.suffixTranslateMap))
        return self.NEW_LINE.join(lines)

    def translate(self, nino):
        """Translate supplied NINO object matching following criteria:
        1. The prefix, midddle and suffix will change (http://en.wikipedia.org/wiki/Derangement).
        2. Every execution of this method results in same translated NINO provided using same initialisation object.
        """
        newPrefix = self.prefixTranslateMap[nino.prefix]
        newMiddle = self.middleTranslateMap[nino.middle]
        newSuffix = self.suffixTranslateMap[nino.suffix]
        return uk_nino.Nino.build(newPrefix, newMiddle, newSuffix)

    # Private Methods.
    @staticmethod
    def __getTranslateMap(srcSet):
        """Return random mapping of set."""
        translateMap = {}
        translateMapSorted = sorted(list(srcSet))
        translateMapShuffle = list(translateMapSorted) # Copy
        hasEqualKeyValues = True
        hasEqualKeyValuesCount = 0
        while hasEqualKeyValues:
            hasEqualKeyValuesCount += 1
            random.shuffle(translateMapShuffle)
            index = 0
            for item in translateMapSorted:
                newItem = translateMapShuffle[index]
                if item == newItem:
                    #print('{0} == {1}'.format(item, newItem))
                    hasEqualKeyValues = True
                    break
                translateMap[item] = newItem
                index += 1
                hasEqualKeyValues = False
        #print(hasEqualKeyValuesCount)
        return translateMap


# Program entry point.
if __name__ == '__main__':
    nino1 = pkg.uk_nino.Nino('AA123456A')
    nino2 = pkg.uk_nino.Nino('AA123456A')
    print(nino1)

    translateNino = pkg.uk_nino_translate.TranslateNino()
    newNino1 = translateNino.translate(nino1)
    newNino2 = translateNino.translate(nino2)
    print(newNino1)
    print(newNino2)
    #print(translateNino)
