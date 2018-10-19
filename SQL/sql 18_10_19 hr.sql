select * from departments;
select * from locations;
select * from employees;

-- 연습문제 6-1
select e.last_name, e.job_id, e.department_id, d.department_name
from   employees e join departments d
on     e.department_id = d.department_id
join   locations l /* join의 순서가 바뀔 수 있다 */
on     d.location_id = l.location_id
and    l.city = 'Toronto';
/* 강사님 풀이1
select last_name, job_id, d.department_id, department_name
from   employees e, departments d
where  e.department_id = d.department_id
and    d.location_id = 1800; << location이 계속 바뀌는 경우 곤란
 풀이 2
select last_name, job_id, d.department_id, department_name
from   employees e, departments d, locations l
where  e.department_id = d.department_id
and    d.location_id = l.location_id
and    l.city = 'Toronto';
 추가 풀이 : join을 같은 줄에 써줘도 on 절을 같은 수 만큼 써주면 됨
select e.last_name, e.job_id, e.department_id, d.department_name
from   employees e join departments d join locations l
on     d.location_id = l.location_id
and    l.city = 'Toronto'
on     e.department_id = d.department_id;
*/

-- 연습문제 6-2
select e1.employee_id, e1.last_name, e1.manager_id, e2.last_name mng_ln
from   employees e1 join employees e2
on     e1.manager_id = e2.employee_id;
/* 강사님 풀이
select e.employee_id, e.last_name, e.manager_id, m.last_name
from   employees e, employees m
where  e.manager_id = m.employee_id;
*/

-- 연습문제 6-3
select e1.employee_id, e1.last_name, e1.manager_id, e2.last_name mng_ln
from   employees e1 left outer join employees e2
on     e1.manager_id = e2.employee_id;
/* 강사님 풀이
select e.employee_id, e.last_name, e.manager_id, m.last_name
from   employees e, employees m
where  e.manager_id = m.employee_id(+);
*/

-- -- -- Chapter 7 subquery
-- SELECT 절
select first_name, salary, (select round(avg(salary)) from employees) avg_sal
from employees;

select rowid, rownum, department_id, department_name
from departments
where rownum = 3; /* 이경우 데이터 return 안됨 1만 됨 */
/* rowid(행의 위치 주소값), rownum은 허수의 열, but 성능 측면에서 rownum 종종 쓰임. */

-- FROM 절
-- -- 상위 3개만 표시하라?
select department_id, round(avg(salary)) dp_sal
from employees
-- where rownum <= 3
group by department_id
-- having rownum <=3
order by dp_sal desc;
/* 위 예시는 다 안됨 아래 같이 사용 */

select *
from (select department_id, round(avg(salary)) dp_sal
      from employees
      group by department_id
      order by dp_sal desc)
where rownum <= 3;

-- where 절
select employee_id, first_name, salary
from employees
where salary > (select round(avg(salary)) from employees);

-- IN
select employee_id, last_name, first_name, salary
from employees
where salary in (select salary from employees
                 where last_name = 'Grant')
and last_name <> 'Grant';

-- ANY
select employee_id, last_name, job_id, salary
from employees
where salary < ANY
                  (select salary from employees where job_id = 'IT_PROG')
and job_id <> 'IT_PROG';                  

-- ALL
select employee_id, last_name, job_id, salary
from employees
where salary < ALL
                  (select salary from employees where job_id = 'IT_PROG')
and job_id <> 'IT_PROG';                  

-- EXISTS
select employee_id, salary, last_name
from employees m
where exists (select employee_id from employees w
              where w.manager_id = m.employee_id);
-- in을 써서 EXISTS와 같은 구문 만들기
select employee_id, salary, last_name
from employees
where employee_id in (select distinct manager_id from employees);

-- 반대
select employee_id, salary, last_name
from employees
where employee_id not in (select distinct manager_id from employees
                          where manager_id is not null);
select employee_id, salary, last_name
from employees m
where not exists (select employee_id from employees w
                  where w.manager_id = m.employee_id);

-- 연습문제 7-1
select first_name, salary, hire_date
from   employees
where  manager_id = (select employee_id from employees where first_name = 'Adam');
/* 강사님 풀이 : Adam이 한명이 아닐 수 있기 때문에 in을 써주어야한다.
select first_name, salary, hire_date
from employees
where manager_id in (select employee_id from employees where first_name = 'Adam');
*/

-- 연습문제 7-2
select employee_id, last_name, first_name, salary
from   employees
where  salary > (select avg(salary) from employees)
and    department_id in (select department_id from employees 
                         where last_name like '%u%');
/* 강사님 풀이
select employee_id, last_name, first_name, salary
from   employees
where  salary > (select avg(salary) from employees)
and    department_id in (select department_id from employees 
                         where last_name like '%u%');
*/

-- 연습문제 7-3
-- not in
select department_id, department_name
from departments
where department_id not in (select distinct department_id from employees
                            where department_id is not null); 
-- not exists
select d.department_id, department_name
from departments d
where not exists (select e.department_id from employees e 
              where e.department_id = d.department_id);
/* 강사님 풀이
select department_id, department_name
from departments
where department_id not in (select distinct department_id 
                            from employees
                            where department_id is not null); 
select department_id, department_name
from departments d
where not exists (select 1 
                  from employees e 
                  where e.department_id = d.department_id);
*/


