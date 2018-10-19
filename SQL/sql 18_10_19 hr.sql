select * from departments;
select * from locations;
select * from employees;

-- �������� 6-1
select e.last_name, e.job_id, e.department_id, d.department_name
from   employees e join departments d
on     e.department_id = d.department_id
join   locations l /* join�� ������ �ٲ� �� �ִ� */
on     d.location_id = l.location_id
and    l.city = 'Toronto';
/* ����� Ǯ��1
select last_name, job_id, d.department_id, department_name
from   employees e, departments d
where  e.department_id = d.department_id
and    d.location_id = 1800; << location�� ��� �ٲ�� ��� ���
 Ǯ�� 2
select last_name, job_id, d.department_id, department_name
from   employees e, departments d, locations l
where  e.department_id = d.department_id
and    d.location_id = l.location_id
and    l.city = 'Toronto';
 �߰� Ǯ�� : join�� ���� �ٿ� ���൵ on ���� ���� �� ��ŭ ���ָ� ��
select e.last_name, e.job_id, e.department_id, d.department_name
from   employees e join departments d join locations l
on     d.location_id = l.location_id
and    l.city = 'Toronto'
on     e.department_id = d.department_id;
*/

-- �������� 6-2
select e1.employee_id, e1.last_name, e1.manager_id, e2.last_name mng_ln
from   employees e1 join employees e2
on     e1.manager_id = e2.employee_id;
/* ����� Ǯ��
select e.employee_id, e.last_name, e.manager_id, m.last_name
from   employees e, employees m
where  e.manager_id = m.employee_id;
*/

-- �������� 6-3
select e1.employee_id, e1.last_name, e1.manager_id, e2.last_name mng_ln
from   employees e1 left outer join employees e2
on     e1.manager_id = e2.employee_id;
/* ����� Ǯ��
select e.employee_id, e.last_name, e.manager_id, m.last_name
from   employees e, employees m
where  e.manager_id = m.employee_id(+);
*/

-- -- -- Chapter 7 subquery
-- SELECT ��
select first_name, salary, (select round(avg(salary)) from employees) avg_sal
from employees;

select rowid, rownum, department_id, department_name
from departments
where rownum = 3; /* �̰�� ������ return �ȵ� 1�� �� */
/* rowid(���� ��ġ �ּҰ�), rownum�� ����� ��, but ���� ���鿡�� rownum ���� ����. */

-- FROM ��
-- -- ���� 3���� ǥ���϶�?
select department_id, round(avg(salary)) dp_sal
from employees
-- where rownum <= 3
group by department_id
-- having rownum <=3
order by dp_sal desc;
/* �� ���ô� �� �ȵ� �Ʒ� ���� ��� */

select *
from (select department_id, round(avg(salary)) dp_sal
      from employees
      group by department_id
      order by dp_sal desc)
where rownum <= 3;

-- where ��
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
-- in�� �Ἥ EXISTS�� ���� ���� �����
select employee_id, salary, last_name
from employees
where employee_id in (select distinct manager_id from employees);

-- �ݴ�
select employee_id, salary, last_name
from employees
where employee_id not in (select distinct manager_id from employees
                          where manager_id is not null);
select employee_id, salary, last_name
from employees m
where not exists (select employee_id from employees w
                  where w.manager_id = m.employee_id);

-- �������� 7-1
select first_name, salary, hire_date
from   employees
where  manager_id = (select employee_id from employees where first_name = 'Adam');
/* ����� Ǯ�� : Adam�� �Ѹ��� �ƴ� �� �ֱ� ������ in�� ���־���Ѵ�.
select first_name, salary, hire_date
from employees
where manager_id in (select employee_id from employees where first_name = 'Adam');
*/

-- �������� 7-2
select employee_id, last_name, first_name, salary
from   employees
where  salary > (select avg(salary) from employees)
and    department_id in (select department_id from employees 
                         where last_name like '%u%');
/* ����� Ǯ��
select employee_id, last_name, first_name, salary
from   employees
where  salary > (select avg(salary) from employees)
and    department_id in (select department_id from employees 
                         where last_name like '%u%');
*/

-- �������� 7-3
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
/* ����� Ǯ��
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


