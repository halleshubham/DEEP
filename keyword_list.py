#-*- coding: utf-8 -*-


class mar_keyword():
    keyword = \
    {
        # logic

        "व":"and",
        u"आणि":"and",
        "वा":"or",
        "सत्य": "True",
        "असत्य":"False",

        "काहीनाही":"None",

        # def
        "व्याख्या":"def",
        "गट":"class",
        "स्वदर्शक":"self",
        "जागतिक":"global",

        # import
        "संदर्भ":"from",
        "आयात":"import",
        "जसा":"as",

        # flow
        "परतावा":"return",
        "वाढवा":"raise",
        "सुरू":"continue",

        # control
        u"जर":"if",
        u"किंवाजर":"elif",
        u"नाहीतर":"else",

        # for loop
        u"साठी":"for",
        u"आत":"in",
        "आतनाही":"not in",

        # while loop
        u"जोपर्यंत":"while",
        "खंडीत":"break",


        # build in methods
        "अंमल":"exec",
        #u'\u091b\u093e\u092a\u093e':"print",
        u"छापा":"print",
        "सह":"with",
        "उत्पाद":"yield",
        #indent
        u"    ":"    ",
}

class mar_builtin_method():
    '''
    python methods
    '''
    keyword = \
    {
u"माहिती":"raw_input",
u"माहितीक": "int(raw_input",
# build-in types
u"ओळ":"str",
"बुलियन":"bool",
"यादी": "list",
"कोश":"dict",
"संच":"set",
"अक्षर":"chr",
"फ़ाईल":"file",
# number methods
#"पुर्णांक":"int",
u"संख्या": "int",
u".काढा":".strip()",

"जटील":"complex",
"तुलना":"cmp",
# string methods
"नेसुरूहोणारे":"startswith",
"नेसंपणारे":"endswith",
"जोडणी":"join",
"विभाजित":"split",
"बदलणे":"replace",
"एन्कोडिंग":"encoding",
"डिकोडिंग":"decoding",
# list methods
"पुरवणे":"append",
"वाढवणे":"extend",
"समाविष्ट":"insert",
"काढणे":"pop",
"पुढील":"next",
"मिटवणे":"remove",
"उलटवणे":"reverse",
"मोजणे":"count",
"अनुक्रम":"index",
"क्रमित":"sort",
# dict methods
#"":"keys",

# file methods
"उघडा":"open",
"वाचा":"read",
"लिहा":"write",
"ओळवाचा":"readline",
"ओळीवाचा":"readlines",
"बंदकरा":"close",
# OO
# build in functions
"लांबी":"len",
"कमाल":"max",
"किमान":"min",
"मोजणे":"enumerate",
"सोडवा":"eval",
"गाळणे":"filter",

u"मध्ये":"range",

"बेरिज":"sum",
"प्रकार":"type",
"वस्तू":"object",

"मदत":"help",

}

class mar_variable():
    keyword = \
        {
            u"अ":"a",
            u"ब":"b",
            u"क":"c",
            u"ड":"d",
            u"ई":"e",
            u"फ़":"f",
            u"ग":"g",
            u"ह":"h"
        }


class mar_symbols():
    keyword = \
        {
            "<=":"<=",
            ">=":">=",
            "=":"=",
            "==":"==",
            "<":"<",
            ">":">",
            "+":"+",
            "-":"-",
            "/":"/",
            "*":"*",
            "(":"(",
            ")":")",
            ":":":",
            ",":",",
            "[":"[",
            "]":"]",
            "{":"{",
            "}":"}",
            "%":"%"

        }

class mar_sys():
    keyword = \
        {

"आवृत्ती":"version",
"बाहेरपडा":"exit",

"विभाग":"modules",
"व्यासपीठ":"platform",

"सामान्यइनपुट":"stdin",
"सामान्यआउटपुट":"stdout",
# sys path with list methods
"मार्ग":"path",
}

