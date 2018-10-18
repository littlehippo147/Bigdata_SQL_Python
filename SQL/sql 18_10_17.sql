select 100 + '200' from dual; /* ���� ���� -> 100 + to_number('200') ��� ���� */
select 100 + 'A' from dual; /* ���� -> to_number('A')���� type error */

-- ����Ŭ������ ���� ���ڸ� ���ڷ� ��ȯ��Ű���� ������ ŭ
select department_id, first_name, hire_date
from employees
where department_id = '30'; /* '30' -> 30 */
-- like�� ���� �����Ϳ��� �� �� �ִ� �������̹Ƿ� �����͸� ���ڷ� ��ȯ���Ѽ� ��
select department_id, first_name, hire_date
from employees
where department_id like '3%'; /* department_id -> to_char(department_id) */

-- -- �� �������� �º����� �������� ���� ������ column�� ���ִ� ���� ���� Best!
-- �Ͻ��� ������ ���� ��ȯ : �������� �ڵ����� ��ȯ
-- ����� ������ ���� ��ȯ : ��ȯ �Լ��� ����Ͽ� ����

-- ��¥ �����Ϳ� to_char �Լ� ���
select sysdate, to_char(sysdate) from dual;
select sysdate, to_char(sysdate, 'YYYY/MM/DD'), to_char(sysdate, 'YEAR  MM  DD')
from   dual;
select sysdate, to_char(sysdate, 'YYYY/MM/DD HH:MI:SS am'),
       to_char(sysdate, 'YYYY/MM/DD HH24:MI:SS')
from   dual;
select sysdate, to_char(sysdate, 'YEAR Year year'), to_char(sysdate, 'MONTH Month month'),
       to_char(sysdate, 'MON Mon mon'), to_char(sysdate, 'DAY, Day, day'), to_char(sysdate, 'DY, Dy, dy')
from   dual;
select sysdate, to_char(sysdate, 'D') from dual;

-- fm ����
select hire_date, to_char(hire_date, 'yyyy/mm/dd'), to_char(hire_date, 'Month Day yyyy'),
       to_char(hire_date, 'DD Month yyyy'), to_char(hire_date, 'fmDD Month yyyy')
from   employees
select to_char(sysdate, 'dd'), to_char(sysdate, 'ddsp'), to_char(sysdate, 'ddspth')
from dual;

-- ���� �����Ϳ� to_char �Լ� ���
select salary, to_char(salary, '$9,999') sal1,
       to_char(salary, 'L999,999,999') sal2,
       to_char(salary, 'L000,000,000') sal3,
       to_char(salary, 'L099,999,999') sal4
from employees;       

select salary, to_char(salary, '$9,999.99') sal1,
       to_char(salary, 'L999,999.99') sal2,
       to_char(salary, 'L000,000.99') sal3,
       to_char(salary, 'L099,999.99') sal4
from employees;

-- to_number
select 100 + to_number('5000', '9999') from dual;
select 100 + to_number('5,000', '9,999') from dual;
select 100 + '5000' from dual;
/* select 100 + '5,000' from dual; ���� */

select first_name, hire_date
from employees
-- where hire_date = to_date('2002/06/07', 'yyyy mm dd');
where hire_date = to_date('07 JUNE/2002', 'dd MONTH/yyyy');

----------------
update employees set hire_date = sysdate
where employee_id = 166;
commit;

-- sysdate ���� �ð� �κ��� �ٸ��� �ٸ� ������ ����
select employee_id, to_char(hire_date, 'yyyy/mm/dd hh:mi:ss')
from employees;

select employee_id, first_name, hire_date
from employees
-- where round(hire_date, 'DAY') = to_date(round(sysdate, 'DAY'), 'DD-MON-YY'); << �� ���
/* �� ����
where hire_date >= to_date('2018/10/17', 'yyyy/mm/dd')
and hire_date < to_date('2018/10/18', 'yyyy/mm/dd');
where hire_date between to_date('2018/10/17', 'yyyy/mm/dd') and to_date('2018/10/18', 'yyyy/mm/dd'); 
�Ǵ� 
select employee_id, first_name, hire_date
from employees
where to_char(hire_date, 'yyyy/mm/dd') = '2018/10/17'; << �߿��� ��� ***
*/
-- ���� ������ ã��
select first_name, hire_date
from employees
where to_char(hire_date, 'yyyy') = '2008';

-- -- ��Ÿ �Լ� NULL ���� ����
-- 1. NVL
select salary, commission_pct, salary + commission_pct /* null ���� �ϳ��� ������ ����� null */
from employees;
select salary, commission_pct, salary + commission_pct, nvl(salary, 0) + nvl(commission_pct, 0)
from employees;

-- 2. NVL2, NULLIF, COALESCE
select nvl2(100, 'A', 'B'), nvl2(null, 10, 20) from dual; /* NVL2*/
select nullif(100, 100), nullif( 'A', 'B') from dual; /*nullif */
select coalesce(1, 2, 3), coalesce(null, 2, 3), coalesce(null, null, 3), coalesce(null, null, null) from dual;

-- 3. GREATEST, LEAST
select greatest('HA', 'HE', 'HI'), least(10, 20, 30) from dual;

-- 4. ���Ǻ� ǥ���� DECODE �Լ�, CASE ��
select first_name, job_id, salary,
       decode(job_id, 'SA_REP', 'SR',
                      'IT_PROG', 'IP',
                      'SH_CLERK', 'SC', 'OTHERS') decode_nm,
       case job_id when 'SA_REP' then 'SR'
                   when 'IT_PROG' then 'IP'
                   when 'SH_CLERK' then 'SC' 
                   else 'OTHERS' end case_nm,
       case when job_id = 'SA_REP' then 'SR'
            when job_id = 'IT_PROG' then 'IP'
            when job_id = 'SH_CLERK' then 'SC' 
            else 'OTHERS' end "case_nm2",
       case when salary <= 5000 then 'low'
            when salary > 5000 and salary <= 10000 then 'med'
            when salary > 10000 and salary <= 20000 then 'high'
            -- when salary > 20000 then 'very high' ��� ���� 
            else 'very high' end salary_nm
from employees;

-- �������� 4-1
select last_name || ' earns ' || to_char(salary, '$99,999') || ' monthly but wants ' 
       || to_char(3 * salary, '$99,999') "Dream Salaries"
from   employees;
/* ����� Ǯ��
select last_name || ' earns ' || to_char(salary, 'fm$999,999,999') || 
       ' monthly but wants ' || to_char(salary * 3, 'fmL999,999,999') "Dream Salaries"
from employees;
*/

-- �������� 4-2
select last_name, first_name, nvl(to_char(commission_pct, '.9'), 'No Commission') "COMM"
from employees;
/* ����� Ǯ��
select last_name, first_name, nvl(to_char(commission_pct), 'No Commission') "COMM"
       case when commission_pct is not null then to_char(commission_pct) else 'No Commission' end
from employees;
*/

-- �������� 4-3
select last_name, hire_date, to_char(hire_date, 'Day') DAY
from employees
-- order by case to_char(hire_date, 'D') when '1' then '8' else to_char(hire_date, 'D') end;
order by decode(to_char(hire_date, 'D'), '1', '8', to_char(hire_date, 'D'));
/* ����� Ǯ��
select last_name, hire_date, to_char(hire_date, 'Day')
from employees
order by to_char(hire_date-1, 'd');
*/

--
select salary, to_char(salary, 'L999,999'), to_char(salary, '$999,999')
from employees;

-- -- �׷��Լ�
select count(salary), sum(salary), avg(salary), min(salary), max(salary)
from employees;

select count(commission_pct), sum(commission_pct)
from employees;

select count(*), count(commission_pct), count(distinct department_id) 
from employees;
-- *�� ���� �Ͽ� ��� ���� counting �ض�

select distinct department_id, job_id
from employees
order by department_id, job_id;
-- ���յ� ���� ���� �ߺ� ����

select count(salary), count(commission_pct), 
       avg(salary), avg(commission_pct), avg(nvl(commission_pct, 0))
from employees;
-- null ���� ��� ���� ��ü�� ���� ����� ���Ϸ��� nvl ���