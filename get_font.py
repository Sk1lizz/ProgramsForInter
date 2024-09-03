DEFAULT_FONT = "slant"

FONT_LIST = ["slant", "graffiti", "poison", "weird", "wavy", "univers", "type_set", 
                 "tombstone", "stop", "threepoint", "smkeyboard", "isometric1", "shimrod", 
                 "serifcap", "xcour", "linux", "gothic", "fuzzy", "fender", "epic", "dotmatrix", 
                 "caligraphy", "avatar", "broadway"]

def get_font(font):
    
    for i in FONT_LIST:
        if font == i:
            return font
    
    return DEFAULT_FONT