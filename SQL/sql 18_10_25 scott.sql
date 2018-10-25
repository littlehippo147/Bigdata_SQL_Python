select * from dept_test;

update dept_test set loc = '서울';
-- 실수를 저장한 경우 rollback은 안됨
commit;

recyclebin;

-- 2018/10/25 14:47:27

select to_char(sysdate, 'yyyy/mm/dd hh24:mi:ss') from dual;

select * from emp;

-- 실수를 저장
delete emp 
where comm is null;

commit;

-- 시간 정보를 이용해 flashback. from 절의 AS OF TIMESTAMP
-- - 시간대를 직접 입력해서 사용하는 경우
select * 
from emp as of timestamp 
         to_date('2018/10/25 14:47:27', 'yyyy/mm/dd hh24:mi:ss')
where comm is null;

-- - 시간 연산 이용 : 제일 많이 이용함 
select * 
from emp as of timestamp sysdate - 20/1440
where comm is null;

-- - systimestamp 이용하는 경우
select * 
from emp as of timestamp systimestamp - interval '12' minute
where comm is null;

insert into emp
select * 
from emp as of timestamp sysdate - 20/1440
where comm is null;

select * from emp;

commit;

update emp set job = 'ADMIN'
where deptno = 30;

commit;

update emp e1 set job = 
(select job 
from emp as of timestamp sysdate - 24/1440 e2
where e1.empno = e2.empno);
