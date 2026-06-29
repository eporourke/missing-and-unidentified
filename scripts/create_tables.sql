CREATE TABLE reference.scrape_log (
  source_name varchar,
  source_url varchar,
  status varchar,
  scraped_at timestamp default now()
);