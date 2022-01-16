/*
Script to create the structure of database used to perform the project of the course of PostgreSQL
*/

create extension if not exists "uuid-ossp";

create table passengers (
	id uuid not null default uuid_generate_v4(),
	origin_station_id uuid not null,
	destination_station_id uuid not null,
    travel_date timestamp not null default current_timestamp,
	constraint passengers_pk primary key (id)
);

comment on
column passengers.id is 'primary key of the table';

comment on
column passengers.origin_station_id is 'foreign key of origin station';

comment on
column passengers.destination_station_id is 'foreign key of destination station';

comment on
column passengers.travel_date is 'date of the travel';
--

create table trainlines (
	id uuid not null default uuid_generate_v4(),
	line_name varchar(50) not null,
	created timestamp not null default current_timestamp,
    status bool default true not null,
	constraint trainlines_pk primary key (id)
);

comment on
column trainlines.id is 'primary key of the table';

comment on
column trainlines.line_name is 'name of the line';

comment on
column trainlines.created is 'date of created row';

comment on
column trainlines.status is 'status of the row';
--

create table stations (
	id uuid not null default uuid_generate_v4(),
	station_name varchar(50) not null,
	created timestamp not null default current_timestamp,
    status bool default true not null,
	constraint stations_pk primary key (id)
);

comment on
column stations.id is 'primary key of the table';

comment on
column stations.station_name is 'name of the station';

comment on
column stations.created is 'date of created row';

comment on
column stations.status is 'status of the row';

alter table passengers add constraint stations_passengers_origin_station_id_fk foreign key (origin_station_id) references stations(id);

alter table passengers add constraint stations_passengers_destination_station_id_fk foreign key (destination_station_id) references stations(id);

create index passengers_origin_station_id_idx on
passengers (origin_station_id);

create index passengers_destination_station_id_idx on
passengers (destination_station_id);

ALTER TABLE stations ADD CONSTRAINT stations_station_name_un UNIQUE (station_name);

--
CREATE TABLE linesstations (
id uuid not null default uuid_generate_v4(),
	line_id uuid not null,
    station_id uuid not null,
    order_number int2 not null,
	created timestamp not null default current_timestamp,
    status bool default true not null,
	constraint linesstations_pk primary key (id)
);

comment on
column linesstations.id is 'primary key fo the table';

comment on
column linesstations.line_id is 'foreign key of line';

comment on
column linesstations.station_id is 'foreign key of station';

comment on
column linesstations.order_number is 'order of the list of stations';

comment on
column linesstations.created is 'date of the created row';

comment on
column linesstations.status is 'status of the row';

alter table linesstations add constraint trainlines_linesstations_line_id_fk foreign key (line_id) references trainlines(id);

alter table linesstations add constraint stations_linesstations_station_id_fk foreign key (station_id) references stations(id);

create index linesstations_line_id_idx on
linesstations (line_id);

create index linesstations_station_id_idx on
linesstations (station_id);
--

create table trains (
	id uuid not null default uuid_generate_v4(),
	capacity int2 not null,
	created timestamp not null default current_timestamp,
    status bool default true not null,
	constraint trains_pk primary key (id)
);

comment on
column trains.id is 'primary key of the table';

comment on
column trains.capacity is 'number of people the train can transports';

comment on
column trains.created is 'date of the created row';

comment on
column trains.status is 'status of the row';
--

create table traintravellog (
	id uuid not null default uuid_generate_v4(),
    train_id uuid not null,
    line_id uuid not null,
    start_date timestamp not null,
    end_date timestamp,
	created timestamp not null default current_timestamp,
    status bool default true not null,
	constraint traintravellog_pk primary key (id)
);

comment on
column traintravellog.id is 'primary key of the table';

comment on
column traintravellog.train_id is 'foreign key of the train';

comment on
column traintravellog.line_id is 'foreign key of the train line';

comment on
column traintravellog.start_date is 'start date of the programation';

comment on
column traintravellog.end_date is 'end date of the programation';

comment on
column traintravellog.created is 'date of the created row';

comment on
column traintravellog.status is 'status of the created row';

alter table traintravellog add constraint trains_traintravellog_train_id_fk foreign key (train_id) references trains(id);

alter table traintravellog add constraint trainlines_traintravellog_line_id_fk foreign key (line_id) references trainlines(id);

create index traintravellog_train_id_idx on
traintravellog (train_id);

create index traintravellog_line_id_idx on
traintravellog (line_id);
--

create table passengertravellog (
	id uuid not null default uuid_generate_v4(),
    passenger_id uuid not null,
    train_id uuid not null,
    station_id uuid not null,
	line_id uuid not null,
    travel_time time not null,
    wait_time time not null,
	created timestamp not null default current_timestamp,
    status bool default true not null,
	constraint passengertravellog_pk primary key (id)
);

comment on
column passengertravellog.id is 'primary key of the table';

comment on
column passengertravellog.passenger_id is 'foreign key of passenger';

comment on
column passengertravellog.train_id is 'foreign key of train';

comment on
column passengertravellog.station_id is 'foreign key of station';

comment on
column passengertravellog.line_id is 'foreign key of line';

comment on
column passengertravellog.travel_time is 'time takes the travel';

comment on
column passengertravellog.wait_time is 'time takes waiting for a train';

comment on
column passengertravellog.created is 'date of created row';

comment on
column passengertravellog.status is 'status of created row';

alter table passengertravellog add constraint passengers_passengertravellog_passenger_id_fk foreign key (passenger_id) references passengers(id);

alter table passengertravellog add constraint stations_passengertravellog_station_id_fk foreign key (station_id) references stations(id);

alter table passengertravellog add constraint trains_passengertravellog_train_id_fk foreign key (train_id) references trains(id);

alter table passengertravellog add constraint trainlines_passengertravellog_line_id_fk foreign key (line_id) references trainlines(id);

create index passengertravellog_passenger_id_idx on
passengertravellog (passenger_id);

create index passengertravellog_train_id_idx on
passengertravellog (train_id);

create index passengertravellog_station_id_idx on
passengertravellog (station_id);

create index passengertravellog_line_id_idx on
passengertravellog (line_id);
