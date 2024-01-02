import re


#
#	SOUNDEX FR 
#	Édouard BERGÉ © 12.2007 v1.2
#   Ported to Python by Gaspard PETIT
#	MIT licence
#

def phonetic(sIn):
    accents = {'É': 'E', 'È': 'E', 'Ë': 'E', 'Ê': 'E', 'Á': 'A', 'À': 'A', 'Ä': 'A', 'Â': 'A',
               'Å': 'A', 'Ã': 'A', 'Æ': 'E', 'Ï': 'I', 'Î': 'I', 'Ì': 'I', 'Í': 'I',
               'Ô': 'O', 'Ö': 'O', 'Ò': 'O', 'Ó': 'O', 'Õ': 'O', 'Ø': 'O', 'Œ': 'OEU',
               'Ú': 'U', 'Ù': 'U', 'Û': 'U', 'Ü': 'U', 'Ñ': 'N', 'Ç': 'S', '¿': 'E'}
    min2maj = {'é': 'É', 'è': 'È', 'ë': 'Ë', 'ê': 'Ê', 'á': 'Á', 'â': 'Â', 'à': 'À', 'Ä': 'A',
               'Â': 'A', 'å': 'Å', 'ã': 'Ã', 'æ': 'Æ', 'ï': 'Ï', 'î': 'Î', 'ì': 'Ì', 'í': 'Í',
               'ô': 'Ô', 'ö': 'Ö', 'ò': 'Ò', 'ó': 'Ó', 'õ': 'Õ', 'ø': 'Ø', 'œ': 'Œ',
               'ú': 'Ú', 'ù': 'Ù', 'û': 'Û', 'ü': 'Ü', 'ç': 'Ç', 'ñ': 'Ñ', 'ß': 'S'}

    sIn = sIn.translate(str.maketrans(min2maj))  # minuscules accentuées ou composées en majuscules simples
    sIn = sIn.translate(str.maketrans(accents))  # majuscules accentuées ou composées en majuscules simples
    sIn = sIn.upper()  # on passe tout le reste en majuscules
    sIn = ''.join(char for char in sIn if char.isalpha())  # on garde uniquement les lettres de A à Z

    sBack = sIn  # on sauve le code (utilisé pour les mots très courts)

    sIn = re.sub(r'O[O]+', 'OU', sIn)  # pré traitement: OO... -> OU
    sIn = re.sub(r'SAOU', 'SOU', sIn)  # pré traitement: SAOU -> SOU
    sIn = re.sub(r'OES', 'OS', sIn)  # pré traitement: OES -> OS
    sIn = re.sub(r'CCH', 'K', sIn)  # pré traitement: CCH -> K
    sIn = re.sub(r'CC([IYE])', r'KS\1', sIn)  # pré traitement: CCI CCY CCE
    sIn = re.sub(r'(.)\1', r'\1', sIn)  # supression des répétitions

    # quelques cas particuliers
    if sIn == "CD":
        return sIn

    if sIn == "BD":
        return sIn

    if sIn == "BV":
        return sIn

    if sIn == "TABAC":
        return "TABA"

    if sIn == "FEU":
        return "FE"

    if sIn == "FE":
        return sIn

    if sIn == "FER":
        return sIn

    if sIn == "FIEF":
        return sIn

    if sIn == "FJORD":
        return sIn

    if sIn == "GOAL":
        return "GOL"

    if sIn == "FLEAU":
        return "FLEO"

    if sIn == "HIER":
        return "IER"

    if sIn == "HEU":
        return "E"

    if sIn == "HE":
        return "E"

    if sIn == "OS":
        return sIn

    if sIn == "RIZ":
        return "RI"

    if sIn == "RAZ":
        return "RA"

    # pré-traitements
    sIn = re.sub(r'OIN[GT]$', 'OIN', sIn)  # Terminations OING -> OIN
    sIn = re.sub(r'E[RS]$', 'E', sIn)  # Remove infinitive and plural participle endings
    sIn = re.sub(r'(C|CH)OEU', 'KE', sIn)  # pré traitement OEU -> EU
    sIn = re.sub(r'MOEU', 'ME', sIn)  # pré traitement OEU -> EU
    sIn = re.sub(r'OE([UI]+)([BCDFGHJKLMNPQRSTVWXZ])', r'E\1\2', sIn)  # pré traitement OEU OEI -> E
    sIn = re.sub(r'^GEN[TS]$', 'JAN', sIn)  # pré traitement GEN -> JAN
    sIn = re.sub(r'CUEI', 'KEI', sIn)  # pré traitement accueil
    sIn = re.sub(r'([^AEIOUYC])AE([BCDFGHJKLMNPQRSTVWXZ])', r'\1E\2', sIn)  # pré traitement AE -> E
    sIn = re.sub(r'AE([QS])', r'E\1', sIn)  # pré traitement AE -> E
    sIn = re.sub(r'AIE([BCDFGJKLMNPQRSTVWXZ])', r'AI\1', sIn)  # pré traitement AIE(consonne) -> AI
    sIn = re.sub(r'ANIEM', 'ANIM', sIn)  # pré traitement NIEM -> NIM
    sIn = re.sub(r'(DRA|TRO|IRO)P$', r'\1', sIn)  # P terminal muet
    sIn = re.sub(r'(LOM)B$', r'\1', sIn)  # B terminal muet
    sIn = re.sub(r'(RON|POR)C$', r'\1', sIn)  # C terminal muet
    sIn = re.sub(r'PECT$', 'PET', sIn)  # C terminal muet
    sIn = re.sub(r'ECUL$', 'CU', sIn)  # L terminal muet
    sIn = re.sub(r'(CHA|CA|E)M(P|PS)$', r'\1N', sIn)  # P or PS terminal muet
    sIn = re.sub(r'(TAN|RAN)G$', r'\1', sIn)  # G terminal muet

    # sons YEUX
    sIn = re.sub(r'([^VO])ILAG', r'\1IAJ', sIn)
    sIn = re.sub(r'([^TRH])UIL(AR|E)(.+)', r'\1UI\2\3', sIn)
    sIn = re.sub(r'([G])UIL([AEO])', r'\1UI\2', sIn)
    sIn = re.sub(r'([NSPM])AIL([AEO])', r'\1AI\2', sIn)

    convMIn = ["DILAI", "DILON", "DILER", "DILEM", "RILON", "TAILE", "GAILET", "AILAI", "AILAR",
               "OUILA", "EILAI", "EILAR", "EILER", "EILEM", "REILET", "EILET", "AILOL"]
    convMOut = ["DIAI", "DION", "DIER", "DIEM", "RION", "TAIE", "GAIET", "AIAI", "AIAR",
                "OUIA", "AIAI", "AIAR", "AIER", "AIEM", "RAIET", "EIET", "AIOL"]
    for convIn, convOut in zip(convMIn, convMOut):
        sIn = sIn.replace(convIn, convOut)

    sIn = re.sub(r'([^AEIOUY])(SC|S)IEM([EA])', r'\1\2IAM\3', sIn)  # IEM -> IAM
    sIn = re.sub(r'^(SC|S)IEM([EA])', r'\1IAM\2', sIn)  # IEM -> IAM

    # MP MB -> NP NB
    convMIn = ['OMB', 'AMB', 'OMP', 'AMP', 'IMB', 'EMP', 'GEMB', 'EMB', 'UMBL', 'CIEN']
    convMOut = ['ONB', 'ANB', 'ONP', 'ANP', 'INB', 'ANP', 'JANB', 'ANB', 'INBL', 'SIAN']

    for convIn, convOut in zip(convMIn, convMOut):
        sIn = sIn.replace(convIn, convOut)

    # Sons en K
    sIn = re.sub(r'^ECHO$', 'EKO', sIn)  # cas particulier: écho
    sIn = re.sub(r'^ECEUR', 'EKEUR', sIn)  # cas particulier: écœuré

    # Choléra Chœur mais pas chocolat!
    sIn = re.sub(r'^CH(OG+|OL+|OR+|EU+|ARIS|M+|IRO|ONDR)', r'K\1', sIn)  # En début de mot
    sIn = re.sub(r'(YN|RI)CH(OG+|OL+|OC+|OP+|OM+|ARIS|M+|IRO|ONDR)', r'\1K\2', sIn)  # Ou devant une consonne
    sIn = re.sub(r'CHS', 'CH', sIn)
    sIn = re.sub(r'CH(AIQ)', r'K\1', sIn)
    sIn = re.sub(r'^ECHO([^UIPY])', r'EKO\1', sIn)
    sIn = re.sub(r'ISCH(I|E)', r'ISK\1', sIn)
    sIn = re.sub(r'^ICHT', 'IKT', sIn)
    sIn = re.sub(r'ORCHID', 'ORKID', sIn)
    sIn = re.sub(r'ONCHIO', 'ONKIO', sIn)
    sIn = re.sub(r'ACHIA', 'AKIA', sIn)  # retouche ACHIA -> AKIA
    sIn = re.sub(r'([^C])ANICH', r'\1ANIK', sIn)  # ANICH -> ANIK  1/2
    sIn = re.sub(r'OMANIK', 'OMANICH', sIn)  # cas particulier  2/2
    sIn = re.sub(r'ACHY([^D])', r'AKI\1', sIn)
    sIn = re.sub(r'([AEIOU])C([BDFGJKLMNPQRTVWXZ])', r'\1K\2', sIn)  # voyelle, C, consonne sauf H

    convPrIn = ['EUCHA', 'YCHIA', 'YCHA', 'YCHO', 'YCHED', 'ACHEO', 'RCHEO', 'RCHES',
                'ECHN', 'OCHTO', 'CHORA', 'CHONDR', 'CHORE', 'MACHM', 'BRONCHO', 'LICHOS', 'LICHOC']
    convPrOut = ['EKA', 'IKIA', 'IKA', 'IKO', 'IKED', 'AKEO', 'RKEO', 'RKES',
                 'EKN', 'OKTO', 'KORA', 'KONDR', 'KORE', 'MAKM', 'BRONKO', 'LIKOS', 'LIKOC']

    for convIn, convOut in zip(convPrIn, convPrOut):
        sIn = sIn.replace(convIn, convOut)

    # Weuh (perfectible)
    convPrIn = ['WA', 'WO', 'WI', 'WHI', 'WHY', 'WHA', 'WHO']
    convPrOut = ['OI', 'O', 'OUI', 'OUI', 'OUI', 'OUA', 'OU']

    for convIn, convOut in zip(convPrIn, convPrOut):
        sIn = sIn.replace(convIn, convOut)

    # Gueu, Gneu, Jeu et quelques autres
    convPrIn = ['GNES', 'GNET', 'GNER', 'GNE', 'GI', 'GNI', 'GNA', 'GNOU', 'GNUR', 'GY', 'OUGAIN',
                'AGEOL', 'AGEOT', 'GEOLO', 'GEOM', 'GEOP', 'GEOG', 'GEOS', 'GEORG', 'GEOR', 'NGEOT',
                'UGEOT', 'GEOT', 'GEOD', 'GEOC', 'GEO', 'GEA', 'GE', 'QU', 'Q', 'CY', 'CI', 'CN',
                'ICM', 'CEAT', 'CE', 'CR', 'CO', 'CUEI', 'CU', 'VENCA', 'CA', 'CS', 'CLEN', 'CL',
                'CZ', 'CTIQ', 'CTIF', 'CTIC', 'CTIS', 'CTIL', 'CTIO', 'CTI', 'CTU', 'CTE', 'CTO',
                'CTR', 'CT', 'PH', 'TH', 'OW', 'LH', 'RDL', 'CHLO', 'CHR', 'PTIA']

    convPrOut = ['NIES', 'NIET', 'NIER', 'NE', 'JI', 'NI', 'NIA', 'NIOU', 'NIUR', 'JI', 'OUGIN',
                 'AJOL', 'AJOT', 'JEOLO', 'JEOM', 'JEOP', 'JEOG', 'JEOS', 'JORJ', 'JEOR', 'NJOT',
                 'UJOT', 'JEOT', 'JEOD', 'JEOC', 'JO', 'JA', 'JE', 'K', 'K', 'SI', 'SI', 'KN',
                 'IKM', 'SAT', 'SE', 'KR', 'KO', 'KEI', 'KU', 'VANSA', 'KA', 'KS', 'KLAN', 'KL',
                 'KZ', 'KTIK', 'KTIF', 'KTIS', 'KTIS', 'KTIL', 'KSIO', 'KTI', 'KTU', 'KTE', 'KTO',
                 'KTR', 'KT', 'F', 'T', 'OU', 'L', 'RL', 'KLO', 'KR', 'PSIA']

    for convIn, convOut in zip(convPrIn, convPrOut):
        sIn = sIn.replace(convIn, convOut)

    sIn = re.sub(r'GU([^RLMBSTPZN])', r'G\1', sIn)  # Gueu!
    sIn = re.sub(r'GNO([MLTNRKG])', r'NIO\1', sIn)  # GNO ! Tout sauf S pour gnos
    sIn = re.sub(r'GNO([MLTNRKG])', r'NIO\1',
                 sIn)  # bis -> gnognotte! Si quelqu'un sait le faire en une seule regexp...

    # TI -> SI v2.0
    convPrIn = ['BUTIE', 'BUTIA', 'BATIA', 'ANTIEL', 'RETION', 'ENTIEL', 'ENTIAL', 'ENTIO', 'ENTIAI', 'UJETION',
                'ATIEM',
                'PETIEN', 'CETIE', 'OFETIE', 'IPETI', 'LBUTION', 'BLUTION', 'LETION', 'LATION', 'SATIET']
    convPrOut = ['BUSIE', 'BUSIA', 'BASIA', 'ANSIEL', 'RESION', 'ENSIEL', 'ENSIAL', 'ENSIO', 'ENSIAI', 'UJESION',
                 'ASIAM',
                 'PESIEN', 'CESIE', 'OFESIE', 'IPESI', 'LBUSION', 'BLUSION', 'LESION', 'LASION', 'SASIET']

    for convIn, convOut in zip(convPrIn, convPrOut):
        sIn = sIn.replace(convIn, convOut)

    sIn = re.sub(r'(.+)ANTI(AL|O)', r'\1ANSI\2', sIn)  # sauf antialcoolique, antialbumine, antialarmer, ...
    sIn = re.sub(r'(.+)INUTI([^V])', r'\1INUSI\2', sIn)  # sauf inutilité, inutilement, diminutive, ...
    sIn = re.sub(r'([^O])UTIEN', r'\1USIEN', sIn)  # sauf soutien, ...

    sIn = re.sub(r'([^DE])RATI[E]$', r'\1RASI', sIn)  # sauf xxxxxcratique, ...

    # TIEN TION -> SIEN SION v3.1
    sIn = re.sub(r'([^SNEU]|KU|KO|RU|LU|BU|TU|AU)T(IEN|ION)', r'\1S\2', sIn)

    # H muet
    sIn = re.sub(r'([^CS])H', r'\1', sIn)  # H muet
    sIn = sIn.replace("ESH", "ES")  # H muet
    sIn = sIn.replace("NSH", "NS")  # H muet
    sIn = sIn.replace("SH", "CH")  # ou pas!

    # NASALES
    convNasIn = ['OMT', 'IMB', 'IMP', 'UMD', 'TIENT', 'RIENT', 'DIENT', 'IEN', 'YMU', 'YMO', 'YMA', 'YME', 'YMI', 'YMN',
                 'YM',
                 'AHO', 'FAIM', 'DAIM', 'SAIM', 'EIN', 'AINS']
    convNasOut = ['ONT', 'INB', 'INP', 'OND', 'TIANT', 'RIANT', 'DIANT', 'IN', 'IMU', 'IMO', 'IMA', 'IME', 'IMI', 'IMN',
                  'IN',
                  'AO', 'FIN', 'DIN', 'SIN', 'AIN', 'INS']
    for convIn, convOut in zip(convNasIn, convNasOut):
        sIn = sIn.replace(convIn, convOut)

    # AIN -> IN v2.0
    sIn = re.sub(r'AIN$', 'IN', sIn)
    sIn = re.sub(r'AIN([BTDK])', r'IN\1', sIn)

    # UN -> IN
    sIn = re.sub(r'([^O])UND', r'\1IND', sIn)
    sIn = re.sub(r'([JTVLFMRPSBD])UN([^IAE])', r'\1IN\2', sIn)
    sIn = re.sub(r'([JTVLFMRPSBD])UN$', r'\1IN', sIn)
    sIn = re.sub(r'RFUM$', 'RFIN', sIn)
    sIn = re.sub(r'LUMB', 'LINB', sIn)

    # EN -> AN
    sIn = re.sub(r'([^BCDFGHJKLMNPQRSTVWXZ])EN', r'\1AN', sIn)
    sIn = re.sub(r'([VTLJMRPDSBFKNG])EN([BRCTDKZSVN])', r'\1AN\2', sIn)
    sIn = re.sub(r'([VTLJMRPDSBFKNG])EN([BRCTDKZSVN])', r'\1AN\2', sIn)
    sIn = re.sub(r'^EN([BCDFGHJKLNPQRSTVXZ]|CH|IV|ORG|OB|UI|UA|UY)', r'AN\1', sIn)
    sIn = re.sub(r'(^[JRVTH])EN([DRTFGSVJMP])', r'\1AN\2', sIn)
    sIn = re.sub(r'SEN([ST])', r'SAN\1', sIn)
    sIn = re.sub(r'^DESENIV', 'DESANIV', sIn)
    sIn = re.sub(r'([^M])EN(UI)', r'\1AN\2', sIn)
    sIn = re.sub(r'(.+[JTVLFMRPSBD])EN([JLFDSTG])', r'\1AN\2', sIn)

    # EI -> AI
    sIn = re.sub(r'([VSBSTNRLPM])E[IY]([ACDFRJLGZ])', r'\1AI\2', sIn)

    # Histoire d'Ô
    convNasIn = ['EAU', 'EU', 'Y', 'EOI', 'JEA', 'OIEM', 'OUANJ', 'OUA', 'OUENJ']
    convNasOut = ['O', 'E', 'I', 'OI', 'JA', 'OIM', 'OUENJ', 'OI', 'OUANJ']
    for convIn, convOut in zip(convNasIn, convNasOut):
        sIn = sIn.replace(convIn, convOut)

    sIn = re.sub(r'AU([^E])', r'O\1', sIn)  # AU without a following E

    # Les retouches!
    sIn = re.sub(r'^BENJ', 'BINJ', sIn)  # Retouche BENJ -> BINJ
    sIn = re.sub(r'RTIEL', 'RSIEL', sIn)  # Retouche RTIEL -> RSIEL
    sIn = re.sub(r'PINK', 'PONK', sIn)  # Retouche PINK -> PONK
    sIn = re.sub(r'KIND', 'KOND', sIn)  # Retouche KIND -> KOND
    sIn = re.sub(r'KUM(N|P)', r'KON\1', sIn)  # Retouche KUMN KUMP
    sIn = re.sub(r'LKOU', 'LKO', sIn)  # Retouche LKOU -> LKO
    sIn = re.sub(r'EDBE', 'EBE', sIn)  # Retouche EDBE pied-bœuf
    sIn = re.sub(r'ARCM', 'ARKM', sIn)  # Retouche SCH -> CH
    sIn = re.sub(r'SCH', 'CH', sIn)  # Retouche SCH -> CH
    sIn = re.sub(r'^OINI', 'ONI', sIn)  # Retouche début OINI -> ONI
    sIn = re.sub(r'([^NDCGRHKO])APT', r'\1AT', sIn)  # Retouche APT -> AT
    sIn = re.sub(r'([L]|KON)PT', r'\1T', sIn)  # Retouche LPT -> LT
    sIn = re.sub(r'OTB', 'OB', sIn)  # Retouche OTB -> OB (hautbois)
    sIn = re.sub(r'IXA', 'ISA', sIn)  # Retouche IXA -> ISA
    sIn = re.sub(r'TG', 'G', sIn)  # Retouche TG -> G
    sIn = re.sub(r'^TZ', 'TS', sIn)  # Retouche début TZ -> TS
    sIn = re.sub(r'PTIE', 'TIE', sIn)  # Retouche PTIE -> TIE
    sIn = re.sub(r'GT', 'T', sIn)  # Retouche GT -> T
    sIn = sIn.replace("ANKIEM", "ANKILEM")  # Retouche tranquillement
    sIn = re.sub(r'(LO|RE)KEMAN', r'\1KAMAN', sIn)  # Retouche KEMAN -> KAMAN
    sIn = re.sub(r'NT(B|M)', r'N\1', sIn)  # Retouche TB -> B  TM -> M
    sIn = re.sub(r'GSU', 'SU', sIn)  # Retouche GS -> SU
    sIn = re.sub(r'ESD', 'ED', sIn)  # Retouche ESD -> ED 
    sIn = re.sub(r'LESKEL', 'LEKEL', sIn)  # Retouche LESQUEL -> LEKEL
    sIn = re.sub(r'CK', 'K', sIn)  # Retouche CK -> K

    # Terminaisons
    sIn = re.sub(r'USIL$', 'USI', sIn)  # Terminaisons USIL -> USI
    sIn = re.sub(r'X$|[TD]S$|[DS]$', '', sIn)  # Terminaisons TS DS LS X T D S...  v2.0
    sIn = re.sub(r'([^KL]+)T$', r'\1', sIn)  # Sauf KT LT terminal
    sIn = re.sub(r'^[H]', '', sIn)  # H pseudo muet en début de mot

    sBack2 = sIn  # On sauve le code (utilisé pour les mots très courts)

    sIn = re.sub(r'TIL$', 'TI', sIn)  # Terminaisons TIL -> TI
    sIn = re.sub(r'LC$', 'LK', sIn)  # Terminaisons LC -> LK
    sIn = re.sub(r'L[E]?[S]?$', 'L', sIn)  # Terminaisons LE LES -> L
    sIn = re.sub(r'(.+)N[E]?[S]?$', r'\1N', sIn)  # Terminaisons NE NES -> N
    sIn = re.sub(r'EZ$', 'E', sIn)  # Terminaisons EZ -> E
    sIn = re.sub(r'OIG$', 'OI', sIn)  # Terminaisons OIG -> OI
    sIn = re.sub(r'OUP$', 'OU', sIn)  # Terminaisons OUP -> OU
    sIn = re.sub(r'([^R])OM$', r'\1ON', sIn)  # Terminaisons OM -> ON sauf ROM
    sIn = re.sub(r'LOP$', 'LO', sIn)  # Terminaisons LOP -> LO
    sIn = re.sub(r'NTANP$', 'NTAN', sIn)  # Terminaisons NTANP -> NTAN
    sIn = re.sub(r'TUN$', 'TIN', sIn)  # Terminaisons TUN -> TIN
    sIn = re.sub(r'AU$', 'O', sIn)  # Terminaisons AU -> O
    sIn = re.sub(r'EI$', 'AI', sIn)  # Terminaisons EI -> AI
    sIn = re.sub(r'R[DG]$', 'R', sIn)  # Terminaisons RD RG -> R
    sIn = re.sub(r'ANC$', 'AN', sIn)  # Terminaisons ANC -> AN
    sIn = re.sub(r'KROC$', 'KRO', sIn)  # Terminaisons C muet de CROC, ESCROC
    sIn = re.sub(r'HOUC$', 'HOU', sIn)  # Terminaisons C muet de CAOUTCHOUC
    sIn = re.sub(r'OMAC$', 'OMA', sIn)  # Terminaisons C muet de ESTOMAC (mais pas HAMAC)
    sIn = re.sub(r'([J])O([NU])[CG]$', r'\1O\2', sIn)  # Terminaisons C et G muet de OUC ONC OUG
    sIn = re.sub(r'([^GTR])([AO])NG$', r'\1\2N', sIn)  # Terminaisons G muet ANG ONG sauf GANG GONG TANG TONG
    sIn = re.sub(r'UC$', 'UK', sIn)  # Terminaisons UC -> UK
    sIn = re.sub(r'AING$', 'IN', sIn)  # Terminaisons AING -> IN
    sIn = re.sub(r'([EISOARN])C$', r'\1K', sIn)  # Terminaisons C -> K
    sIn = re.sub(r'([ABD-MO-Z]+)[EH]+$', r'\1', sIn)  # Terminaisons E ou H sauf pour C et N
    sIn = re.sub(r'EN$', 'AN', sIn)  # Terminaisons EN -> AN (difficile à faire avant sans avoir des soucis)
    sIn = re.sub(r'(NJ)EN$', r'\1AN', sIn)  # Terminaisons EN -> AN
    sIn = re.sub(r'^PAIEM', 'PAIM', sIn)  # PAIE -> PAI
    sIn = re.sub(r'([^NTB])EF$', r'\1', sIn)  # F muet en fin de mot

    sIn = re.sub(r'(.)\1', r'\1', sIn)  # Suppression des répétitions (suite à certains remplacements)

    # Cas particuliers, bah au final, je n'en ai qu'un ici
    convPartIn = ['FUEL']
    convPartOut = ['FIOUL']
    for i in range(len(convPartIn)):
        sIn = sIn.replace(convPartIn[i], convPartOut[i])

    # Ce sera le seul code retourné à une seule lettre!
    if sIn == 'O':
        return sIn

    # seconde chance sur les mots courts qui ont souffert de la simplification
    if len(sIn) < 2:
        # Sigles ou abréviations
        if bool(re.match(
                "[BCDFGHJKLMNPQRSTVWXYZ][BCDFGHJKLMNPQRSTVWXYZ][BCDFGHJKLMNPQRSTVWXYZ][BCDFGHJKLMNPQRSTVWXYZ]*",
                sBack)):
            return sBack

        if bool(re.match("[RFMLVSPJDF][AEIOU]", sBack)):
            if len(sBack) == 3:
                return sBack[:2]  # mots de trois lettres supposés simples
            if len(sBack) == 4:
                return sBack[:3]  # mots de quatre lettres supposés simples

        if len(sBack2) > 1:
            return sBack2

    if len(sIn) > 1:
        return sIn[:16]  # Je limite à 16 caractères mais vous faites comme vous voulez!
    else:
        return ''


if __name__ == '__main__':
    example = "Python"
    result = phonetic(example)
    print(f"{example} -> {result}")
    print(phonetic("Gilles") == phonetic("Jill"))

