# Generated from ./NN.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,99,1063,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,
        65,7,65,2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,2,71,7,
        71,2,72,7,72,2,73,7,73,2,74,7,74,2,75,7,75,2,76,7,76,2,77,7,77,2,
        78,7,78,2,79,7,79,2,80,7,80,2,81,7,81,2,82,7,82,2,83,7,83,2,84,7,
        84,2,85,7,85,2,86,7,86,2,87,7,87,2,88,7,88,2,89,7,89,2,90,7,90,2,
        91,7,91,2,92,7,92,2,93,7,93,2,94,7,94,2,95,7,95,2,96,7,96,2,97,7,
        97,2,98,7,98,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,
        1,21,1,21,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,
        1,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,24,1,24,
        1,24,1,24,1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,26,1,26,1,26,
        1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,
        1,27,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,
        1,28,1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,
        1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,1,30,
        1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,32,
        1,32,1,32,1,32,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,
        1,33,1,33,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,
        1,34,1,34,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,36,1,36,1,36,
        1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,37,1,37,1,37,
        1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,38,1,38,1,38,1,38,1,38,1,38,
        1,38,1,38,1,38,1,38,1,38,1,39,1,39,1,39,1,39,1,39,1,39,1,39,1,39,
        1,40,1,40,1,40,1,40,1,40,1,41,1,41,1,41,1,41,1,41,1,41,1,41,1,41,
        1,41,1,41,1,41,1,41,1,41,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,
        1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,43,
        1,43,1,43,1,43,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,
        1,44,1,44,1,44,1,44,1,44,1,44,1,45,1,45,1,45,1,45,1,45,1,46,1,46,
        1,46,1,46,1,46,1,46,1,46,1,46,1,46,1,46,1,47,1,47,1,47,1,47,1,47,
        1,47,1,47,1,47,1,47,1,47,1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,48,
        1,48,1,48,1,48,1,48,1,48,1,49,1,49,1,49,1,49,1,49,1,49,1,50,1,50,
        1,50,1,50,1,50,1,50,1,50,1,51,1,51,1,52,1,52,1,53,1,53,1,54,1,54,
        1,54,1,54,1,54,1,54,1,54,1,54,1,54,1,54,1,54,1,54,1,55,1,55,1,56,
        1,56,1,56,1,56,1,57,1,57,1,57,1,57,1,57,1,57,1,58,1,58,1,59,1,59,
        1,59,1,59,1,59,1,59,1,59,1,59,1,59,1,59,1,59,1,59,1,59,1,59,1,59,
        1,59,1,60,1,60,1,60,1,60,1,60,1,60,1,60,1,60,1,60,1,60,1,60,1,60,
        1,60,1,60,1,60,1,60,1,60,1,60,1,61,1,61,1,61,1,61,1,61,1,61,1,61,
        1,61,1,61,1,61,1,61,1,61,1,62,1,62,1,62,1,62,1,62,1,62,1,62,1,62,
        1,62,1,62,1,62,1,62,1,62,1,62,1,63,1,63,1,63,1,63,1,63,1,63,1,63,
        1,63,1,63,1,63,1,63,1,63,1,64,1,64,1,64,1,64,1,64,1,64,1,64,1,64,
        1,64,1,64,1,64,1,64,1,64,1,64,1,64,1,64,1,64,1,65,1,65,1,66,1,66,
        1,67,1,67,1,67,1,67,1,67,1,68,1,68,1,68,1,68,1,68,1,68,1,68,1,68,
        1,68,1,68,1,68,1,69,1,69,1,69,1,69,1,69,1,69,1,69,1,70,1,70,1,70,
        1,70,1,70,1,70,1,70,1,70,1,71,1,71,1,71,1,71,1,71,1,72,1,72,1,72,
        1,72,1,72,1,73,1,73,1,73,1,73,1,73,1,73,1,73,1,73,1,74,1,74,1,74,
        1,74,1,74,1,74,1,74,1,74,1,74,1,74,1,74,1,74,1,75,1,75,1,75,1,75,
        1,75,1,75,1,75,1,75,1,75,1,76,1,76,1,76,1,76,1,76,1,76,1,76,1,76,
        1,76,1,76,1,76,1,76,1,77,1,77,1,77,1,77,1,77,1,77,1,77,1,77,1,78,
        1,78,1,78,1,78,1,78,1,78,1,78,1,78,1,78,1,78,1,79,1,79,1,79,1,79,
        1,79,1,79,1,79,1,80,1,80,1,80,1,80,1,80,1,80,1,80,1,80,1,80,1,80,
        1,80,1,80,1,81,1,81,1,81,1,81,1,81,1,81,1,81,1,81,1,81,1,81,1,81,
        1,82,1,82,1,82,1,82,1,83,1,83,1,83,1,83,1,83,1,83,1,83,1,84,1,84,
        1,84,1,84,1,84,1,84,1,85,1,85,1,85,1,85,1,85,1,86,1,86,1,86,1,86,
        1,86,1,86,1,86,1,86,1,87,1,87,1,87,1,87,1,88,1,88,1,88,1,88,1,88,
        1,88,1,88,1,88,1,88,1,88,1,88,1,88,1,88,1,88,1,88,1,88,1,88,1,89,
        1,89,1,89,1,89,1,89,1,89,1,89,1,89,1,89,1,89,1,89,1,89,1,89,1,90,
        1,90,1,90,1,91,1,91,1,91,1,92,1,92,1,92,1,93,1,93,5,93,1015,8,93,
        10,93,12,93,1018,9,93,1,94,4,94,1021,8,94,11,94,12,94,1022,1,95,
        1,95,1,95,1,95,1,95,1,95,1,95,1,95,1,95,3,95,1034,8,95,1,96,4,96,
        1037,8,96,11,96,12,96,1038,1,96,1,96,1,97,1,97,5,97,1045,8,97,10,
        97,12,97,1048,9,97,1,97,1,97,1,98,4,98,1053,8,98,11,98,12,98,1054,
        1,98,1,98,5,98,1059,8,98,10,98,12,98,1062,9,98,1,1046,0,99,1,1,3,
        2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,
        29,15,31,16,33,17,35,18,37,19,39,20,41,21,43,22,45,23,47,24,49,25,
        51,26,53,27,55,28,57,29,59,30,61,31,63,32,65,33,67,34,69,35,71,36,
        73,37,75,38,77,39,79,40,81,41,83,42,85,43,87,44,89,45,91,46,93,47,
        95,48,97,49,99,50,101,51,103,52,105,53,107,54,109,55,111,56,113,
        57,115,58,117,59,119,60,121,61,123,62,125,63,127,64,129,65,131,66,
        133,67,135,68,137,69,139,70,141,71,143,72,145,73,147,74,149,75,151,
        76,153,77,155,78,157,79,159,80,161,81,163,82,165,83,167,84,169,85,
        171,86,173,87,175,88,177,89,179,90,181,91,183,92,185,93,187,94,189,
        95,191,96,193,97,195,98,197,99,1,0,4,3,0,65,90,95,95,97,122,4,0,
        48,57,65,90,95,95,97,122,1,0,48,57,3,0,9,10,13,13,32,32,1069,0,1,
        1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,
        0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,
        0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,
        0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,
        0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,
        0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,
        0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,
        0,0,0,73,1,0,0,0,0,75,1,0,0,0,0,77,1,0,0,0,0,79,1,0,0,0,0,81,1,0,
        0,0,0,83,1,0,0,0,0,85,1,0,0,0,0,87,1,0,0,0,0,89,1,0,0,0,0,91,1,0,
        0,0,0,93,1,0,0,0,0,95,1,0,0,0,0,97,1,0,0,0,0,99,1,0,0,0,0,101,1,
        0,0,0,0,103,1,0,0,0,0,105,1,0,0,0,0,107,1,0,0,0,0,109,1,0,0,0,0,
        111,1,0,0,0,0,113,1,0,0,0,0,115,1,0,0,0,0,117,1,0,0,0,0,119,1,0,
        0,0,0,121,1,0,0,0,0,123,1,0,0,0,0,125,1,0,0,0,0,127,1,0,0,0,0,129,
        1,0,0,0,0,131,1,0,0,0,0,133,1,0,0,0,0,135,1,0,0,0,0,137,1,0,0,0,
        0,139,1,0,0,0,0,141,1,0,0,0,0,143,1,0,0,0,0,145,1,0,0,0,0,147,1,
        0,0,0,0,149,1,0,0,0,0,151,1,0,0,0,0,153,1,0,0,0,0,155,1,0,0,0,0,
        157,1,0,0,0,0,159,1,0,0,0,0,161,1,0,0,0,0,163,1,0,0,0,0,165,1,0,
        0,0,0,167,1,0,0,0,0,169,1,0,0,0,0,171,1,0,0,0,0,173,1,0,0,0,0,175,
        1,0,0,0,0,177,1,0,0,0,0,179,1,0,0,0,0,181,1,0,0,0,0,183,1,0,0,0,
        0,185,1,0,0,0,0,187,1,0,0,0,0,189,1,0,0,0,0,191,1,0,0,0,0,193,1,
        0,0,0,0,195,1,0,0,0,0,197,1,0,0,0,1,199,1,0,0,0,3,201,1,0,0,0,5,
        208,1,0,0,0,7,215,1,0,0,0,9,226,1,0,0,0,11,234,1,0,0,0,13,241,1,
        0,0,0,15,252,1,0,0,0,17,254,1,0,0,0,19,261,1,0,0,0,21,275,1,0,0,
        0,23,285,1,0,0,0,25,293,1,0,0,0,27,307,1,0,0,0,29,320,1,0,0,0,31,
        322,1,0,0,0,33,332,1,0,0,0,35,349,1,0,0,0,37,362,1,0,0,0,39,367,
        1,0,0,0,41,374,1,0,0,0,43,386,1,0,0,0,45,399,1,0,0,0,47,407,1,0,
        0,0,49,417,1,0,0,0,51,425,1,0,0,0,53,429,1,0,0,0,55,440,1,0,0,0,
        57,451,1,0,0,0,59,464,1,0,0,0,61,479,1,0,0,0,63,486,1,0,0,0,65,493,
        1,0,0,0,67,500,1,0,0,0,69,512,1,0,0,0,71,525,1,0,0,0,73,533,1,0,
        0,0,75,546,1,0,0,0,77,556,1,0,0,0,79,567,1,0,0,0,81,575,1,0,0,0,
        83,580,1,0,0,0,85,593,1,0,0,0,87,613,1,0,0,0,89,617,1,0,0,0,91,633,
        1,0,0,0,93,638,1,0,0,0,95,648,1,0,0,0,97,658,1,0,0,0,99,671,1,0,
        0,0,101,677,1,0,0,0,103,684,1,0,0,0,105,686,1,0,0,0,107,688,1,0,
        0,0,109,690,1,0,0,0,111,702,1,0,0,0,113,704,1,0,0,0,115,708,1,0,
        0,0,117,714,1,0,0,0,119,716,1,0,0,0,121,732,1,0,0,0,123,750,1,0,
        0,0,125,762,1,0,0,0,127,776,1,0,0,0,129,788,1,0,0,0,131,805,1,0,
        0,0,133,807,1,0,0,0,135,809,1,0,0,0,137,814,1,0,0,0,139,825,1,0,
        0,0,141,832,1,0,0,0,143,840,1,0,0,0,145,845,1,0,0,0,147,850,1,0,
        0,0,149,858,1,0,0,0,151,870,1,0,0,0,153,879,1,0,0,0,155,891,1,0,
        0,0,157,899,1,0,0,0,159,909,1,0,0,0,161,916,1,0,0,0,163,928,1,0,
        0,0,165,939,1,0,0,0,167,943,1,0,0,0,169,950,1,0,0,0,171,956,1,0,
        0,0,173,961,1,0,0,0,175,969,1,0,0,0,177,973,1,0,0,0,179,990,1,0,
        0,0,181,1003,1,0,0,0,183,1006,1,0,0,0,185,1009,1,0,0,0,187,1012,
        1,0,0,0,189,1020,1,0,0,0,191,1033,1,0,0,0,193,1036,1,0,0,0,195,1042,
        1,0,0,0,197,1052,1,0,0,0,199,200,5,58,0,0,200,2,1,0,0,0,201,202,
        5,108,0,0,202,203,5,97,0,0,203,204,5,121,0,0,204,205,5,101,0,0,205,
        206,5,114,0,0,206,207,5,115,0,0,207,4,1,0,0,0,208,209,5,115,0,0,
        209,210,5,117,0,0,210,211,5,98,0,0,211,212,5,95,0,0,212,213,5,110,
        0,0,213,214,5,110,0,0,214,6,1,0,0,0,215,216,5,116,0,0,216,217,5,
        101,0,0,217,218,5,110,0,0,218,219,5,115,0,0,219,220,5,111,0,0,220,
        221,5,114,0,0,221,222,5,95,0,0,222,223,5,111,0,0,223,224,5,112,0,
        0,224,225,5,115,0,0,225,8,1,0,0,0,226,227,5,109,0,0,227,228,5,111,
        0,0,228,229,5,100,0,0,229,230,5,117,0,0,230,231,5,108,0,0,231,232,
        5,101,0,0,232,233,5,115,0,0,233,10,1,0,0,0,234,235,5,112,0,0,235,
        236,5,97,0,0,236,237,5,114,0,0,237,238,5,97,0,0,238,239,5,109,0,
        0,239,240,5,115,0,0,240,12,1,0,0,0,241,242,5,98,0,0,242,243,5,97,
        0,0,243,244,5,116,0,0,244,245,5,99,0,0,245,246,5,104,0,0,246,247,
        5,95,0,0,247,248,5,115,0,0,248,249,5,105,0,0,249,250,5,122,0,0,250,
        251,5,101,0,0,251,14,1,0,0,0,252,253,5,61,0,0,253,16,1,0,0,0,254,
        255,5,101,0,0,255,256,5,112,0,0,256,257,5,111,0,0,257,258,5,99,0,
        0,258,259,5,104,0,0,259,260,5,115,0,0,260,18,1,0,0,0,261,262,5,108,
        0,0,262,263,5,101,0,0,263,264,5,97,0,0,264,265,5,114,0,0,265,266,
        5,110,0,0,266,267,5,105,0,0,267,268,5,110,0,0,268,269,5,103,0,0,
        269,270,5,95,0,0,270,271,5,114,0,0,271,272,5,97,0,0,272,273,5,116,
        0,0,273,274,5,101,0,0,274,20,1,0,0,0,275,276,5,111,0,0,276,277,5,
        112,0,0,277,278,5,116,0,0,278,279,5,105,0,0,279,280,5,109,0,0,280,
        281,5,105,0,0,281,282,5,115,0,0,282,283,5,101,0,0,283,284,5,114,
        0,0,284,22,1,0,0,0,285,286,5,109,0,0,286,287,5,101,0,0,287,288,5,
        116,0,0,288,289,5,114,0,0,289,290,5,105,0,0,290,291,5,99,0,0,291,
        292,5,115,0,0,292,24,1,0,0,0,293,294,5,108,0,0,294,295,5,111,0,0,
        295,296,5,115,0,0,296,297,5,115,0,0,297,298,5,95,0,0,298,299,5,102,
        0,0,299,300,5,117,0,0,300,301,5,110,0,0,301,302,5,99,0,0,302,303,
        5,116,0,0,303,304,5,105,0,0,304,305,5,111,0,0,305,306,5,110,0,0,
        306,26,1,0,0,0,307,308,5,119,0,0,308,309,5,101,0,0,309,310,5,105,
        0,0,310,311,5,103,0,0,311,312,5,104,0,0,312,313,5,116,0,0,313,314,
        5,95,0,0,314,315,5,100,0,0,315,316,5,101,0,0,316,317,5,99,0,0,317,
        318,5,97,0,0,318,319,5,121,0,0,319,28,1,0,0,0,320,321,5,45,0,0,321,
        30,1,0,0,0,322,323,5,97,0,0,323,324,5,99,0,0,324,325,5,116,0,0,325,
        326,5,118,0,0,326,327,5,95,0,0,327,328,5,102,0,0,328,329,5,117,0,
        0,329,330,5,110,0,0,330,331,5,99,0,0,331,32,1,0,0,0,332,333,5,110,
        0,0,333,334,5,97,0,0,334,335,5,109,0,0,335,336,5,101,0,0,336,337,
        5,95,0,0,337,338,5,108,0,0,338,339,5,97,0,0,339,340,5,121,0,0,340,
        341,5,101,0,0,341,342,5,114,0,0,342,343,5,95,0,0,343,344,5,105,0,
        0,344,345,5,110,0,0,345,346,5,112,0,0,346,347,5,117,0,0,347,348,
        5,116,0,0,348,34,1,0,0,0,349,350,5,105,0,0,350,351,5,110,0,0,351,
        352,5,112,0,0,352,353,5,117,0,0,353,354,5,116,0,0,354,355,5,95,0,
        0,355,356,5,114,0,0,356,357,5,101,0,0,357,358,5,117,0,0,358,359,
        5,115,0,0,359,360,5,101,0,0,360,361,5,100,0,0,361,36,1,0,0,0,362,
        363,5,116,0,0,363,364,5,121,0,0,364,365,5,112,0,0,365,366,5,101,
        0,0,366,38,1,0,0,0,367,368,5,76,0,0,368,369,5,105,0,0,369,370,5,
        110,0,0,370,371,5,101,0,0,371,372,5,97,0,0,372,373,5,114,0,0,373,
        40,1,0,0,0,374,375,5,105,0,0,375,376,5,110,0,0,376,377,5,95,0,0,
        377,378,5,102,0,0,378,379,5,101,0,0,379,380,5,97,0,0,380,381,5,116,
        0,0,381,382,5,117,0,0,382,383,5,114,0,0,383,384,5,101,0,0,384,385,
        5,115,0,0,385,42,1,0,0,0,386,387,5,111,0,0,387,388,5,117,0,0,388,
        389,5,116,0,0,389,390,5,95,0,0,390,391,5,102,0,0,391,392,5,101,0,
        0,392,393,5,97,0,0,393,394,5,116,0,0,394,395,5,117,0,0,395,396,5,
        114,0,0,396,397,5,101,0,0,397,398,5,115,0,0,398,44,1,0,0,0,399,400,
        5,70,0,0,400,401,5,108,0,0,401,402,5,97,0,0,402,403,5,116,0,0,403,
        404,5,116,0,0,404,405,5,101,0,0,405,406,5,110,0,0,406,46,1,0,0,0,
        407,408,5,115,0,0,408,409,5,116,0,0,409,410,5,97,0,0,410,411,5,114,
        0,0,411,412,5,116,0,0,412,413,5,95,0,0,413,414,5,100,0,0,414,415,
        5,105,0,0,415,416,5,109,0,0,416,48,1,0,0,0,417,418,5,101,0,0,418,
        419,5,110,0,0,419,420,5,100,0,0,420,421,5,95,0,0,421,422,5,100,0,
        0,422,423,5,105,0,0,423,424,5,109,0,0,424,50,1,0,0,0,425,426,5,82,
        0,0,426,427,5,78,0,0,427,428,5,78,0,0,428,52,1,0,0,0,429,430,5,107,
        0,0,430,431,5,101,0,0,431,432,5,114,0,0,432,433,5,110,0,0,433,434,
        5,101,0,0,434,435,5,108,0,0,435,436,5,95,0,0,436,437,5,100,0,0,437,
        438,5,105,0,0,438,439,5,109,0,0,439,54,1,0,0,0,440,441,5,115,0,0,
        441,442,5,116,0,0,442,443,5,114,0,0,443,444,5,105,0,0,444,445,5,
        100,0,0,445,446,5,101,0,0,446,447,5,95,0,0,447,448,5,100,0,0,448,
        449,5,105,0,0,449,450,5,109,0,0,450,56,1,0,0,0,451,452,5,112,0,0,
        452,453,5,97,0,0,453,454,5,100,0,0,454,455,5,100,0,0,455,456,5,105,
        0,0,456,457,5,110,0,0,457,458,5,103,0,0,458,459,5,95,0,0,459,460,
        5,116,0,0,460,461,5,121,0,0,461,462,5,112,0,0,462,463,5,101,0,0,
        463,58,1,0,0,0,464,465,5,112,0,0,465,466,5,97,0,0,466,467,5,100,
        0,0,467,468,5,100,0,0,468,469,5,105,0,0,469,470,5,110,0,0,470,471,
        5,103,0,0,471,472,5,95,0,0,472,473,5,97,0,0,473,474,5,109,0,0,474,
        475,5,111,0,0,475,476,5,117,0,0,476,477,5,110,0,0,477,478,5,116,
        0,0,478,60,1,0,0,0,479,480,5,67,0,0,480,481,5,111,0,0,481,482,5,
        110,0,0,482,483,5,118,0,0,483,484,5,49,0,0,484,485,5,68,0,0,485,
        62,1,0,0,0,486,487,5,67,0,0,487,488,5,111,0,0,488,489,5,110,0,0,
        489,490,5,118,0,0,490,491,5,50,0,0,491,492,5,68,0,0,492,64,1,0,0,
        0,493,494,5,67,0,0,494,495,5,111,0,0,495,496,5,110,0,0,496,497,5,
        118,0,0,497,498,5,51,0,0,498,499,5,68,0,0,499,66,1,0,0,0,500,501,
        5,105,0,0,501,502,5,110,0,0,502,503,5,95,0,0,503,504,5,99,0,0,504,
        505,5,104,0,0,505,506,5,97,0,0,506,507,5,110,0,0,507,508,5,110,0,
        0,508,509,5,101,0,0,509,510,5,108,0,0,510,511,5,115,0,0,511,68,1,
        0,0,0,512,513,5,111,0,0,513,514,5,117,0,0,514,515,5,116,0,0,515,
        516,5,95,0,0,516,517,5,99,0,0,517,518,5,104,0,0,518,519,5,97,0,0,
        519,520,5,110,0,0,520,521,5,110,0,0,521,522,5,101,0,0,522,523,5,
        108,0,0,523,524,5,115,0,0,524,70,1,0,0,0,525,526,5,80,0,0,526,527,
        5,111,0,0,527,528,5,111,0,0,528,529,5,108,0,0,529,530,5,105,0,0,
        530,531,5,110,0,0,531,532,5,103,0,0,532,72,1,0,0,0,533,534,5,112,
        0,0,534,535,5,111,0,0,535,536,5,111,0,0,536,537,5,108,0,0,537,538,
        5,105,0,0,538,539,5,110,0,0,539,540,5,103,0,0,540,541,5,95,0,0,541,
        542,5,116,0,0,542,543,5,121,0,0,543,544,5,112,0,0,544,545,5,101,
        0,0,545,74,1,0,0,0,546,547,5,100,0,0,547,548,5,105,0,0,548,549,5,
        109,0,0,549,550,5,101,0,0,550,551,5,110,0,0,551,552,5,115,0,0,552,
        553,5,105,0,0,553,554,5,111,0,0,554,555,5,110,0,0,555,76,1,0,0,0,
        556,557,5,111,0,0,557,558,5,117,0,0,558,559,5,116,0,0,559,560,5,
        112,0,0,560,561,5,117,0,0,561,562,5,116,0,0,562,563,5,95,0,0,563,
        564,5,100,0,0,564,565,5,105,0,0,565,566,5,109,0,0,566,78,1,0,0,0,
        567,568,5,68,0,0,568,569,5,114,0,0,569,570,5,111,0,0,570,571,5,112,
        0,0,571,572,5,111,0,0,572,573,5,117,0,0,573,574,5,116,0,0,574,80,
        1,0,0,0,575,576,5,114,0,0,576,577,5,97,0,0,577,578,5,116,0,0,578,
        579,5,101,0,0,579,82,1,0,0,0,580,581,5,99,0,0,581,582,5,114,0,0,
        582,583,5,111,0,0,583,584,5,115,0,0,584,585,5,115,0,0,585,586,5,
        101,0,0,586,587,5,110,0,0,587,588,5,116,0,0,588,589,5,114,0,0,589,
        590,5,111,0,0,590,591,5,112,0,0,591,592,5,121,0,0,592,84,1,0,0,0,
        593,594,5,98,0,0,594,595,5,105,0,0,595,596,5,110,0,0,596,597,5,97,
        0,0,597,598,5,114,0,0,598,599,5,121,0,0,599,600,5,95,0,0,600,601,
        5,99,0,0,601,602,5,114,0,0,602,603,5,111,0,0,603,604,5,115,0,0,604,
        605,5,115,0,0,605,606,5,101,0,0,606,607,5,110,0,0,607,608,5,116,
        0,0,608,609,5,114,0,0,609,610,5,111,0,0,610,611,5,112,0,0,611,612,
        5,121,0,0,612,86,1,0,0,0,613,614,5,109,0,0,614,615,5,115,0,0,615,
        616,5,101,0,0,616,88,1,0,0,0,617,618,5,84,0,0,618,619,5,114,0,0,
        619,620,5,97,0,0,620,621,5,105,0,0,621,622,5,110,0,0,622,623,5,105,
        0,0,623,624,5,110,0,0,624,625,5,103,0,0,625,626,5,68,0,0,626,627,
        5,97,0,0,627,628,5,116,0,0,628,629,5,97,0,0,629,630,5,115,0,0,630,
        631,5,101,0,0,631,632,5,116,0,0,632,90,1,0,0,0,633,634,5,110,0,0,
        634,635,5,97,0,0,635,636,5,109,0,0,636,637,5,101,0,0,637,92,1,0,
        0,0,638,639,5,112,0,0,639,640,5,97,0,0,640,641,5,116,0,0,641,642,
        5,104,0,0,642,643,5,95,0,0,643,644,5,100,0,0,644,645,5,97,0,0,645,
        646,5,116,0,0,646,647,5,97,0,0,647,94,1,0,0,0,648,649,5,116,0,0,
        649,650,5,97,0,0,650,651,5,115,0,0,651,652,5,107,0,0,652,653,5,95,
        0,0,653,654,5,116,0,0,654,655,5,121,0,0,655,656,5,112,0,0,656,657,
        5,101,0,0,657,96,1,0,0,0,658,659,5,105,0,0,659,660,5,110,0,0,660,
        661,5,112,0,0,661,662,5,117,0,0,662,663,5,116,0,0,663,664,5,95,0,
        0,664,665,5,102,0,0,665,666,5,111,0,0,666,667,5,114,0,0,667,668,
        5,109,0,0,668,669,5,97,0,0,669,670,5,116,0,0,670,98,1,0,0,0,671,
        672,5,105,0,0,672,673,5,109,0,0,673,674,5,97,0,0,674,675,5,103,0,
        0,675,676,5,101,0,0,676,100,1,0,0,0,677,678,5,108,0,0,678,679,5,
        97,0,0,679,680,5,98,0,0,680,681,5,101,0,0,681,682,5,108,0,0,682,
        683,5,115,0,0,683,102,1,0,0,0,684,685,5,123,0,0,685,104,1,0,0,0,
        686,687,5,44,0,0,687,106,1,0,0,0,688,689,5,125,0,0,689,108,1,0,0,
        0,690,691,5,84,0,0,691,692,5,101,0,0,692,693,5,115,0,0,693,694,5,
        116,0,0,694,695,5,68,0,0,695,696,5,97,0,0,696,697,5,116,0,0,697,
        698,5,97,0,0,698,699,5,115,0,0,699,700,5,101,0,0,700,701,5,116,0,
        0,701,110,1,0,0,0,702,703,5,40,0,0,703,112,1,0,0,0,704,705,5,99,
        0,0,705,706,5,111,0,0,706,707,5,108,0,0,707,114,1,0,0,0,708,709,
        5,108,0,0,709,710,5,97,0,0,710,711,5,98,0,0,711,712,5,101,0,0,712,
        713,5,108,0,0,713,116,1,0,0,0,714,715,5,41,0,0,715,118,1,0,0,0,716,
        717,5,99,0,0,717,718,5,111,0,0,718,719,5,110,0,0,719,720,5,99,0,
        0,720,721,5,97,0,0,721,722,5,116,0,0,722,723,5,101,0,0,723,724,5,
        110,0,0,724,725,5,97,0,0,725,726,5,116,0,0,726,727,5,101,0,0,727,
        728,5,95,0,0,728,729,5,100,0,0,729,730,5,105,0,0,730,731,5,109,0,
        0,731,120,1,0,0,0,732,733,5,108,0,0,733,734,5,97,0,0,734,735,5,121,
        0,0,735,736,5,101,0,0,736,737,5,114,0,0,737,738,5,115,0,0,738,739,
        5,95,0,0,739,740,5,111,0,0,740,741,5,102,0,0,741,742,5,95,0,0,742,
        743,5,116,0,0,743,744,5,101,0,0,744,745,5,110,0,0,745,746,5,115,
        0,0,746,747,5,111,0,0,747,748,5,114,0,0,748,749,5,115,0,0,749,122,
        1,0,0,0,750,751,5,114,0,0,751,752,5,101,0,0,752,753,5,115,0,0,753,
        754,5,104,0,0,754,755,5,97,0,0,755,756,5,112,0,0,756,757,5,101,0,
        0,757,758,5,95,0,0,758,759,5,100,0,0,759,760,5,105,0,0,760,761,5,
        109,0,0,761,124,1,0,0,0,762,763,5,116,0,0,763,764,5,114,0,0,764,
        765,5,97,0,0,765,766,5,110,0,0,766,767,5,115,0,0,767,768,5,112,0,
        0,768,769,5,111,0,0,769,770,5,115,0,0,770,771,5,101,0,0,771,772,
        5,95,0,0,772,773,5,100,0,0,773,774,5,105,0,0,774,775,5,109,0,0,775,
        126,1,0,0,0,776,777,5,112,0,0,777,778,5,101,0,0,778,779,5,114,0,
        0,779,780,5,109,0,0,780,781,5,117,0,0,781,782,5,116,0,0,782,783,
        5,101,0,0,783,784,5,95,0,0,784,785,5,100,0,0,785,786,5,105,0,0,786,
        787,5,109,0,0,787,128,1,0,0,0,788,789,5,97,0,0,789,790,5,102,0,0,
        790,791,5,116,0,0,791,792,5,101,0,0,792,793,5,114,0,0,793,794,5,
        95,0,0,794,795,5,97,0,0,795,796,5,99,0,0,796,797,5,116,0,0,797,798,
        5,105,0,0,798,799,5,118,0,0,799,800,5,95,0,0,800,801,5,102,0,0,801,
        802,5,117,0,0,802,803,5,110,0,0,803,804,5,99,0,0,804,130,1,0,0,0,
        805,806,5,91,0,0,806,132,1,0,0,0,807,808,5,93,0,0,808,134,1,0,0,
        0,809,810,5,114,0,0,810,811,5,101,0,0,811,812,5,108,0,0,812,813,
        5,117,0,0,813,136,1,0,0,0,814,815,5,108,0,0,815,816,5,101,0,0,816,
        817,5,97,0,0,817,818,5,107,0,0,818,819,5,121,0,0,819,820,5,95,0,
        0,820,821,5,114,0,0,821,822,5,101,0,0,822,823,5,108,0,0,823,824,
        5,117,0,0,824,138,1,0,0,0,825,826,5,115,0,0,826,827,5,105,0,0,827,
        828,5,103,0,0,828,829,5,109,0,0,829,830,5,111,0,0,830,831,5,100,
        0,0,831,140,1,0,0,0,832,833,5,115,0,0,833,834,5,111,0,0,834,835,
        5,102,0,0,835,836,5,116,0,0,836,837,5,109,0,0,837,838,5,97,0,0,838,
        839,5,120,0,0,839,142,1,0,0,0,840,841,5,116,0,0,841,842,5,97,0,0,
        842,843,5,110,0,0,843,844,5,104,0,0,844,144,1,0,0,0,845,846,5,78,
        0,0,846,847,5,111,0,0,847,848,5,110,0,0,848,849,5,101,0,0,849,146,
        1,0,0,0,850,851,5,114,0,0,851,852,5,101,0,0,852,853,5,115,0,0,853,
        854,5,104,0,0,854,855,5,97,0,0,855,856,5,112,0,0,856,857,5,101,0,
        0,857,148,1,0,0,0,858,859,5,99,0,0,859,860,5,111,0,0,860,861,5,110,
        0,0,861,862,5,99,0,0,862,863,5,97,0,0,863,864,5,116,0,0,864,865,
        5,101,0,0,865,866,5,110,0,0,866,867,5,97,0,0,867,868,5,116,0,0,868,
        869,5,101,0,0,869,150,1,0,0,0,870,871,5,109,0,0,871,872,5,117,0,
        0,872,873,5,108,0,0,873,874,5,116,0,0,874,875,5,105,0,0,875,876,
        5,112,0,0,876,877,5,108,0,0,877,878,5,121,0,0,878,152,1,0,0,0,879,
        880,5,109,0,0,880,881,5,97,0,0,881,882,5,116,0,0,882,883,5,109,0,
        0,883,884,5,117,0,0,884,885,5,108,0,0,885,886,5,116,0,0,886,887,
        5,105,0,0,887,888,5,112,0,0,888,889,5,108,0,0,889,890,5,121,0,0,
        890,154,1,0,0,0,891,892,5,112,0,0,892,893,5,101,0,0,893,894,5,114,
        0,0,894,895,5,109,0,0,895,896,5,117,0,0,896,897,5,116,0,0,897,898,
        5,101,0,0,898,156,1,0,0,0,899,900,5,116,0,0,900,901,5,114,0,0,901,
        902,5,97,0,0,902,903,5,110,0,0,903,904,5,115,0,0,904,905,5,112,0,
        0,905,906,5,111,0,0,906,907,5,115,0,0,907,908,5,101,0,0,908,158,
        1,0,0,0,909,910,5,98,0,0,910,911,5,105,0,0,911,912,5,110,0,0,912,
        913,5,97,0,0,913,914,5,114,0,0,914,915,5,121,0,0,915,160,1,0,0,0,
        916,917,5,109,0,0,917,918,5,117,0,0,918,919,5,108,0,0,919,920,5,
        116,0,0,920,921,5,105,0,0,921,922,5,95,0,0,922,923,5,99,0,0,923,
        924,5,108,0,0,924,925,5,97,0,0,925,926,5,115,0,0,926,927,5,115,0,
        0,927,162,1,0,0,0,928,929,5,114,0,0,929,930,5,101,0,0,930,931,5,
        103,0,0,931,932,5,114,0,0,932,933,5,101,0,0,933,934,5,115,0,0,934,
        935,5,115,0,0,935,936,5,105,0,0,936,937,5,111,0,0,937,938,5,110,
        0,0,938,164,1,0,0,0,939,940,5,99,0,0,940,941,5,115,0,0,941,942,5,
        118,0,0,942,166,1,0,0,0,943,944,5,105,0,0,944,945,5,109,0,0,945,
        946,5,97,0,0,946,947,5,103,0,0,947,948,5,101,0,0,948,949,5,115,0,
        0,949,168,1,0,0,0,950,951,5,118,0,0,951,952,5,97,0,0,952,953,5,108,
        0,0,953,954,5,105,0,0,954,955,5,100,0,0,955,170,1,0,0,0,956,957,
        5,115,0,0,957,958,5,97,0,0,958,959,5,109,0,0,959,960,5,101,0,0,960,
        172,1,0,0,0,961,962,5,97,0,0,962,963,5,118,0,0,963,964,5,101,0,0,
        964,965,5,114,0,0,965,966,5,97,0,0,966,967,5,103,0,0,967,968,5,101,
        0,0,968,174,1,0,0,0,969,970,5,109,0,0,970,971,5,97,0,0,971,972,5,
        120,0,0,972,176,1,0,0,0,973,974,5,97,0,0,974,975,5,100,0,0,975,976,
        5,97,0,0,976,977,5,112,0,0,977,978,5,116,0,0,978,979,5,105,0,0,979,
        980,5,118,0,0,980,981,5,101,0,0,981,982,5,95,0,0,982,983,5,97,0,
        0,983,984,5,118,0,0,984,985,5,101,0,0,985,986,5,114,0,0,986,987,
        5,97,0,0,987,988,5,103,0,0,988,989,5,101,0,0,989,178,1,0,0,0,990,
        991,5,97,0,0,991,992,5,100,0,0,992,993,5,97,0,0,993,994,5,112,0,
        0,994,995,5,116,0,0,995,996,5,105,0,0,996,997,5,118,0,0,997,998,
        5,101,0,0,998,999,5,95,0,0,999,1000,5,109,0,0,1000,1001,5,97,0,0,
        1001,1002,5,120,0,0,1002,180,1,0,0,0,1003,1004,5,49,0,0,1004,1005,
        5,68,0,0,1005,182,1,0,0,0,1006,1007,5,50,0,0,1007,1008,5,68,0,0,
        1008,184,1,0,0,0,1009,1010,5,51,0,0,1010,1011,5,68,0,0,1011,186,
        1,0,0,0,1012,1016,7,0,0,0,1013,1015,7,1,0,0,1014,1013,1,0,0,0,1015,
        1018,1,0,0,0,1016,1014,1,0,0,0,1016,1017,1,0,0,0,1017,188,1,0,0,
        0,1018,1016,1,0,0,0,1019,1021,7,2,0,0,1020,1019,1,0,0,0,1021,1022,
        1,0,0,0,1022,1020,1,0,0,0,1022,1023,1,0,0,0,1023,190,1,0,0,0,1024,
        1025,5,84,0,0,1025,1026,5,114,0,0,1026,1027,5,117,0,0,1027,1034,
        5,101,0,0,1028,1029,5,70,0,0,1029,1030,5,97,0,0,1030,1031,5,108,
        0,0,1031,1032,5,115,0,0,1032,1034,5,101,0,0,1033,1024,1,0,0,0,1033,
        1028,1,0,0,0,1034,192,1,0,0,0,1035,1037,7,3,0,0,1036,1035,1,0,0,
        0,1037,1038,1,0,0,0,1038,1036,1,0,0,0,1038,1039,1,0,0,0,1039,1040,
        1,0,0,0,1040,1041,6,96,0,0,1041,194,1,0,0,0,1042,1046,5,34,0,0,1043,
        1045,9,0,0,0,1044,1043,1,0,0,0,1045,1048,1,0,0,0,1046,1047,1,0,0,
        0,1046,1044,1,0,0,0,1047,1049,1,0,0,0,1048,1046,1,0,0,0,1049,1050,
        5,34,0,0,1050,196,1,0,0,0,1051,1053,7,2,0,0,1052,1051,1,0,0,0,1053,
        1054,1,0,0,0,1054,1052,1,0,0,0,1054,1055,1,0,0,0,1055,1056,1,0,0,
        0,1056,1060,5,46,0,0,1057,1059,7,2,0,0,1058,1057,1,0,0,0,1059,1062,
        1,0,0,0,1060,1058,1,0,0,0,1060,1061,1,0,0,0,1061,198,1,0,0,0,1062,
        1060,1,0,0,0,8,0,1016,1022,1033,1038,1046,1054,1060,1,6,0,0
    ]

class NNLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    T__26 = 27
    T__27 = 28
    T__28 = 29
    T__29 = 30
    T__30 = 31
    T__31 = 32
    T__32 = 33
    T__33 = 34
    T__34 = 35
    T__35 = 36
    T__36 = 37
    T__37 = 38
    T__38 = 39
    T__39 = 40
    T__40 = 41
    T__41 = 42
    T__42 = 43
    T__43 = 44
    T__44 = 45
    T__45 = 46
    T__46 = 47
    T__47 = 48
    T__48 = 49
    T__49 = 50
    T__50 = 51
    T__51 = 52
    T__52 = 53
    T__53 = 54
    T__54 = 55
    T__55 = 56
    T__56 = 57
    T__57 = 58
    T__58 = 59
    T__59 = 60
    T__60 = 61
    T__61 = 62
    T__62 = 63
    T__63 = 64
    T__64 = 65
    T__65 = 66
    T__66 = 67
    T__67 = 68
    T__68 = 69
    T__69 = 70
    T__70 = 71
    T__71 = 72
    T__72 = 73
    T__73 = 74
    T__74 = 75
    T__75 = 76
    T__76 = 77
    T__77 = 78
    T__78 = 79
    T__79 = 80
    T__80 = 81
    T__81 = 82
    T__82 = 83
    T__83 = 84
    T__84 = 85
    T__85 = 86
    T__86 = 87
    T__87 = 88
    T__88 = 89
    T__89 = 90
    T__90 = 91
    T__91 = 92
    T__92 = 93
    ID = 94
    INT = 95
    BOOL = 96
    WS = 97
    STRING = 98
    DOUBLE = 99

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':'", "'layers'", "'sub_nn'", "'tensor_ops'", "'modules'", 
            "'params'", "'batch_size'", "'='", "'epochs'", "'learning_rate'", 
            "'optimiser'", "'metrics'", "'loss_function'", "'weight_decay'", 
            "'-'", "'actv_func'", "'name_layer_input'", "'input_reused'", 
            "'type'", "'Linear'", "'in_features'", "'out_features'", "'Flatten'", 
            "'start_dim'", "'end_dim'", "'RNN'", "'kernel_dim'", "'stride_dim'", 
            "'padding_type'", "'padding_amount'", "'Conv1D'", "'Conv2D'", 
            "'Conv3D'", "'in_channels'", "'out_channels'", "'Pooling'", 
            "'pooling_type'", "'dimension'", "'output_dim'", "'Dropout'", 
            "'rate'", "'crossentropy'", "'binary_crossentropy'", "'mse'", 
            "'TrainingDataset'", "'name'", "'path_data'", "'task_type'", 
            "'input_format'", "'image'", "'labels'", "'{'", "','", "'}'", 
            "'TestDataset'", "'('", "'col'", "'label'", "')'", "'concatenate_dim'", 
            "'layers_of_tensors'", "'reshape_dim'", "'transpose_dim'", "'permute_dim'", 
            "'after_activ_func'", "'['", "']'", "'relu'", "'leaky_relu'", 
            "'sigmod'", "'softmax'", "'tanh'", "'None'", "'reshape'", "'concatenate'", 
            "'multiply'", "'matmultiply'", "'permute'", "'transpose'", "'binary'", 
            "'multi_class'", "'regression'", "'csv'", "'images'", "'valid'", 
            "'same'", "'average'", "'max'", "'adaptive_average'", "'adaptive_max'", 
            "'1D'", "'2D'", "'3D'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "INT", "BOOL", "WS", "STRING", "DOUBLE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "T__27", "T__28", "T__29", "T__30", "T__31", 
                  "T__32", "T__33", "T__34", "T__35", "T__36", "T__37", 
                  "T__38", "T__39", "T__40", "T__41", "T__42", "T__43", 
                  "T__44", "T__45", "T__46", "T__47", "T__48", "T__49", 
                  "T__50", "T__51", "T__52", "T__53", "T__54", "T__55", 
                  "T__56", "T__57", "T__58", "T__59", "T__60", "T__61", 
                  "T__62", "T__63", "T__64", "T__65", "T__66", "T__67", 
                  "T__68", "T__69", "T__70", "T__71", "T__72", "T__73", 
                  "T__74", "T__75", "T__76", "T__77", "T__78", "T__79", 
                  "T__80", "T__81", "T__82", "T__83", "T__84", "T__85", 
                  "T__86", "T__87", "T__88", "T__89", "T__90", "T__91", 
                  "T__92", "ID", "INT", "BOOL", "WS", "STRING", "DOUBLE" ]

    grammarFileName = "NN.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


