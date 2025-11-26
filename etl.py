# Mini ETL pipeline using functions only

def extract(raw_list):
    # Extract only complete records
    return [r for r in raw_list if "temp" in r and "city" in r]

def transform(record):
    # Clean one record
    cleaned = {}
    cleaned["city"] = record["city"].strip().title()
    cleaned["temp"] = float(record["temp"])   # Might raise ValueError
    return cleaned

def load(clean_records):
    # Pretend to load to warehouse
    for rec in clean_records:
        print(f"Loaded: {rec}")
        
        raw_data = [
    {"city": "   london", "temp": "20.5"},
    {"city": "tokyo", "temp": "not a number"},
    {"city": "berlin"}
]