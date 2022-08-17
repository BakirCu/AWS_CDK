class Error(Exception):
    
    def check_value(data, key):
        if key not in data:
            raise ValueError(f"data doesn't contains key: {key}")