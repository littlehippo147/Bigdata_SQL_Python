-- -- �׷� �Լ�
select count(0), count(1), count(100), count('a'), count(null) from dual;

-- �ұ׷� Grouping : GROUP BY
select department_id, count(*), avg(salary)
from employees;
/* column�� �Ӽ��� ���� �ʾƼ� ����� error -> ���ο� �� �ʿ� GROUP BY */
select department_id, count(*), round(avg(salary), 2)
from employees
group by department_id
order by department_id;
/* ������ order by�� �ʼ��� �ƴ� but ���� �ǹ������� �����ؼ� ������ ���� */

select department_id from employees group by department_id;
select distinct department_id from employees; /* �� �� ���� */

select department_id, job_id, count(*), round(avg(salary), 2)
from employees
-- where avg(salary) >= 10000
group by department_id, job_id
order by department_id, job_id;
/* where ������ �׷� �Լ� �� �� ����. �׷�ȭ ���� where �������� �����ϱ� ����
because �ؼ� ������ from -> (where -> group by) -> having -> order by -> select 
�׷� ����� ���� ������ having ���� �̿��� */

-- HAVING : �׷� ��� ����
select department_id, job_id, count(*), round(avg(salary), 2)
from employees
/* where department_id in (80, 90) 80, 90�� �����͸� ���� �̾Ƴ��� �׷�ȭ */
group by department_id, job_id
having avg(salary) >= 10000
/* having department_id in (80, 90) ��� �����͸� �׷�ȭ�ϰ� 80, 90�� �����͸� �̾Ƴ� */
order by department_id, job_id;
-- having �������� ���� column ���� �� �� ������ ���� �鿡�� ��ȿ��

-- �������� 5-1
select department_id, min(salary) MIN_SALARY, max(salary) MAX_SALARY, sum(salary) 
       SUM_SALARY, round(avg(salary), 0) AVG_SALARY, count(department_id) DEPT_CNT
from employees
group by department_id
order by department_id;
/* ����� Ǯ��
select department_id, round(min(salary)), round(max(salary)), round(sum(salary)), 
       round(avg(salary)), count(*)
from employees
group by department_id
order by department_id;
*/

-- �������� 5-2
select manager_id, min(salary)
from employees
where manager_id is not null
group by manager_id
having min(salary) > 6000
order by min(salary) desc;
/* ����� Ǯ��
select manager_id, min(salary)
from employees
where manager_id is not null
group by manager_id
having min(salary) > 6000
order by min(salary) desc;
*/

-- �������� 5-3
-- count �̿�
select count(*) "total", 
       count(decode(to_char(hire_date, 'yyyy'), 2002, hire_date, null)) "2002",
       count(decode(to_char(hire_date, 'yyyy'), 2003, hire_date, null)) "2003",
       count(decode(to_char(hire_date, 'yyyy'), 2004, hire_date, null)) "2004",
       count(decode(to_char(hire_date, 'yyyy'), 2005, hire_date, null)) "2005"
from employees;
-- sum �̿�
select count(*) "total", 
       sum(decode(to_char(hire_date, 'yyyy'), 2002, 1, 0)) "2002",
       sum(decode(to_char(hire_date, 'yyyy'), 2003, 1, 0)) "2003",
       sum(decode(to_char(hire_date, 'yyyy'), 2004, 1, 0)) "2004",
       sum(decode(to_char(hire_date, 'yyyy'), 2005, 1, 0)) "2005"
from employees;
/* ����� Ǯ��
select count(*),
 count(decode(to_char(hire_date, 'yyyy'), '2002', 'a', null)),
 �ݺ� 2003, 2004, 2005
 �Ǵ�
 sum(decode(to_char(hire_date, 'yyyy'), '2002', 1, 0)),
from employees
job_id ����
select job_id, count(*), count(decode(), , , null), ...
from employees
group by job_id;
*/

-- outer join hr DB example
select distinct department_id
from employees;
select * from departments;
select * from locations;
