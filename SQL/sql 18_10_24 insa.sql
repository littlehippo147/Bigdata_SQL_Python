create table emp1 (
 empno number(4)      primary key,
 ename varchar2(30)   not null);
 
 insert into emp1
 values (1, '¿Ã¡§»£');
 
 commit;
 
 select * from emp1;