use sys;

drop table if exists Student;
drop table if exists DormKeeper;
drop table if exists Dormitory;
drop table if exists Building;
drop table if exists Repair;
drop table if exists Visitor;

set sql_safe_updates=0; 
create table Student(
    s_id char(20) primary key,
    s_name varchar(40),
    s_sex varchar(2),
    s_tele varchar(30),
    s_dorm_id char(8),
    s_build_id varchar(10),
    s_photo blob,

    constraint CK_Student1 check(s_sex in ('M', 'F')),
    constraint CK_Student2 check(s_name is not null)
);

create table DormKeeper(
    dk_id char(20) primary key,
    dk_name varchar(40),
    dk_sex varchar(2),
    dk_tele varchar(30),
    dk_build_id varchar(10),
    dk_photo blob,

    constraint CK_DormKeeper1 check(dk_sex in ('M', 'F')),
    constraint CK_DormKeeper2 check(dk_name is not null)
);

create table Dormitory(
    d_id char(8),
    d_build varchar(10),
    d_max int,

    constraint PK_Dormitory primary key(d_id, d_build)
);

create table Building(
    b_id varchar(10) primary key,
    b_name varchar(40),

    constraint CK_Building1 check(b_name is not null)
);

create table Repair(
    r_id char(24) primary key,
    r_man_id char(20),
    r_build varchar(10),
    r_dorm char(8),
    r_state char(2),
    r_content varchar(100),
    r_stu_id char(20),

    constraint CK_Repair1 check(r_state in ('T', 'F'))
);

create table Visitor(
    v_id char(24) primary key,
    v_name varchar(40),
    v_tele varchar(30),
    v_content varchar(100),
    v_build_id varchar(10),
    v_date date,

    constraint CK_Visitor1 check(v_name is not null)
);

insert into Student values('PB18114514', '李田所', 'M', '191919', '0114', 'GX2', null);
insert into Student values('PB19114514', '李填索', 'M', '114514', '0114', 'GX2', null);
insert into Student values('PB20114514', '李甜锁', 'F', '114114', '1919', 'GX1', null);
insert into Student values('PB21114514', '李天梭', 'M', '514114', '0114', 'GX2', null);
insert into Student values('PB22114514', '李恬琐', 'M', '514514', '0514', 'GX2', null);
insert into Student values('PB23114514', '李添娑', 'F', '810810', '0810', 'GX1', null);

insert into DormKeeper values('DK21114514', '田所浩一', 'F', '191980', 'GX1', null);
insert into DormKeeper values('DK22114514', '田所浩二', 'M', '191981', 'GX2', null);

insert into Dormitory values('0114', 'GX2', 4);
insert into Dormitory values('1919', 'GX1', 4);
insert into Dormitory values('0514', 'GX2', 4);
insert into Dormitory values('0810', 'GX1', 4);
insert into Dormitory values('1116', 'GX1', 4);

insert into Building values('GX1', '高新1号楼');
insert into Building values('GX2', '高新2号楼');

insert into Repair values('202406114514', 'RP21114514', 'GX2', '0114', 'T', '宿舍太臭了', 'PB19114514');
insert into Repair values('202406114515', 'RP21114514', 'GX1', '1919', 'F', '床板坏了', 'PB20114514');

insert into Visitor values('202406114514', '先辈', '123456', '给男朋友过生日', 'GX2', '2024-06-11');
insert into Visitor values('202406114515', '后辈', '654321', '给女朋友过生日', 'GX1', '2024-06-11');

