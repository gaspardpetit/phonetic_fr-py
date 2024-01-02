"""Module providing conversion of French words to a phonetic representation."""
import re


#
#	SOUNDEX FR
#	Édouard BERGÉ © 12.2007 v1.2
#   Ported to Python by Gaspard PETIT
#	MIT licence
#

ACCENTS = {'É': 'E', 'È': 'E', 'Ë': 'E', 'Ê': 'E', 'Á': 'A', 'À': 'A', 'Ä': 'A', 'Â': 'A',
            'Å': 'A', 'Ã': 'A', 'Æ': 'E', 'Ï': 'I', 'Î': 'I', 'Ì': 'I', 'Í': 'I',
            'Ô': 'O', 'Ö': 'O', 'Ò': 'O', 'Ó': 'O', 'Õ': 'O', 'Ø': 'O', 'Œ': 'OEU',
            'Ú': 'U', 'Ù': 'U', 'Û': 'U', 'Ü': 'U', 'Ñ': 'N', 'Ç': 'S', '¿': 'E'}
MIN_TO_MAJ = {'é': 'É', 'è': 'È', 'ë': 'Ë', 'ê': 'Ê', 'á': 'Á', 'â': 'Â', 'à': 'À', 'Ä': 'A',
            'Â': 'A', 'å': 'Å', 'ã': 'Ã', 'æ': 'Æ', 'ï': 'Ï', 'î': 'Î', 'ì': 'Ì', 'í': 'Í',
            'ô': 'Ô', 'ö': 'Ö', 'ò': 'Ò', 'ó': 'Ó', 'õ': 'Õ', 'ø': 'Ø', 'œ': 'Œ',
            'ú': 'Ú', 'ù': 'Ù', 'û': 'Û', 'ü': 'Ü', 'ç': 'Ç', 'ñ': 'Ñ', 'ß': 'S'}

# pylint: disable=too-many-return-statements,too-many-branches,too-many-statements
def phonetic(word):
    """
    Converts a French word into its phonetic representation.

    Parameters:
    - french_word (str): The input French word.

    Returns:
    str: The phonetic representation of the input word.

    Example:
    >>> phonetic("Python")
    'PITON'
    """

    # on garde uniquement les lettres de A à Z
    word = ''.join(char for char in word if char.isalpha())

    # on passe tout le reste en majuscules
    word = word.upper()

    # on sauve le code (utilisé pour les mots très courts)
    saved_word = word
    # minuscules accentuées ou composées en majuscules simples
    saved_word = saved_word.translate(str.maketrans(MIN_TO_MAJ))
    # majuscules accentuées ou composées en majuscules simples
    saved_word = saved_word.translate(str.maketrans(ACCENTS))

    # pré traitement: OO... -> OU
    word, _ = re.subn(r'O[O]+', 'OU', word)
    # pré traitement: SAOU -> SOU
    word, _ = re.subn(r'SAOU', 'SOU', word)
    # pré traitement: OES -> OS
    word, _ = re.subn(r'OES', 'OS', word)
    # pré traitement: CCH -> K
    word, _ = re.subn(r'CCH', 'K', word)
    # pré traitement: CCI CCY CCE
    word, _ = re.subn(r'CC([IYE])', r'KS\1', word)

    # minuscules accentuées ou composées en majuscules simples
    word = word.translate(str.maketrans(MIN_TO_MAJ))
    # majuscules accentuées ou composées en majuscules simples
    word = word.translate(str.maketrans(ACCENTS))

    # supression des répétitions
    conv_mapping = {
        "DILLEM": "DIEM"
    }
    for conv_in, conv_out in conv_mapping.items():
        word = word.replace(conv_in, conv_out)
    word, _ = re.subn(r'(.)\1', r'\1', word)

    # quelques cas particuliers
    special_cases = {
        "CD": "CD",
        "BD": "BD",
        "BV": "BV",
        "TABAC": "TABA",
        "FEU": "FE",
        "FE": "FE",
        "FER": "FER",
        "VER": "VER",
        "FIEF": "FIEF",
        "FJORD": "FJORD",
        "GOAL": "GOL",
        "FLEAU": "FLEO",
        "HIER": "IER",
        "HEU": "E",
        "HE": "E",
        "OS": "OS",
        "RIZ": "RI",
        "RAZ": "RA",
    }

    if word in special_cases:
        return special_cases[word]

    # pré-traitements
    # Terminations OING -> OIN
    word, _ = re.subn(r'OIN[GT]$', 'OIN', word)
    # Remove infinitive and plural participle endings
    word, _ = re.subn(r'E[RS]$', 'E', word)
    # pré traitement OEU -> EU
    word, _ = re.subn(r'(C|CH)OEU', 'KE', word)
    # pré traitement OEU -> EU
    word, _ = re.subn(r'MOEU', 'ME', word)
    # pré traitement OEU OEI -> E
    word, _ = re.subn(r'OE([UI]+)([BCDFGHJKLMNPQRSTVWXZ])', r'E\1\2', word)
    # pré traitement GEN -> JAN
    word, _ = re.subn(r'^GEN[TS]$', 'JAN', word)
    # pré traitement accueil
    word, _ = re.subn(r'CUEI', 'KEI', word)
    # pré traitement AE -> E
    word, _ = re.subn(r'([^AEIOUYC])AE([BCDFGHJKLMNPQRSTVWXZ])', r'\1E\2', word)
    # pré traitement AE -> E
    word, _ = re.subn(r'AE([QS])', r'E\1', word)
    # pré traitement AIE(consonne) -> AI
    word, _ = re.subn(r'AIE([BCDFGJKLMNPQRSTVWXZ])', r'AI\1', word)
    # pré traitement NIEM -> NIM
    word, _ = re.subn(r'ANIEM', 'ANIM', word)
    # P terminal muet
    word, _ = re.subn(r'(DRA|TRO|IRO)P$', r'\1', word)
    # B terminal muet
    word, _ = re.subn(r'(LOM)B$', r'\1', word)
    # C terminal muet
    word, _ = re.subn(r'(RON|POR)C$', r'\1', word)
    # C terminal muet
    word, _ = re.subn(r'PECT$', 'PET', word)
    # L terminal muet
    word, _ = re.subn(r'ECUL$', 'CU', word)
    # P or PS terminal muet
    word, _ = re.subn(r'(CHA|CA|E)M(P|PS)$', r'\1N', word)
    # G terminal muet
    word, _ = re.subn(r'(TAN|RAN)G$', r'\1', word)

    # sons YEUX
    word, _ = re.subn(r'([^VO])ILAG', r'\1IAJ', word)
    word, _ = re.subn(r'([^TRH])UIL(AR|E)(.+)', r'\1UI\2\3', word)
    word, _ = re.subn(r'([G])UIL([AEO])', r'\1UI\2', word)
    word, _ = re.subn(r'([NSPM])AIL([AEO])', r'\1AI\2', word)

    conv_mapping = {
        "DILAI": "DIAI",
        "DILON": "DION",
        "DILER": "DIER",
        "RILON": "RION",
        "TAILE": "TAIE",
        "GAILET": "GAIET",
        "AILAI": "AIAI",
        "AILAR": "AIAR",
        "OUILA": "OUIA",
        "EILAI": "AIAI",
        "EILAR": "AIAR",
        "EILER": "AIER",
        "EILEM": "AIEM",
        "REILET": "RAIET",
        "EILET": "EIET",
        "AILOL": "AIOL"
    }

    for conv_in, conv_out in conv_mapping.items():
        word = word.replace(conv_in, conv_out)

    # IEM -> IAM
    word, _ = re.subn(r'([^AEIOUY])(SC|S)IEM([EA])', r'\1\2IAM\3', word)
    # IEM -> IAM
    word, _ = re.subn(r'^(SC|S)IEM([EA])', r'\1IAM\2', word)

    # MP MB -> NP NB
    conv_m_in = ['OMB', 'AMB', 'OMP', 'AMP', 'IMB', 'EMP', 'GEMB', 'EMB', 'UMBL', 'CIEN']
    conv_m_ou = ['ONB', 'ANB', 'ONP', 'ANP', 'INB', 'ANP', 'JANB', 'ANB', 'INBL', 'SIAN']

    for conv_in, conv_out in zip(conv_m_in, conv_m_ou):
        word = word.replace(conv_in, conv_out)

    # Sons en K
    # cas particulier: écho
    word, _ = re.subn(r'^ECHO$', 'EKO', word)
    # cas particulier: écœuré
    word, _ = re.subn(r'^ECEUR', 'EKEUR', word)

    # Choléra Chœur mais pas chocolat!
    # En début de mot
    word, _ = re.subn(r'^CH(OG+|OL+|OR+|EU+|ARIS|M+|IRO|ONDR)', r'K\1', word)
    # Ou devant une consonne
    word, _ = re.subn(r'(YN|RI)CH(OG+|OL+|OC+|OP+|OM+|ARIS|M+|IRO|ONDR)', r'\1K\2', word)
    word, _ = re.subn(r'CHS', 'CH', word)
    word, _ = re.subn(r'CH(AIQ)', r'K\1', word)
    word, _ = re.subn(r'^ECHO([^UIPY])', r'EKO\1', word)
    word, _ = re.subn(r'ISCH(I|E)', r'ISK\1', word)
    word, _ = re.subn(r'^ICHT', 'IKT', word)
    word, _ = re.subn(r'ORCHID', 'ORKID', word)
    word, _ = re.subn(r'ONCHIO', 'ONKIO', word)
    # retouche ACHIA -> AKIA
    word, _ = re.subn(r'ACHIA', 'AKIA', word)
    # ANICH -> ANIK  1/2
    word, _ = re.subn(r'([^C])ANICH', r'\1ANIK', word)
    # cas particulier  2/2
    word, _ = re.subn(r'OMANIK', 'OMANICH', word)
    word, _ = re.subn(r'ACHY([^D])', r'AKI\1', word)
    # voyelle, C, consonne sauf H
    word, _ = re.subn(r'([AEIOU])C([BDFGJKLMNPQRTVWXZ])', r'\1K\2', word)

    conv_pr_in = ['EUCHA', 'YCHIA', 'YCHA', 'YCHO', 'YCHED', 'ACHEO', 'RCHEO', 'RCHES',
                'ECHN', 'OCHTO', 'CHORA', 'CHONDR', 'CHORE', 'MACHM', 'BRONCHO', 'LICHOS', 'LICHOC']
    conv_pr_out = ['EKA', 'IKIA', 'IKA', 'IKO', 'IKED', 'AKEO', 'RKEO', 'RKES',
                 'EKN', 'OKTO', 'KORA', 'KONDR', 'KORE', 'MAKM', 'BRONKO', 'LIKOS', 'LIKOC']

    for conv_in, conv_out in zip(conv_pr_in, conv_pr_out):
        word = word.replace(conv_in, conv_out)

    # Weuh (perfectible)
    conv_pr_in = ['WA', 'WO', 'WI', 'WHI', 'WHY', 'WHA', 'WHO']
    conv_pr_out = ['OI', 'O', 'OUI', 'OUI', 'OUI', 'OUA', 'OU']

    for conv_in, conv_out in zip(conv_pr_in, conv_pr_out):
        word = word.replace(conv_in, conv_out)

    # Gueu, Gneu, Jeu et quelques autres
    conv_pr_in = ['GNES', 'GNET', 'GNER', 'GNE', 'GI', 'GNI', 'GNA', 'GNOU', 'GNUR', 'GY', 'OUGAIN',
                'AGEOL', 'AGEOT', 'GEOLO', 'GEOM', 'GEOP', 'GEOG', 'GEOS', 'GEORG', 'GEOR', 'NGEOT',
                'UGEOT', 'GEOT', 'GEOD', 'GEOC', 'GEO', 'GEA', 'GE', 'QU', 'Q', 'CY', 'CI', 'CN',
                'ICM', 'CEAT', 'CE', 'CR', 'CO', 'CUEI', 'CU', 'VENCA', 'CA', 'CS', 'CLEN', 'CL',
                'CZ', 'CTIQ', 'CTIF', 'CTIC', 'CTIS', 'CTIL', 'CTIO', 'CTI', 'CTU', 'CTE', 'CTO',
                'CTR', 'CT', 'PH', 'TH', 'OW', 'LH', 'RDL', 'CHLO', 'CHR', 'PTIA']

    conv_pr_out = ['NIES', 'NIET', 'NIER', 'NE', 'JI', 'NI', 'NIA', 'NIOU', 'NIUR', 'JI', 'OUGIN',
                 'AJOL', 'AJOT', 'JEOLO', 'JEOM', 'JEOP', 'JEOG', 'JEOS', 'JORJ', 'JEOR', 'NJOT',
                 'UJOT', 'JEOT', 'JEOD', 'JEOC', 'JO', 'JA', 'JE', 'K', 'K', 'SI', 'SI', 'KN',
                 'IKM', 'SAT', 'SE', 'KR', 'KO', 'KEI', 'KU', 'VANSA', 'KA', 'KS', 'KLAN', 'KL',
                 'KZ', 'KTIK', 'KTIF', 'KTIS', 'KTIS', 'KTIL', 'KSIO', 'KTI', 'KTU', 'KTE', 'KTO',
                 'KTR', 'KT', 'F', 'T', 'OU', 'L', 'RL', 'KLO', 'KR', 'PSIA']

    for conv_in, conv_out in zip(conv_pr_in, conv_pr_out):
        word = word.replace(conv_in, conv_out)

    word, _ = re.subn(r'GU([^RLMBSTPZN])', r'G\1', word)  # Gueu!
    word, _ = re.subn(r'GNO([MLTNRKG])', r'NIO\1', word)  # GNO ! Tout sauf S pour gnos
    word, _ = re.subn(r'GNO([MLTNRKG])', r'NIO\1',
                 word)  # bis -> gnognotte! Si quelqu'un sait le faire en une seule regexp...

    # TI -> SI v2.0
    conv_pr_in = ['BUTIE', 'BUTIA', 'BATIA', 'ANTIEL', 'RETION', 'ENTIEL', 'ENTIAL', 'ENTIO',
                  'ENTIAI', 'UJETION', 'ATIEM', 'PETIEN', 'CETIE', 'OFETIE', 'IPETI', 'LBUTION',
                   'BLUTION', 'LETION', 'LATION', 'SATIET']
    conv_pr_out = ['BUSIE', 'BUSIA', 'BASIA', 'ANSIEL', 'RESION', 'ENSIEL', 'ENSIAL', 'ENSIO',
                   'ENSIAI', 'UJESION', 'ASIAM', 'PESIEN', 'CESIE', 'OFESIE', 'IPESI', 'LBUSION',
                   'BLUSION', 'LESION', 'LASION', 'SASIET']

    for conv_in, conv_out in zip(conv_pr_in, conv_pr_out):
        word = word.replace(conv_in, conv_out)

    # sauf antialcoolique, antialbumine, antialarmer, ...
    word, _ = re.subn(r'(.+)ANTI(AL|O)', r'\1ANSI\2', word)
    # sauf inutilité, inutilement, diminutive, ...
    word, _ = re.subn(r'(.+)INUTI([^V])', r'\1INUSI\2', word)
    # sauf soutien, ...
    word, _ = re.subn(r'([^O])UTIEN', r'\1USIEN', word)

    # sauf xxxxxcratique, ...
    word, _ = re.subn(r'([^DE])RATI[E]$', r'\1RASI', word)

    # TIEN TION -> SIEN SION v3.1
    word, _ = re.subn(r'([^SNEU]|KU|KO|RU|LU|BU|TU|AU)T(IEN|ION)', r'\1S\2', word)

    # H muet
    word, _ = re.subn(r'([^CS])H', r'\1', word)
    word = word.replace("ESH", "ES")
    word = word.replace("NSH", "NS")
    # ou pas!
    word = word.replace("SH", "CH")

    # NASALES
    conv_nas_in = ['OMT', 'IMB', 'IMP', 'UMD', 'TIENT', 'RIENT', 'DIENT', 'IEN', 'YMU', 'YMO',
                 'YMA', 'YME', 'YMI', 'YMN', 'YM', 'AHO', 'FAIM', 'DAIM', 'SAIM', 'EIN', 'AINS']
    con_nas_out = ['ONT', 'INB', 'INP', 'OND', 'TIANT', 'RIANT', 'DIANT', 'IN', 'IMU', 'IMO',
                  'IMA', 'IME', 'IMI', 'IMN', 'IN', 'AO', 'FIN', 'DIN', 'SIN', 'AIN', 'INS']
    for conv_in, conv_out in zip(conv_nas_in, con_nas_out):
        word = word.replace(conv_in, conv_out)

    # AIN -> IN v2.0
    word, _ = re.subn(r'AIN$', 'IN', word)
    word, _ = re.subn(r'AIN([BTDK])', r'IN\1', word)

    # UN -> IN
    word, _ = re.subn(r'([^O])UND', r'\1IND', word)
    word, _ = re.subn(r'([JTVLFMRPSBD])UN([^IAE])', r'\1IN\2', word)
    word, _ = re.subn(r'([JTVLFMRPSBD])UN$', r'\1IN', word)
    word, _ = re.subn(r'RFUM$', 'RFIN', word)
    word, _ = re.subn(r'LUMB', 'LINB', word)

    # EN -> AN
    word, _ = re.subn(r'([^BCDFGHJKLMNPQRSTVWXZ])EN', r'\1AN', word)
    word, _ = re.subn(r'([VTLJMRPDSBFKNG])EN([BRCTDKZSVN])', r'\1AN\2', word)
    word, _ = re.subn(r'([VTLJMRPDSBFKNG])EN([BRCTDKZSVN])', r'\1AN\2', word)
    word, _ = re.subn(r'^EN([BCDFGHJKLNPQRSTVXZ]|CH|IV|ORG|OB|UI|UA|UY)', r'AN\1', word)
    word, _ = re.subn(r'(^[JRVTH])EN([DRTFGSVJMP])', r'\1AN\2', word)
    word, _ = re.subn(r'SEN([ST])', r'SAN\1', word)
    word, _ = re.subn(r'^DESENIV', 'DESANIV', word)
    word, _ = re.subn(r'([^M])EN(UI)', r'\1AN\2', word)
    word, _ = re.subn(r'(.+[JTVLFMRPSBD])EN([JLFDSTG])', r'\1AN\2', word)

    # EI -> AI
    word, _ = re.subn(r'([VSBSTNRLPM])E[IY]([ACDFRJLGZ])', r'\1AI\2', word)

    # AIR -> ER
    word, _ = re.subn(r'AIR$', 'ER', word)
    word, _ = re.subn(r'AIRE$', 'ER', word)
    word, _ = re.subn(r'AIRD$', 'ER', word)

    # Histoire d'Ô
    conv_nas_in = ['EAU', 'EU', 'Y', 'EOI', 'JEA', 'OIEM', 'OUANJ', 'OUA', 'OUENJ']
    con_nas_out = ['O', 'E', 'I', 'OI', 'JA', 'OIM', 'OUENJ', 'OI', 'OUANJ']
    for conv_in, conv_out in zip(conv_nas_in, con_nas_out):
        word = word.replace(conv_in, conv_out)

    # AU without a following E
    word, _ = re.subn(r'AU([^E])', r'O\1', word)

    # Les retouches!
    # Retouche BENJ -> BINJ
    word, _ = re.subn(r'^BENJ', 'BINJ', word)
    # Retouche RTIEL -> RSIEL
    word, _ = re.subn(r'RTIEL', 'RSIEL', word)
    # Retouche PINK -> PONK
    word, _ = re.subn(r'PINK', 'PONK', word)
    # Retouche KIND -> KOND
    word, _ = re.subn(r'KIND', 'KOND', word)
    # Retouche KUMN KUMP
    word, _ = re.subn(r'KUM(N|P)', r'KON\1', word)
    # Retouche LKOU -> LKO
    word, _ = re.subn(r'LKOU', 'LKO', word)
    # Retouche EDBE pied-bœuf
    word, _ = re.subn(r'EDBE', 'EBE', word)
    # Retouche SCH -> CH
    word, _ = re.subn(r'ARCM', 'ARKM', word)
    # Retouche SCH -> CH
    word, _ = re.subn(r'SCH', 'CH', word)
    # Retouche début OINI -> ONI
    word, _ = re.subn(r'^OINI', 'ONI', word)
    # Retouche APT -> AT
    word, _ = re.subn(r'([^NDCGRHKO])APT', r'\1AT', word)
    # Retouche LPT -> LT
    word, _ = re.subn(r'([L]|KON)PT', r'\1T', word)
    # Retouche OTB -> OB (hautbois)
    word, _ = re.subn(r'OTB', 'OB', word)
    # Retouche IXA -> ISA
    word, _ = re.subn(r'IXA', 'ISA', word)
    # Retouche TG -> G
    word, _ = re.subn(r'TG', 'G', word)
    # Retouche début TZ -> TS
    word, _ = re.subn(r'^TZ', 'TS', word)
    # Retouche PTIE -> TIE
    word, _ = re.subn(r'PTIE', 'TIE', word)
    # Retouche GT -> T
    word, _ = re.subn(r'GT', 'T', word)
    # Retouche tranquillement
    word = word.replace("ANKIEM", "ANKILEM")
    # Retouche KEMAN -> KAMAN
    word, _ = re.subn(r'(LO|RE)KEMAN', r'\1KAMAN', word)
    # Retouche TB -> B  TM -> M
    word, _ = re.subn(r'NT(B|M)', r'N\1', word)
    # Retouche GS -> SU
    word, _ = re.subn(r'GSU', 'SU', word)
    # Retouche ESD -> ED
    word, _ = re.subn(r'ESD', 'ED', word)
    # Retouche LESQUEL -> LEKEL
    word, _ = re.subn(r'LESKEL', 'LEKEL', word)
    # Retouche CK -> K
    word, _ = re.subn(r'CK', 'K', word)

    # Terminaisons
    # Terminaisons USIL -> USI
    word, _ = re.subn(r'USIL$', 'USI', word)
    # Terminaisons TS DS LS X T D S...  v2.0
    word, _ = re.subn(r'X$|[TD]S$|[DS]$', '', word)
    # Sauf KT LT terminal
    word, _ = re.subn(r'([^KL]+)T$', r'\1', word)
    # H pseudo muet en début de mot
    word, _ = re.subn(r'^[H]', '', word)

    # On sauve le code (utilisé pour les mots très courts)
    saved_word2 = word

    # Terminaisons TIL -> TI
    word, _ = re.subn(r'TIL$', 'TI', word)
    # Terminaisons LC -> LK
    word, _ = re.subn(r'LC$', 'LK', word)
    # Terminaisons LE LES -> L
    word, _ = re.subn(r'L[E]?[S]?$', 'L', word)
    # Terminaisons NE NES -> N
    word, _ = re.subn(r'(.+)N[E]?[S]?$', r'\1N', word)
    # Terminaisons EZ -> E
    word, _ = re.subn(r'EZ$', 'E', word)
    # Terminaisons OIG -> OI
    word, _ = re.subn(r'OIG$', 'OI', word)
    # Terminaisons OUP -> OU
    word, _ = re.subn(r'OUP$', 'OU', word)
    # Terminaisons OM -> ON sauf ROM
    word, _ = re.subn(r'([^R])OM$', r'\1ON', word)
    # Terminaisons LOP -> LO
    word, _ = re.subn(r'LOP$', 'LO', word)
    # Terminaisons NTANP -> NTAN
    word, _ = re.subn(r'NTANP$', 'NTAN', word)
    # Terminaisons TUN -> TIN
    word, _ = re.subn(r'TUN$', 'TIN', word)
    # Terminaisons AU -> O
    word, _ = re.subn(r'AU$', 'O', word)
    # Terminaisons EI -> AI
    word, _ = re.subn(r'EI$', 'AI', word)
    # Terminaisons RD RG -> R
    word, _ = re.subn(r'R[DG]$', 'R', word)
    # Terminaisons ANC -> AN
    word, _ = re.subn(r'ANC$', 'AN', word)
    # Terminaisons C muet de CROC, ESCROC
    word, _ = re.subn(r'KROC$', 'KRO', word)
    # Terminaisons C muet de CAOUTCHOUC
    word, _ = re.subn(r'HOUC$', 'HOU', word)
    # Terminaisons C muet de ESTOMAC (mais pas HAMAC)
    word, _ = re.subn(r'OMAC$', 'OMA', word)
    # Terminaisons C et G muet de OUC ONC OUG
    word, _ = re.subn(r'([J])O([NU])[CG]$', r'\1O\2', word)
    # Terminaisons G muet ANG ONG sauf GANG GONG TANG TONG
    word, _ = re.subn(r'([^GTR])([AO])NG$', r'\1\2N', word)
    # Terminaisons UC -> UK
    word, _ = re.subn(r'UC$', 'UK', word)
    # Terminaisons AING -> IN
    word, _ = re.subn(r'AING$', 'IN', word)
    # Terminaisons C -> K
    word, _ = re.subn(r'([EISOARN])C$', r'\1K', word)
    # Terminaisons E ou H sauf pour C et N
    word, _ = re.subn(r'([ABD-MO-Z]+)[EH]+$', r'\1', word)
    # Terminaisons EN -> AN (difficile à faire avant sans avoir des soucis)
    word, _ = re.subn(r'EN$', 'AN', word)
    # Terminaisons EN -> AN
    word, _ = re.subn(r'(NJ)EN$', r'\1AN', word)
    # PAIE -> PAI
    word, _ = re.subn(r'^PAIEM', 'PAIM', word)
    # F muet en fin de mot
    word, _ = re.subn(r'([^NTB])EF$', r'\1', word)

    # Suppression des répétitions (suite à certains remplacements)
    word, _ = re.subn(r'(.)\1', r'\1', word)

    # Cas particuliers, bah au final, je n'en ai qu'un ici
    conv_part_in = ['FUEL']
    conv_part_out = ['FIOUL']
    for conv_in, conv_out in zip(conv_part_in, conv_part_out):
        word = word.replace(conv_in, conv_out)

    # Ce sera le seul code retourné à une seule lettre!
    if word == 'O':
        return word

    # seconde chance sur les mots courts qui ont souffert de la simplification
    if len(word) < 2:
        # Sigles ou abréviations
        if bool(re.match(
                "[BCDFGHJKLMNPQRSTVWXYZ]"+
                "[BCDFGHJKLMNPQRSTVWXYZ]"+
                "[BCDFGHJKLMNPQRSTVWXYZ]"+
                "[BCDFGHJKLMNPQRSTVWXYZ]*",
                saved_word)):
            return saved_word

        if bool(re.match("[RFMLVSPJDF][AEIOU]", saved_word)):
            if 2 <= len(saved_word) <= 4:
                # mots de trois ou quatre lettres supposés simples
                return saved_word[:len(saved_word) - 1]

        if len(saved_word2) > 1:
            return saved_word2

    elif len(word) > 1:
        return word[:16]  # Je limite à 16 caractères mais vous faites comme vous voulez!

    return ''

def phonetic_text(input_str):
    """replaces each words from a string by its equivalent phonetic representation"""
    current_word = ""
    result = ""
    for char in input_str:
        if char.isspace():
            if current_word:
                result += phonetic(current_word) + char
                current_word = ""
            else:
                result += char
        else:
            current_word += char
    if current_word:
        result += phonetic(current_word)
    return result

def main():
    """Sample usage"""

    # Obtain phonetic representation of a word
    example = "python"
    result = phonetic(example)
    print(f"{example} -> {result}")

    # Compare two names with sounding alike
    are_alike = phonetic("Gilles") == phonetic("Jill")
    print(f"Gilles sounds like Jill: {are_alike}")

    # Improve Levenshtein's distance
    # pylint: disable=import-outside-toplevel
    from Levenshtein import distance
    word_a = "drapeau"
    word_b = "crapaud"
    raw_distance = distance(word_a, word_b)
    print(f"Levenshtein distance of '{word_a}' and '{word_b}': {raw_distance}")
    phonetic_distance = distance(phonetic(word_a), phonetic(word_b))
    print(f"Phonetic Levenshtein distance of '{word_a}' and '{word_b}': {phonetic_distance}")

    # Convert a text to its phonetic representation
    original = "Le ver vert glisse vers le verre"
    transformed = phonetic_text("Le ver vert glisse vers le verre")
    print(f"{original}\n{transformed}")

if __name__ == '__main__':
    main()
    