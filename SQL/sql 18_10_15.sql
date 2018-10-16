select *
from  employees;

select *
from  departments;

select last_name, first_name, hire_date
from  employees;

select salary, salary + 100, salary - 100, salary * 100, salary / 100 
from employees;

select hire_date, hire_date + 1, hire_date - 1
from  employees;

select hire_date, hire_date * 1, hire_date / 1
from  employees;

select last_name, salary 급여, commission_pct as "보너스", salary * commission_pct * 12 as "총 급여"
from employees;
  
select salary "sal", commission_pct as BONUS, salary * commission_pct * 12 as "총 급여"
from employees;
  
select last_name, first_name, job_id, last_name || first_name || job_id as "Name"
from employees;
  
select 100, 'AAA'
from employees;

select 100, 'AAA'
from dual;

select last_name, first_name, job_id, last_name || '의 이름은 ' || first_name || '이다.'
from employees;

select last_name, first_name, job_id, last_name || 's name is ' || first_name
from employees;

select last_name, first_name, job_id, last_name || '''s name is ' || first_name
from employees;

select last_name, first_name, job_id, last_name || q'['s name is ]' || first_name
from employees;

select distinct department_id
from employees;

select last_name, first_name, department_id
from employees
where department_id = 30;

select last_name, first_name, department_id
from employees
where 30 = department_id;


select last_name, first_name, department_id
from employees
where last_name = 'King';

select last_name, first_name, department_id, hire_date
from employees
where hire_date = '07-JUN-02';
--where hire_date = '2002/06/07';

select last_name, first_name, department_id, salary
from employees
where salary >= 5000
and salary <= 6000;

select last_name, first_name, department_id, salary
from employees
where salary between 5000 and 6000;

select last_name, first_name, department_id, salary
from employees
where department_id in (10, 20, 30);

select last_name, first_name, department_id, salary
from employees
where last_name like 'King';

select last_name, first_name, department_id, salary
from employees
where last_name like '__m%';

select last_name, first_name, department_id, salary
from employees
where department_id like '1%';
