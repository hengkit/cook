import re
def get_date(paragraph):
    match = re.match(r'^(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)[^.!?]*[.!?]', paragraph, re.IGNORECASE)

    return match.group(0) if match else None
def get_coords(paragraph):
    match = re.search(
        r'latitude\s(\d+)\sdegrees\s(\d+)\sminute[s]?(?:\s(North|South))?[,|;]\s*longitude\s(\d+)\sdegrees\s(\d+)\sminute[s]?(?:\s(South|East|West))?',
       paragraph, re.IGNORECASE | re.DOTALL
    )
    
    if match:
        # Extract latitude information
        lat_degrees = match.group(1)
        lat_minutes = match.group(2) if match.group(2) else "0"  # Default to "0" if minutes are missing
        lat_direction = match.group(3)
        
        # Extract longitude information
        long_degrees = match.group(4)
        long_minutes = match.group(5) if match.group(5) else "0"  # Default to "0" if minutes are missing
        long_direction = match.group(6)
    
        # Format and return both latitude and longitude
        
        latitude = round(int(lat_degrees) + int(lat_minutes)/60,3)
        if lat_direction != "North":
            latitude *= -1
        
        longitude = round(int(long_degrees) + int(long_minutes)/60,3) * -1
        if longitude < -180:
            longitude = 360 + longitude 
   
        return latitude, longitude
    else:
        return None, None

def parse_raw(filename):
    
    with open(filename, 'r') as file:
        content = file.read()
    paragraphs = re.findall(r'<p>(.*?)</p>', content, re.DOTALL)
    for paragraph in paragraphs:
        date = get_date(paragraph)
        lat, lon = get_coords(paragraph)
        if date:
            route.append(f"{date} :: {lat} :: {lon}\n")
def write_csv(outfile):
    with open(outfile, "w") as file:
        for date in route:
            file.write(date)

if __name__ == "__main__":
    infile = 'cook.html'
    outfile = "endeavour2.csv"
    route =[]
    coordinates = parse_raw(infile)
    write_csv(outfile)