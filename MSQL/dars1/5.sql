show  databases;
create  database  Malumot;
use  Malumot;
select database();
show tables;

create  table oquv(
    id  int auto_increment  primary  key,
    ism  TEXT,
    yil  timestamp
);

show  tables;
desc  oquv;
select *from  oquv;

insert  into  oquv(ism,  yil)  values 
    ("Jasur", '1993-09-01  08:40:34'),
    ("Elbek", '2002-03-23  11:30:04'),
    ("Temur", '2001-10-10  18:10:34'),
    ("Dima",  '1992-12-02  23:40:00'),
    ("Dew",   '1998-02-12  20:13:54');

select *from  oquv;
select *from  oquv  order by  yil;
select *from  oquv  order by  yil  desc;
select *from  oquv  order by  id;
select *from  oquv  order by  ism;

select  *,  Year(yil) from oquv;
select  *,  Year(yil)  as  yilni_ozi from oquv;

select  *from  oquv  where (Year(now()) - Year(yil)) > 23;
select  *from  oquv  where (Year(now()) - Year(yil)) < 24;
select  *from  oquv  where (Year(now()) - Year(yil)) = 23;

select  *  from  oquv;

 select concat(ism  ,  yil )   as  ism_yil  from  oquv; 
 select id , concat(ism  ,  yil )   as  ism_yil  from  oquv; 
 select concat(ism  , "  " ,   yil )   as  ism_yil  from  oquv;
 select id, concat(ism  , "  " , yil )   as  ism_yil  from  oquv;
 select id, concat(ism  , "  " , yil ) as ism_yil from oquv order by ism;

 select  sum(ball) from  xn2   WHERE  ball = 2;
 select  sum(ball) from  xn2   WHERE  ism  like  "M%";
