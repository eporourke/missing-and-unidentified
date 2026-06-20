# Missing and unclaimed remains database - design and implementation

## Sources and details

NamUS
DataMX.io

## Problems and solutions

Problem: Exported files only contain demographic information and leave out information such as clothing, tattoos, scars, etc. This information is essential when pulling together multiple information sources to make comparisons.

This information needs to be pulled somehow to be put in the database, but NamUS has approximately 40,000 missing and unclaimed remains records. For the moment, it doesn't look like there's a method to get this data. There's no public API and it's possible this data can't be scraped.

Problem: Clothing is often grouped in one text box, when each article of clothing should be split to one data point.

Additionally, there's the question of how to structure the data. What is the best way to do so without a) losing information, and b) overcomplicating the data.

First thoughts are that each article of clothing needs to have a column. Color is an unreliable metric, so it should be a boolean. OR, 3 values, another for "unknown" if there is no clothing or it's degraded beyond recognition.

Color is still an important detail and could possibly be added as an associated text box.