# for a array value of a key
unflat_json = {'user':
                   {'Rachel':
                        {'UserID': 1717171717,
                         'Email': 'rachel1999@gmail.com',
                         'friends': ['John', 'Jeremy', 'Emily']
                         }
                    }
               }


# Function for flattening
# json


def flatten_json(y):
    out = {}

    def flatten(x, name=''):

        # If the Nested key-value
        # pair is of dict type
        if type(x) is dict:

            for a in x:
                flatten(x[a], name + a + '_')

        # If the Nested key-value
        # pair is of list type
        # elif type(x) is list:
        #
        #     i = 0
        #
        #     for a in x:
        #         flatten(a, name + str(i) + '_')
        #         i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out


# Driver code
print(flatten_json(unflat_json))

from flatten_json import flatten

unflat_json = {'user':
                   {'Rachel':
                        {'UserID': 1717171717,
                         'Email': 'rachel1999@gmail.com',
                         'friends': ['John', 'Jeremy', 'Emily']
                         }
                    }
               }

a = {
    "identification": {
        "gtin": "062600965240",
        "gtin14": "00062600965240",
        "targetMarketCountryCode": "124",
        "catalogueGln": "0068780050639",
        "dataProviderName": "Johnson & Johnson Inc.",
        "baseGln": "0062600000019"
    },
    "ecommerceContent": [
        {
            "brandOwnerVersionCode": "NA",
            "nutritionVersionCode": "NA",
            "productNameEnglish": "Neutrogena Light Therapy Acne Spot Treatment",
            "productNameFrench": "Neutrogena Traitement Ciblé de Luminothérapie Antiacné",
            "functionalNameEnglish": "light therapy acne spot treatment",
            "functionalNameFrench": "traitement ciblé de luminothérapie antiacné",
            "brandNameEnglish": "Neutrogena",
            "brandNameFrench": "Neutrogena",
            "gpcCode": "10000903",
            "netContentsEnglish": "Contains 1 device\nBattery included",
            "netContentsFrench": "Contient 1 appareil\nPile incluse",
            "onPackProductMarketingEnglish": "New\n\nDermatologist in-office acne technology\n\nTreats breakouts fast\nClinically proven\n2-minute acne treatments\n\nThe science of acne light therapy\nThe energy from red and blue lights gently filters through skin and has been scientifically shown to target acne-causing bacteria, reducing the appearance of breakouts.\n\nChemical free treatment\nUV free\nQuick & easy\n\nNeutrogena Light Therapy Acne Spot Treatment is clinically proven to speed the reduction of breakouts.\nAll with no mess, no residue and no flaking so you can use it anywhere, anytime.\n\nIndications for use: The Neutrogena Light Therapy Acne Spot Treatment is indicated to treat mild to moderate inflammatory acne.",
            "onPackProductMarketingFrench": "Nouveau\n\nTechnologie antiacné utilisée par les dermatologues\n\nTraite rapidement les poussées d'acné\nÉprouve en clinique\nChaque traitement antiacné dure 2 minutes\n\nLa science de la luminothérapie antiacné\nL'énergie de la lumière rouge et bleue pénètre doucement dans la peau, cible les bactéries responsables de l'acné et réduit l'apparence des boutons, preuves scientifiques à l'appui.\n\nSans produits chimiques\nSans rayons UV\nRapide et facile\n\nLe traitement ciblé de luminothérapie antiacné Neutrogena favorise la réduction des boutons d'acné, preuves cliniques à l'appui.\nIl ne cause ni dégâts, ni résidus, ni desquamation et peut s'utiliser partout, en tout temps.\n\nIndication : Le traitement ciblé de luminothérapie antiacné est indiqué pour le traitement de l'acné inflammatoire légère ou modérée.",
            "manufacturersAddressEnglish": "Johnson & Johnson GmbH\nJohnson & Johnson\nPlatz 2, 41470 Neuss\nGermany",
            "manufacturersAddressFrench": "Johnson & Johnson GmbH\nJohnson & Johnson\nPlatz 2, 41470 Neuss\nGermany",
            "importerAddressEnglish": "Johnson & Johnson Inc.\nMarkham, L3R 5L2\nCanada\n1-888-663-8876\nwww.neutrogena.ca",
            "importerAddressFrench": "Johnson & Johnson Inc.\nMarkham, L3R 5L2\nCanada\n1-888-663-8876\nwww.neutrogena.ca",
            "productCareandUseInstructionsEnglish": "Treat for 2 minutes, 3 times a day.\nSee leaflet inside for direction for use.",
            "productCareandUseInstructionsFrench": "Faites le traitement pendant 2 minutes, 3 fois par jour. Consultez la notice à l'intérieur pour le mode d'emploi.",
            "productWarningsEnglish": "WARNINGS: It is not recommended to use Neutrogena Light Therapy Acne Spot Treatment if you are pregnant, may be pregnant, or nursing, as the device was not tested on pregnant or nursing women. PRECAUTIONS: This device is limited to use by a single person.",
            "productWarningsFrench": "MISE EN GARDE : N'utilisez pas le traitement ciblé de luminothérapie ciblé de luminothérapie antiacné si vous êtes enceinte, si vous allaitez, étant donné que l'appareil n'a pas été testé chez les femmes enceintes ou qui allaitent. PRÉCAUTION : Réservé à l'usage personnel.",
            "height": "161.3",
            "heightUOM": "MM",
            "width": "52.1",
            "widthUOM": "MM",
            "depth": "33",
            "depthUOM": "MM",
            "grossWeight": "54",
            "grossWeightUOM": "GR",
            "trademarkInformationEnglish": "© J&J Inc. 2016",
            "trademarkInformationFrench": "© J&J Inc. 2016",
            "warrantyDescriptionEnglish": "Johnson & Johnson Inc.\nMarkham, L3R 5L2\nCanada\n1-888-663-8876\nwww.neutrogena.ca",
            "warrantyDescriptionFrench": "Johnson & Johnson Inc.\nMarkham, L3R 5L2\nCanada\n1-888-663-8876\nwww.neutrogena.ca",
            "identification": {
                "nameOfBrandOwnerOrSubmitter": "Johnson & Johnson Inc.",
                "dateUpdated": "2020-10-14T09:46:33.460-04:00",
                "ecommerceStatusNutritionStatus": "Rejected",
                "excellenceLevel": "1",
                "gln": "0062600000019",
                "gtin": "00062600965240",
                "systemVersion": "2018-03-06T10:17:47.000-05:00"
            },
            "imageGroup": [
                {
                    "angle": "N",
                    "facing": "1",
                    "format": "TIF",
                    "gdti": "754000000025700000000034069011",
                    "imageCategory": "9",
                    "imageType": "A",
                    "language": "en",
                    "state": "1"
                },
                {
                    "angle": "N",
                    "facing": "1",
                    "format": "TIF",
                    "gdti": "754000000025700000000034068947",
                    "imageCategory": "9",
                    "imageType": "A",
                    "language": "fr",
                    "state": "1"
                },
                {
                    "angle": "C",
                    "facing": "1",
                    "format": "TIF",
                    "gdti": "754000000014100000000046229825",
                    "imageCategory": "2",
                    "imageType": "A",
                    "language": "en",
                    "state": "1"
                },
                {
                    "angle": "C",
                    "facing": "1",
                    "format": "TIF",
                    "gdti": "754000000014100000000046229954",
                    "imageCategory": "2",
                    "imageType": "A",
                    "language": "fr",
                    "state": "1"
                },
                {
                    "angle": "C",
                    "facing": "1",
                    "format": "TIF",
                    "gdti": "754000000014100000000046229723",
                    "imageCategory": "2",
                    "imageType": "A",
                    "language": "ml",
                    "state": "0"
                }
            ],
            "nutritionAndIngredients": [],
            "components": []
        }
    ]
}

flat_json = flatten(a)

print(flat_json)
