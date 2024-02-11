import time
import resource

def track_time_and_memory(func):
    def wrapper(*args, **kwargs):
        # Start time
        start_time = time.time()
        
        # Start memory usage
        start_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        
        # Call the function
        result = func(*args, **kwargs)
        
        # End time
        end_time = time.time()
        
        # End memory usage
        end_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        
        # Calculate time taken
        elapsed_time = end_time - start_time
        
        # Calculate memory used (in MB)
        memory_used = (end_memory - start_memory) / 1024  # Convert from KB to MB
        
        print(f"Time taken: {elapsed_time:.4f} seconds")
        print(f"Memory used: {memory_used:.2f} MB")
        
        return result
    
    return wrapper
