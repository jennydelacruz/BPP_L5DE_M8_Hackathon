# BPP_L5DE_M8_Hackathon

## **GROUP 3 - Halyna, Chris Ashdown, Chris Benson, Jennifer.**

Methodology:

- Selected one sheet (month-year) to process for each file. Therefore worked with December 2011 for both Edinburgh day time data and Strathspey weather data.
- Worked together as a group to create the pipeline, deciding on one iPython notebook for the entire pipeline.

File structure: 

* data
  * clean_daytime_data.csv: copy of edinburgh-daytime.xlsx selecting only the columns of interest
  * clean_temperature_data.csv: copy of strathspey-weather.xlsx selecting only the columns of interest.
* GROUP3_MAIN.ipynb: is the core script containing the whole data pipeline including reading the data, filtering, cleaning, producing the output file and testing.
* output
  * merged.csv: cleaned, merged file that includes only the columns of interest.

Data pipeline plan:

1. [X] Explore the files/data given to us - check for data inconsistencies, content, headers, etc.
2. [X] Clean the files:

    1. [X] fixing headers,
    2. [X] text misalignment (empty rows),
    3. [X] data types,
    4. [X] extra symbols,
    5. [X] remove extra spaces,
    6. [X] remove unecessary columns
    7. [X] select subset of the data (december 2011)
3. [ ] Normalise the data in all sheets.
4. [X] add data validations:

    1. [X] including tests like row counts
5. [X] Generate outputs: csv file with merge summary
6. [ ] Scale the solution to handle all sheets from both files
7. [ ] Break the code into modules (e.g. ingest, clean, etc.)
8. [ ] Data transformations: generate a minute-by-minute temperature estimate for 2012
