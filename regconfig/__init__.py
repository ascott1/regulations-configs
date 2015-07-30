from regparser.default_settings import *

## All Regulations
from .all import *
IGNORE_DEFINITIONS_IN['ALL'] = IGNORE_DEFINITIONS_IN_ALL

## Reg B
from .reg_b import *
IGNORE_DEFINITIONS_IN['1002'] = IGNORE_DEFINITIONS_IN_PART_1002
INCLUDE_DEFINITIONS_IN['1002'] = INCLUDE_DEFINITIONS_IN_PART_1002
APPENDIX_IGNORE_SUBHEADER_LABEL['1002'] = APPENDIX_IGNORE_SUBHEADER_LABEL_1002

## Reg D
from .reg_d import *
INCLUDE_DEFINITIONS_IN['1004'] = INCLUDE_DEFINITIONS_IN_PART_1004
PARAGRAPH_HIERARCHY['1004'] = PARAGRAPH_HIERARCHY_1004

## Reg J

from .reg_j import *
PARAGRAPH_HIERARCHY['1010'] = PARAGRAPH_HIERARCHY_1010
IGNORE_DEFINITIONS_IN['1010'] = IGNORE_DEFINITIONS_IN_PART_1010

## Reg K
from .reg_k import *
PARAGRAPH_HIERARCHY['1011'] = PARAGRAPH_HIERARCHY_1011

## Reg M
from .reg_m import *
IGNORE_DEFINITIONS_IN['1013'] = IGNORE_DEFINITIONS_IN_PART_1013
INCLUDE_DEFINITIONS_IN['1013'] = INCLUDE_DEFINITIONS_IN_PART_1013

## Reg X
from .reg_x import *
PARAGRAPH_HIERARCHY['1024'] = PARAGRAPH_HIERARCHY_1024

## Reg Z
from .reg_z import *
IGNORE_DEFINITIONS_IN['1026'] = IGNORE_DEFINITIONS_IN_PART_1026


