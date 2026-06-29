# Missing and unclaimed remains database 

## Work in Progress/Draft

### About
There's a growing awareness that information on missing people and unclaimed remains are fragmented across systems, preventing opportunities for identification and a measure of closure for loved ones. NamUS was created in an effort to mitigate this, but it's not mandatory for state and county governments to report to it.

I'm certainly not the first or the last person to have a fascination with the mysteries behind why someone has gone missing. This is pretty evident in the explosion of popularity in true crime content.

In addition, economic migration is a subject I return to again and again. For a lot of people, economic policy can be an abstraction. I've always searched out stories about the people for whom it's not. A big example being NAFTA and its impact - whether it's factory workers in the US who have lost jobs due to closures, or people in Central America who make the journey here for jobs. (source - https://bja.ojp.gov/program/muhr/overview)

I can't imagine how difficult it must be to live day after day, never knowing what's happened to someone you love. Particularly if they're making a journey fraught with danger and uncertainty. 

So many people have been doing all kinds of things to solve these cases and try to get answers. This certainly isn't anything groundbreaking, but it is my contribution.

## Design and Implementation

### Tools

PostgreSQL | DBeaver<br>
Python | VSCode<br>

### Sources and details

NamUS<br>
Individual Coroner Websites and State Clearinghouses (To be listed)<br>
DataMX.io/RNPDNO<br>
Murder Accountability Project

### Problems and solutions

Problem: Exported files only contain demographic information and leave out information such as clothing, tattoos, scars, etc. This information is essential when pulling together multiple information sources to make comparisons.

This information needs to be pulled somehow to be put in the database, but NamUS has approximately 40,000 missing and unclaimed remains records. For the moment, it doesn't look like there's a method to get this data. There's no public API and it's possible this data can't be scraped.

Problem: Clothing is often grouped in one text box, when each article of clothing should be split to one data point.

Additionally, there's the question of how to structure the data. What is the best way to do so without a) losing information, and b) overcomplicating the data.

First thoughts are that each article of clothing needs to have a column. Color is an unreliable metric, so it should be a boolean. OR, 3 values, another for "unknown" if there is no clothing or it's degraded beyond recognition.
(rethinking boolean)
Color is still an important detail and could possibly be added as an associated text box.

Problem: Many state and local jurisdictions don't enter information into NamUS. Information is fragmented and difficult to find.

Problem: How to deal with duplicates when records are in both NamUS and another database/dataset.

Problem: License - is it okay to republish the data?

Problem: RNPDNO to integrate a source from Mexico with an intent to focus on border related disappearances. Will require a lot of thinking about how to sift through this data, as it's 135,000 records.

## Data cleaning

When selecting for certain characteristics, such as tattoo, scar, etc. if there are notes saying these things are not present in shows up in the search results. It's still data, and I think it should be preserved regardless. This reinforces my thoughts that perhaps the base value for each should be Y/N - and in the text box, preserve those notes that say nothing was found. That way these results don't come up when people select for tattoos, but the information is still there.

Note: Total loaded records exceed current website count by 4. No duplicate case numbers were found. Discrepancy may reflect timing differences between state-level exports and website totals.
### Hyotheses

- If a jurisdiction has the resources to publish information online, they're also reporting to NamUS

### In the Weeds - Data Management

In my strongly held opinion, consistency and futureproofing are the foundation of any data project. Before jumping in, I test my system(s)* with a small amount of data, make necessary changes, and continue this process until I feel like I've covered my bases. If I'm not sure about implementing something I find out if I can put in place later.

File naming conventions:
Date downloaded_organization_status_demographics

- Date of download to know where to begin when pulling new records
- organization the data came from
- status of the victim - missing, unidentified, murdered
- The content of the file if I couldn't pull the whole database - for instance if it's just female, white males, clothing details, etc.

*I am picky about my tools/systems. I usually know what I want, and I'll go through and test all kinds of platforms until I find the closest option. But usually it's a trade off, and I need to decide what feature I want more than another.

### Additional branches/forks/repos/directions/etc.

The Murder Accountability Project provides data on uncleared homicides. Interested in layering this data over the NamUS data to explore possible demographic connections.