/*
 Some interesting queries
 */
-- Get stations that exist in more than one line
with common_stations as(
    select
        s.id
    from
        linesstations l
        inner join trainlines t on t.id = l.line_id
        inner join stations s on s.id = l.station_id
    group by
        s.id
    having
        count(s.station_name) > 2
)
select
    t.line_name,
    s.station_name
from
    linesstations l
    inner join trainlines t on t.id = l.line_id
    inner join stations s on s.id = l.station_id
where
    s.id in (
        select
            id
        from
            common_stations
    )
order by
    t.line_name,
    l.order_number;

-- Get the stations on an specific line
select
    t.id,
    t.line_name,
    s.station_name
from
    linesstations l
    inner join trainlines t on t.id = l.line_id
    inner join stations s on s.id = l.station_id
where
    lower(t.line_name) like 'tax%'
order by
    t.line_name,
    l.order_number;

-- Get the passenger travel across the route with times
select
    p.id passenger_id,
    t.id train_id,
    tl.line_name,
    s.station_name,
    pt.travel_time,
    pt.wait_time,
    sum(pt.travel_time) over (partition by pt.passenger_id) total_travel_time,
    sum(pt.wait_time) over (partition by pt.passenger_id) total_wait_time,
    sum(pt.travel_time) over (partition by pt.passenger_id) + sum(pt.wait_time) over (partition by pt.passenger_id) total_elapsed_time
from
    passengers p
    inner join passengertravellog pt on pt.passenger_id = p.id
    inner join trains t on t.id = pt.train_id
    inner join stations s on s.id = pt.station_id
    inner join trainlines tl on tl.id = pt.line_id
where
    1 = 1
    and p.id = 'ace93614-dac6-492b-b15b-01984819bf74'
order by
    pt.created;