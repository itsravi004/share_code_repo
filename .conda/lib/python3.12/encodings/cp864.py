"""Python Character Mapping Codec generated from 'VENDORS/MICSFT/PC/CP864.TXT' with gencodec.py."""  # "

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
        name="cp864",
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
        0x0025: 0x066A,  #  ARABIC PERCENT SIGN
        0x0080: 0x00B0,  #  DEGREE SIGN
        0x0081: 0x00B7,  #  MIDDLE DOT
        0x0082: 0x2219,  #  BULLET OPERATOR
        0x0083: 0x221A,  #  SQUARE ROOT
        0x0084: 0x2592,  #  MEDIUM SHADE
        0x0085: 0x2500,  #  FORMS LIGHT HORIZONTAL
        0x0086: 0x2502,  #  FORMS LIGHT VERTICAL
        0x0087: 0x253C,  #  FORMS LIGHT VERTICAL AND HORIZONTAL
        0x0088: 0x2524,  #  FORMS LIGHT VERTICAL AND LEFT
        0x0089: 0x252C,  #  FORMS LIGHT DOWN AND HORIZONTAL
        0x008A: 0x251C,  #  FORMS LIGHT VERTICAL AND RIGHT
        0x008B: 0x2534,  #  FORMS LIGHT UP AND HORIZONTAL
        0x008C: 0x2510,  #  FORMS LIGHT DOWN AND LEFT
        0x008D: 0x250C,  #  FORMS LIGHT DOWN AND RIGHT
        0x008E: 0x2514,  #  FORMS LIGHT UP AND RIGHT
        0x008F: 0x2518,  #  FORMS LIGHT UP AND LEFT
        0x0090: 0x03B2,  #  GREEK SMALL BETA
        0x0091: 0x221E,  #  INFINITY
        0x0092: 0x03C6,  #  GREEK SMALL PHI
        0x0093: 0x00B1,  #  PLUS-OR-MINUS SIGN
        0x0094: 0x00BD,  #  FRACTION 1/2
        0x0095: 0x00BC,  #  FRACTION 1/4
        0x0096: 0x2248,  #  ALMOST EQUAL TO
        0x0097: 0x00AB,  #  LEFT POINTING GUILLEMET
        0x0098: 0x00BB,  #  RIGHT POINTING GUILLEMET
        0x0099: 0xFEF7,  #  ARABIC LIGATURE LAM WITH ALEF WITH HAMZA ABOVE ISOLATED FORM
        0x009A: 0xFEF8,  #  ARABIC LIGATURE LAM WITH ALEF WITH HAMZA ABOVE FINAL FORM
        0x009B: None,  #  UNDEFINED
        0x009C: None,  #  UNDEFINED
        0x009D: 0xFEFB,  #  ARABIC LIGATURE LAM WITH ALEF ISOLATED FORM
        0x009E: 0xFEFC,  #  ARABIC LIGATURE LAM WITH ALEF FINAL FORM
        0x009F: None,  #  UNDEFINED
        0x00A1: 0x00AD,  #  SOFT HYPHEN
        0x00A2: 0xFE82,  #  ARABIC LETTER ALEF WITH MADDA ABOVE FINAL FORM
        0x00A5: 0xFE84,  #  ARABIC LETTER ALEF WITH HAMZA ABOVE FINAL FORM
        0x00A6: None,  #  UNDEFINED
        0x00A7: None,  #  UNDEFINED
        0x00A8: 0xFE8E,  #  ARABIC LETTER ALEF FINAL FORM
        0x00A9: 0xFE8F,  #  ARABIC LETTER BEH ISOLATED FORM
        0x00AA: 0xFE95,  #  ARABIC LETTER TEH ISOLATED FORM
        0x00AB: 0xFE99,  #  ARABIC LETTER THEH ISOLATED FORM
        0x00AC: 0x060C,  #  ARABIC COMMA
        0x00AD: 0xFE9D,  #  ARABIC LETTER JEEM ISOLATED FORM
        0x00AE: 0xFEA1,  #  ARABIC LETTER HAH ISOLATED FORM
        0x00AF: 0xFEA5,  #  ARABIC LETTER KHAH ISOLATED FORM
        0x00B0: 0x0660,  #  ARABIC-INDIC DIGIT ZERO
        0x00B1: 0x0661,  #  ARABIC-INDIC DIGIT ONE
        0x00B2: 0x0662,  #  ARABIC-INDIC DIGIT TWO
        0x00B3: 0x0663,  #  ARABIC-INDIC DIGIT THREE
        0x00B4: 0x0664,  #  ARABIC-INDIC DIGIT FOUR
        0x00B5: 0x0665,  #  ARABIC-INDIC DIGIT FIVE
        0x00B6: 0x0666,  #  ARABIC-INDIC DIGIT SIX
        0x00B7: 0x0667,  #  ARABIC-INDIC DIGIT SEVEN
        0x00B8: 0x0668,  #  ARABIC-INDIC DIGIT EIGHT
        0x00B9: 0x0669,  #  ARABIC-INDIC DIGIT NINE
        0x00BA: 0xFED1,  #  ARABIC LETTER FEH ISOLATED FORM
        0x00BB: 0x061B,  #  ARABIC SEMICOLON
        0x00BC: 0xFEB1,  #  ARABIC LETTER SEEN ISOLATED FORM
        0x00BD: 0xFEB5,  #  ARABIC LETTER SHEEN ISOLATED FORM
        0x00BE: 0xFEB9,  #  ARABIC LETTER SAD ISOLATED FORM
        0x00BF: 0x061F,  #  ARABIC QUESTION MARK
        0x00C0: 0x00A2,  #  CENT SIGN
        0x00C1: 0xFE80,  #  ARABIC LETTER HAMZA ISOLATED FORM
        0x00C2: 0xFE81,  #  ARABIC LETTER ALEF WITH MADDA ABOVE ISOLATED FORM
        0x00C3: 0xFE83,  #  ARABIC LETTER ALEF WITH HAMZA ABOVE ISOLATED FORM
        0x00C4: 0xFE85,  #  ARABIC LETTER WAW WITH HAMZA ABOVE ISOLATED FORM
        0x00C5: 0xFECA,  #  ARABIC LETTER AIN FINAL FORM
        0x00C6: 0xFE8B,  #  ARABIC LETTER YEH WITH HAMZA ABOVE INITIAL FORM
        0x00C7: 0xFE8D,  #  ARABIC LETTER ALEF ISOLATED FORM
        0x00C8: 0xFE91,  #  ARABIC LETTER BEH INITIAL FORM
        0x00C9: 0xFE93,  #  ARABIC LETTER TEH MARBUTA ISOLATED FORM
        0x00CA: 0xFE97,  #  ARABIC LETTER TEH INITIAL FORM
        0x00CB: 0xFE9B,  #  ARABIC LETTER THEH INITIAL FORM
        0x00CC: 0xFE9F,  #  ARABIC LETTER JEEM INITIAL FORM
        0x00CD: 0xFEA3,  #  ARABIC LETTER HAH INITIAL FORM
        0x00CE: 0xFEA7,  #  ARABIC LETTER KHAH INITIAL FORM
        0x00CF: 0xFEA9,  #  ARABIC LETTER DAL ISOLATED FORM
        0x00D0: 0xFEAB,  #  ARABIC LETTER THAL ISOLATED FORM
        0x00D1: 0xFEAD,  #  ARABIC LETTER REH ISOLATED FORM
        0x00D2: 0xFEAF,  #  ARABIC LETTER ZAIN ISOLATED FORM
        0x00D3: 0xFEB3,  #  ARABIC LETTER SEEN INITIAL FORM
        0x00D4: 0xFEB7,  #  ARABIC LETTER SHEEN INITIAL FORM
        0x00D5: 0xFEBB,  #  ARABIC LETTER SAD INITIAL FORM
        0x00D6: 0xFEBF,  #  ARABIC LETTER DAD INITIAL FORM
        0x00D7: 0xFEC1,  #  ARABIC LETTER TAH ISOLATED FORM
        0x00D8: 0xFEC5,  #  ARABIC LETTER ZAH ISOLATED FORM
        0x00D9: 0xFECB,  #  ARABIC LETTER AIN INITIAL FORM
        0x00DA: 0xFECF,  #  ARABIC LETTER GHAIN INITIAL FORM
        0x00DB: 0x00A6,  #  BROKEN VERTICAL BAR
        0x00DC: 0x00AC,  #  NOT SIGN
        0x00DD: 0x00F7,  #  DIVISION SIGN
        0x00DE: 0x00D7,  #  MULTIPLICATION SIGN
        0x00DF: 0xFEC9,  #  ARABIC LETTER AIN ISOLATED FORM
        0x00E0: 0x0640,  #  ARABIC TATWEEL
        0x00E1: 0xFED3,  #  ARABIC LETTER FEH INITIAL FORM
        0x00E2: 0xFED7,  #  ARABIC LETTER QAF INITIAL FORM
        0x00E3: 0xFEDB,  #  ARABIC LETTER KAF INITIAL FORM
        0x00E4: 0xFEDF,  #  ARABIC LETTER LAM INITIAL FORM
        0x00E5: 0xFEE3,  #  ARABIC LETTER MEEM INITIAL FORM
        0x00E6: 0xFEE7,  #  ARABIC LETTER NOON INITIAL FORM
        0x00E7: 0xFEEB,  #  ARABIC LETTER HEH INITIAL FORM
        0x00E8: 0xFEED,  #  ARABIC LETTER WAW ISOLATED FORM
        0x00E9: 0xFEEF,  #  ARABIC LETTER ALEF MAKSURA ISOLATED FORM
        0x00EA: 0xFEF3,  #  ARABIC LETTER YEH INITIAL FORM
        0x00EB: 0xFEBD,  #  ARABIC LETTER DAD ISOLATED FORM
        0x00EC: 0xFECC,  #  ARABIC LETTER AIN MEDIAL FORM
        0x00ED: 0xFECE,  #  ARABIC LETTER GHAIN FINAL FORM
        0x00EE: 0xFECD,  #  ARABIC LETTER GHAIN ISOLATED FORM
        0x00EF: 0xFEE1,  #  ARABIC LETTER MEEM ISOLATED FORM
        0x00F0: 0xFE7D,  #  ARABIC SHADDA MEDIAL FORM
        0x00F1: 0x0651,  #  ARABIC SHADDAH
        0x00F2: 0xFEE5,  #  ARABIC LETTER NOON ISOLATED FORM
        0x00F3: 0xFEE9,  #  ARABIC LETTER HEH ISOLATED FORM
        0x00F4: 0xFEEC,  #  ARABIC LETTER HEH MEDIAL FORM
        0x00F5: 0xFEF0,  #  ARABIC LETTER ALEF MAKSURA FINAL FORM
        0x00F6: 0xFEF2,  #  ARABIC LETTER YEH FINAL FORM
        0x00F7: 0xFED0,  #  ARABIC LETTER GHAIN MEDIAL FORM
        0x00F8: 0xFED5,  #  ARABIC LETTER QAF ISOLATED FORM
        0x00F9: 0xFEF5,  #  ARABIC LIGATURE LAM WITH ALEF WITH MADDA ABOVE ISOLATED FORM
        0x00FA: 0xFEF6,  #  ARABIC LIGATURE LAM WITH ALEF WITH MADDA ABOVE FINAL FORM
        0x00FB: 0xFEDD,  #  ARABIC LETTER LAM ISOLATED FORM
        0x00FC: 0xFED9,  #  ARABIC LETTER KAF ISOLATED FORM
        0x00FD: 0xFEF1,  #  ARABIC LETTER YEH ISOLATED FORM
        0x00FE: 0x25A0,  #  BLACK SQUARE
        0x00FF: None,  #  UNDEFINED
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
    "\u066a"  #  0x0025 -> ARABIC PERCENT SIGN
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
    "\xb0"  #  0x0080 -> DEGREE SIGN
    "\xb7"  #  0x0081 -> MIDDLE DOT
    "\u2219"  #  0x0082 -> BULLET OPERATOR
    "\u221a"  #  0x0083 -> SQUARE ROOT
    "\u2592"  #  0x0084 -> MEDIUM SHADE
    "\u2500"  #  0x0085 -> FORMS LIGHT HORIZONTAL
    "\u2502"  #  0x0086 -> FORMS LIGHT VERTICAL
    "\u253c"  #  0x0087 -> FORMS LIGHT VERTICAL AND HORIZONTAL
    "\u2524"  #  0x0088 -> FORMS LIGHT VERTICAL AND LEFT
    "\u252c"  #  0x0089 -> FORMS LIGHT DOWN AND HORIZONTAL
    "\u251c"  #  0x008a -> FORMS LIGHT VERTICAL AND RIGHT
    "\u2534"  #  0x008b -> FORMS LIGHT UP AND HORIZONTAL
    "\u2510"  #  0x008c -> FORMS LIGHT DOWN AND LEFT
    "\u250c"  #  0x008d -> FORMS LIGHT DOWN AND RIGHT
    "\u2514"  #  0x008e -> FORMS LIGHT UP AND RIGHT
    "\u2518"  #  0x008f -> FORMS LIGHT UP AND LEFT
    "\u03b2"  #  0x0090 -> GREEK SMALL BETA
    "\u221e"  #  0x0091 -> INFINITY
    "\u03c6"  #  0x0092 -> GREEK SMALL PHI
    "\xb1"  #  0x0093 -> PLUS-OR-MINUS SIGN
    "\xbd"  #  0x0094 -> FRACTION 1/2
    "\xbc"  #  0x0095 -> FRACTION 1/4
    "\u2248"  #  0x0096 -> ALMOST EQUAL TO
    "\xab"  #  0x0097 -> LEFT POINTING GUILLEMET
    "\xbb"  #  0x0098 -> RIGHT POINTING GUILLEMET
    "\ufef7"  #  0x0099 -> ARABIC LIGATURE LAM WITH ALEF WITH HAMZA ABOVE ISOLATED FORM
    "\ufef8"  #  0x009a -> ARABIC LIGATURE LAM WITH ALEF WITH HAMZA ABOVE FINAL FORM
    "\ufffe"  #  0x009b -> UNDEFINED
    "\ufffe"  #  0x009c -> UNDEFINED
    "\ufefb"  #  0x009d -> ARABIC LIGATURE LAM WITH ALEF ISOLATED FORM
    "\ufefc"  #  0x009e -> ARABIC LIGATURE LAM WITH ALEF FINAL FORM
    "\ufffe"  #  0x009f -> UNDEFINED
    "\xa0"  #  0x00a0 -> NON-BREAKING SPACE
    "\xad"  #  0x00a1 -> SOFT HYPHEN
    "\ufe82"  #  0x00a2 -> ARABIC LETTER ALEF WITH MADDA ABOVE FINAL FORM
    "\xa3"  #  0x00a3 -> POUND SIGN
    "\xa4"  #  0x00a4 -> CURRENCY SIGN
    "\ufe84"  #  0x00a5 -> ARABIC LETTER ALEF WITH HAMZA ABOVE FINAL FORM
    "\ufffe"  #  0x00a6 -> UNDEFINED
    "\ufffe"  #  0x00a7 -> UNDEFINED
    "\ufe8e"  #  0x00a8 -> ARABIC LETTER ALEF FINAL FORM
    "\ufe8f"  #  0x00a9 -> ARABIC LETTER BEH ISOLATED FORM
    "\ufe95"  #  0x00aa -> ARABIC LETTER TEH ISOLATED FORM
    "\ufe99"  #  0x00ab -> ARABIC LETTER THEH ISOLATED FORM
    "\u060c"  #  0x00ac -> ARABIC COMMA
    "\ufe9d"  #  0x00ad -> ARABIC LETTER JEEM ISOLATED FORM
    "\ufea1"  #  0x00ae -> ARABIC LETTER HAH ISOLATED FORM
    "\ufea5"  #  0x00af -> ARABIC LETTER KHAH ISOLATED FORM
    "\u0660"  #  0x00b0 -> ARABIC-INDIC DIGIT ZERO
    "\u0661"  #  0x00b1 -> ARABIC-INDIC DIGIT ONE
    "\u0662"  #  0x00b2 -> ARABIC-INDIC DIGIT TWO
    "\u0663"  #  0x00b3 -> ARABIC-INDIC DIGIT THREE
    "\u0664"  #  0x00b4 -> ARABIC-INDIC DIGIT FOUR
    "\u0665"  #  0x00b5 -> ARABIC-INDIC DIGIT FIVE
    "\u0666"  #  0x00b6 -> ARABIC-INDIC DIGIT SIX
    "\u0667"  #  0x00b7 -> ARABIC-INDIC DIGIT SEVEN
    "\u0668"  #  0x00b8 -> ARABIC-INDIC DIGIT EIGHT
    "\u0669"  #  0x00b9 -> ARABIC-INDIC DIGIT NINE
    "\ufed1"  #  0x00ba -> ARABIC LETTER FEH ISOLATED FORM
    "\u061b"  #  0x00bb -> ARABIC SEMICOLON
    "\ufeb1"  #  0x00bc -> ARABIC LETTER SEEN ISOLATED FORM
    "\ufeb5"  #  0x00bd -> ARABIC LETTER SHEEN ISOLATED FORM
    "\ufeb9"  #  0x00be -> ARABIC LETTER SAD ISOLATED FORM
    "\u061f"  #  0x00bf -> ARABIC QUESTION MARK
    "\xa2"  #  0x00c0 -> CENT SIGN
    "\ufe80"  #  0x00c1 -> ARABIC LETTER HAMZA ISOLATED FORM
    "\ufe81"  #  0x00c2 -> ARABIC LETTER ALEF WITH MADDA ABOVE ISOLATED FORM
    "\ufe83"  #  0x00c3 -> ARABIC LETTER ALEF WITH HAMZA ABOVE ISOLATED FORM
    "\ufe85"  #  0x00c4 -> ARABIC LETTER WAW WITH HAMZA ABOVE ISOLATED FORM
    "\ufeca"  #  0x00c5 -> ARABIC LETTER AIN FINAL FORM
    "\ufe8b"  #  0x00c6 -> ARABIC LETTER YEH WITH HAMZA ABOVE INITIAL FORM
    "\ufe8d"  #  0x00c7 -> ARABIC LETTER ALEF ISOLATED FORM
    "\ufe91"  #  0x00c8 -> ARABIC LETTER BEH INITIAL FORM
    "\ufe93"  #  0x00c9 -> ARABIC LETTER TEH MARBUTA ISOLATED FORM
    "\ufe97"  #  0x00ca -> ARABIC LETTER TEH INITIAL FORM
    "\ufe9b"  #  0x00cb -> ARABIC LETTER THEH INITIAL FORM
    "\ufe9f"  #  0x00cc -> ARABIC LETTER JEEM INITIAL FORM
    "\ufea3"  #  0x00cd -> ARABIC LETTER HAH INITIAL FORM
    "\ufea7"  #  0x00ce -> ARABIC LETTER KHAH INITIAL FORM
    "\ufea9"  #  0x00cf -> ARABIC LETTER DAL ISOLATED FORM
    "\ufeab"  #  0x00d0 -> ARABIC LETTER THAL ISOLATED FORM
    "\ufead"  #  0x00d1 -> ARABIC LETTER REH ISOLATED FORM
    "\ufeaf"  #  0x00d2 -> ARABIC LETTER ZAIN ISOLATED FORM
    "\ufeb3"  #  0x00d3 -> ARABIC LETTER SEEN INITIAL FORM
    "\ufeb7"  #  0x00d4 -> ARABIC LETTER SHEEN INITIAL FORM
    "\ufebb"  #  0x00d5 -> ARABIC LETTER SAD INITIAL FORM
    "\ufebf"  #  0x00d6 -> ARABIC LETTER DAD INITIAL FORM
    "\ufec1"  #  0x00d7 -> ARABIC LETTER TAH ISOLATED FORM
    "\ufec5"  #  0x00d8 -> ARABIC LETTER ZAH ISOLATED FORM
    "\ufecb"  #  0x00d9 -> ARABIC LETTER AIN INITIAL FORM
    "\ufecf"  #  0x00da -> ARABIC LETTER GHAIN INITIAL FORM
    "\xa6"  #  0x00db -> BROKEN VERTICAL BAR
    "\xac"  #  0x00dc -> NOT SIGN
    "\xf7"  #  0x00dd -> DIVISION SIGN
    "\xd7"  #  0x00de -> MULTIPLICATION SIGN
    "\ufec9"  #  0x00df -> ARABIC LETTER AIN ISOLATED FORM
    "\u0640"  #  0x00e0 -> ARABIC TATWEEL
    "\ufed3"  #  0x00e1 -> ARABIC LETTER FEH INITIAL FORM
    "\ufed7"  #  0x00e2 -> ARABIC LETTER QAF INITIAL FORM
    "\ufedb"  #  0x00e3 -> ARABIC LETTER KAF INITIAL FORM
    "\ufedf"  #  0x00e4 -> ARABIC LETTER LAM INITIAL FORM
    "\ufee3"  #  0x00e5 -> ARABIC LETTER MEEM INITIAL FORM
    "\ufee7"  #  0x00e6 -> ARABIC LETTER NOON INITIAL FORM
    "\ufeeb"  #  0x00e7 -> ARABIC LETTER HEH INITIAL FORM
    "\ufeed"  #  0x00e8 -> ARABIC LETTER WAW ISOLATED FORM
    "\ufeef"  #  0x00e9 -> ARABIC LETTER ALEF MAKSURA ISOLATED FORM
    "\ufef3"  #  0x00ea -> ARABIC LETTER YEH INITIAL FORM
    "\ufebd"  #  0x00eb -> ARABIC LETTER DAD ISOLATED FORM
    "\ufecc"  #  0x00ec -> ARABIC LETTER AIN MEDIAL FORM
    "\ufece"  #  0x00ed -> ARABIC LETTER GHAIN FINAL FORM
    "\ufecd"  #  0x00ee -> ARABIC LETTER GHAIN ISOLATED FORM
    "\ufee1"  #  0x00ef -> ARABIC LETTER MEEM ISOLATED FORM
    "\ufe7d"  #  0x00f0 -> ARABIC SHADDA MEDIAL FORM
    "\u0651"  #  0x00f1 -> ARABIC SHADDAH
    "\ufee5"  #  0x00f2 -> ARABIC LETTER NOON ISOLATED FORM
    "\ufee9"  #  0x00f3 -> ARABIC LETTER HEH ISOLATED FORM
    "\ufeec"  #  0x00f4 -> ARABIC LETTER HEH MEDIAL FORM
    "\ufef0"  #  0x00f5 -> ARABIC LETTER ALEF MAKSURA FINAL FORM
    "\ufef2"  #  0x00f6 -> ARABIC LETTER YEH FINAL FORM
    "\ufed0"  #  0x00f7 -> ARABIC LETTER GHAIN MEDIAL FORM
    "\ufed5"  #  0x00f8 -> ARABIC LETTER QAF ISOLATED FORM
    "\ufef5"  #  0x00f9 -> ARABIC LIGATURE LAM WITH ALEF WITH MADDA ABOVE ISOLATED FORM
    "\ufef6"  #  0x00fa -> ARABIC LIGATURE LAM WITH ALEF WITH MADDA ABOVE FINAL FORM
    "\ufedd"  #  0x00fb -> ARABIC LETTER LAM ISOLATED FORM
    "\ufed9"  #  0x00fc -> ARABIC LETTER KAF ISOLATED FORM
    "\ufef1"  #  0x00fd -> ARABIC LETTER YEH ISOLATED FORM
    "\u25a0"  #  0x00fe -> BLACK SQUARE
    "\ufffe"  #  0x00ff -> UNDEFINED
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
    0x00A0: 0x00A0,  #  NON-BREAKING SPACE
    0x00A2: 0x00C0,  #  CENT SIGN
    0x00A3: 0x00A3,  #  POUND SIGN
    0x00A4: 0x00A4,  #  CURRENCY SIGN
    0x00A6: 0x00DB,  #  BROKEN VERTICAL BAR
    0x00AB: 0x0097,  #  LEFT POINTING GUILLEMET
    0x00AC: 0x00DC,  #  NOT SIGN
    0x00AD: 0x00A1,  #  SOFT HYPHEN
    0x00B0: 0x0080,  #  DEGREE SIGN
    0x00B1: 0x0093,  #  PLUS-OR-MINUS SIGN
    0x00B7: 0x0081,  #  MIDDLE DOT
    0x00BB: 0x0098,  #  RIGHT POINTING GUILLEMET
    0x00BC: 0x0095,  #  FRACTION 1/4
    0x00BD: 0x0094,  #  FRACTION 1/2
    0x00D7: 0x00DE,  #  MULTIPLICATION SIGN
    0x00F7: 0x00DD,  #  DIVISION SIGN
    0x03B2: 0x0090,  #  GREEK SMALL BETA
    0x03C6: 0x0092,  #  GREEK SMALL PHI
    0x060C: 0x00AC,  #  ARABIC COMMA
    0x061B: 0x00BB,  #  ARABIC SEMICOLON
    0x061F: 0x00BF,  #  ARABIC QUESTION MARK
    0x0640: 0x00E0,  #  ARABIC TATWEEL
    0x0651: 0x00F1,  #  ARABIC SHADDAH
    0x0660: 0x00B0,  #  ARABIC-INDIC DIGIT ZERO
    0x0661: 0x00B1,  #  ARABIC-INDIC DIGIT ONE
    0x0662: 0x00B2,  #  ARABIC-INDIC DIGIT TWO
    0x0663: 0x00B3,  #  ARABIC-INDIC DIGIT THREE
    0x0664: 0x00B4,  #  ARABIC-INDIC DIGIT FOUR
    0x0665: 0x00B5,  #  ARABIC-INDIC DIGIT FIVE
    0x0666: 0x00B6,  #  ARABIC-INDIC DIGIT SIX
    0x0667: 0x00B7,  #  ARABIC-INDIC DIGIT SEVEN
    0x0668: 0x00B8,  #  ARABIC-INDIC DIGIT EIGHT
    0x0669: 0x00B9,  #  ARABIC-INDIC DIGIT NINE
    0x066A: 0x0025,  #  ARABIC PERCENT SIGN
    0x2219: 0x0082,  #  BULLET OPERATOR
    0x221A: 0x0083,  #  SQUARE ROOT
    0x221E: 0x0091,  #  INFINITY
    0x2248: 0x0096,  #  ALMOST EQUAL TO
    0x2500: 0x0085,  #  FORMS LIGHT HORIZONTAL
    0x2502: 0x0086,  #  FORMS LIGHT VERTICAL
    0x250C: 0x008D,  #  FORMS LIGHT DOWN AND RIGHT
    0x2510: 0x008C,  #  FORMS LIGHT DOWN AND LEFT
    0x2514: 0x008E,  #  FORMS LIGHT UP AND RIGHT
    0x2518: 0x008F,  #  FORMS LIGHT UP AND LEFT
    0x251C: 0x008A,  #  FORMS LIGHT VERTICAL AND RIGHT
    0x2524: 0x0088,  #  FORMS LIGHT VERTICAL AND LEFT
    0x252C: 0x0089,  #  FORMS LIGHT DOWN AND HORIZONTAL
    0x2534: 0x008B,  #  FORMS LIGHT UP AND HORIZONTAL
    0x253C: 0x0087,  #  FORMS LIGHT VERTICAL AND HORIZONTAL
    0x2592: 0x0084,  #  MEDIUM SHADE
    0x25A0: 0x00FE,  #  BLACK SQUARE
    0xFE7D: 0x00F0,  #  ARABIC SHADDA MEDIAL FORM
    0xFE80: 0x00C1,  #  ARABIC LETTER HAMZA ISOLATED FORM
    0xFE81: 0x00C2,  #  ARABIC LETTER ALEF WITH MADDA ABOVE ISOLATED FORM
    0xFE82: 0x00A2,  #  ARABIC LETTER ALEF WITH MADDA ABOVE FINAL FORM
    0xFE83: 0x00C3,  #  ARABIC LETTER ALEF WITH HAMZA ABOVE ISOLATED FORM
    0xFE84: 0x00A5,  #  ARABIC LETTER ALEF WITH HAMZA ABOVE FINAL FORM
    0xFE85: 0x00C4,  #  ARABIC LETTER WAW WITH HAMZA ABOVE ISOLATED FORM
    0xFE8B: 0x00C6,  #  ARABIC LETTER YEH WITH HAMZA ABOVE INITIAL FORM
    0xFE8D: 0x00C7,  #  ARABIC LETTER ALEF ISOLATED FORM
    0xFE8E: 0x00A8,  #  ARABIC LETTER ALEF FINAL FORM
    0xFE8F: 0x00A9,  #  ARABIC LETTER BEH ISOLATED FORM
    0xFE91: 0x00C8,  #  ARABIC LETTER BEH INITIAL FORM
    0xFE93: 0x00C9,  #  ARABIC LETTER TEH MARBUTA ISOLATED FORM
    0xFE95: 0x00AA,  #  ARABIC LETTER TEH ISOLATED FORM
    0xFE97: 0x00CA,  #  ARABIC LETTER TEH INITIAL FORM
    0xFE99: 0x00AB,  #  ARABIC LETTER THEH ISOLATED FORM
    0xFE9B: 0x00CB,  #  ARABIC LETTER THEH INITIAL FORM
    0xFE9D: 0x00AD,  #  ARABIC LETTER JEEM ISOLATED FORM
    0xFE9F: 0x00CC,  #  ARABIC LETTER JEEM INITIAL FORM
    0xFEA1: 0x00AE,  #  ARABIC LETTER HAH ISOLATED FORM
    0xFEA3: 0x00CD,  #  ARABIC LETTER HAH INITIAL FORM
    0xFEA5: 0x00AF,  #  ARABIC LETTER KHAH ISOLATED FORM
    0xFEA7: 0x00CE,  #  ARABIC LETTER KHAH INITIAL FORM
    0xFEA9: 0x00CF,  #  ARABIC LETTER DAL ISOLATED FORM
    0xFEAB: 0x00D0,  #  ARABIC LETTER THAL ISOLATED FORM
    0xFEAD: 0x00D1,  #  ARABIC LETTER REH ISOLATED FORM
    0xFEAF: 0x00D2,  #  ARABIC LETTER ZAIN ISOLATED FORM
    0xFEB1: 0x00BC,  #  ARABIC LETTER SEEN ISOLATED FORM
    0xFEB3: 0x00D3,  #  ARABIC LETTER SEEN INITIAL FORM
    0xFEB5: 0x00BD,  #  ARABIC LETTER SHEEN ISOLATED FORM
    0xFEB7: 0x00D4,  #  ARABIC LETTER SHEEN INITIAL FORM
    0xFEB9: 0x00BE,  #  ARABIC LETTER SAD ISOLATED FORM
    0xFEBB: 0x00D5,  #  ARABIC LETTER SAD INITIAL FORM
    0xFEBD: 0x00EB,  #  ARABIC LETTER DAD ISOLATED FORM
    0xFEBF: 0x00D6,  #  ARABIC LETTER DAD INITIAL FORM
    0xFEC1: 0x00D7,  #  ARABIC LETTER TAH ISOLATED FORM
    0xFEC5: 0x00D8,  #  ARABIC LETTER ZAH ISOLATED FORM
    0xFEC9: 0x00DF,  #  ARABIC LETTER AIN ISOLATED FORM
    0xFECA: 0x00C5,  #  ARABIC LETTER AIN FINAL FORM
    0xFECB: 0x00D9,  #  ARABIC LETTER AIN INITIAL FORM
    0xFECC: 0x00EC,  #  ARABIC LETTER AIN MEDIAL FORM
    0xFECD: 0x00EE,  #  ARABIC LETTER GHAIN ISOLATED FORM
    0xFECE: 0x00ED,  #  ARABIC LETTER GHAIN FINAL FORM
    0xFECF: 0x00DA,  #  ARABIC LETTER GHAIN INITIAL FORM
    0xFED0: 0x00F7,  #  ARABIC LETTER GHAIN MEDIAL FORM
    0xFED1: 0x00BA,  #  ARABIC LETTER FEH ISOLATED FORM
    0xFED3: 0x00E1,  #  ARABIC LETTER FEH INITIAL FORM
    0xFED5: 0x00F8,  #  ARABIC LETTER QAF ISOLATED FORM
    0xFED7: 0x00E2,  #  ARABIC LETTER QAF INITIAL FORM
    0xFED9: 0x00FC,  #  ARABIC LETTER KAF ISOLATED FORM
    0xFEDB: 0x00E3,  #  ARABIC LETTER KAF INITIAL FORM
    0xFEDD: 0x00FB,  #  ARABIC LETTER LAM ISOLATED FORM
    0xFEDF: 0x00E4,  #  ARABIC LETTER LAM INITIAL FORM
    0xFEE1: 0x00EF,  #  ARABIC LETTER MEEM ISOLATED FORM
    0xFEE3: 0x00E5,  #  ARABIC LETTER MEEM INITIAL FORM
    0xFEE5: 0x00F2,  #  ARABIC LETTER NOON ISOLATED FORM
    0xFEE7: 0x00E6,  #  ARABIC LETTER NOON INITIAL FORM
    0xFEE9: 0x00F3,  #  ARABIC LETTER HEH ISOLATED FORM
    0xFEEB: 0x00E7,  #  ARABIC LETTER HEH INITIAL FORM
    0xFEEC: 0x00F4,  #  ARABIC LETTER HEH MEDIAL FORM
    0xFEED: 0x00E8,  #  ARABIC LETTER WAW ISOLATED FORM
    0xFEEF: 0x00E9,  #  ARABIC LETTER ALEF MAKSURA ISOLATED FORM
    0xFEF0: 0x00F5,  #  ARABIC LETTER ALEF MAKSURA FINAL FORM
    0xFEF1: 0x00FD,  #  ARABIC LETTER YEH ISOLATED FORM
    0xFEF2: 0x00F6,  #  ARABIC LETTER YEH FINAL FORM
    0xFEF3: 0x00EA,  #  ARABIC LETTER YEH INITIAL FORM
    0xFEF5: 0x00F9,  #  ARABIC LIGATURE LAM WITH ALEF WITH MADDA ABOVE ISOLATED FORM
    0xFEF6: 0x00FA,  #  ARABIC LIGATURE LAM WITH ALEF WITH MADDA ABOVE FINAL FORM
    0xFEF7: 0x0099,  #  ARABIC LIGATURE LAM WITH ALEF WITH HAMZA ABOVE ISOLATED FORM
    0xFEF8: 0x009A,  #  ARABIC LIGATURE LAM WITH ALEF WITH HAMZA ABOVE FINAL FORM
    0xFEFB: 0x009D,  #  ARABIC LIGATURE LAM WITH ALEF ISOLATED FORM
    0xFEFC: 0x009E,  #  ARABIC LIGATURE LAM WITH ALEF FINAL FORM
}
