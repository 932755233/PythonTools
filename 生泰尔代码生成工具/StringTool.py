import re


# 输入'MettePurRequestBillAdapter'
# 输出['Mette', 'Pur', 'Request', 'Bill', 'Adapter']
def extract_words_starting_with_capital(text):
    pattern = r'[A-Z]{1}[a-z]+'
    words = re.findall(pattern, text)
    return words


def format_xml_show_title(text):
    if len(text) == 1:
        return r'&#8195;&#8195;&#8195;%s' % text
    elif len(text) == 2:
        return r'%s&#8195;&#8195;%s' % (text[0], text[1])
    elif len(text) == 3:
        return r'%s&#8194;%s&#8194;%s' % (text[0], text[1], text[2])
    else:
        return text
