show  databases ;

Drop  database xn2;
Drop  database tatu;

create  database  Foundation;
use  Foundation;
select  database();

create table xn1(
    id  int  auto_increment primary key,
    ism Varchar(30),
    familya  TEXT,
    ball  int
);

desc  xn1;


insert  into  xn1( ism,  familya,  ball) values  ("Muhriddin",  "Sobirjonov",  94);
insert  into  xn1( ism,  familya,  ball) values  ("Muhammadrasul",  "Shixnazarov",  94);
insert  into  xn1( ism,  familya,  ball) values  ("Ortiqbek",  "Sherov",  94);
insert  into  xn1(ism,  familya,  ball) values  ("Ruxsora",  "O'rinboyeva",  94);
insert  into  xn1( ism,  familya,  ball) values  ("Dildora", "Sadikova",  94);
insert  into  xn1( ism,  familya,  ball) values  ("SHOXISTA", "TANGIRBERGANOVA" ,  94);

select  *from  xn1;
select  ism  from  xn1;
select *from xn1  order by  ism;
SELECT  *FROM xn1 WHERE LENGTH(ism) < 8;
SELECT  ism,  ball FROM xn1 WHERE LENGTH(ism) < 8;

SELECT  *FROM xn1 WHERE ism  = "Muhammadrasul" ;
SELECT  *FROM xn1 WHERE ball  = 94 ;

SELECT  *FROM xn1 WHERE ism like "%a";
SELECT  *FROM xn1 WHERE ism like "M%";

SELECT  *FROM xn1 WHERE ism like "%a_";
SELECT  *FROM xn1 WHERE ism like "_a%";
SELECT  *FROM xn1 WHERE ism like "__a%";


UPDATE  xn2 SET  ball = 87  WHERE ism LIKE "Muhriddin";
UPDATE  xn2 SET  ball = 77  WHERE ism LIKE "Muhammadrasul";

SELECT  count(*) FROM  xn2 WHERE  ball  = 94;

DELETE FROM  xn1 WHERE  familya  LIKE  "Sherov";  --!  Bittalab  o'chirish 

DELETE FROM  xn1 id;  -- !  Barchasini  o'chirish  
   -- id  int  auto_increment primary key,

   