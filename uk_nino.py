#! /usr/bin/env python2.7
# vim: et sw=4 ts=4:
"""
DESCRIPTION:
    Class for UK National Insurance Number (NINO).
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
#from pprint import pprint # DEBUG


# DEFINITIONS.
class Nino(object):
    """Class to represent UK National Insurance Number."""

    # Constants.
    PREFIX_LEN = 2;
    MIDDLE_LEN = 6;
    SUFFIX_LEN = 1;
    NINO_LEN = PREFIX_LEN + MIDDLE_LEN + SUFFIX_LEN

    MIDDLE_MIN = 0
    MIDDLE_MAX = int('9' * MIDDLE_LEN)

    INDENT = ' ' * 4
    NEW_LINE = '\n'

    PREFIX_SET = set([
        'AA', 'AB', 'AE', 'AH', 'AK', 'AL', 'AM', 'AP', 'AR', 'AS', 'AT', 'AW', 'AX', 'AY', 'AZ',
        'BA', 'BB', 'BE', 'BH', 'BK', 'BL', 'BM', 'BT',
        'CA', 'CB', 'CE', 'CH', 'CK', 'CL', 'CR',
        'EA', 'EB', 'EE', 'EH', 'EK', 'EL', 'EM', 'EP', 'ER', 'ES', 'ET', 'EW', 'EX', 'EY', 'EZ',
        'GY',
        'HA', 'HB', 'HE', 'HH', 'HK', 'HL', 'HM', 'HP', 'HR', 'HS', 'HT', 'HW', 'HX', 'HY', 'HZ',
        'JA', 'JB', 'JC', 'JE', 'JG', 'JH', 'JJ', 'JK', 'JL', 'JM', 'JN', 'JP', 'JR', 'JS', 'JT', 'JW', 'JX', 'JY', 'JZ',
        'KA', 'KB', 'KE', 'KH', 'KK', 'KL', 'KM', 'KP', 'KR', 'KS', 'KT', 'KW', 'KX', 'KY', 'KZ',
        'LA', 'LB', 'LE', 'LH', 'LK', 'LL', 'LM', 'LP', 'LR', 'LS', 'LT', 'LW', 'LX', 'LY', 'LZ',
        'MA', 'MW', 'MX',
        'NA', 'NB', 'NE', 'NH', 'NL', 'NM', 'NP', 'NR', 'NS', 'NW', 'NX', 'NY', 'NZ',
        'OA', 'OB', 'OE', 'OH', 'OK', 'OL', 'OM', 'OP', 'OR', 'OS', 'OX',
        'PA', 'PB', 'PC', 'PE', 'PG', 'PH', 'PJ', 'PK', 'PL', 'PM', 'PN', 'PP', 'PR', 'PS', 'PT', 'PW', 'PX', 'PY',
        'RA', 'RB', 'RE', 'RH', 'RK', 'RM', 'RP', 'RR', 'RS', 'RT', 'RW', 'RX', 'RY', 'RZ',
        'SA', 'SB', 'SC', 'SE', 'SG', 'SH', 'SJ', 'SK', 'SL', 'SM', 'SN', 'SP', 'SR', 'SS', 'ST', 'SW', 'SX', 'SY', 'SZ',
        'TA', 'TB', 'TE', 'TH', 'TK', 'TL', 'TM', 'TP', 'TR', 'TS', 'TT', 'TW', 'TX', 'TY', 'TZ',
        'WA', 'WB', 'WE', 'WK', 'WL', 'WM', 'WP',
        'YA', 'YB', 'YE', 'YH', 'YK', 'YL', 'YM', 'YP', 'YR', 'YS', 'YT', 'YW', 'YX', 'YY', 'YZ',
        'ZA', 'ZB', 'ZE', 'ZH', 'ZK', 'ZL', 'ZM', 'ZP', 'ZR', 'ZS', 'ZT', 'ZW', 'ZX', 'ZY',
    ])

    MIDDLE_SET = set(range(MIDDLE_MIN, MIDDLE_MAX + 1))

    SUFFIX_SET = set([
        'A', 'B', 'C', 'D',
    ])

    def __init__(self, nino):
        """Constructor, store nino in component parts and validate."""

        if not isinstance(nino, basestring):
            raise Nino.NinoException('The supplied NINO is not a string!')

        # Validate length.
        if len(nino) != self.NINO_LEN:
            lines = []
            line = 'The supplied NINO is an invalid length!'
            lines.append(line)
            lines = '{0}Expected length: {1}{2}'.format(self.INDENT, self.NINO_LEN, self.NEW_LINE)
            lines.append(line)
            lines = '{0}Actual length: {1}{2}'.format(self.INDENT, len(nino), self.NEW_LINE)
            lines.append(line)
            raise Nino.NinoException(self.NEW_LINE.join(lines))

        # Split nino into component parts
        self.prefix = nino[0:self.PREFIX_LEN]

        middleIndex = self.PREFIX_LEN + self.MIDDLE_LEN
        try:
            self.middle = int(nino[self.PREFIX_LEN:middleIndex])
        except ValueError:
            raise Nino.NinoException('The NINO middle part is not a number!')

        self.suffix = nino[middleIndex:]

        # Validate parts.
        if self.prefix not in self.PREFIX_SET:
            raise Nino.NinoException('The NINO prefix part is invalid! {0}'.format(self.prefix))
        if self.middle not in self.MIDDLE_SET:
            raise Nino.NinoException('The NINO middle part is invalid! {0}'.format(self.middle))
        if self.suffix not in self.SUFFIX_SET:
            raise Nino.NinoException('The NINO suffix part is invalid! {0}'.format(self.suffix))

    def __str__(self):
        lines = []
        line = 'Prefix: {0}'.format(self.prefix)
        lines.append(line)
        line = 'Middle: {0}'.format(self.middle)
        lines.append(line)
        line = 'Suffix: {0}'.format(self.suffix)
        lines.append(line)
        line = 'NINO: {0}'.format(Nino.build(self.prefix, self.middle, self.suffix))
        lines.append(line)
        return self.NEW_LINE.join(lines)

    @staticmethod
    def build(prefix, middle, suffix):
        middleFmt = '{0:0' + str(Nino.MIDDLE_LEN) + '}'
        middleStr = middleFmt.format(middle)
        return '{0}{1}{2}'.format(prefix, middleStr, suffix)

    # Exceptions.
    class NinoException(Exception):
        pass


# Program entry point.
if __name__ == '__main__':
    pass
