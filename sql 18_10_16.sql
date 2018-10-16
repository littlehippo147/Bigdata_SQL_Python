-- escape �ĺ��� ����
select employee_id, last_name, job_id
from employees
where job_id like '%SA\_%' escape '\';

-- null �� ã��
select last_name, first_name, job_id, commission_pct
from employees
where commission_pct is null;

-- �� ������
select employee_id, last_name, job_id, salary
from employees
where salary >= 10000
and job_id like '%MAN%';

select employee_id, last_name, job_id, salary
from employees
where salary >= 10000
or job_id like '%MAN%';

-- OR�� in
select last_name, job_id, salary
from employees
where (job_id = 'SA_REP' or job_id = 'AD_PRES')
and salary > 15000;

select last_name, job_id, salary
from employees
where job_id in ('SA_REP', 'AD_PRES')
and salary > 15000;

-- ���� order by, desc, nulls
select last_name, first_name, salary "�޿�"
from   employees
order by commission_pct nulls first;

select last_name, first_name, salary
from   employees
order by salary desc;

select department_id, last_name, first_name, salary
from employees
order by department_id nulls first;

select department_id, last_name, first_name, salary
from employees
order by department_id desc;

select department_id, salary, last_name, first_name
from employees
order by department_id, salary;

select department_id, salary, last_name, first_name
from employees
order by department_id, salary desc;

select department_id, salary, last_name, first_name
from employees
order by department_id desc, salary;

select department_id, salary, last_name, first_name
from employees
order by department_id desc, salary desc;

/* �ȵǴ� ���� */
select department_id, salary �޿�, �޿� + 100 last_name, first_name
from employees
order by department_id desc, salary desc;

select department_id, salary �޿�, last_name, first_name
from employees
where �޿� > 5000
order by department_id desc, salary desc;
/**/

/* order by���� ���ο� �� �Ӹ��� �� �� ��ȣ Ȱ�� ���� */
select department_id, salary �޿�, last_name, first_name
from employees
order by department_id desc, �޿� desc;

select department_id, salary, last_name, first_name
from employees
order by 1 desc, 2 desc;
/**/

-- �������� 2-1
select last_name, first_name, hire_date, salary
from employees
where salary not between 5000 and 12000;

-- �������� 2-2
select last_name, job_id, hire_date
from employees
where last_name in ('Matos', 'Taylor')
order by hire_date;

-- �������� 2-3
select last_name, salary, commission_pct
from employees
where commission_pct is not null
order by salary desc, commission_pct desc;

-- �������� 2-4
select last_name, first_name
from employees
where last_name like '__a%'
or last_name like '__e%';

-- �������� 2-5
select last_name, job_id, salary
from employees
where job_id in ('SA_MAN', 'ST_CLERK')
and salary not in (2500, 3500, 7000);

-- chapter 3. ���� �� �Լ�
-- -- ���� �Լ�
-- -- -- ��ҹ��� ��ȯ �Լ� : �ַ� where���� ����
select last_name, first_name, upper(last_name), lower(first_name), initcap('abc def')
from   employees;

-- -- -- ���� ���� �Լ�
-- 1. concat
select last_name, first_name, concat(last_name, first_name) "Full name"
from employees;
/* concat�� ���ڸ� 2������ �ۿ� ������*/
--select last_name, first_name, concat(last_name, ' ', first_name) "Full name"
select last_name, first_name, concat(concat(last_name, ' '), first_name) "Full name"
from employees;
select last_name, first_name, last_name || ' ' || first_name "Full name"
from employees;

-- 2. substr
select last_name, first_name, concat(last_name, first_name) "Full name", 
       substr(concat(last_name, first_name), 1, 3) sub1, substr(concat(last_name, first_name), 5, 4) sub2, 
       substr(concat(last_name, first_name), -6, 2) sub3
from employees;
  /* �������� 2-4 substr �̿��� ��� */
  select last_name, first_name
  from   employees
  where  substr(last_name, 3, 1) in ('a', 'e')

-- 3. length
select last_name, first_name, length(first_name) "Length", concat(last_name, first_name) "Full name", 
       substr(concat(last_name, first_name), 1, 3) sub1, substr(concat(last_name, first_name), 5, 4) sub2, 
       substr(concat(last_name, first_name), -6, 2) sub3
from employees;

-- 4. instr : ���ڿ� index ����
select last_name, first_name, concat(last_name, first_name) "Full name",
       instr(concat(last_name, first_name), 'e', 1, 1) instr1,
       instr(concat(last_name, first_name), 'e', 7, 1) instr2,
       instr(concat(last_name, first_name), 'e', 1, 2) instr3
from   employees;

-- 5. lpad
select last_name, first_name, concat(last_name, first_name) "Full name",
       lpad(first_name, 20, ' ') lpad, rpad(last_name, 20, ' ') rpad,
       instr(concat(last_name, first_name), 'e', 1, 1) instr1,
       instr(concat(last_name, first_name), 'e', 7, 1) instr2,
       instr(concat(last_name, first_name), 'e', 1, 2) instr3
from   employees;

-- 6. replace
select last_name, first_name, concat(last_name, first_name) "Full name",
       replace(concat(last_name, first_name), 'ra', '@') rep
from   employees

-- 7. trim : �� �� Ư�� ���� ����
select last_name, first_name, upper(concat(last_name, first_name)) "Full name",
       trim('D' from upper(concat(last_name, first_name))) trim
from   employees;

-- -- ���� �Լ�
-- 1. round
select round(456.789), round(456.789, 0), round(456.789, 1), round(456.789, 2),
       round(456.789, -1), round(456.789, -2) from dual;

-- 2. trunc
select trunc(456.789), trunc(456.789, 0), trunc(456.789, 1), trunc(456.789, 2),
       trunc(456.789, -1), trunc(456.789, -2) from dual;

-- 3. mod, sign
select mod(20, 4), mod(20, 3), mod(20, 7), mod(20, -3), 20/7, 
       sign(50), sign(-10), sign(0) from dual;

-- -- ��¥ �Լ�
/* ��¥ �ð� ���� �ٲٱ� */
alter session set nls_date_format = 'yyyy/mm/dd hh24:mi:ss';
alter session set nls_date_format = 'DD-MON-RR';
/* alter�� �⺻�� �� ������ �� �� */ 

-- -- -- ��¥ ������ ����
select sysdate, sysdate + 1/24, sysdate - 1/24 from dual;
select sysdate, sysdate + 30/1440, sysdate - 30/1440 from dual;
select sysdate + 1, sysdate, (sysdate + 1) - sysdate from dual;
-- select sysdate + 1, sysdate, (sysdate + 1) + sysdate from dual; << ��¥������ ������ �ȵ�

-- -- -- ��¥ ���� �Լ�
-- 1. months_between(�ֱ� ��¥, ���� ��¥)
select first_name, months_between(sysdate, hire_date) "�ټ� ����"
from   employees;
-- 2. add_months, next_day(��¥, '����'), last_day
select sysdate, add_months(sysdate, 2), next_day(sysdate, 'FRIDAY') ,
       last_day(sysdate) from dual;
--3. ��¥ round, trunc
select sysdate, round(sysdate, 'dd'), round(sysdate, 'mm'),
       trunc(sysdate, 'dd'), trunc(sysdate, 'mm') from dual;
       
-- -- -- ��¥ �Լ�
alter session set time_zone = '+9:00';
select sysdate, current_date, systimestamp, current_timestamp from dual;

alter session set time_zone = '-7:00';
select sysdate, current_date, systimestamp, current_timestamp from dual;

-- �������� 3-1
select employee_id, last_name, salary, round(salary * 1.155) "New Salary"
from employees;
select employee_id, last_name, salary, trunc(salary * 1.155) "New Salary"
from employees;

-- �������� 3-2
select initcap(first_name) "Name", length(first_name) "Length"
from employees
where substr(first_name, 1, 1) in ('J', 'A', 'M');
/* where instr(first_name, 'J', 1, 1) = 1
   or    instr(first_name, 'A', 1, 1) = 1
   or    instr(first_name, 'M', 1, 1) = 1 */

-- �������� 3-3
select last_name, round(months_between(sysdate, hire_date)) "MONTHS_WORKED"
from employees
order by MONTHS_WORKED;
/* order by 2; */