urls = [
    # {
    #     # ------------------------------FRIUTS------------------------------
    #     "url": 'https://shop.hazi-hinam.co.il/#/catalog?viewMode=category_targeting&categoryId=45&subCategoryId=10886',
    #     "itemsToScrape": {
    #         "1": "בננה",                 # banana
    #         "2": "קלמנטינה",            # clementine
    #         "3": "תפוז",                # orange
    #         "4": "תפוח עץ סמיט",       # green apple
    #         "5": "לימון",              # lemon
    #         "6": "מלון",               # melon
    #         "7": "אשכולית אדומה",     # red_grapefruit
    #         "8": "אבוקדו",            # avocado
    #         "9": "פומלית",            # pomelo
    #         "10": "קיווי",         # kiwi
    #     },
    # },
    # {
    #     # ------------------------------VEGG------------------------------------
    #     "url": "https://shop.hazi-hinam.co.il/#/catalog?viewMode=category_targeting&categoryId=45&subCategoryId=10883",
    #     "itemsToScrape": {
    #         "11": "עגבניה",                    # tomato
    #         "12": "בצל יבש",                   # onion
    #         "13": "פלפל אדום",               # gamba
    #         "14": "מלפפון",                   # cucumber
    #         "15": "קישוא",                  # green_zucchini
    #         "16": "שומר",                    # cabbage
    #         "17": "פלפל חריף ירוק",        # green_hot_pepper
    #         "18": "קולורבי",               # kohlrabi
    #         "19": "חציל",                   # eggplant
    #         "20": "צנונית בתפזורת",                   # radish
    #     },
    # },
    # # ------------------------------SNACKS------------------------------
    # {
    #     "url": 'https://shop.hazi-hinam.co.il/#/catalog?viewMode=category_targeting&categoryId=66&subCategoryId=11208',
    #     "itemsToScrape": {
    #         "21": "דובונים חטיף תפוח אדמה",  # dubonim 40 g
    #         "22": "ביסלי בטעם גריל",  # bilslyGril 60 g
    #         "23": "במבה",  # bambaOsem 80 g
    #         "24": "אפרופו חטיף תירס קלאסי",  # apropoOsem 100 g
    #         "25": "חטיף פוף טבעות קלאסי",  # poof 40 g
    #         "26": "ארנבונים חטיף תפוח אדמה",  # bunnies 40 g
    #         "27": "כיפלי בטעם גריל",  # kifly 80 g
    #         "28": "דוריטוס בטעם טבעי",  # doritos 70 g
    #         "29": "אובלטים מלוחים דקיקים מלוח",  # ovlets 300 g
    #         "30": "פופקורן להכנה במיקרוגל בטעם טבעי 6 שקיות",  # hotpop popcorn 6*100 g
    #     },
    # },
    # # ------------------------------SWEET------------------------------
    # {
    #     "url": 'https://shop.hazi-hinam.co.il/#/catalog?viewMode=category_targeting&categoryId=66&subCategoryId=10843',
    #     "itemsToScrape": {
    #         "31": "קליק ביסקוויט",  # click red 65 g
    #         "32": "טעמי חטיף במילוי קרם נוגט וקרמל",  # teami 40 g
    #         "33": "כיף כף מקלות אגוזים",  # kifkef nuts 40 g
    #         "34": "מארז 5 חטיפי באונטי",  # bounty 5 units
    #         "35": "מיקס חטיפי מיני בואנו",  # pack of min bueno 200 g
    #         "36": "כיף כף פצפצים בגביע",  # bkifkef gavia 135 g
    #         "37": "מטבעות שוקולד חלב",  # chocklate coins 36 g
    #         "38": "טורטית חטיף וופל מצופה",  # tortit 40 g
    #         "39": "שוקולד לבן ועוגיות",  # hershiz whita and cookies choc 40 g
    #         "40": "ביצת הפתעה",  # suprsie kiner
    #     },
    # },
    # # ------------------------------CHICKEN------------------------------
    # {
    #     "url": 'https://shop.hazi-hinam.co.il/#/catalog?viewMode=category_targeting&categoryId=46&subCategoryId=10888',
    #     "itemsToScrape": {
    #         "41": "עוף שלם טרי",  # Fresh whole chicken - by kg
    #         "42": "כבד עוף טרי",  # Fresh chicken liver - by kg
    #         "43": "כרעיים עוף טרי",  # Fresh chicken legs - by kg
    #         "44": "סטייק פרגיות טרי",  # Fresh chicken steak - by kg
    #         "45": "שוקיים עוף טרי",  # Fresh chicken shanks - by kg
    #     },
    # },
    # # ------------------------------Beef and lamb------------------------------
    # {
    #     "url": 'https://shop.hazi-hinam.co.il/#/catalog?viewMode=category_targeting&categoryId=46&subCategoryId=10890',
    #     "itemsToScrape": {
    #         "46": "אנטריקוט טרי",  # Fresh entrecote - by kg
    #         "47": "סינטה טרי",  # Fresh sinta - by kg
    #         "48": "אוסובוקו עגל טרי",  # Fresh veal ossobuco - by kg
    #         "49": "בקר טחון טרי",  # Freshly ground beef - by kg
    #         "50": "צלי כתף טרי",  # Fresh shoulder roast - by kg
    #     },
    # },
    # # ------------------------------FISHES------------------------------
    # {
    #     "url": 'https://shop.hazi-hinam.co.il/#/catalog?viewMode=category_targeting&categoryId=87&subCategoryId=11233',
    #     "itemsToScrape": {
    #         "51": "דג בורי טרי גדול",  # BURI FISH - by kg
    #         "52": "פילה סלמון שלם טרי",  # Fresh whole salmon fillet - by kg
    #         "53": "דג לברק טרי",  # Fresh lavrak - by kg
    #         "54": "דג לוקוס טרי",  # fresh lokus fish - by kg
    #         "55": "דג דניס טרי",  # Fresh Dennis fish - by kg
    #     },
    # },
    # # ------------------------------DAIRY------------------------------
    # {
    #     "url": 'https://shop.hazi-hinam.co.il/#/catalog?viewMode=category_targeting&categoryId=78&subCategoryId=11211',
    #     "itemsToScrape": {
    #         "56": "חלב עיזים",                      # goat milk - 1 liter
    #         "57": "משקה אייס קפה",                  # ice coffie drink - 1 liter
    #         "58": "משקה שוקו בבקבוק",               # shoko drink - 1 liter
    #     },
    # },
    # {
    #     "url": 'https://shop.hazi-hinam.co.il/#/catalog?viewMode=category_targeting&categoryId=78&subCategoryId=10864',
    #     "itemsToScrape": {
    #         # Pack of 8 pieces of Activia cream yogurt 1.5% fat
    #         "59": "מארז 8 יח' אקטיביה יוגורט קרמי 1.5% שומן",
    #         # 1 Yogurt with Gluten Free Chocolate Crackers 4.2%
    #         "60": "יוגורט עם פצפוצי שוקולד ללא גלוטן 4.2%",
    #         # Frilly yogurt with 1.5% strawberry - 500 grams
    #         "61": "יוגורט פרילי עם תות 1.5%",
    #     },
    # },
    # {
    #     "url": 'https://shop.hazi-hinam.co.il/#/catalog?viewMode=category_targeting&categoryId=78&subCategoryId=10865',
    #     "itemsToScrape": {
    #         # Cottage 5% mehadrin - 250 GRAMS
    #         "62": "קוטג' 5% מהדרין",
    #         # 5% white cheese - 250 grams
    #         "63": "גבינה לבנה 5%",
    #         # Napoleon natural cheese cream cheese 25% - 225 grams
    #         "64": "נפוליאון גבינת שמנת בטעם טבעי 25%",
    #         # 5% creamy cheese symphony - 200 grams
    #         "65": "סימפוניה גבינה במרקם שמנת 5%",
    #         # Labana cheese 5% - 250 grams
    #         "66": "גבינת לאבנה 5%",
    #     },
    # },
    # {
    #     "url": 'https://shop.hazi-hinam.co.il/#/catalog?viewMode=category_targeting&categoryId=78&subCategoryId=10866',
    #     "itemsToScrape": {
    #         # Camembert cheese - 200 GRAMS
    #         "67": "גבינת קממבר",
    #         # Roquefort cheese - 180 grams
    #         "68": "גבינת רוקפור",
    #         # Mozzarella - 100 grams
    #         "69": "מוצרלה פרסקה 18% שומן",
    #         # Berry cheese - 125 grams
    #         "70": "גבינת ברי",
    #         # Dreamy cheese 25% fat - 200 grams
    #         "71": "גבינה חלומי  25% שומן",
    #         # Bulgarian cheese 16% - 250 grams
    #         "72": "גבינה בולגרית 16%",
    #         # zftit cheese 5% - 200 grams
    #         "73": "גבינה צפתית מעודנת 5%",
    #         # feta shipping cheese - 250 grams
    #         "74": "גבינת פטה כבשים 5%",
    #         # hemed cheese 16% - 2500 grams
    #         "75": "גבינת חמד 16% שקית",
    #         # rikota cheese - 300 grams
    #         "76": "גבינת ריקוטה פרסקה",
    #     },
    # },
    # ------------------------------BRAD AND BAKERY------------------------------
    # {
    #     "url": 'https://shop.hazi-hinam.co.il/#/catalog?viewMode=category_targeting&categoryId=67&subCategoryId=11237',
    #     "itemsToScrape": {
    #         # shifon bread - 750 grams
    #         "77": "לחם שיפון 100%",
    #         # cosmin bread - 500 grams
    #         "78": "לחם כוסמין 100%",
    #         "79": "חלה קלועה / חלה מתוקה עגולה לבחירה",  # Braided challah
    #         "80": "לחם דגנים",  # dganim bread - 750 grams
    #         "81": "לחם חיטה מלאה",  # whole wheat bread - 750 grams
    #         "82": "לחם כפרי",  # kafri bread - 500 grams
    #         "83": "מארז 10 פיתות תימניות עבודת יד",  # Pack of 10 pitas
    #         "84": "שמונה לחמניות המבורגר",  # Eight hamburger rolls
    #         "85": "מארז 6 לחמניות כוסמין",  # Pack of 6 cosmin rolls
    #     },
    # },
    # {
    #     "url": 'https://shop.hazi-hinam.co.il/#/catalog?viewMode=category_targeting&categoryId=67&subCategoryId=10859',
    #     "itemsToScrape": {
    #         # Rice crackers from whole brown rice - 100 grams
    #         "86": "פריכיות אורז מאורז חום מלא",
    #         # Crisps with a dark chocolate base - 70 grams
    #         "87": "פריכיות עם תחתית שוקולד מריר",
    #         "88": "טוסטעים צנימים עם שומשום",  # tostthaim - 100 grams
    #         "89": "צנימים",  # znim - 250 grams
    #         "90": "פתית חיטה מלאה",  # patit hita melea - 250 grams
    #     },
    # },
    # {
    #     "url": 'https://shop.hazi-hinam.co.il/#/catalog?viewMode=category_targeting&categoryId=67&subCategoryId=11485',
    #     "itemsToScrape": {
    #         # choclate cake - 400 grams
    #         "91": "עוגת הבית בטעם שוקולד",
    #         # shmarim cake - 350 grams
    #         "92": "עוגת הבית שמרים קלאסית בטעם שוקולד",
    #         "93": "עוגת הבית בטעם תפוז",  # orange cake - 400 grams
    #         "94": "עוגיות שוקולד צ'יפס במילוי קרם בטעם שוקולד",  # chocolate cookies - 220 grams
    #         "95": "עוגיות ערגליות תות",  # argaliot toot cookies - 300 grams
    #         "96": "עוגיות לוטוס Lotus",  # lotus cookies - 312 grams
    #         "97": "עוגיות בטעם חמאה",  # butter cookies - 340 grams
    #     },
    # },
    # # ------------------------------DRINKS AND ALCOHOL------------------------------
    {
        "url": 'https://shop.hazi-hinam.co.il/#/catalog?viewMode=category_targeting&categoryId=79&subCategoryId=10850',
        "itemsToScrape": {
            "98": "תירוש כרמל מיץ ענבים",  # Tirosh wine
            "99": "יין גוורצטרמינר לבן חצי יבש",  # Gewurztraminer wine

        },
    },
    {
        "url": 'https://shop.hazi-hinam.co.il/#/catalog?viewMode=category_targeting&categoryId=79&subCategoryId=10851',
        "itemsToScrape": {
            "100": "משקה קל בטעם תפוזים",  # ORANGE JUICE - 1.5 LITER
            "101": "פריגת ענבים",  # GRAPE JUICE - 1.5 LITER
            "102": "תה קר בטעם ענבים",  # FUZETEA - 1.5 LITER
            "103": "נקטר תפוחים",  # APPLE NECTAR - 1 LITER
            "104": "משקה בטעם מנגו",  # MANGO JUICE - 1.5 LITER
            "105": "משקה אלוורה בטעם אפרסק",  # alovera drink - 1  liter

        },
    },
    {
        "url": 'https://shop.hazi-hinam.co.il/#/catalog?viewMode=category_targeting&categoryId=79&subCategoryId=11424',
        "itemsToScrape": {
            "106": "קוקה קולה קלאסי",  # COCA COLA - 1.5 LITER
            "107": "קוקה קולה זירו zero",  # ZERO COCA COLA - 1.5 LITER
            "108": "סבן אפ",  # SEVENUP - 1.5 LITER
            "109": "משקה מוגז לימודה ורודה",  # SCHWEPS - 1.5 LITER
            "110": "משקה בטעם פירות יער מוגז עדין",  # SCHWEPS - 1.5 LITER
            "111": "פאנטה זירו בטעם תפוח",  # FANTA - 1  liter

        },
    },
    {
        "url": 'https://shop.hazi-hinam.co.il/#/catalog?viewMode=category_targeting&categoryId=79&subCategoryId=11209',
        "itemsToScrape": {
            "112": "בירה היינקן שישייה",  # SIX PACK OF HEINEKEN
            "113": "בירה קורונה שישייה",  # SIX PACK OF CORONA
            "114": "בירה גולדסטאר שישייה",  # SIX PACK OF GOLDSTAR
            "115": "בירה טובורג רד שישייה",  # SIX PACK OF TUBORG
            "116": "בירה קרלסברג שישייה",  # SIX PACK OF CARLSBERG
            "117": "בירה מכבי שישייה",  # SIX PACK OF MACKBVI
            "118": "בירה סטלה ארטואה שישייה",  # SIX PACK OF STELLA ARTOA
        },
    },
]
