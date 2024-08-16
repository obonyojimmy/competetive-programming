from datetime import datetime, timedelta

def parse_time(time_str, is_24_hour_format):
    """
    Parse a time string into a datetime object.
    Handle 24-hour format or 12-hour format based on the flag.
    """
    #print(time_str, is_24_hour_format)
    if ":" in time_str:
        if is_24_hour_format:
            return datetime.strptime(time_str, "%H:%M")
        else:
            return datetime.strptime(time_str, "%I:%M")
    else:
        if is_24_hour_format:
            return datetime.strptime(time_str, "%H")
        else:
            return datetime.strptime(time_str, "%I")

def calculate_total_time(time_ranges):
    total_minutes = 0
    
    for time_range in time_ranges:
        start_str, end_str = time_range.split('-')
        start_str, end_str = start_str.strip(), end_str.strip()
        is_24_hour_format = detect_time_format(start_str) or detect_time_format(end_str)
        start_time = parse_time(start_str, is_24_hour_format)
        end_time = parse_time(end_str, is_24_hour_format)
        
        if is_24_hour_format:
            # Directly calculate the difference for 24-hour format
            if end_time < start_time:
                end_time += timedelta(days=1)
        else:
            # Handle AM/PM logic for 12-hour format
            if end_time <= start_time:
                end_time += timedelta(hours=12)
        
        time_diff = end_time - start_time
        total_minutes += time_diff.total_seconds() / 60
    
    return total_minutes / 60  # Convert minutes to hours

def detect_time_format(time_range):
    """
    Detect if the given time range is in 24-hour or 12-hour format.
    If hours are greater than 12, it's likely in 24-hour format.
    """
    start_time = int(time_range.split('-')[0].split(':')[0])
    return start_time > 12

def sum_timesheet(file_path):
    total_time = 0.0
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()  # Remove any leading/trailing whitespace
            if line:
                time_ranges = line.split(",")
                total_time += calculate_total_time(time_ranges,)
                
    return total_time

if __name__ == "__main__":
    # Testing with the sample input
    timesheet = "samples/december.txt"
    result = sum_timesheet(timesheet)
    print(f"Total time: {result} hours")
