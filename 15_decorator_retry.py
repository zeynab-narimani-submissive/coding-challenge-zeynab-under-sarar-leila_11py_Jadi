def decorator_retry(func):
    def wrapper(*args, **kwargs):
        for _ in range(3):  # Retry up to 3 times
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Error occurred: {e}. Retrying...")
        print("Failed after 3 attempts.")
    return wrapper
@decorator_retry
def risky_function(x):
    x / 0
        
risky_function(85)  # This will trigger retries