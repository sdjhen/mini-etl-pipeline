# Mini ETL pipeline using functions only

def extract(raw_list):
    # Extract only complete records
    return [r for r in raw_list if "temp" in r and "city" in r]