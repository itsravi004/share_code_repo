"""Python Character Mapping Codec generated from 'VENDORS/MICSFT/PC/CP857.TXT' with gencodec.py."""  # "

import codecs

### Codec APIs


class Codec(codecs.Codec):
    def encode(self, input, errors="strict"):
        return codecs.charmap_encode(input, errors, encoding_map)

    def decode(self, input, errors="strict"):
        return codecs.charmap_decode(input, errors, decoding_table)


class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return codecs.charmap_encode(input, self.errors, encoding_map)[0]


class IncrementalDecoder(codecs.IncrementalDecoder):
    def decode(self, input, final=False):
        return codecs.charmap_decode(input, self.errors, decoding_table)[0]


class StreamWriter(Codec, codecs.StreamWriter):
    pass


class StreamReader(Codec, codecs.StreamReader):
    pass


### encodings module API


def getregentry():
    return codecs.CodecInfo(
        name="cp857",
        encode=Codec().encode,
        decode=Codec().decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
        streamreader=StreamReader,
        streamwriter=StreamWriter,
    )


### Decoding Map

decoding_map = codecs.make_identity_dict(range(256))
decoding_map.update(
    {
        0x0080: 0x00C7,  #  LATIN CAPITAL LETTER C WITH CEDILLA
        0x0081: 0x00FC,  #  LATIN SMALL LETTER U WITH DIAERESIS
        0x0082: 0x00E9,  #  LATIN SMALL LETTER E WITH ACUTE
        0x0083: 0x00E2,  #  LATIN SMALL LETTER A WITH CIRCUMFLEX
        0x0084: 0x00E4,  #  LATIN SMALL LETTER A WITH DIAERESIS
        0x0085: 0x00E0,  #  LATIN SMALL LETTER A WITH GRAVE
        0x0086: 0x00E5,  #  LATIN SMALL LETTER A WITH RING ABOVE
        0x0087: 0x00E7,  #  LATIN SMALL LETTER C WITH CEDILLA
        0x0088: 0x00EA,  #  LATIN SMALL LETTER E WITH CIRCUMFLEX
        0x0089: 0x00EB,  #  LATIN SMALL LETTER E WITH DIAERESIS
        0x008A: 0x00E8,  #  LATIN SMALL LETTER E WITH GRAVE
        0x008B: 0x00EF,  #  LATIN SMALL LETTER I WITH DIAERESIS
        0x008C: 0x00EE,  #  LATIN SMALL LETTER I WITH CIRCUMFLEX
        0x008D: 0x0131,  #  LATIN SMALL LETTER DOTLESS I
        0x008E: 0x00C4,  #  LATIN CAPITAL LETTER A WITH DIAERESIS
        0x008F: 0x00C5,  #  LATIN CAPITAL LETTER A WITH RING ABOVE
        0x0090: 0x00C9,  #  LATIN CAPITAL LETTER E WITH ACUTE
        0x0091: 0x00E6,  #  LATIN SMALL LIGATURE AE
        0x0092: 0x00C6,  #  LATIN CAPITAL LIGATURE AE
        0x0093: 0x00F4,  #  LATIN SMALL LETTER O WITH CIRCUMFLEX
        0x0094: 0x00F6,  #  LATIN SMALL LETTER O WITH DIAERESIS
        0x0095: 0x00F2,  #  LATIN SMALL LETTER O WITH GRAVE
        0x0096: 0x00FB,  #  LATIN SMALL LETTER U WITH CIRCUMFLEX
        0x0097: 0x00F9,  #  LATIN SMALL LETTER U WITH GRAVE
        0x0098: 0x0130,  #  LATIN CAPITAL LETTER I WITH DOT ABOVE
        0x0099: 0x00D6,  #  LATIN CAPITAL LETTER O WITH DIAERESIS
        0x009A: 0x00DC,  #  LATIN CAPITAL LETTER U WITH DIAERESIS
        0x009B: 0x00F8,  #  LATIN SMALL LETTER O WITH STROKE
        0x009C: 0x00A3,  #  POUND SIGN
        0x009D: 0x00D8,  #  LATIN CAPITAL LETTER O WITH STROKE
        0x009E: 0x015E,  #  LATIN CAPITAL LETTER S WITH CEDILLA
        0x009F: 0x015F,  #  LATIN SMALL LETTER S WITH CEDILLA
        0x00A0: 0x00E1,  #  LATIN SMALL LETTER A WITH ACUTE
        0x00A1: 0x00ED,  #  LATIN SMALL LETTER I WITH ACUTE
        0x00A2: 0x00F3,  #  LATIN SMALL LETTER O WITH ACUTE
        0x00A3: 0x00FA,  #  LATIN SMALL LETTER U WITH ACUTE
        0x00A4: 0x00F1,  #  LATIN SMALL LETTER N WITH TILDE
        0x00A5: 0x00D1,  #  LATIN CAPITAL LETTER N WITH TILDE
        0x00A6: 0x011E,  #  LATIN CAPITAL LETTER G WITH BREVE
        0x00A7: 0x011F,  #  LATIN SMALL LETTER G WITH BREVE
        0x00A8: 0x00BF,  #  INVERTED QUESTION MARK
        0x00A9: 0x00AE,  #  REGISTERED SIGN
        0x00AA: 0x00AC,  #  NOT SIGN
        0x00AB: 0x00BD,  #  VULGAR FRACTION ONE HALF
        0x00AC: 0x00BC,  #  VULGAR FRACTION ONE QUARTER
        0x00AD: 0x00A1,  #  INVERTED EXCLAMATION MARK
        0x00AE: 0x00AB,  #  LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
        0x00AF: 0x00BB,  #  RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
        0x00B0: 0x2591,  #  LIGHT SHADE
        0x00B1: 0x2592,  #  MEDIUM SHADE
        0x00B2: 0x2593,  #  DARK SHADE
        0x00B3: 0x2502,  #  BOX DRAWINGS LIGHT VERTICAL
        0x00B4: 0x2524,  #  BOX DRAWINGS LIGHT VERTICAL AND LEFT
        0x00B5: 0x00C1,  #  LATIN CAPITAL LETTER A WITH ACUTE
        0x00B6: 0x00C2,  #  LATIN CAPITAL LETTER A WITH CIRCUMFLEX
        0x00B7: 0x00C0,  #  LATIN CAPITAL LETTER A WITH GRAVE
        0x00B8: 0x00A9,  #  COPYRIGHT SIGN
        0x00B9: 0x2563,  #  BOX DRAWINGS DOUBLE VERTICAL AND LEFT
        0x00BA: 0x2551,  #  BOX DRAWINGS DOUBLE VERTICAL
        0x00BB: 0x2557,  #  BOX DRAWINGS DOUBLE DOWN AND LEFT
        0x00BC: 0x255D,  #  BOX DRAWINGS DOUBLE UP AND LEFT
        0x00BD: 0x00A2,  #  CENT SIGN
        0x00BE: 0x00A5,  #  YEN SIGN
        0x00BF: 0x2510,  #  BOX DRAWINGS LIGHT DOWN AND LEFT
        0x00C0: 0x2514,  #  BOX DRAWINGS LIGHT UP AND RIGHT
        0x00C1: 0x2534,  #  BOX DRAWINGS LIGHT UP AND HORIZONTAL
        0x00C2: 0x252C,  #  BOX DRAWINGS LIGHT DOWN AND HORIZONTAL
        0x00C3: 0x251C,  #  BOX DRAWINGS LIGHT VERTICAL AND RIGHT
        0x00C4: 0x2500,  #  BOX DRAWINGS LIGHT HORIZONTAL
        0x00C5: 0x253C,  #  BOX DRAWINGS LIGHT VERTICAL AND HORIZONTAL
        0x00C6: 0x00E3,  #  LATIN SMALL LETTER A WITH TILDE
        0x00C7: 0x00C3,  #  LATIN CAPITAL LETTER A WITH TILDE
        0x00C8: 0x255A,  #  BOX DRAWINGS DOUBLE UP AND RIGHT
        0x00C9: 0x2554,  #  BOX DRAWINGS DOUBLE DOWN AND RIGHT
        0x00CA: 0x2569,  #  BOX DRAWINGS DOUBLE UP AND HORIZONTAL
        0x00CB: 0x2566,  #  BOX DRAWINGS DOUBLE DOWN AND HORIZONTAL
        0x00CC: 0x2560,  #  BOX DRAWINGS DOUBLE VERTICAL AND RIGHT
        0x00CD: 0x2550,  #  BOX DRAWINGS DOUBLE HORIZONTAL
        0x00CE: 0x256C,  #  BOX DRAWINGS DOUBLE VERTICAL AND HORIZONTAL
        0x00CF: 0x00A4,  #  CURRENCY SIGN
        0x00D0: 0x00BA,  #  MASCULINE ORDINAL INDICATOR
        0x00D1: 0x00AA,  #  FEMININE ORDINAL INDICATOR
        0x00D2: 0x00CA,  #  LATIN CAPITAL LETTER E WITH CIRCUMFLEX
        0x00D3: 0x00CB,  #  LATIN CAPITAL LETTER E WITH DIAERESIS
        0x00D4: 0x00C8,  #  LATIN CAPITAL LETTER E WITH GRAVE
        0x00D5: None,  #  UNDEFINED
        0x00D6: 0x00CD,  #  LATIN CAPITAL LETTER I WITH ACUTE
        0x00D7: 0x00CE,  #  LATIN CAPITAL LETTER I WITH CIRCUMFLEX
        0x00D8: 0x00CF,  #  LATIN CAPITAL LETTER I WITH DIAERESIS
        0x00D9: 0x2518,  #  BOX DRAWINGS LIGHT UP AND LEFT
        0x00DA: 0x250C,  #  BOX DRAWINGS LIGHT DOWN AND RIGHT
        0x00DB: 0x2588,  #  FULL BLOCK
        0x00DC: 0x2584,  #  LOWER HALF BLOCK
        0x00DD: 0x00A6,  #  BROKEN BAR
        0x00DE: 0x00CC,  #  LATIN CAPITAL LETTER I WITH GRAVE
        0x00DF: 0x2580,  #  UPPER HALF BLOCK
        0x00E0: 0x00D3,  #  LATIN CAPITAL LETTER O WITH ACUTE
        0x00E1: 0x00DF,  #  LATIN SMALL LETTER SHARP S
        0x00E2: 0x00D4,  #  LATIN CAPITAL LETTER O WITH CIRCUMFLEX
        0x00E3: 0x00D2,  #  LATIN CAPITAL LETTER O WITH GRAVE
        0x00E4: 0x00F5,  #  LATIN SMALL LETTER O WITH TILDE
        0x00E5: 0x00D5,  #  LATIN CAPITAL LETTER O WITH TILDE
        0x00E6: 0x00B5,  #  MICRO SIGN
        0x00E7: None,  #  UNDEFINED
        0x00E8: 0x00D7,  #  MULTIPLICATION SIGN
        0x00E9: 0x00DA,  #  LATIN CAPITAL LETTER U WITH ACUTE
        0x00EA: 0x00DB,  #  LATIN CAPITAL LETTER U WITH CIRCUMFLEX
        0x00EB: 0x00D9,  #  LATIN CAPITAL LETTER U WITH GRAVE
        0x00ED: 0x00FF,  #  LATIN SMALL LETTER Y WITH DIAERESIS
        0x00EE: 0x00AF,  #  MACRON
        0x00EF: 0x00B4,  #  ACUTE ACCENT
        0x00F0: 0x00AD,  #  SOFT HYPHEN
        0x00F1: 0x00B1,  #  PLUS-MINUS SIGN
        0x00F2: None,  #  UNDEFINED
        0x00F3: 0x00BE,  #  VULGAR FRACTION THREE QUARTERS
        0x00F4: 0x00B6,  #  PILCROW SIGN
        0x00F5: 0x00A7,  #  SECTION SIGN
        0x00F6: 0x00F7,  #  DIVISION SIGN
        0x00F7: 0x00B8,  #  CEDILLA
        0x00F8: 0x00B0,  #  DEGREE SIGN
        0x00F9: 0x00A8,  #  DIAERESIS
        0x00FA: 0x00B7,  #  MIDDLE DOT
        0x00FB: 0x00B9,  #  SUPERSCRIPT ONE
        0x00FC: 0x00B3,  #  SUPERSCRIPT THREE
        0x00FD: 0x00B2,  #  SUPERSCRIPT TWO
        0x00FE: 0x25A0,  #  BLACK SQUARE
        0x00FF: 0x00A0,  #  NO-BREAK SPACE
    }
)

### Decoding Table

decoding_table = (
    "\x00"  #  0x0000 -> NULL
    "\x01"  #  0x0001 -> START OF HEADING
    "\x02"  #  0x0002 -> START OF TEXT
    "\x03"  #  0x0003 -> END OF TEXT
    "\x04"  #  0x0004 -> END OF TRANSMISSION
    "\x05"  #  0x0005 -> ENQUIRY
    "\x06"  #  0x0006 -> ACKNOWLEDGE
    "\x07"  #  0x0007 -> BELL
    "\x08"  #  0x0008 -> BACKSPACE
    "\t"  #  0x0009 -> HORIZONTAL TABULATION
    "\n"  #  0x000a -> LINE FEED
    "\x0b"  #  0x000b -> VERTICAL TABULATION
    "\x0c"  #  0x000c -> FORM FEED
    "\r"  #  0x000d -> CARRIAGE RETURN
    "\x0e"  #  0x000e -> SHIFT OUT
    "\x0f"  #  0x000f -> SHIFT IN
    "\x10"  #  0x0010 -> DATA LINK ESCAPE
    "\x11"  #  0x0011 -> DEVICE CONTROL ONE
    "\x12"  #  0x0012 -> DEVICE CONTROL TWO
    "\x13"  #  0x0013 -> DEVICE CONTROL THREE
    "\x14"  #  0x0014 -> DEVICE CONTROL FOUR
    "\x15"  #  0x0015 -> NEGATIVE ACKNOWLEDGE
    "\x16"  #  0x0016 -> SYNCHRONOUS IDLE
    "\x17"  #  0x0017 -> END OF TRANSMISSION BLOCK
    "\x18"  #  0x0018 -> CANCEL
    "\x19"  #  0x0019 -> END OF MEDIUM
    "\x1a"  #  0x001a -> SUBSTITUTE
    "\x1b"  #  0x001b -> ESCAPE
    "\x1c"  #  0x001c -> FILE SEPARATOR
    "\x1d"  #  0x001d -> GROUP SEPARATOR
    "\x1e"  #  0x001e -> RECORD SEPARATOR
    "\x1f"  #  0x001f -> UNIT SEPARATOR
    " "  #  0x0020 -> SPACE
    "!"  #  0x0021 -> EXCLAMATION MARK
    '"'  #  0x0022 -> QUOTATION MARK
    "#"  #  0x0023 -> NUMBER SIGN
    "$"  #  0x0024 -> DOLLAR SIGN
    "%"  #  0x0025 -> PERCENT SIGN
    "&"  #  0x0026 -> AMPERSAND
    "'"  #  0x0027 -> APOSTROPHE
    "("  #  0x0028 -> LEFT PARENTHESIS
    ")"  #  0x0029 -> RIGHT PARENTHESIS
    "*"  #  0x002a -> ASTERISK
    "+"  #  0x002b -> PLUS SIGN
    ","  #  0x002c -> COMMA
    "-"  #  0x002d -> HYPHEN-MINUS
    "."  #  0x002e -> FULL STOP
    "/"  #  0x002f -> SOLIDUS
    "0"  #  0x0030 -> DIGIT ZERO
    "1"  #  0x0031 -> DIGIT ONE
    "2"  #  0x0032 -> DIGIT TWO
    "3"  #  0x0033 -> DIGIT THREE
    "4"  #  0x0034 -> DIGIT FOUR
    "5"  #  0x0035 -> DIGIT FIVE
    "6"  #  0x0036 -> DIGIT SIX
    "7"  #  0x0037 -> DIGIT SEVEN
    "8"  #  0x0038 -> DIGIT EIGHT
    "9"  #  0x0039 -> DIGIT NINE
    ":"  #  0x003a -> COLON
    ";"  #  0x003b -> SEMICOLON
    "<"  #  0x003c -> LESS-THAN SIGN
    "="  #  0x003d -> EQUALS SIGN
    ">"  #  0x003e -> GREATER-THAN SIGN
    "?"  #  0x003f -> QUESTION MARK
    "@"  #  0x0040 -> COMMERCIAL AT
    "A"  #  0x0041 -> LATIN CAPITAL LETTER A
    "B"  #  0x0042 -> LATIN CAPITAL LETTER B
    "C"  #  0x0043 -> LATIN CAPITAL LETTER C
    "D"  #  0x0044 -> LATIN CAPITAL LETTER D
    "E"  #  0x0045 -> LATIN CAPITAL LETTER E
    "F"  #  0x0046 -> LATIN CAPITAL LETTER F
    "G"  #  0x0047 -> LATIN CAPITAL LETTER G
    "H"  #  0x0048 -> LATIN CAPITAL LETTER H
    "I"  #  0x0049 -> LATIN CAPITAL LETTER I
    "J"  #  0x004a -> LATIN CAPITAL LETTER J
    "K"  #  0x004b -> LATIN CAPITAL LETTER K
    "L"  #  0x004c -> LATIN CAPITAL LETTER L
    "M"  #  0x004d -> LATIN CAPITAL LETTER M
    "N"  #  0x004e -> LATIN CAPITAL LETTER N
    "O"  #  0x004f -> LATIN CAPITAL LETTER O
    "P"  #  0x0050 -> LATIN CAPITAL LETTER P
    "Q"  #  0x0051 -> LATIN CAPITAL LETTER Q
    "R"  #  0x0052 -> LATIN CAPITAL LETTER R
    "S"  #  0x0053 -> LATIN CAPITAL LETTER S
    "T"  #  0x0054 -> LATIN CAPITAL LETTER T
    "U"  #  0x0055 -> LATIN CAPITAL LETTER U
    "V"  #  0x0056 -> LATIN CAPITAL LETTER V
    "W"  #  0x0057 -> LATIN CAPITAL LETTER W
    "X"  #  0x0058 -> LATIN CAPITAL LETTER X
    "Y"  #  0x0059 -> LATIN CAPITAL LETTER Y
    "Z"  #  0x005a -> LATIN CAPITAL LETTER Z
    "["  #  0x005b -> LEFT SQUARE BRACKET
    "\\"  #  0x005c -> REVERSE SOLIDUS
    "]"  #  0x005d -> RIGHT SQUARE BRACKET
    "^"  #  0x005e -> CIRCUMFLEX ACCENT
    "_"  #  0x005f -> LOW LINE
    "`"  #  0x0060 -> GRAVE ACCENT
    "a"  #  0x0061 -> LATIN SMALL LETTER A
    "b"  #  0x0062 -> LATIN SMALL LETTER B
    "c"  #  0x0063 -> LATIN SMALL LETTER C
    "d"  #  0x0064 -> LATIN SMALL LETTER D
    "e"  #  0x0065 -> LATIN SMALL LETTER E
    "f"  #  0x0066 -> LATIN SMALL LETTER F
    "g"  #  0x0067 -> LATIN SMALL LETTER G
    "h"  #  0x0068 -> LATIN SMALL LETTER H
    "i"  #  0x0069 -> LATIN SMALL LETTER I
    "j"  #  0x006a -> LATIN SMALL LETTER J
    "k"  #  0x006b -> LATIN SMALL LETTER K
    "l"  #  0x006c -> LATIN SMALL LETTER L
    "m"  #  0x006d -> LATIN SMALL LETTER M
    "n"  #  0x006e -> LATIN SMALL LETTER N
    "o"  #  0x006f -> LATIN SMALL LETTER O
    "p"  #  0x0070 -> LATIN SMALL LETTER P
    "q"  #  0x0071 -> LATIN SMALL LETTER Q
    "r"  #  0x0072 -> LATIN SMALL LETTER R
    "s"  #  0x0073 -> LATIN SMALL LETTER S
    "t"  #  0x0074 -> LATIN SMALL LETTER T
    "u"  #  0x0075 -> LATIN SMALL LETTER U
    "v"  #  0x0076 -> LATIN SMALL LETTER V
    "w"  #  0x0077 -> LATIN SMALL LETTER W
    "x"  #  0x0078 -> LATIN SMALL LETTER X
    "y"  #  0x0079 -> LATIN SMALL LETTER Y
    "z"  #  0x007a -> LATIN SMALL LETTER Z
    "{"  #  0x007b -> LEFT CURLY BRACKET
    "|"  #  0x007c -> VERTICAL LINE
    "}"  #  0x007d -> RIGHT CURLY BRACKET
    "~"  #  0x007e -> TILDE
    "\x7f"  #  0x007f -> DELETE
    "\xc7"  #  0x0080 -> LATIN CAPITAL LETTER C WITH CEDILLA
    "\xfc"  #  0x0081 -> LATIN SMALL LETTER U WITH DIAERESIS
    "\xe9"  #  0x0082 -> LATIN SMALL LETTER E WITH ACUTE
    "\xe2"  #  0x0083 -> LATIN SMALL LETTER A WITH CIRCUMFLEX
    "\xe4"  #  0x0084 -> LATIN SMALL LETTER A WITH DIAERESIS
    "\xe0"  #  0x0085 -> LATIN SMALL LETTER A WITH GRAVE
    "\xe5"  #  0x0086 -> LATIN SMALL LETTER A WITH RING ABOVE
    "\xe7"  #  0x0087 -> LATIN SMALL LETTER C WITH CEDILLA
    "\xea"  #  0x0088 -> LATIN SMALL LETTER E WITH CIRCUMFLEX
    "\xeb"  #  0x0089 -> LATIN SMALL LETTER E WITH DIAERESIS
    "\xe8"  #  0x008a -> LATIN SMALL LETTER E WITH GRAVE
    "\xef"  #  0x008b -> LATIN SMALL LETTER I WITH DIAERESIS
    "\xee"  #  0x008c -> LATIN SMALL LETTER I WITH CIRCUMFLEX
    "\u0131"  #  0x008d -> LATIN SMALL LETTER DOTLESS I
    "\xc4"  #  0x008e -> LATIN CAPITAL LETTER A WITH DIAERESIS
    "\xc5"  #  0x008f -> LATIN CAPITAL LETTER A WITH RING ABOVE
    "\xc9"  #  0x0090 -> LATIN CAPITAL LETTER E WITH ACUTE
    "\xe6"  #  0x0091 -> LATIN SMALL LIGATURE AE
    "\xc6"  #  0x0092 -> LATIN CAPITAL LIGATURE AE
    "\xf4"  #  0x0093 -> LATIN SMALL LETTER O WITH CIRCUMFLEX
    "\xf6"  #  0x0094 -> LATIN SMALL LETTER O WITH DIAERESIS
    "\xf2"  #  0x0095 -> LATIN SMALL LETTER O WITH GRAVE
    "\xfb"  #  0x0096 -> LATIN SMALL LETTER U WITH CIRCUMFLEX
    "\xf9"  #  0x0097 -> LATIN SMALL LETTER U WITH GRAVE
    "\u0130"  #  0x0098 -> LATIN CAPITAL LETTER I WITH DOT ABOVE
    "\xd6"  #  0x0099 -> LATIN CAPITAL LETTER O WITH DIAERESIS
    "\xdc"  #  0x009a -> LATIN CAPITAL LETTER U WITH DIAERESIS
    "\xf8"  #  0x009b -> LATIN SMALL LETTER O WITH STROKE
    "\xa3"  #  0x009c -> POUND SIGN
    "\xd8"  #  0x009d -> LATIN CAPITAL LETTER O WITH STROKE
    "\u015e"  #  0x009e -> LATIN CAPITAL LETTER S WITH CEDILLA
    "\u015f"  #  0x009f -> LATIN SMALL LETTER S WITH CEDILLA
    "\xe1"  #  0x00a0 -> LATIN SMALL LETTER A WITH ACUTE
    "\xed"  #  0x00a1 -> LATIN SMALL LETTER I WITH ACUTE
    "\xf3"  #  0x00a2 -> LATIN SMALL LETTER O WITH ACUTE
    "\xfa"  #  0x00a3 -> LATIN SMALL LETTER U WITH ACUTE
    "\xf1"  #  0x00a4 -> LATIN SMALL LETTER N WITH TILDE
    "\xd1"  #  0x00a5 -> LATIN CAPITAL LETTER N WITH TILDE
    "\u011e"  #  0x00a6 -> LATIN CAPITAL LETTER G WITH BREVE
    "\u011f"  #  0x00a7 -> LATIN SMALL LETTER G WITH BREVE
    "\xbf"  #  0x00a8 -> INVERTED QUESTION MARK
    "\xae"  #  0x00a9 -> REGISTERED SIGN
    "\xac"  #  0x00aa -> NOT SIGN
    "\xbd"  #  0x00ab -> VULGAR FRACTION ONE HALF
    "\xbc"  #  0x00ac -> VULGAR FRACTION ONE QUARTER
    "\xa1"  #  0x00ad -> INVERTED EXCLAMATION MARK
    "\xab"  #  0x00ae -> LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
    "\xbb"  #  0x00af -> RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
    "\u2591"  #  0x00b0 -> LIGHT SHADE
    "\u2592"  #  0x00b1 -> MEDIUM SHADE
    "\u2593"  #  0x00b2 -> DARK SHADE
    "\u2502"  #  0x00b3 -> BOX DRAWINGS LIGHT VERTICAL
    "\u2524"  #  0x00b4 -> BOX DRAWINGS LIGHT VERTICAL AND LEFT
    "\xc1"  #  0x00b5 -> LATIN CAPITAL LETTER A WITH ACUTE
    "\xc2"  #  0x00b6 -> LATIN CAPITAL LETTER A WITH CIRCUMFLEX
    "\xc0"  #  0x00b7 -> LATIN CAPITAL LETTER A WITH GRAVE
    "\xa9"  #  0x00b8 -> COPYRIGHT SIGN
    "\u2563"  #  0x00b9 -> BOX DRAWINGS DOUBLE VERTICAL AND LEFT
    "\u2551"  #  0x00ba -> BOX DRAWINGS DOUBLE VERTICAL
    "\u2557"  #  0x00bb -> BOX DRAWINGS DOUBLE DOWN AND LEFT
    "\u255d"  #  0x00bc -> BOX DRAWINGS DOUBLE UP AND LEFT
    "\xa2"  #  0x00bd -> CENT SIGN
    "\xa5"  #  0x00be -> YEN SIGN
    "\u2510"  #  0x00bf -> BOX DRAWINGS LIGHT DOWN AND LEFT
    "\u2514"  #  0x00c0 -> BOX DRAWINGS LIGHT UP AND RIGHT
    "\u2534"  #  0x00c1 -> BOX DRAWINGS LIGHT UP AND HORIZONTAL
    "\u252c"  #  0x00c2 -> BOX DRAWINGS LIGHT DOWN AND HORIZONTAL
    "\u251c"  #  0x00c3 -> BOX DRAWINGS LIGHT VERTICAL AND RIGHT
    "\u2500"  #  0x00c4 -> BOX DRAWINGS LIGHT HORIZONTAL
    "\u253c"  #  0x00c5 -> BOX DRAWINGS LIGHT VERTICAL AND HORIZONTAL
    "\xe3"  #  0x00c6 -> LATIN SMALL LETTER A WITH TILDE
    "\xc3"  #  0x00c7 -> LATIN CAPITAL LETTER A WITH TILDE
    "\u255a"  #  0x00c8 -> BOX DRAWINGS DOUBLE UP AND RIGHT
    "\u2554"  #  0x00c9 -> BOX DRAWINGS DOUBLE DOWN AND RIGHT
    "\u2569"  #  0x00ca -> BOX DRAWINGS DOUBLE UP AND HORIZONTAL
    "\u2566"  #  0x00cb -> BOX DRAWINGS DOUBLE DOWN AND HORIZONTAL
    "\u2560"  #  0x00cc -> BOX DRAWINGS DOUBLE VERTICAL AND RIGHT
    "\u2550"  #  0x00cd -> BOX DRAWINGS DOUBLE HORIZONTAL
    "\u256c"  #  0x00ce -> BOX DRAWINGS DOUBLE VERTICAL AND HORIZONTAL
    "\xa4"  #  0x00cf -> CURRENCY SIGN
    "\xba"  #  0x00d0 -> MASCULINE ORDINAL INDICATOR
    "\xaa"  #  0x00d1 -> FEMININE ORDINAL INDICATOR
    "\xca"  #  0x00d2 -> LATIN CAPITAL LETTER E WITH CIRCUMFLEX
    "\xcb"  #  0x00d3 -> LATIN CAPITAL LETTER E WITH DIAERESIS
    "\xc8"  #  0x00d4 -> LATIN CAPITAL LETTER E WITH GRAVE
    "\ufffe"  #  0x00d5 -> UNDEFINED
    "\xcd"  #  0x00d6 -> LATIN CAPITAL LETTER I WITH ACUTE
    "\xce"  #  0x00d7 -> LATIN CAPITAL LETTER I WITH CIRCUMFLEX
    "\xcf"  #  0x00d8 -> LATIN CAPITAL LETTER I WITH DIAERESIS
    "\u2518"  #  0x00d9 -> BOX DRAWINGS LIGHT UP AND LEFT
    "\u250c"  #  0x00da -> BOX DRAWINGS LIGHT DOWN AND RIGHT
    "\u2588"  #  0x00db -> FULL BLOCK
    "\u2584"  #  0x00dc -> LOWER HALF BLOCK
    "\xa6"  #  0x00dd -> BROKEN BAR
    "\xcc"  #  0x00de -> LATIN CAPITAL LETTER I WITH GRAVE
    "\u2580"  #  0x00df -> UPPER HALF BLOCK
    "\xd3"  #  0x00e0 -> LATIN CAPITAL LETTER O WITH ACUTE
    "\xdf"  #  0x00e1 -> LATIN SMALL LETTER SHARP S
    "\xd4"  #  0x00e2 -> LATIN CAPITAL LETTER O WITH CIRCUMFLEX
    "\xd2"  #  0x00e3 -> LATIN CAPITAL LETTER O WITH GRAVE
    "\xf5"  #  0x00e4 -> LATIN SMALL LETTER O WITH TILDE
    "\xd5"  #  0x00e5 -> LATIN CAPITAL LETTER O WITH TILDE
    "\xb5"  #  0x00e6 -> MICRO SIGN
    "\ufffe"  #  0x00e7 -> UNDEFINED
    "\xd7"  #  0x00e8 -> MULTIPLICATION SIGN
    "\xda"  #  0x00e9 -> LATIN CAPITAL LETTER U WITH ACUTE
    "\xdb"  #  0x00ea -> LATIN CAPITAL LETTER U WITH CIRCUMFLEX
    "\xd9"  #  0x00eb -> LATIN CAPITAL LETTER U WITH GRAVE
    "\xec"  #  0x00ec -> LATIN SMALL LETTER I WITH GRAVE
    "\xff"  #  0x00ed -> LATIN SMALL LETTER Y WITH DIAERESIS
    "\xaf"  #  0x00ee -> MACRON
    "\xb4"  #  0x00ef -> ACUTE ACCENT
    "\xad"  #  0x00f0 -> SOFT HYPHEN
    "\xb1"  #  0x00f1 -> PLUS-MINUS SIGN
    "\ufffe"  #  0x00f2 -> UNDEFINED
    "\xbe"  #  0x00f3 -> VULGAR FRACTION THREE QUARTERS
    "\xb6"  #  0x00f4 -> PILCROW SIGN
    "\xa7"  #  0x00f5 -> SECTION SIGN
    "\xf7"  #  0x00f6 -> DIVISION SIGN
    "\xb8"  #  0x00f7 -> CEDILLA
    "\xb0"  #  0x00f8 -> DEGREE SIGN
    "\xa8"  #  0x00f9 -> DIAERESIS
    "\xb7"  #  0x00fa -> MIDDLE DOT
    "\xb9"  #  0x00fb -> SUPERSCRIPT ONE
    "\xb3"  #  0x00fc -> SUPERSCRIPT THREE
    "\xb2"  #  0x00fd -> SUPERSCRIPT TWO
    "\u25a0"  #  0x00fe -> BLACK SQUARE
    "\xa0"  #  0x00ff -> NO-BREAK SPACE
)

### Encoding Map

encoding_map = {
    0x0000: 0x0000,  #  NULL
    0x0001: 0x0001,  #  START OF HEADING
    0x0002: 0x0002,  #  START OF TEXT
    0x0003: 0x0003,  #  END OF TEXT
    0x0004: 0x0004,  #  END OF TRANSMISSION
    0x0005: 0x0005,  #  ENQUIRY
    0x0006: 0x0006,  #  ACKNOWLEDGE
    0x0007: 0x0007,  #  BELL
    0x0008: 0x0008,  #  BACKSPACE
    0x0009: 0x0009,  #  HORIZONTAL TABULATION
    0x000A: 0x000A,  #  LINE FEED
    0x000B: 0x000B,  #  VERTICAL TABULATION
    0x000C: 0x000C,  #  FORM FEED
    0x000D: 0x000D,  #  CARRIAGE RETURN
    0x000E: 0x000E,  #  SHIFT OUT
    0x000F: 0x000F,  #  SHIFT IN
    0x0010: 0x0010,  #  DATA LINK ESCAPE
    0x0011: 0x0011,  #  DEVICE CONTROL ONE
    0x0012: 0x0012,  #  DEVICE CONTROL TWO
    0x0013: 0x0013,  #  DEVICE CONTROL THREE
    0x0014: 0x0014,  #  DEVICE CONTROL FOUR
    0x0015: 0x0015,  #  NEGATIVE ACKNOWLEDGE
    0x0016: 0x0016,  #  SYNCHRONOUS IDLE
    0x0017: 0x0017,  #  END OF TRANSMISSION BLOCK
    0x0018: 0x0018,  #  CANCEL
    0x0019: 0x0019,  #  END OF MEDIUM
    0x001A: 0x001A,  #  SUBSTITUTE
    0x001B: 0x001B,  #  ESCAPE
    0x001C: 0x001C,  #  FILE SEPARATOR
    0x001D: 0x001D,  #  GROUP SEPARATOR
    0x001E: 0x001E,  #  RECORD SEPARATOR
    0x001F: 0x001F,  #  UNIT SEPARATOR
    0x0020: 0x0020,  #  SPACE
    0x0021: 0x0021,  #  EXCLAMATION MARK
    0x0022: 0x0022,  #  QUOTATION MARK
    0x0023: 0x0023,  #  NUMBER SIGN
    0x0024: 0x0024,  #  DOLLAR SIGN
    0x0025: 0x0025,  #  PERCENT SIGN
    0x0026: 0x0026,  #  AMPERSAND
    0x0027: 0x0027,  #  APOSTROPHE
    0x0028: 0x0028,  #  LEFT PARENTHESIS
    0x0029: 0x0029,  #  RIGHT PARENTHESIS
    0x002A: 0x002A,  #  ASTERISK
    0x002B: 0x002B,  #  PLUS SIGN
    0x002C: 0x002C,  #  COMMA
    0x002D: 0x002D,  #  HYPHEN-MINUS
    0x002E: 0x002E,  #  FULL STOP
    0x002F: 0x002F,  #  SOLIDUS
    0x0030: 0x0030,  #  DIGIT ZERO
    0x0031: 0x0031,  #  DIGIT ONE
    0x0032: 0x0032,  #  DIGIT TWO
    0x0033: 0x0033,  #  DIGIT THREE
    0x0034: 0x0034,  #  DIGIT FOUR
    0x0035: 0x0035,  #  DIGIT FIVE
    0x0036: 0x0036,  #  DIGIT SIX
    0x0037: 0x0037,  #  DIGIT SEVEN
    0x0038: 0x0038,  #  DIGIT EIGHT
    0x0039: 0x0039,  #  DIGIT NINE
    0x003A: 0x003A,  #  COLON
    0x003B: 0x003B,  #  SEMICOLON
    0x003C: 0x003C,  #  LESS-THAN SIGN
    0x003D: 0x003D,  #  EQUALS SIGN
    0x003E: 0x003E,  #  GREATER-THAN SIGN
    0x003F: 0x003F,  #  QUESTION MARK
    0x0040: 0x0040,  #  COMMERCIAL AT
    0x0041: 0x0041,  #  LATIN CAPITAL LETTER A
    0x0042: 0x0042,  #  LATIN CAPITAL LETTER B
    0x0043: 0x0043,  #  LATIN CAPITAL LETTER C
    0x0044: 0x0044,  #  LATIN CAPITAL LETTER D
    0x0045: 0x0045,  #  LATIN CAPITAL LETTER E
    0x0046: 0x0046,  #  LATIN CAPITAL LETTER F
    0x0047: 0x0047,  #  LATIN CAPITAL LETTER G
    0x0048: 0x0048,  #  LATIN CAPITAL LETTER H
    0x0049: 0x0049,  #  LATIN CAPITAL LETTER I
    0x004A: 0x004A,  #  LATIN CAPITAL LETTER J
    0x004B: 0x004B,  #  LATIN CAPITAL LETTER K
    0x004C: 0x004C,  #  LATIN CAPITAL LETTER L
    0x004D: 0x004D,  #  LATIN CAPITAL LETTER M
    0x004E: 0x004E,  #  LATIN CAPITAL LETTER N
    0x004F: 0x004F,  #  LATIN CAPITAL LETTER O
    0x0050: 0x0050,  #  LATIN CAPITAL LETTER P
    0x0051: 0x0051,  #  LATIN CAPITAL LETTER Q
    0x0052: 0x0052,  #  LATIN CAPITAL LETTER R
    0x0053: 0x0053,  #  LATIN CAPITAL LETTER S
    0x0054: 0x0054,  #  LATIN CAPITAL LETTER T
    0x0055: 0x0055,  #  LATIN CAPITAL LETTER U
    0x0056: 0x0056,  #  LATIN CAPITAL LETTER V
    0x0057: 0x0057,  #  LATIN CAPITAL LETTER W
    0x0058: 0x0058,  #  LATIN CAPITAL LETTER X
    0x0059: 0x0059,  #  LATIN CAPITAL LETTER Y
    0x005A: 0x005A,  #  LATIN CAPITAL LETTER Z
    0x005B: 0x005B,  #  LEFT SQUARE BRACKET
    0x005C: 0x005C,  #  REVERSE SOLIDUS
    0x005D: 0x005D,  #  RIGHT SQUARE BRACKET
    0x005E: 0x005E,  #  CIRCUMFLEX ACCENT
    0x005F: 0x005F,  #  LOW LINE
    0x0060: 0x0060,  #  GRAVE ACCENT
    0x0061: 0x0061,  #  LATIN SMALL LETTER A
    0x0062: 0x0062,  #  LATIN SMALL LETTER B
    0x0063: 0x0063,  #  LATIN SMALL LETTER C
    0x0064: 0x0064,  #  LATIN SMALL LETTER D
    0x0065: 0x0065,  #  LATIN SMALL LETTER E
    0x0066: 0x0066,  #  LATIN SMALL LETTER F
    0x0067: 0x0067,  #  LATIN SMALL LETTER G
    0x0068: 0x0068,  #  LATIN SMALL LETTER H
    0x0069: 0x0069,  #  LATIN SMALL LETTER I
    0x006A: 0x006A,  #  LATIN SMALL LETTER J
    0x006B: 0x006B,  #  LATIN SMALL LETTER K
    0x006C: 0x006C,  #  LATIN SMALL LETTER L
    0x006D: 0x006D,  #  LATIN SMALL LETTER M
    0x006E: 0x006E,  #  LATIN SMALL LETTER N
    0x006F: 0x006F,  #  LATIN SMALL LETTER O
    0x0070: 0x0070,  #  LATIN SMALL LETTER P
    0x0071: 0x0071,  #  LATIN SMALL LETTER Q
    0x0072: 0x0072,  #  LATIN SMALL LETTER R
    0x0073: 0x0073,  #  LATIN SMALL LETTER S
    0x0074: 0x0074,  #  LATIN SMALL LETTER T
    0x0075: 0x0075,  #  LATIN SMALL LETTER U
    0x0076: 0x0076,  #  LATIN SMALL LETTER V
    0x0077: 0x0077,  #  LATIN SMALL LETTER W
    0x0078: 0x0078,  #  LATIN SMALL LETTER X
    0x0079: 0x0079,  #  LATIN SMALL LETTER Y
    0x007A: 0x007A,  #  LATIN SMALL LETTER Z
    0x007B: 0x007B,  #  LEFT CURLY BRACKET
    0x007C: 0x007C,  #  VERTICAL LINE
    0x007D: 0x007D,  #  RIGHT CURLY BRACKET
    0x007E: 0x007E,  #  TILDE
    0x007F: 0x007F,  #  DELETE
    0x00A0: 0x00FF,  #  NO-BREAK SPACE
    0x00A1: 0x00AD,  #  INVERTED EXCLAMATION MARK
    0x00A2: 0x00BD,  #  CENT SIGN
    0x00A3: 0x009C,  #  POUND SIGN
    0x00A4: 0x00CF,  #  CURRENCY SIGN
    0x00A5: 0x00BE,  #  YEN SIGN
    0x00A6: 0x00DD,  #  BROKEN BAR
    0x00A7: 0x00F5,  #  SECTION SIGN
    0x00A8: 0x00F9,  #  DIAERESIS
    0x00A9: 0x00B8,  #  COPYRIGHT SIGN
    0x00AA: 0x00D1,  #  FEMININE ORDINAL INDICATOR
    0x00AB: 0x00AE,  #  LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
    0x00AC: 0x00AA,  #  NOT SIGN
    0x00AD: 0x00F0,  #  SOFT HYPHEN
    0x00AE: 0x00A9,  #  REGISTERED SIGN
    0x00AF: 0x00EE,  #  MACRON
    0x00B0: 0x00F8,  #  DEGREE SIGN
    0x00B1: 0x00F1,  #  PLUS-MINUS SIGN
    0x00B2: 0x00FD,  #  SUPERSCRIPT TWO
    0x00B3: 0x00FC,  #  SUPERSCRIPT THREE
    0x00B4: 0x00EF,  #  ACUTE ACCENT
    0x00B5: 0x00E6,  #  MICRO SIGN
    0x00B6: 0x00F4,  #  PILCROW SIGN
    0x00B7: 0x00FA,  #  MIDDLE DOT
    0x00B8: 0x00F7,  #  CEDILLA
    0x00B9: 0x00FB,  #  SUPERSCRIPT ONE
    0x00BA: 0x00D0,  #  MASCULINE ORDINAL INDICATOR
    0x00BB: 0x00AF,  #  RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
    0x00BC: 0x00AC,  #  VULGAR FRACTION ONE QUARTER
    0x00BD: 0x00AB,  #  VULGAR FRACTION ONE HALF
    0x00BE: 0x00F3,  #  VULGAR FRACTION THREE QUARTERS
    0x00BF: 0x00A8,  #  INVERTED QUESTION MARK
    0x00C0: 0x00B7,  #  LATIN CAPITAL LETTER A WITH GRAVE
    0x00C1: 0x00B5,  #  LATIN CAPITAL LETTER A WITH ACUTE
    0x00C2: 0x00B6,  #  LATIN CAPITAL LETTER A WITH CIRCUMFLEX
    0x00C3: 0x00C7,  #  LATIN CAPITAL LETTER A WITH TILDE
    0x00C4: 0x008E,  #  LATIN CAPITAL LETTER A WITH DIAERESIS
    0x00C5: 0x008F,  #  LATIN CAPITAL LETTER A WITH RING ABOVE
    0x00C6: 0x0092,  #  LATIN CAPITAL LIGATURE AE
    0x00C7: 0x0080,  #  LATIN CAPITAL LETTER C WITH CEDILLA
    0x00C8: 0x00D4,  #  LATIN CAPITAL LETTER E WITH GRAVE
    0x00C9: 0x0090,  #  LATIN CAPITAL LETTER E WITH ACUTE
    0x00CA: 0x00D2,  #  LATIN CAPITAL LETTER E WITH CIRCUMFLEX
    0x00CB: 0x00D3,  #  LATIN CAPITAL LETTER E WITH DIAERESIS
    0x00CC: 0x00DE,  #  LATIN CAPITAL LETTER I WITH GRAVE
    0x00CD: 0x00D6,  #  LATIN CAPITAL LETTER I WITH ACUTE
    0x00CE: 0x00D7,  #  LATIN CAPITAL LETTER I WITH CIRCUMFLEX
    0x00CF: 0x00D8,  #  LATIN CAPITAL LETTER I WITH DIAERESIS
    0x00D1: 0x00A5,  #  LATIN CAPITAL LETTER N WITH TILDE
    0x00D2: 0x00E3,  #  LATIN CAPITAL LETTER O WITH GRAVE
    0x00D3: 0x00E0,  #  LATIN CAPITAL LETTER O WITH ACUTE
    0x00D4: 0x00E2,  #  LATIN CAPITAL LETTER O WITH CIRCUMFLEX
    0x00D5: 0x00E5,  #  LATIN CAPITAL LETTER O WITH TILDE
    0x00D6: 0x0099,  #  LATIN CAPITAL LETTER O WITH DIAERESIS
    0x00D7: 0x00E8,  #  MULTIPLICATION SIGN
    0x00D8: 0x009D,  #  LATIN CAPITAL LETTER O WITH STROKE
    0x00D9: 0x00EB,  #  LATIN CAPITAL LETTER U WITH GRAVE
    0x00DA: 0x00E9,  #  LATIN CAPITAL LETTER U WITH ACUTE
    0x00DB: 0x00EA,  #  LATIN CAPITAL LETTER U WITH CIRCUMFLEX
    0x00DC: 0x009A,  #  LATIN CAPITAL LETTER U WITH DIAERESIS
    0x00DF: 0x00E1,  #  LATIN SMALL LETTER SHARP S
    0x00E0: 0x0085,  #  LATIN SMALL LETTER A WITH GRAVE
    0x00E1: 0x00A0,  #  LATIN SMALL LETTER A WITH ACUTE
    0x00E2: 0x0083,  #  LATIN SMALL LETTER A WITH CIRCUMFLEX
    0x00E3: 0x00C6,  #  LATIN SMALL LETTER A WITH TILDE
    0x00E4: 0x0084,  #  LATIN SMALL LETTER A WITH DIAERESIS
    0x00E5: 0x0086,  #  LATIN SMALL LETTER A WITH RING ABOVE
    0x00E6: 0x0091,  #  LATIN SMALL LIGATURE AE
    0x00E7: 0x0087,  #  LATIN SMALL LETTER C WITH CEDILLA
    0x00E8: 0x008A,  #  LATIN SMALL LETTER E WITH GRAVE
    0x00E9: 0x0082,  #  LATIN SMALL LETTER E WITH ACUTE
    0x00EA: 0x0088,  #  LATIN SMALL LETTER E WITH CIRCUMFLEX
    0x00EB: 0x0089,  #  LATIN SMALL LETTER E WITH DIAERESIS
    0x00EC: 0x00EC,  #  LATIN SMALL LETTER I WITH GRAVE
    0x00ED: 0x00A1,  #  LATIN SMALL LETTER I WITH ACUTE
    0x00EE: 0x008C,  #  LATIN SMALL LETTER I WITH CIRCUMFLEX
    0x00EF: 0x008B,  #  LATIN SMALL LETTER I WITH DIAERESIS
    0x00F1: 0x00A4,  #  LATIN SMALL LETTER N WITH TILDE
    0x00F2: 0x0095,  #  LATIN SMALL LETTER O WITH GRAVE
    0x00F3: 0x00A2,  #  LATIN SMALL LETTER O WITH ACUTE
    0x00F4: 0x0093,  #  LATIN SMALL LETTER O WITH CIRCUMFLEX
    0x00F5: 0x00E4,  #  LATIN SMALL LETTER O WITH TILDE
    0x00F6: 0x0094,  #  LATIN SMALL LETTER O WITH DIAERESIS
    0x00F7: 0x00F6,  #  DIVISION SIGN
    0x00F8: 0x009B,  #  LATIN SMALL LETTER O WITH STROKE
    0x00F9: 0x0097,  #  LATIN SMALL LETTER U WITH GRAVE
    0x00FA: 0x00A3,  #  LATIN SMALL LETTER U WITH ACUTE
    0x00FB: 0x0096,  #  LATIN SMALL LETTER U WITH CIRCUMFLEX
    0x00FC: 0x0081,  #  LATIN SMALL LETTER U WITH DIAERESIS
    0x00FF: 0x00ED,  #  LATIN SMALL LETTER Y WITH DIAERESIS
    0x011E: 0x00A6,  #  LATIN CAPITAL LETTER G WITH BREVE
    0x011F: 0x00A7,  #  LATIN SMALL LETTER G WITH BREVE
    0x0130: 0x0098,  #  LATIN CAPITAL LETTER I WITH DOT ABOVE
    0x0131: 0x008D,  #  LATIN SMALL LETTER DOTLESS I
    0x015E: 0x009E,  #  LATIN CAPITAL LETTER S WITH CEDILLA
    0x015F: 0x009F,  #  LATIN SMALL LETTER S WITH CEDILLA
    0x2500: 0x00C4,  #  BOX DRAWINGS LIGHT HORIZONTAL
    0x2502: 0x00B3,  #  BOX DRAWINGS LIGHT VERTICAL
    0x250C: 0x00DA,  #  BOX DRAWINGS LIGHT DOWN AND RIGHT
    0x2510: 0x00BF,  #  BOX DRAWINGS LIGHT DOWN AND LEFT
    0x2514: 0x00C0,  #  BOX DRAWINGS LIGHT UP AND RIGHT
    0x2518: 0x00D9,  #  BOX DRAWINGS LIGHT UP AND LEFT
    0x251C: 0x00C3,  #  BOX DRAWINGS LIGHT VERTICAL AND RIGHT
    0x2524: 0x00B4,  #  BOX DRAWINGS LIGHT VERTICAL AND LEFT
    0x252C: 0x00C2,  #  BOX DRAWINGS LIGHT DOWN AND HORIZONTAL
    0x2534: 0x00C1,  #  BOX DRAWINGS LIGHT UP AND HORIZONTAL
    0x253C: 0x00C5,  #  BOX DRAWINGS LIGHT VERTICAL AND HORIZONTAL
    0x2550: 0x00CD,  #  BOX DRAWINGS DOUBLE HORIZONTAL
    0x2551: 0x00BA,  #  BOX DRAWINGS DOUBLE VERTICAL
    0x2554: 0x00C9,  #  BOX DRAWINGS DOUBLE DOWN AND RIGHT
    0x2557: 0x00BB,  #  BOX DRAWINGS DOUBLE DOWN AND LEFT
    0x255A: 0x00C8,  #  BOX DRAWINGS DOUBLE UP AND RIGHT
    0x255D: 0x00BC,  #  BOX DRAWINGS DOUBLE UP AND LEFT
    0x2560: 0x00CC,  #  BOX DRAWINGS DOUBLE VERTICAL AND RIGHT
    0x2563: 0x00B9,  #  BOX DRAWINGS DOUBLE VERTICAL AND LEFT
    0x2566: 0x00CB,  #  BOX DRAWINGS DOUBLE DOWN AND HORIZONTAL
    0x2569: 0x00CA,  #  BOX DRAWINGS DOUBLE UP AND HORIZONTAL
    0x256C: 0x00CE,  #  BOX DRAWINGS DOUBLE VERTICAL AND HORIZONTAL
    0x2580: 0x00DF,  #  UPPER HALF BLOCK
    0x2584: 0x00DC,  #  LOWER HALF BLOCK
    0x2588: 0x00DB,  #  FULL BLOCK
    0x2591: 0x00B0,  #  LIGHT SHADE
    0x2592: 0x00B1,  #  MEDIUM SHADE
    0x2593: 0x00B2,  #  DARK SHADE
    0x25A0: 0x00FE,  #  BLACK SQUARE
}
