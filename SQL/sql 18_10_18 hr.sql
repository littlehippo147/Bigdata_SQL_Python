-- -- 그룹 함수
select count(0), count(1), count(100), count('a'), count(null) from dual;

-- 소그룹 Grouping : GROUP BY
select department_id, count(*), avg(salary)
from employees;
/* column의 속성이 맞지 않아서 생기는 error -> 새로운 절 필요 GROUP BY */
select department_id, count(*), round(avg(salary), 2)
from employees
group by department_id
order by department_id;
/* 원래는 order by가 필수는 아님 but 현장 실무에서는 정렬해서 데이터 생성 */

select department_id from employees group by department_id;
select distinct department_id from employees; /* 둘 다 같다 */

select department_id, job_id, count(*), round(avg(salary), 2)
from employees
-- where avg(salary) >= 10000
group by department_id, job_id
order by department_id, job_id;
/* where 절에는 그룹 함수 쓸 수 없음. 그룹화 전에 where 조건절을 실행하기 때문
because 해석 순서가 from -> (where -> group by) -> having -> order by -> select 
그룹 결과의 조건 제한은 having 절을 이용함 */

-- HAVING : 그룹 결과 제한
select department_id, job_id, count(*), round(avg(salary), 2)
from employees
/* where department_id in (80, 90) 80, 90인 데이터만 먼저 뽑아내고 그룹화 */
group by department_id, job_id
having avg(salary) >= 10000
/* having department_id in (80, 90) 모든 데이터를 그룹화하고 80, 90인 데이터만 뽑아냄 */
order by department_id, job_id;
-- having 절에서도 단일 column 조건 쓸 수 있지만 성능 면에서 비효율

-- 연습문제 5-1
select department_id, min(salary) MIN_SALARY, max(salary) MAX_SALARY, sum(salary) 
       SUM_SALARY, round(avg(salary), 0) AVG_SALARY, count(department_id) DEPT_CNT
from employees
group by department_id
order by department_id;
/* 강사님 풀이
select department_id, round(min(salary)), round(max(salary)), round(sum(salary)), 
       round(avg(salary)), count(*)
from employees
group by department_id
order by department_id;
*/

-- 연습문제 5-2
select manager_id, min(salary)
from employees
where manager_id is not null
group by manager_id
having min(salary) > 6000
order by min(salary) desc;

-- 강사님 풀이
select manager_id, min(salary)
from employees
where manager_id is not null
group by manager_id
having min(salary) > 6000
order by min(salary) desc;


-- 연습문제 5-3
-- count 이용
select count(*) "total", 
       count(decode(to_char(hire_date, 'yyyy'), 2002, hire_date, null)) "2002",
       count(decode(to_char(hire_date, 'yyyy'), 2003, hire_date, null)) "2003",
       count(decode(to_char(hire_date, 'yyyy'), 2004, hire_date, null)) "2004",
       count(decode(to_char(hire_date, 'yyyy'), 2005, hire_date, null)) "2005"
from employees;
-- sum 이용
select count(*) "total", 
       sum(decode(to_char(hire_date, 'yyyy'), 2002, 1, 0)) "2002",
       sum(decode(to_char(hire_date, 'yyyy'), 2003, 1, 0)) "2003",
       sum(decode(to_char(hire_date, 'yyyy'), 2004, 1, 0)) "2004",
       sum(decode(to_char(hire_date, 'yyyy'), 2005, 1, 0)) "2005"
from employees;

-- 강사님 풀이
select count(*),
 count(decode(to_char(hire_date, 'yyyy'), '2002', 'a', null)),
 반복 2003, 2004, 2005
 또는
 sum(decode(to_char(hire_date, 'yyyy'), '2002', 1, 0)),
from employees
job_id 별로
select job_id, count(*), count(decode(), , , null), ...
from employees
group by job_id;


-- outer join hr DB example
select distinct department_id
from employees;
select * from departments;
select * from locations;
