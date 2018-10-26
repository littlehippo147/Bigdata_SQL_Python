select * from departments;

update departments set department_name = 'TEST'
where location_id = 1700;

commit;

update departments d1 
set department_name =(select department_name 
                      from   departments as of timestamp sysdate - 10/1440 d2
                      where  d1.department_id = d2.department_id);
                      
-- 연습문제 1
select * from employees
where hire_date >= to_date('2003/01/01', 'yyyy/mm/dd')
and   job_id = 'ST_CLERK';

-- -- 강사님 풀이
select *
from employees
where hire_date >= to_date('2003/01/01', 'yyyy/mm/dd')
and job_id = 'ST_CLERK';


-- 연습문제 2
select count(*) "사원 수"
from employees
where last_name like ('%n');

select count(*) "사원 수"
from employees
where substr(last_name, length(last_name), 1) = 'n';

-- 강사님 풀이


-- 연습문제 3
select first_name, hire_date
from employees
where to_char(hire_date, 'dd') < 16;

-- 강사님 풀이



-- 연습문제 4
select first_name, salary, round(salary/1000) "급여단위"
from employees;

-- 강사님 풀이

