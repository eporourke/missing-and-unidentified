-- create schema if not exists reference;

-- field mapping table

create table reference.field_mapping as
select
    table_name as source_table,
    column_name as source_column,
    null::text as standard_field,
    data_type,
    ordinal_position
from information_schema.columns
where table_schema = 'raw'
order by table_name, column_name;

-- field_matrix - count of each column

create or replace view reference.field_matrix as
select
    source_column,
    string_agg(source_table, ', ' order by source_table) as appears_in_tables,
    count(*) as table_count
from reference.field_mapping
group by source_column
order by source_column;

-- spreadsheet view

--create extension if not exists tablefunc;

select *
from crosstab(
  $$
  select
      source_column,
      source_table,
      '✓' as present
  from reference.field_mapping
  order by 1, 2
  $$,
  $$
  select distinct source_table
  from reference.field_mapping
  order by 1
  $$
) as ct (
  source_column text,
  namus_missing text,
  namus_unidentified text,
  el_paso_unidentified text,
  murder_accountability text
);

----
--
--- pull columns from each table

select column_name
from information_schema.columns
where table_schema = 'raw'
  and table_name = 'namus_unidentified'
order by column_name;



