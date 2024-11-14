import csv, re
infile = "dates.txt"
outfile = "dates.csv"
with open(infile, 'r') as file:
    reader = csv.reader(file, delimiter='\t')
    headers = next(reader)
    with open(outfile, "w") as file:
        for row in reader:
            year, month, daydate = row
            match = re.search(r'(\w+),\s(\d+)(?:st|nd|rd|th)?\.', daydate, re.IGNORECASE)
        
            if match:
                day = match.group(1)
                dayofmonth = match.group(2)
            date = f"{year}/{month}/{dayofmonth}"
            file.write(f"{date},{day})