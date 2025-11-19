# BPP_L5DE_M8_Hackathon

**GROUP 3 - Halyna, Chris Ashdown, Chris Benson, Jennifer.** 

Data pipeline plan: 

1. Explore the files/data given to us - check for data inconsistencies, content, headers, etc.
2. Clean the files:
   1. fixing headers,
   2. text misalignment (empty rows),
   3. clock changes,
   4. data types,
   5. extra symbols,
   6. remove extra spaces,
   7. remove rows that don't meet requirements.
3. Normalise the data in all sheets.
4. Validate - filter data to the subset of interest -> 2012
   1. including tests like row counts, data consistency
5. Data transformations: generate a minute-by-minute temperature estimate for 2012
6. Generate outputs: csv file with merge summary
