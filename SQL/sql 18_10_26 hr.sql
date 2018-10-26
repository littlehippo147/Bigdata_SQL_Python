update departments set department_name = 'Accounting'
where department_id = 110;
commit;

-- �������� 1
select *
from (select e.department_id, d.department_name, round(avg(salary)) "��ձ޿�"
      from  employees e join departments d
      on e.department_id = d.department_id
      group by e.department_id, d.department_name
      order by 3 desc)
where rownum <= 1;

-- ����� Ǯ��
select department_id, avg(salary) from employees
group by department_id
order by 2 desc; /* ��� �޿� ���� ���� �μ� ã�� ���� ã�� */
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

-- �������� 2
select job_id, count(*) "��� ��"
from employees e join departments d
on e.department_id = d.department_id
and department_name in ('Accounting', 'Shipping')
group by job_id;

-- ����� Ǯ��
select job_id, count(*)
from employees
where department_id in (select department_id
                        from departments
                        where department_name in ('Accounting', 'Shipping'))
group by job_id;
 --
select job_id, count(*) "��� ��"
from employees e, departments d
where e.department_id = d.department_id
and department_name in ('Accounting', 'Shipping')
group by job_id;


-- �������� 3
select *
from (select e.department_id, d.department_name, count(*) "��� ��"
      from departments d join employees e
      on e.department_id = d.department_id
      group by e.department_id, d.department_name
      order by 3 desc)
where rownum = 1;

-- ����� Ǯ��
select e.department_id, department_name, count(*) 
from departments d, employees e
where d.department_id = e.department_id
group by e.department_id, department_name
having count(*) = (select max(count(*)) from employees
                   group by department_id);

-- �������� 4
select m.employee_id "������ ID", m.first_name "������ �̸�", m.salary "������ �޿�", e.first_name "��������"
from employees e, employees m
where e.manager_id = m.employee_id
and m.salary >= 15000
order by m.employee_id;


-- ����� Ǯ��
select e.employee_id, e.first_name, m.salary, m.employee_id, m.first_name, e.salary
from employees e, employees m
where e.manager_id = m.employee_id
and m.salary >= 15000
order by m.employee_id;

-- �������� 5
select first_name, to_char(hire_date, 'DY') "����"
from employees                           /* �� �ٺ����� �� �� �� ��  */
where to_char(hire_date, 'DY') in (select "����" from (select to_char(hire_date, 'DY') "����", count(*) "��� ��" from employees
                                                      group by to_char(hire_date, 'DY')
                                                      having count(*) = (select max(count(*)) from employees 
                                                                         group by to_char(hire_date, 'DY'))));

-- ����� Ǯ��
select first_name, to_char(hire_date, 'day')
from employees
where to_char(hire_date, 'day') in (select to_char(hire_date, 'day') from employees
                                                      group by to_char(hire_date, 'day')
                                                      having count(*) = (select max(count(*)) from employees 
                                                                         group by to_char(hire_date, 'day')));

