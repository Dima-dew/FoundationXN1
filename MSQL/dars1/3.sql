show  databases;
use  xn2;
select  database();

show  tables;
desc  inson;
select *from  inson;

insert  into  inson values ("Jalol",  "Jamilov", 22),
("Islom",  "Rustamov", 12),
("Bobur",  "Jalolov", 32),
("Botir",  "Komilov", 32)

select  *from inson  order  by  yosh;
-- //!===================where===========================
select  *from inson  where yosh =  32;
select  *from inson  where yosh >= 12   and  yosh  < 20;
-- //!===================where=====between======================
select  *from inson  where yosh between   30;
 
-- int auto_increment primary key