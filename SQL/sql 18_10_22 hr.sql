-- 전통적인 join
select first_name, salary, j.job_id, job_title
from employees e, jobs j
where e.job_id = j.job_id;
-- ANSI의 표준 join
select first_name, salary, j.job_id, job_title
from employees e join jobs j
on e.job_id = j.job_id;

select first_name, salary, d.department_id, department_name
from employees e, departments d
where e.department_id = d.department_id(+);

-- -- -- Chapter 8 집합 연산자
-- UNION
select department_id, job_id, salary 
from employees
where salary between 4000 and 6000
union /* 중복 제거, 자동정렬 */
select department_id, job_id, salary 
from employees
where department_id = 20;
-- UNION ALL
select department_id, job_id, salary 
from employees
where salary between 4000 and 6000
union all
select department_id, job_id, salary 
from employees
where department_id = 20;
-- INTERSECT
select department_id, job_id, salary 
from employees
where salary between 4000 and 6000
intersect
select department_id, job_id, salary 
from employees
where department_id = 20;
-- MINUS
select department_id, job_id, salary 
from employees
where salary between 4000 and 6000
minus
select department_id, job_id, salary 
from employees
where department_id = 20;
/* select 순서 바꾸기 */
select department_id, job_id, salary 
from employees
where department_id = 20
minus
select department_id, job_id, salary 
from employees
where salary between 4000 and 6000;

-- 첫번째 select 열로 표현
select employee_id, first_name, salary
from employees
union
select department_id, department_name, null
from departments;

select employee_id, first_name, salary
from employees
union all
select department_id, department_name, null
from departments;

-- ORDER BY보다 집합 연산자 먼저 처리. ORDER BY는 맨 마지막
select employee_id, first_name, salary
from employees
union
select department_id, department_name, null
from departments
order by first_name;


-- 연습문제 8-1
select distinct job_id, department_id
from employees
where department_id = 10
union all
select distinct job_id, department_id
from employees
where department_id = 50
union all
select distinct job_id, department_id
from employees
where department_id = 20;
/* 강사님 풀이
select distinct job_id, department_id
from employees
where department_id = 10
union all
select distinct job_id, department_id
from employees
where department_id = 50
union all
select distinct job_id, department_id
from employees
where department_id = 20;
*/

-- 연습문제 8-2
select department_id, job_id, sum(salary)
from employees
where department_id in (10, 20, 30)
group by rollup(department_id, job_id);
/* 강사님 풀이
select department_id, job_id, sum(salary)
from employees
where department_id = 10
group by department_id, job_id
union all
select department_id, null, sum(salary)
from employees
where department_id = 10
group by department_id
union all
select department_id, job_id, sum(salary)
from employees
where department_id = 20
group by department_id, job_id
union all
select department_id, null, sum(salary)
from employees
where department_id = 20
group by department_id
union all
select department_id, job_id, sum(salary)
from employees
where department_id = 30
group by department_id, job_id
union all
select department_id, null, sum(salary)
from employees
where department_id = 30
group by department_id
union all
select null, null, sum(salary)
from employees
where department_id in(10, 20, 30);
*/