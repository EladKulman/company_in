
COMPANIES = {}
COMPANIES_SUM = {}


def get_all_companies_summary():
    global COMPANIES_SUM
    result = []
    for c in COMPANIES_SUM:
        result.append(COMPANIES_SUM[c])
    return result

def get_all_companies_details():
    global COMPANIES
    return COMPANIES  

def get_company_details(company_name):
    global COMPANIES
    if company_name in COMPANIES:
        return COMPANIES[company_name], None
    else:
        return None, 'company not exist'




def add_company(company_data):
    try:
        global COMPANIES
        company_name = company_data['name']
        if company_name in COMPANIES:
            return None, 'Company Already in List'
        company_sum_keys_to_extract = ["logo", "name", "type"]
        company_data_keys_to_extract = ["logo", "name", "domain", "description", "industry", "type", "raised", "raised", "annualRevenu", 'marketCap',
        'location']
        company_sum = {key: company_data[key] for key in company_sum_keys_to_extract}
        company_relevant_data = {}
        for key in company_data_keys_to_extract:
            if key in company_data:
                company_relevant_data[key] = company_data[key]
        COMPANIES_SUM[company_name] = company_sum
        COMPANIES[company_name] = company_relevant_data
        return True, None
    except Exception as e:
        print(e)
        return None, 'error'