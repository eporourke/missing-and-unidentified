drop view if exists staging.stg_map_unsolved;
drop view if exists staging.stg_map_clean;

create view staging.stg_map_clean as
select
    *,
    trim(split_part(cntyfips, ',', 1)) as county,
    trim(split_part(cntyfips, ',', 2)) as state_abbr,
    agentype as agency_type,
    actiontype as action_type,
    vicage as vic_age,
    vicsex as vic_sex,
    vicrace as vic_race,
    vicethnic as vic_ethnic,
    offage as off_age,
    offsex as off_sex,
    offrace as off_race,
    offethnic as off_ethnic,
    subcircum as sub_circum,
    viccount as vic_count,
    offcount as off_count,
    to_date(lpad(filedate::bigint::text, 6, '0'), 'MMDDYY') as file_date
from raw.murder_accountability;

create or replace view staging.stg_map_unsolved as
select *
from staging.stg_map_clean
where solved = 'No'
  and county = 'De Kalb';