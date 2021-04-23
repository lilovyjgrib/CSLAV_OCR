def shit2utf8(text):
    decoding_map = {i:i for i in 'ЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮйцукенгшщзхъэждлорпавыфячсмитьбю.!";: -/\n\t'}
    # those are similar characters in both encodings
    decoding_map.update(
        {
            '#': '\u0486',
            '$': '\u0486' + '\u0301',
            '%': '\u0486' + '\u0300',
            '&': '\u0483',
            '*': '\uA673',
            '+': '\u2DE1' + '\u0487',  # combining VE
            '0': '\u043E' + '\u0301',
            '1': '\u0301',
            '2': '\u0300',
            '3': '\u0486',
            '4': '\u0486' + '\u0301',
            '5': '\u0486' + '\u0300',
            '6': '\u0311',  # combining inverted breve
            '7': '\u0483',  # titlo
            '8': '\u033E',  # combining vertical tilde
            '9': '\u0436' + '\u0483',  # zhe with titlo above
            '<': '\u2DEF',  # combining HA
            '=': '\u2DE9' + '\u0487',  # combining EN
            '>': '\u2DEC' + '\u0487',  # combining ER
            '?': '\u2DF1' + '\u0487',  # combining CHE
            '@': '\u0300',
            'A': '\u0430' + '\u0300',  # latin A maps to AZ with grave accent
            'B': '\u0463' + '\u0311',  # latin B maps to Yat' with inverted breve
            'C': '\u2DED' + '\u0487',  # combining ES
            'D': '\u0434' + '\u2DED' + '\u0487',
            'E': '\u0435' + '\u0300',  # latin E maps to e with grave accent
            'F': '\u0472',  # F maps to THETA
            'G': '\u0433' + '\u0483',  # G maps to ge with TITLO
            'H': '\u0461' + '\u0301',  # latin H maps to omega with acute accent
            'I': '\u0406',
            'J': '\u0456' + '\u0300',
            'K': '\uA656' + '\u0486',  # YA with psili
            'L': '\u043B' + '\u2DE3',  # el with cobining de
            'M': '\u0476',  # capital IZHITSA with kendema
            'N': '\u047A' + '\u0486',  # capital WIDE ON with psili
            'O': '\u047A',  # just capital WIDE ON
            'P': '\u0470',  # capital PSI
            'Q': '\u047C',  # capital omega with great apostrophe
            'R': '\u0440' + '\u0483',  # lowercase re with titlo
            'S': '\u0467' + '\u0300',  # lowercase small yus with grave
            'T': '\u047E',  # capital OT
            'U': '\u041E' + '\u0443',  # diagraph capital UK
            'V': '\u0474',  # capital IZHITSA
            'W': '\u0460',  # capital OMEGA
            'X': '\u046E',  # capital XI
            'Y': '\uA64B' + '\u0300',  # monograph uk with grave
            'Z': '\u0466',  # capital SMALL YUS
            '\\': '\u0483',  # yet another titlo
            '^': '\u0311',  # combining inverted breve
            '_': '\u033E',  # yet another yerik
            'a': '\u0430' + '\u0301',  # latin A maps to AZ with acute accent
            'b': '\u2DEA' + '\u0487',  # combining ON
            'c': '\u2DED' + '\u0487',  # combining ES
            'd': '\u2DE3',  # combining DE
            'e': '\u0435' + '\u0301',  # latin E maps to e with acute accent
            'f': '\u0473',  # lowercase theta
            'g': '\u2DE2' + '\u0487',  # combining ge
            'h': '\u044B' + '\u0301',  # ery with acute accent
            'i': '\u0456',
            'j': '\u0456' + '\u0301',  # i with acute accent
            'k': '\uA657' + '\u0486',  # iotaed a with psili
            'l': '\u043B' + '\u0483',  # el with titlo
            'm': '\u0477',  # izhitsa with izhe titlo
            'n': '\u047B' + '\u0486',  # wide on with psili
            'o': '\u047B',  # wide on
            'p': '\u0471',  # lowercase psi
            'q': '\u047D',  # lowercase omega with great apostrophe
            'r': '\u0440' + '\u2DED' + '\u0487',  # lowercase er with combining es
            's': '\u0467' + '\u0301',  # lowercase small yus with acute accent
            't': '\u047F',  # lowercase ot
            'u': '\u1C82' + '\u0443',  # diagraph uk
            'v': '\u0475',  # lowercase izhitsa
            'w': '\u0461',  # lowercase omega
            'x': '\u046F',  # lowercase xi
            'y': '\uA64B' + '\u0301',  # monograph uk with acute accent
            'z': '\u0467',  # lowercase small yus
            '{': '\uA64B' + '\u0311',  # monograph uk with inverted breve
            '|': '\u0467' + '\u0486' + '\u0300',  # lowercase small yus with apostroph
            '}': '\u0438' + '\u0483',  # the numeral eight
            '~': '\u0301',  # yet another acute accent
            ### SECOND HALF IS THE CYRILLIC BLOCK
            '.': '·',  # жирная точка по центру
            'Ђ': '\u0475' + '\u0301',  # lowercase izhitsa with acute
            'Ѓ': '\u0410' + '\u0486' + '\u0301',  # uppercase A with psili and acute
            '‚': '\u201A',
            'ѓ': '\u0430' + '\u0486' + '\u0301',  # lowercase A with psili and acute
            '„': '\u201E',
            '…': '\u046F' + '\u0483',  # the numberal sixty
            '†': '\u0430' + '\u0311',  # lowercase a with inverted breve
            '‡': '\u0456' + '\u0311',  # lowercase i with inverted breve
            '€': '\u2DE5',  # combining ze
            '‰': '\u0467' + '\u0311',  # lowercase small yus with inverted breve
            'Љ': '\u0466' + '\u0486',  # upercase small yus with psili
            '‹': '\u0456' + '\u0483',  # the numeral ten
            'Њ': '\u0460' + '\u0486',  # capital OMEGA with psili
            'Ќ': '\u041E' + '\u0443' + '\u0486' + '\u0301',  # diagraph uk with apostroph
            'Ћ': '\uA656' + '\u0486' + '\u0301',  # uppercase Iotated A with apostroph
            'Џ': '\u047A' + '\u0486' + '\u0301',  # uppercase Round O with apostroph
            'ђ': '\u0475' + '\u2DE2' + '\u0487',  # lowercase izhitsa with combining ge
            '‘': '\u2018',
            '’': '\u2019',
            '“': '\u201C',
            '”': '\u201D',
            '•': '\u2DE4',  # combining zhe
            '–': '\u2013',
            '—': '\u2014',
            '™': '\u0442' + '\u0483',
            'љ': '\u0467' + '\u0486',  # lowercase small yus with psili
            '›': '\u0475' + '\u0311',  # izhitsa with inverted breve
            'њ': '\u0461' + '\u0486',  # lowercase omega with psili
            'ќ': '\u1C82' + '\u0443' + '\u0486' + '\u0301',  # digraph uk with apostrophe
            'ћ': '\uA657' + '\u0486' + '\u0301',  # lowercase iotated a with apostrophe
            'џ': '\u047B' + '\u0486' + '\u0301',  # lowercase Round O with apostrophe
            'Ў': '\u041E' + '\u0443' + '\u0486',  # Capital Digraph Uk with psili
            'ў': '\u1C82' + '\u0443' + '\u0486',  # lowercase of the above
            'Ј': '\u0406' + '\u0486' + '\u0301',  # Uppercase I with apostrophe
            '¤': '\u0482',  # cyrillic thousands sign
            'Ґ': '\u0410' + '\u0486',  # capital A with psili
            '¦': '\u0445' + '\u0483',  # lowercase kha with titlo
            '§': '\u0447' + '\u0483',  # the numeral ninety
            'Ё': '\u0463' + '\u0300',  # lowecase yat with grave accent
            '©': '\u0441' + '\u0483',  # the numeral two hundred
            '«': '\u00AB',
            '¬': '\u00AC',
            '®': '\u0440' + '\u2DE3',  # lowercase er with dobro titlo
            'Ї': '\u0406' + '\u0486',
            '°': '\uA67E',  # kavyka
            '±': '\uA657' + '\u0486' + '\u0300',
            'І': '\u0406',
            'і': '\u0456' + '\u0308',
            'ґ': '\u0430' + '\u0486',
            'µ': '\u0443',  # small letter u (why encoded at the micro sign?!)
            'ё': '\u0463' + '\u0301',  # lowercase yat with acute accent
            '№': '\u0430' + '\u0483',  # the numeral one
            'є': '\u0454',  # wide E
            '»': '\u00BB',
            'ј': '\u0456' + '\u0486' + '\u0301',  # lowercase i with apostrophe
            'Ѕ': '\u0405',
            'ѕ': '\u0455',
            'ї': '\u0456' + '\u0486',  # lowercase i with psili
            'У': '\uA64A',
            'Э': '\u0462',  # capital yat
            'Я': '\uA656',  # capital Iotified A
            'у': '\uA64B',  # monograph Uk (why?!)
            'э': '\u0463',  # lowercase yat
            'я': '\uA657',  # iotated a
            ### FURTHER THOSE UNIQE TO THIS PARTICULAR TEXT (the evangelion of 1606)
            'ӣ': '\u2DE0' + '\u0487',  # надстр б под титлом
            'Ӣ': '\u2DF6' + '\u0487',  # надстр а
            'μ': 'у',
            'Ө': '\u2DF0' + '\u0487',  # ц надстр под титлом
            'Ҳ': '\u2DE6' + '\u0487',  # к надстр под титлом
            'Ҵ': '\u2DEE',  # т надстр
            'Ӥ': '\u2DF7',  # Е надстр
            'ӥ': '\u2DE7' + '\u0487',  # л надстр под титлом
            'Ӯ': '\u2DF4',  # фета надстр
            'Ҷ': 'ꙍ',  # широкий от
            'ӯ': '҇',  # покрытие
            'Ӫ': '\u2DF3',  # щ надстрочное под титлом
            'ѹ': '\uFE2E' + '\uFE2F',  # титло на︮︯д буквой
            'Ӂ': 'ꙋ',  # ук лигатура
            'Ұ': 'ᲂ',  # острое о
            ',': ',',
            'ӡ': 'ꙁ',  # старая дзета
            'ү': 'ᲁ',  # д с длинными ножками
            'ө': '\u2DF2',  # ш надстр под титлом
            'Ҏ': '.',  # нежирная точка
            'ѣ': 'ᲇ',  # ять с загнутым концом
            'Һ': 'ѽ',  # широкий от с великим апострофом
            'Ѹ': '҃',  # титло меж҃ду буквами
            'ұ': '\u2DE8',  # м надстрочное
            'Ѷ': '‶',  # двойной обратный штрих
            'ӊ': 'ꙋ' + '\u0301',  # ук лигатура с лёгким ударением
            'ӈ': 'ꙋ' + '\u0301',
            'ӱ': '🕀',
            'Ӱ': '🕂',
            'ҵ': '\u2DED' + '\u0487',  # с надстр
            'Ӆ': 'ꙋ',  # короткий ук
            'җ': '\u0463' + '\u0300',  # ять с тяжёлым ударением
            'Ӈ': 'ꙋ' + '\u0300',  # ук лигатура с тяжёлым ударением
            'ӳ': '0' + '...',  # подкова повёрнутая вправо с тремя точками
            'Ӭ': '\u2DFB',  # ю надстр
            'Ӧ': '\u2DEB' + '\u0487',  # п надстр
            'ӭ': '\u2DFD' + '\u0487',  # юс малый надстр
            'ӂ': 'ꙋ',  # ук лигатура перед ч надстр
            'Ӵ': '...' + 'Ɔ',  # подкова повёрнутая влево с тремя точками
            'Ҹ': 'ꙍ' + '\u0301'  # широкий от с лёгким ударением
        }
    )

    utf8text = ''.join([decoding_map[sym] for sym in text])  # writes symbols' decodings to a new str
    return utf8text


def setchars(text, dump_list='', punct=True, superscripts=True, exceptions='', lower=False):
    def analog(sym):  # merges some small distinctions to simplify the text & learning
        if sym == '·':
            res = '.'
        elif sym == 'ꙍ':
            res = '\u047F'
        elif sym == 'ꙋ':
            res = 'у'
        elif sym == 'ᲂ':
            res = 'о'
        elif sym == 'ꙁ':
            res = 'з'
        elif sym == 'ѽ':
            res = '\u047F'
        elif sym == 'ᲁ':
            res = 'д'
        elif sym == 'ᲇ':
            res = '\u0463'
        elif sym == '\u047A':
            res = 'О'
        elif sym == 'ѻ':
            res = 'о'
        elif sym == '\uFE2F':
            res = '҃'
        elif sym == 'ї':
            res = '\u0456'
        elif sym == 'ѿ':
            res = 'ѡ'
        elif sym == 'ѷ':
            res = 'ѵ'
        elif sym == 'ꙑ':
            res = 'ы'
        else:
            res = ''
        return res

    if lower is True:
        text = text.lower()

    text_upd = ''  # реализует замену сложных оппозиций на аналоги и пропуск ненужных звуков
    for char in text:
        if char in dump_list:
            text_upd += analog(char)
        else:
            text_upd += char

    to_dump = ''  # добавляет пунктуацию в список для убора
    if not punct:
        to_dump += '꙳!";:-/.,\u00BB\u201A\u201E·\u2018\u2019\u201C\u201D\u2013\u2014\u0482\u00AB\u00AC'
    if not superscripts:
        to_dump += '\u0486\u0301‶\u2DE8\u2DF2\uFE2F\uFE2E\u2DF3\u2DF4\u2DE7\u2DF7\u2DEE\u2DE6\u2DF0' \
                      '\u2DF6\u2DE0\u0308\uA67E\u0486\u0300\u0301\u0483\u2DE1\u0487\u0311\u033E\u2DEF\u2DE9' \
                      '\u2DEC\u2DF1\u2DED\u0486\u2DE3\u2DEA\u2DE2\u2DE5\u2DE4̓҅ⸯ꙯҄̒'

    for i in exceptions:  # реалзует исключения из пунктуации и надстрочников
        to_dump = to_dump.replace(i, '')

    if not to_dump == '':
        for sym in to_dump:
            text_upd = text_upd.replace(sym, '')

    return text_upd


def two_sticks(txt):
    digraphs = {'к':'\u0456к', 'ы':'ь\u0456', 'К':'\u0406К', 'Ы':'Ь\u0406', ' ':''}
    for i in digraphs:
        txt = txt.replace(i, digraphs[i])
    return txt
