def country_labels():
    """This function serves as an external database in order
    to replace country labels, as defined by Eurostat,
    with full country names.
    """

    country_dict = {
        'BE' : 'Belgium',
        'BG' : 'Bulgaria',
        'CZ' : 'Czechia',
        'DK' : 'Denmark',
        'DE' : 'Germany',
        'DE_TOT' : 'Germany with ex-GDR',
        'EE' : 'Estonia',
        'IE' : 'Ireland',
        'EL' : 'Greece',
        'ES' : 'Spain',
        'FR' : 'France',
        'FX' : 'Metropolitan France',
        'HR' : 'Croatia',
        'IT' : 'Italy',
        'CY' : 'Cyprus',
        'LV' : 'Latvia',
        'LT' : 'Lithuania',
        'LU' : 'Luxembourg',
        'HU' : 'Hungary',
        'MT' : 'Malta',
        'NL' : 'Netherlands',
        'AT' : 'Austria',
        'PL' : 'Poland',
        'PT' : 'Portugal',
        'RO' : 'Romania',
        'SI' : 'Slovenia',
        'SK' : 'Slovakia',
        'FI' : 'Finland',
        'SE' : 'Sweden',
        'IS' : 'Iceland',
        'LI' : 'Liechtenstein',
        'NO' : 'Norway',
        'CH' : 'Switzerland',
        'UK' : 'United Kingdom',
        'BA' : 'Bosnia and Herzegovina',
        'ME' : 'Montenegro',
        'MD' : 'Moldova',
        'MK' : 'North Macedonia',
        'AL' : 'Albania',
        'RS' : 'Serbia',
        'TR' : 'Turkey',
        'UA' : 'Ukraine',
        'XK' : 'Kosovo',
        'GE' : 'Georgia',
        'AD' : 'Andorra',
        'BY' : 'Belarus',
        'MC' : 'Monaco',
        'RU' : 'Russia',
        'SM' : 'San Marino',
        'AM' : 'Armenia',
        'AZ' : 'Azerbaijan'
        }

    return country_dict

def hicp_labels():
    """An auxiliary external database `dict()` object to be used,
    in `.rename()` function for Harmonized Index of Consumer Prices (HICP)
    labels.
    """
    
    hicp_dict = {
        'CP00':'All-items HICP',
        'CP01':'Food and non-alcoholic beverages',
        'CP03':'Clothing and footwear',
        'CP04':'Housing, water, electricity, gas and other fuels',
	'CP06':'Health',
	'CP0611':'Pharmaceutical products',
	'CP0621':'Medical services',
	'CP0711':'Motor cars',
	'CP0713':'Bicycles',
	'CP081':'Postal services',
	'CP0941':'Recreational and sporting services',
	'CP0942':'Cultural services',
	'CP10102':'Primary education',
	'CP102':'Secondary education',
	'CP104':'Tertiary education',
	'CP12322':'Articles for babies',
	'CP12401':'Child care services',
	'CP126':'Financial services n.e.c.',
	'CP12701':'Administrative fees'
            }

    return hicp_dict

def ppp_labels():
    """An auxiliary external database `dict()` object to be used,
    in `.rename()` function for Harmonized Purchasing Power Parity (PPP)
    labels.
    """
    

    ppp_dict = {
        'EXP_NAC_PC_GDP' : 'Nominal expenditure as a percentage of GDP (GDP=100)',
        'EXP_EUR_HAB' : 'Nominal expenditure per inhabitant (in euro)',
        'PPP_EU27_2020' : 'Purchasing power parities (EU27_2020=1)',
        'EXP_EUR' : 'Nominal expenditure (in euro)',
        'GDP'   : 'Gross domestic product',
        'A01'   : 'Actual individual consumption',
        'A0101' : 'Food and non-alcoholic beverage',
        'A0103' : 'Clothing and footwear',
        'A0104' : 'Housing, water, electricity, gas and other fuels',
        'A0106' : 'Health',
        'A0109' : 'Recreation and culture',
        'A0110' : 'Education',
        'P0201' : 'Consumer services',
        'P0202' : 'Government services'
        }
    
    return ppp_dict