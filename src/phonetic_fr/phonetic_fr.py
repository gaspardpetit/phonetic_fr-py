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
def phonetic(french_word):
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
    french_word = ''.join(char for char in french_word if char.isalpha())

    # on passe tout le reste en majuscules
    french_word = french_word.upper()

    # on sauve le code (utilisé pour les mots très courts)
    saved_word = french_word
    # minuscules accentuées ou composées en majuscules simples
    saved_word = saved_word.translate(str.maketrans(MIN_TO_MAJ))
    # majuscules accentuées ou composées en majuscules simples
    saved_word = saved_word.translate(str.maketrans(ACCENTS))

    # pré traitement: OO... -> OU
    french_word = re.sub(r'O[O]+', 'OU', french_word)
    # pré traitement: SAOU -> SOU
    french_word = re.sub(r'SAOU', 'SOU', french_word)
    # pré traitement: OES -> OS
    french_word = re.sub(r'OES', 'OS', french_word)
    # pré traitement: CCH -> K
    french_word = re.sub(r'CCH', 'K', french_word)
    # pré traitement: CCI CCY CCE
    french_word = re.sub(r'CC([IYE])', r'KS\1', french_word)

    # minuscules accentuées ou composées en majuscules simples
    french_word = french_word.translate(str.maketrans(MIN_TO_MAJ))
    # majuscules accentuées ou composées en majuscules simples
    french_word = french_word.translate(str.maketrans(ACCENTS))

    # supression des répétitions
    conv_mapping = {
        "DILLEM": "DIEM"
    }
    for conv_in, conv_out in conv_mapping.items():
        french_word = french_word.replace(conv_in, conv_out)
    french_word = re.sub(r'(.)\1', r'\1', french_word)

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

    if french_word in special_cases:
        return special_cases[french_word]

    # pré-traitements
    # Terminations OING -> OIN
    french_word = re.sub(r'OIN[GT]$', 'OIN', french_word)
    # Remove infinitive and plural participle endings
    french_word = re.sub(r'E[RS]$', 'E', french_word)
    # pré traitement OEU -> EU
    french_word = re.sub(r'(C|CH)OEU', 'KE', french_word)
    # pré traitement OEU -> EU
    french_word = re.sub(r'MOEU', 'ME', french_word)
    # pré traitement OEU OEI -> E
    french_word = re.sub(r'OE([UI]+)([BCDFGHJKLMNPQRSTVWXZ])', r'E\1\2', french_word)
    # pré traitement GEN -> JAN
    french_word = re.sub(r'^GEN[TS]$', 'JAN', french_word)
    # pré traitement accueil
    french_word = re.sub(r'CUEI', 'KEI', french_word)
    # pré traitement AE -> E
    french_word = re.sub(r'([^AEIOUYC])AE([BCDFGHJKLMNPQRSTVWXZ])', r'\1E\2', french_word)
    # pré traitement AE -> E
    french_word = re.sub(r'AE([QS])', r'E\1', french_word)
    # pré traitement AIE(consonne) -> AI
    french_word = re.sub(r'AIE([BCDFGJKLMNPQRSTVWXZ])', r'AI\1', french_word)
    # pré traitement NIEM -> NIM
    french_word = re.sub(r'ANIEM', 'ANIM', french_word)
    # P terminal muet
    french_word = re.sub(r'(DRA|TRO|IRO)P$', r'\1', french_word)
    # B terminal muet
    french_word = re.sub(r'(LOM)B$', r'\1', french_word)
    # C terminal muet
    french_word = re.sub(r'(RON|POR)C$', r'\1', french_word)
    # C terminal muet
    french_word = re.sub(r'PECT$', 'PET', french_word)
    # L terminal muet
    french_word = re.sub(r'ECUL$', 'CU', french_word)
    # P or PS terminal muet
    french_word = re.sub(r'(CHA|CA|E)M(P|PS)$', r'\1N', french_word)
    # G terminal muet
    french_word = re.sub(r'(TAN|RAN)G$', r'\1', french_word)

    # sons YEUX
    french_word = re.sub(r'([^VO])ILAG', r'\1IAJ', french_word)
    french_word = re.sub(r'([^TRH])UIL(AR|E)(.+)', r'\1UI\2\3', french_word)
    french_word = re.sub(r'([G])UIL([AEO])', r'\1UI\2', french_word)
    french_word = re.sub(r'([NSPM])AIL([AEO])', r'\1AI\2', french_word)

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
        french_word = french_word.replace(conv_in, conv_out)

    # IEM -> IAM
    french_word = re.sub(r'([^AEIOUY])(SC|S)IEM([EA])', r'\1\2IAM\3', french_word)
    # IEM -> IAM
    french_word = re.sub(r'^(SC|S)IEM([EA])', r'\1IAM\2', french_word)

    # MP MB -> NP NB
    conv_m_in = ['OMB', 'AMB', 'OMP', 'AMP', 'IMB', 'EMP', 'GEMB', 'EMB', 'UMBL', 'CIEN']
    conv_m_ou = ['ONB', 'ANB', 'ONP', 'ANP', 'INB', 'ANP', 'JANB', 'ANB', 'INBL', 'SIAN']

    for conv_in, conv_out in zip(conv_m_in, conv_m_ou):
        french_word = french_word.replace(conv_in, conv_out)

    # Sons en K
    # cas particulier: écho
    french_word = re.sub(r'^ECHO$', 'EKO', french_word)
    # cas particulier: écœuré
    french_word = re.sub(r'^ECEUR', 'EKEUR', french_word)

    # Choléra Chœur mais pas chocolat!
    # En début de mot
    french_word = re.sub(r'^CH(OG+|OL+|OR+|EU+|ARIS|M+|IRO|ONDR)', r'K\1', french_word)
    # Ou devant une consonne
    french_word = re.sub(r'(YN|RI)CH(OG+|OL+|OC+|OP+|OM+|ARIS|M+|IRO|ONDR)', r'\1K\2', french_word)
    french_word = re.sub(r'CHS', 'CH', french_word)
    french_word = re.sub(r'CH(AIQ)', r'K\1', french_word)
    french_word = re.sub(r'^ECHO([^UIPY])', r'EKO\1', french_word)
    french_word = re.sub(r'ISCH(I|E)', r'ISK\1', french_word)
    french_word = re.sub(r'^ICHT', 'IKT', french_word)
    french_word = re.sub(r'ORCHID', 'ORKID', french_word)
    french_word = re.sub(r'ONCHIO', 'ONKIO', french_word)
    # retouche ACHIA -> AKIA
    french_word = re.sub(r'ACHIA', 'AKIA', french_word)
    # ANICH -> ANIK  1/2
    french_word = re.sub(r'([^C])ANICH', r'\1ANIK', french_word)
    # cas particulier  2/2
    french_word = re.sub(r'OMANIK', 'OMANICH', french_word)
    french_word = re.sub(r'ACHY([^D])', r'AKI\1', french_word)
    # voyelle, C, consonne sauf H
    french_word = re.sub(r'([AEIOU])C([BDFGJKLMNPQRTVWXZ])', r'\1K\2', french_word)

    conv_pr_in = ['EUCHA', 'YCHIA', 'YCHA', 'YCHO', 'YCHED', 'ACHEO', 'RCHEO', 'RCHES',
                'ECHN', 'OCHTO', 'CHORA', 'CHONDR', 'CHORE', 'MACHM', 'BRONCHO', 'LICHOS', 'LICHOC']
    conv_pr_out = ['EKA', 'IKIA', 'IKA', 'IKO', 'IKED', 'AKEO', 'RKEO', 'RKES',
                 'EKN', 'OKTO', 'KORA', 'KONDR', 'KORE', 'MAKM', 'BRONKO', 'LIKOS', 'LIKOC']

    for conv_in, conv_out in zip(conv_pr_in, conv_pr_out):
        french_word = french_word.replace(conv_in, conv_out)

    # Weuh (perfectible)
    conv_pr_in = ['WA', 'WO', 'WI', 'WHI', 'WHY', 'WHA', 'WHO']
    conv_pr_out = ['OI', 'O', 'OUI', 'OUI', 'OUI', 'OUA', 'OU']

    for conv_in, conv_out in zip(conv_pr_in, conv_pr_out):
        french_word = french_word.replace(conv_in, conv_out)

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
        french_word = french_word.replace(conv_in, conv_out)

    french_word = re.sub(r'GU([^RLMBSTPZN])', r'G\1', french_word)  # Gueu!
    french_word = re.sub(r'GNO([MLTNRKG])', r'NIO\1', french_word)  # GNO ! Tout sauf S pour gnos
    french_word = re.sub(r'GNO([MLTNRKG])', r'NIO\1',
                 french_word)  # bis -> gnognotte! Si quelqu'un sait le faire en une seule regexp...

    # TI -> SI v2.0
    conv_pr_in = ['BUTIE', 'BUTIA', 'BATIA', 'ANTIEL', 'RETION', 'ENTIEL', 'ENTIAL', 'ENTIO',
                  'ENTIAI', 'UJETION', 'ATIEM', 'PETIEN', 'CETIE', 'OFETIE', 'IPETI', 'LBUTION',
                   'BLUTION', 'LETION', 'LATION', 'SATIET']
    conv_pr_out = ['BUSIE', 'BUSIA', 'BASIA', 'ANSIEL', 'RESION', 'ENSIEL', 'ENSIAL', 'ENSIO',
                   'ENSIAI', 'UJESION', 'ASIAM', 'PESIEN', 'CESIE', 'OFESIE', 'IPESI', 'LBUSION',
                   'BLUSION', 'LESION', 'LASION', 'SASIET']

    for conv_in, conv_out in zip(conv_pr_in, conv_pr_out):
        french_word = french_word.replace(conv_in, conv_out)

    # sauf antialcoolique, antialbumine, antialarmer, ...
    french_word = re.sub(r'(.+)ANTI(AL|O)', r'\1ANSI\2', french_word)
    # sauf inutilité, inutilement, diminutive, ...
    french_word = re.sub(r'(.+)INUTI([^V])', r'\1INUSI\2', french_word)
    # sauf soutien, ...
    french_word = re.sub(r'([^O])UTIEN', r'\1USIEN', french_word)

    # sauf xxxxxcratique, ...
    french_word = re.sub(r'([^DE])RATI[E]$', r'\1RASI', french_word)

    # TIEN TION -> SIEN SION v3.1
    french_word = re.sub(r'([^SNEU]|KU|KO|RU|LU|BU|TU|AU)T(IEN|ION)', r'\1S\2', french_word)

    # H muet
    french_word = re.sub(r'([^CS])H', r'\1', french_word)
    french_word = french_word.replace("ESH", "ES")
    french_word = french_word.replace("NSH", "NS")
    # ou pas!
    french_word = french_word.replace("SH", "CH")

    # NASALES
    conv_nas_in = ['OMT', 'IMB', 'IMP', 'UMD', 'TIENT', 'RIENT', 'DIENT', 'IEN', 'YMU', 'YMO',
                 'YMA', 'YME', 'YMI', 'YMN', 'YM', 'AHO', 'FAIM', 'DAIM', 'SAIM', 'EIN', 'AINS']
    con_nas_out = ['ONT', 'INB', 'INP', 'OND', 'TIANT', 'RIANT', 'DIANT', 'IN', 'IMU', 'IMO',
                  'IMA', 'IME', 'IMI', 'IMN', 'IN', 'AO', 'FIN', 'DIN', 'SIN', 'AIN', 'INS']
    for conv_in, conv_out in zip(conv_nas_in, con_nas_out):
        french_word = french_word.replace(conv_in, conv_out)

    # AIN -> IN v2.0
    french_word = re.sub(r'AIN$', 'IN', french_word)
    french_word = re.sub(r'AIN([BTDK])', r'IN\1', french_word)

    # UN -> IN
    french_word = re.sub(r'([^O])UND', r'\1IND', french_word)
    french_word = re.sub(r'([JTVLFMRPSBD])UN([^IAE])', r'\1IN\2', french_word)
    french_word = re.sub(r'([JTVLFMRPSBD])UN$', r'\1IN', french_word)
    french_word = re.sub(r'RFUM$', 'RFIN', french_word)
    french_word = re.sub(r'LUMB', 'LINB', french_word)

    # EN -> AN
    french_word = re.sub(r'([^BCDFGHJKLMNPQRSTVWXZ])EN', r'\1AN', french_word)
    french_word = re.sub(r'([VTLJMRPDSBFKNG])EN([BRCTDKZSVN])', r'\1AN\2', french_word)
    french_word = re.sub(r'([VTLJMRPDSBFKNG])EN([BRCTDKZSVN])', r'\1AN\2', french_word)
    french_word = re.sub(r'^EN([BCDFGHJKLNPQRSTVXZ]|CH|IV|ORG|OB|UI|UA|UY)', r'AN\1', french_word)
    french_word = re.sub(r'(^[JRVTH])EN([DRTFGSVJMP])', r'\1AN\2', french_word)
    french_word = re.sub(r'SEN([ST])', r'SAN\1', french_word)
    french_word = re.sub(r'^DESENIV', 'DESANIV', french_word)
    french_word = re.sub(r'([^M])EN(UI)', r'\1AN\2', french_word)
    french_word = re.sub(r'(.+[JTVLFMRPSBD])EN([JLFDSTG])', r'\1AN\2', french_word)

    # EI -> AI
    french_word = re.sub(r'([VSBSTNRLPM])E[IY]([ACDFRJLGZ])', r'\1AI\2', french_word)

    # Histoire d'Ô
    conv_nas_in = ['EAU', 'EU', 'Y', 'EOI', 'JEA', 'OIEM', 'OUANJ', 'OUA', 'OUENJ']
    con_nas_out = ['O', 'E', 'I', 'OI', 'JA', 'OIM', 'OUENJ', 'OI', 'OUANJ']
    for conv_in, conv_out in zip(conv_nas_in, con_nas_out):
        french_word = french_word.replace(conv_in, conv_out)

    # AU without a following E
    french_word = re.sub(r'AU([^E])', r'O\1', french_word)

    # Les retouches!
    # Retouche BENJ -> BINJ
    french_word = re.sub(r'^BENJ', 'BINJ', french_word)
    # Retouche RTIEL -> RSIEL
    french_word = re.sub(r'RTIEL', 'RSIEL', french_word)
    # Retouche PINK -> PONK
    french_word = re.sub(r'PINK', 'PONK', french_word)
    # Retouche KIND -> KOND
    french_word = re.sub(r'KIND', 'KOND', french_word)
    # Retouche KUMN KUMP
    french_word = re.sub(r'KUM(N|P)', r'KON\1', french_word)
    # Retouche LKOU -> LKO
    french_word = re.sub(r'LKOU', 'LKO', french_word)
    # Retouche EDBE pied-bœuf
    french_word = re.sub(r'EDBE', 'EBE', french_word)
    # Retouche SCH -> CH
    french_word = re.sub(r'ARCM', 'ARKM', french_word)
    # Retouche SCH -> CH
    french_word = re.sub(r'SCH', 'CH', french_word)
    # Retouche début OINI -> ONI
    french_word = re.sub(r'^OINI', 'ONI', french_word)
    # Retouche APT -> AT
    french_word = re.sub(r'([^NDCGRHKO])APT', r'\1AT', french_word)
    # Retouche LPT -> LT
    french_word = re.sub(r'([L]|KON)PT', r'\1T', french_word)
    # Retouche OTB -> OB (hautbois)
    french_word = re.sub(r'OTB', 'OB', french_word)
    # Retouche IXA -> ISA
    french_word = re.sub(r'IXA', 'ISA', french_word)
    # Retouche TG -> G
    french_word = re.sub(r'TG', 'G', french_word)
    # Retouche début TZ -> TS
    french_word = re.sub(r'^TZ', 'TS', french_word)
    # Retouche PTIE -> TIE
    french_word = re.sub(r'PTIE', 'TIE', french_word)
    # Retouche GT -> T
    french_word = re.sub(r'GT', 'T', french_word)
    # Retouche tranquillement
    french_word = french_word.replace("ANKIEM", "ANKILEM")
    # Retouche KEMAN -> KAMAN
    french_word = re.sub(r'(LO|RE)KEMAN', r'\1KAMAN', french_word)
    # Retouche TB -> B  TM -> M
    french_word = re.sub(r'NT(B|M)', r'N\1', french_word)
    # Retouche GS -> SU
    french_word = re.sub(r'GSU', 'SU', french_word)
    # Retouche ESD -> ED
    french_word = re.sub(r'ESD', 'ED', french_word)
    # Retouche LESQUEL -> LEKEL
    french_word = re.sub(r'LESKEL', 'LEKEL', french_word)
    # Retouche CK -> K
    french_word = re.sub(r'CK', 'K', french_word)

    # Terminaisons
    # Terminaisons USIL -> USI
    french_word = re.sub(r'USIL$', 'USI', french_word)
    # Terminaisons TS DS LS X T D S...  v2.0
    french_word = re.sub(r'X$|[TD]S$|[DS]$', '', french_word)
    # Sauf KT LT terminal
    french_word = re.sub(r'([^KL]+)T$', r'\1', french_word)
    # H pseudo muet en début de mot
    french_word = re.sub(r'^[H]', '', french_word)

    # On sauve le code (utilisé pour les mots très courts)
    saved_word2 = french_word

    # Terminaisons TIL -> TI
    french_word = re.sub(r'TIL$', 'TI', french_word)
    # Terminaisons LC -> LK
    french_word = re.sub(r'LC$', 'LK', french_word)
    # Terminaisons LE LES -> L
    french_word = re.sub(r'L[E]?[S]?$', 'L', french_word)
    # Terminaisons NE NES -> N
    french_word = re.sub(r'(.+)N[E]?[S]?$', r'\1N', french_word)
    # Terminaisons EZ -> E
    french_word = re.sub(r'EZ$', 'E', french_word)
    # Terminaisons OIG -> OI
    french_word = re.sub(r'OIG$', 'OI', french_word)
    # Terminaisons OUP -> OU
    french_word = re.sub(r'OUP$', 'OU', french_word)
    # Terminaisons OM -> ON sauf ROM
    french_word = re.sub(r'([^R])OM$', r'\1ON', french_word)
    # Terminaisons LOP -> LO
    french_word = re.sub(r'LOP$', 'LO', french_word)
    # Terminaisons NTANP -> NTAN
    french_word = re.sub(r'NTANP$', 'NTAN', french_word)
    # Terminaisons TUN -> TIN
    french_word = re.sub(r'TUN$', 'TIN', french_word)
    # Terminaisons AU -> O
    french_word = re.sub(r'AU$', 'O', french_word)
    # Terminaisons EI -> AI
    french_word = re.sub(r'EI$', 'AI', french_word)
    # Terminaisons RD RG -> R
    french_word = re.sub(r'R[DG]$', 'R', french_word)
    # Terminaisons ANC -> AN
    french_word = re.sub(r'ANC$', 'AN', french_word)
    # Terminaisons C muet de CROC, ESCROC
    french_word = re.sub(r'KROC$', 'KRO', french_word)
    # Terminaisons C muet de CAOUTCHOUC
    french_word = re.sub(r'HOUC$', 'HOU', french_word)
    # Terminaisons C muet de ESTOMAC (mais pas HAMAC)
    french_word = re.sub(r'OMAC$', 'OMA', french_word)
    # Terminaisons C et G muet de OUC ONC OUG
    french_word = re.sub(r'([J])O([NU])[CG]$', r'\1O\2', french_word)
    # Terminaisons G muet ANG ONG sauf GANG GONG TANG TONG
    french_word = re.sub(r'([^GTR])([AO])NG$', r'\1\2N', french_word)
    # Terminaisons UC -> UK
    french_word = re.sub(r'UC$', 'UK', french_word)
    # Terminaisons AING -> IN
    french_word = re.sub(r'AING$', 'IN', french_word)
    # Terminaisons C -> K
    french_word = re.sub(r'([EISOARN])C$', r'\1K', french_word)
    # Terminaisons E ou H sauf pour C et N
    french_word = re.sub(r'([ABD-MO-Z]+)[EH]+$', r'\1', french_word)
    # Terminaisons EN -> AN (difficile à faire avant sans avoir des soucis)
    french_word = re.sub(r'EN$', 'AN', french_word)
    # Terminaisons EN -> AN
    french_word = re.sub(r'(NJ)EN$', r'\1AN', french_word)
    # PAIE -> PAI
    french_word = re.sub(r'^PAIEM', 'PAIM', french_word)
    # F muet en fin de mot
    french_word = re.sub(r'([^NTB])EF$', r'\1', french_word)

    # Suppression des répétitions (suite à certains remplacements)
    french_word = re.sub(r'(.)\1', r'\1', french_word)

    # Cas particuliers, bah au final, je n'en ai qu'un ici
    conv_part_in = ['FUEL']
    conv_part_out = ['FIOUL']
    for conv_in, conv_out in zip(conv_part_in, conv_part_out):
        french_word = french_word.replace(conv_in, conv_out)

    # Ce sera le seul code retourné à une seule lettre!
    if french_word == 'O':
        return french_word

    # seconde chance sur les mots courts qui ont souffert de la simplification
    if len(french_word) < 2:
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

    elif len(french_word) > 1:
        return french_word[:16]  # Je limite à 16 caractères mais vous faites comme vous voulez!

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
    