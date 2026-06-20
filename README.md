# Missing and unclaimed remains database 

### About
There's a growing awareness that information on missing people and unclaimed remains are fragmented across systems, preventing opportunities for identification and a measure of closure for loved ones. NamUS was created in an effort to mitigate this, but it's not mandatory for state and county governments to report to it.

I'm certainly not the first or the last person to have a fascination with the mysteries behind why someone has gone missing. This is pretty evident in the explosion of popularity in true crime content.

In addition, economic migration is a subject I return to again and again. For a lot of people, economic policy can be an abstraction. I've always searched out stories about the people for whom it's not. A big example being NAFTA and its impact - whether it's factory workers in the US who have lost jobs due to closures, or people in Central America who make the journey here for jobs.

I can't imagine how difficult it must be to live day after day, never knowing what's happened to someone you love. Particularly if they're making a journey fraught with danger and uncertainty. 

So many people have been doing all kinds of things to solve these cases and try to get answers. This certainly isn't anything groundbreaking, but it is my contribution.

## Design and Implementation

### Tools

PostgreSQL

### Sources and details

NamUS
DataMX.io

### Problems and solutions

Problem: Exported files only contain demographic information and leave out information such as clothing, tattoos, scars, etc. This information is essential when pulling together multiple information sources to make comparisons.

This information needs to be pulled somehow to be put in the database, but NamUS has approximately 40,000 missing and unclaimed remains records. For the moment, it doesn't look like there's a method to get this data. There's no public API and it's possible this data can't be scraped.

Problem: Clothing is often grouped in one text box, when each article of clothing should be split to one data point.

Additionally, there's the question of how to structure the data. What is the best way to do so without a) losing information, and b) overcomplicating the data.

First thoughts are that each article of clothing needs to have a column. Color is an unreliable metric, so it should be a boolean. OR, 3 values, another for "unknown" if there is no clothing or it's degraded beyond recognition.

Color is still an important detail and could possibly be added as an associated text box.

Problem: Many state and local jurisdictions don't enter information into NamUS. Information is fragmented and difficult to find.