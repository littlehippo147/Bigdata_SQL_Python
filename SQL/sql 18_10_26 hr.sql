update departments set department_name = 'Accounting'
where department_id = 110;
commit;

-- 연습문제 1
select *
from (select e.department_id, d.department_name, round(avg(salary)) "평균급여"
      from  employees e join departments d
      on e.department_id = d.department_id
      group by e.department_id, d.department_name
      order by 3 desc)
where rownum <= 1;

-- 강사님 풀이
select department_id, avg(salary) from employees
group by department_id
order by 2 desc; /* 평균 급여 가장 높은 부서 찾고 직접 찾기 */
select e.department_id, d.department_name, round(avg(salary))
from  employees e, departments d
where e.department_id = d.department_id
and e.department_id = 90
group by e.department_id, d.department_name; 
 --
select e.department_id, d.department_name, round(avg(salary))
from  employees e, departments d
where e.department_id = d.department_id
group by e.department_id, d.department_name
having avg(salary) = (select max(avg(salary))
                      from employees
                      group by department_id);

-- 연습문제 2
select job_id, count(*) "사원 수"
from employees e join departments d
on e.department_id = d.department_id
and department_name in ('Accounting', 'Shipping')
group by job_id;

-- 강사님 풀이
select job_id, count(*)
from employees
where department_id in (select department_id
                        from departments
                        where department_name in ('Accounting', 'Shipping'))
group by job_id;
 --
select job_id, count(*) "사원 수"
from employees e, departments d
where e.department_id = d.department_id
and department_name in ('Accounting', 'Shipping')
group by job_id;


-- 연습문제 3
select *
from (select e.department_id, d.department_name, count(*) "사원 수"
      from departments d join employees e
      on e.department_id = d.department_id
      group by e.department_id, d.department_name
      order by 3 desc)
where rownum = 1;

-- 강사님 풀이
select e.department_id, department_name, count(*) 
from departments d, employees e
where d.department_id = e.department_id
group by e.department_id, department_name
having count(*) = (select max(count(*)) from employees
                   group by department_id);

-- 연습문제 4
select m.employee_id "관리자 ID", m.first_name "관리자 이름", m.salary "관리자 급여", e.first_name "부하직원"
from employees e, employees m
where e.manager_id = m.employee_id
and m.salary >= 15000
order by m.employee_id;


-- 강사님 풀이
select e.employee_id, e.first_name, m.salary, m.employee_id, m.first_name, e.salary
from employees e, employees m
where e.manager_id = m.employee_id
and m.salary >= 15000
order by m.employee_id;

-- 연습문제 5
select first_name, to_char(hire_date, 'DY') "요일"
from employees                           /* ↓ 바보같이 한 번 더 씀  */
where to_char(hire_date, 'DY') in (select "요일" from (select to_char(hire_date, 'DY') "요일", count(*) "사원 수" from employees
                                                      group by to_char(hire_date, 'DY')
                                                      having count(*) = (select max(count(*)) from employees 
                                                                         group by to_char(hire_date, 'DY'))));

-- 강사님 풀이
select first_name, to_char(hire_date, 'day')
from employees
where to_char(hire_date, 'day') in (select to_char(hire_date, 'day') from employees
                                                      group by to_char(hire_date, 'day')
                                                      having count(*) = (select max(count(*)) from employees 
                                                                         group by to_char(hire_date, 'day')));

