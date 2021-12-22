urls = [
    {
        # ------------------------------FRIUTS------------------------------
        "url": 'https://www.tivtaam.co.il/categories/90071/products',
        "itemsToScrape": {
            "1": "בננות",                 # banana
            "2": "קלמנטינה",             # clementine
            "3": "תפוזים",           # orange
            "4": "תפוח עץ סמיט",    # green apple
            "5": "לימון",                 # lemon
            "6": "מלון",                  # melon                        חסר
            "7": "אשכולית אדומה",         # red_grapefruit
            "8": "אבוקדו",                # avocado
            "9": "פומלית",                # pomelo
            "10": "קיווי",                # kiwi
        },
    },
    {
        # ------------------------------VEGG------------------------------------
        "url": "https://www.tivtaam.co.il/categories/90066/products",
        "itemsToScrape": {
            # tomato
            "11": "עגבניות",
            # onion
            "12": "בצל יבש",
            # gamba
            "13": "פלפל אדום",
            # cucumber
            "14": "מלפפונים",
            # green_zucchini
            "15": "קשואים",
            # cabbage
            "16": "שומר",
            # green_hot_pepper
            "17": "פלפל חריף",
            # kohlrabi
            "18": "קולורבי",
            # eggplant
            "19": "חצילים",
            # radish
            "20": "צנון",

        },
    },
    # ------------------------------SNACKS------------------------------
    {
        "url": 'https://www.tivtaam.co.il/categories/90269/products',
        "itemsToScrape": {
            # dubonim 40 g
            "21": "דובונים חטיף תפוחי אדמה",
            # bilslyGril 60 g
            "22": "חטיף ביסלי בטעם גריל",
            # bambaOsem 80 g
            "23": "חטיף במבה",
            # apropoOsem 100 g
            "24": "חטיף אפרופו קלאסי",
            # poof 40 g
            "25": "פליי חטיף תירס בטעם קטשופ",
            # bunnies 40 g
            "26": "ארנבונים חטיף תפוחי אדמה",
            # kifly 80 g
            "27": "כיפלי חטיף בטעם גריל",
            # doritos 70 g
            "28": "דוריטוס בטעם טבעי",
            # ovlets 300 g
            "29": "אובלטים מלוחים קימל",
            # hotpop popcorn 6*100 g
            "30": "פופקורן להכנה במיקרוגל בטעם טבעי בתוספת מלח",
        },
    },
    # ------------------------------SWEET------------------------------
    {
        "url": 'https://www.tivtaam.co.il/categories/90262/products',
        "itemsToScrape": {
            # click red 65 g
            "31": "קליק ביסקויט",
            # teami 40 g
            "32": "חטיף טעמי",
            # kifkef nuts 40 g
            "33": "כיף כף מקלות מצופים שוקולד חלב",
            # bonati 40 g
            "34": "חטיף באונטי שוקולד קוקוס",
            # pack of min bueno 200 g
            "35": "קינדר בואנו מיני מיקס",
            # bkifkef gavia 135 g
            "36": "כיף כף פצפצים",
            # chocklate coins 36 g
            "37": "מטבעות שוקולד חלב",
            # torata 40 g
            "38": "חטיף טורטית",
            # hershiz whita and cookies choc 40 g
            "39": "קוקיס אנד קרים חטיף בטעם שוקולד לבן עם שברי עוגיות",
            # suprsie kiner
            "40": "ביצת הפתעה מצופה שוקולד 3 יחידות",
        },
    },
    # ------------------------------CHICKEN------------------------------
    {
        "url": 'https://www.tivtaam.co.il/categories/90083/products',
        "itemsToScrape": {
            # Fresh whole chicken - by kg
            "41": "עוף שלם טרי",
            # Fresh chicken liver - by kg
            "42": "כבד עוף טרי",
            # Fresh chicken legs - by kg
            "43": "כרעיים עוף טרי",
            # Fresh chicken steak - by kg
            "44": "סטייק פרגיות צרפתי",
            # Fresh chicken shanks - by kg
            "45": "שוקיים עוף טרי",
        },
    },
    #     # ------------------------------Beef and lamb------------------------------
    {
        "url": 'https://www.tivtaam.co.il/categories/90082/products',
        "itemsToScrape": {
            "46": "אנטריקוט טרי",  # Fresh entrecote - by kg
            # Fresh sinta - by kg
            "47": "סינטה לבן טרי מפורק",
            # Fresh veal ossobuco - by kg
            "48": "אוסובוקו בקר טרי",
            # Freshly ground beef - by kg
            "49": "בקר טחון טרי",
            # Fresh shoulder roast - by kg
            "50": "צלי כתף טרי",
        },
    },
    #     # ------------------------------FISHES------------------------------
    {
        "url": 'https://www.tivtaam.co.il/categories/90100/products',
        "itemsToScrape": {
            # BURI FISH - by kg
            "51": "בורי",
            # Fresh whole salmon fillet - by kg
            "52": "פילה סלמון טרי",
            # Fresh lavrak - by kg
            "53": "לברק טרי",
            # fresh lokus fish - by kg
            "54": "דג לוקוס טרי",
            # Fresh Dennis fish - by kg
            "55": "דניס",
        },
    },
    {
        # ------------------------------DAIRY------------------------------
        "url": 'https://www.tivtaam.co.il/categories/90176/products',
        "itemsToScrape": {
            "56": "חלב עיזים 3.6% קרטון",                      # goat milk - 1 liter
            "57": "משקה חלב אייס קפה",                  # ice coffie drink - 1 liter
            "58": "משקה שוקו",               # shoko drink - 1 liter
            # Pack of 8 pieces of Activia cream yogurt 1.5% fat
            "59": "יוגורט לבן 1.5% 8 יחידות",
            # 1 Yogurt with Gluten Free Chocolate Crackers 4.2%
            "60": "יוגורט עם אורז תפוח מצופה שוקולד ואורז תפוח עם קקאו"
            # Frilly yogurt with 1.5% strawberry - 500 grams
            "61": "פרילי יוגורט עם תות 1.5%",
            # Cottage 5% mehadrin - 250 GRAMS
            "62": "קוטג' 5%",
            # 5% white cheese - 250 grams
            "63": "סקי גבינה לבנה 5%",
            # Napoleon natural cheese cream cheese 25% - 225 grams
            "64": "נפוליאון גבינת שמנת בטעם טבעי 25%",
            # 5% creamy cheese symphony - 200 grams
            "65": "סימפוניה גבינה במרקם שמנת 5%",
            # Labana cheese 5% - 250 grams
            "66": "גבינת לאבנה 5%",
            # Camembert cheese - 200 GRAMS
            "67": "גבינת קממבר",
            # Roquefort cheese - 180 grams
            "68": "גבינת גליל רוקפור",
            # Mozzarella - 100 grams
            "69": "גבינת מוצרלה פרסקה",
            # Berry cheese - 125 grams
            "70": "גבינת ברי",
            # Dreamy cheese 25% fat - 200 grams
            "71": "חלומי פרוס 22%",
            # Bulgarian cheese 16% - 250 grams
            "72": "גבינה בולגרית 16%",
            # zftit cheese 5% - 200 grams
            "73": "גבינה צפתית מעודנת 5%",
            # feta shipping cheese - 250 grams
            "74": "גבינת פטה כבשים 5%",
            # hemed cheese 16% - 2500 grams
            "75": "גבינת חמד 16%",
            # rikota cheese - 300 grams
            "76": "גבינת ריקוטה פרסקה מעודן 9%",
        },
    },
]
