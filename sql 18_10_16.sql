-- escape 식별자 지정
select employee_id, last_name, job_id
from employees
where job_id like '%SA\_%' escape '\';

-- null 값 찾기
select last_name, first_name, job_id, commission_pct
from employees
where commission_pct is null;

-- 논리 연산자
select employee_id, last_name, job_id, salary
from employees
where salary >= 10000
and job_id like '%MAN%';

select employee_id, last_name, job_id, salary
from employees
where salary >= 10000
or job_id like '%MAN%';

-- OR와 in
select last_name, job_id, salary
from employees
where (job_id = 'SA_REP' or job_id = 'AD_PRES')
and salary > 15000;

select last_name, job_id, salary
from employees
where job_id in ('SA_REP', 'AD_PRES')
and salary > 15000;

-- 정렬 order by, desc, nulls
select last_name, first_name, salary "급여"
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

/* 안되는 예시 */
select department_id, salary 급여, 급여 + 100 last_name, first_name
from employees
order by department_id desc, salary desc;

select department_id, salary 급여, last_name, first_name
from employees
where 급여 > 5000
order by department_id desc, salary desc;
/**/

/* order by문은 새로운 열 머리글 및 열 번호 활용 가능 */
select department_id, salary 급여, last_name, first_name
from employees
order by department_id desc, 급여 desc;

select department_id, salary, last_name, first_name
from employees
order by 1 desc, 2 desc;
/**/

-- 연습문제 2-1
select last_name, first_name, hire_date, salary
from employees
where salary not between 5000 and 12000;

-- 연습문제 2-2
select last_name, job_id, hire_date
from employees
where last_name in ('Matos', 'Taylor')
order by hire_date;

-- 연습문제 2-3
select last_name, salary, commission_pct
from employees
where commission_pct is not null
order by salary desc, commission_pct desc;

-- 연습문제 2-4
select last_name, first_name
from employees
where last_name like '__a%'
or last_name like '__e%';

-- 연습문제 2-5
select last_name, job_id, salary
from employees
where job_id in ('SA_MAN', 'ST_CLERK')
and salary not in (2500, 3500, 7000);

-- chapter 3. 단일 행 함수
-- -- 문자 함수
-- -- -- 대소문자 변환 함수 : 주로 where에서 쓰임
select last_name, first_name, upper(last_name), lower(first_name), initcap('abc def')
from   employees;

-- -- -- 문자 조작 함수
-- 1. concat
select last_name, first_name, concat(last_name, first_name) "Full name"
from employees;
/* concat은 인자를 2개까지 밖에 못받음*/
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
  /* 연습문제 2-4 substr 이용한 방법 */
  select last_name, first_name
  from   employees
  where  substr(last_name, 3, 1) in ('a', 'e')

-- 3. length
select last_name, first_name, length(first_name) "Length", concat(last_name, first_name) "Full name", 
       substr(concat(last_name, first_name), 1, 3) sub1, substr(concat(last_name, first_name), 5, 4) sub2, 
       substr(concat(last_name, first_name), -6, 2) sub3
from employees;

-- 4. instr : 문자열 index 추출
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

-- 7. trim : 앞 뒤 특정 문자 제거
select last_name, first_name, upper(concat(last_name, first_name)) "Full name",
       trim('D' from upper(concat(last_name, first_name))) trim
from   employees;

-- -- 숫자 함수
-- 1. round
select round(456.789), round(456.789, 0), round(456.789, 1), round(456.789, 2),
       round(456.789, -1), round(456.789, -2) from dual;

-- 2. trunc
select trunc(456.789), trunc(456.789, 0), trunc(456.789, 1), trunc(456.789, 2),
       trunc(456.789, -1), trunc(456.789, -2) from dual;

-- 3. mod, sign
select mod(20, 4), mod(20, 3), mod(20, 7), mod(20, -3), 20/7, 
       sign(50), sign(-10), sign(0) from dual;

-- -- 날짜 함수
/* 날짜 시간 포멧 바꾸기 */
alter session set nls_date_format = 'yyyy/mm/dd hh24:mi:ss';
alter session set nls_date_format = 'DD-MON-RR';
/* alter는 기본값 등 변경할 때 씀 */ 

-- -- -- 날짜 데이터 연산
select sysdate, sysdate + 1/24, sysdate - 1/24 from dual;
select sysdate, sysdate + 30/1440, sysdate - 30/1440 from dual;
select sysdate + 1, sysdate, (sysdate + 1) - sysdate from dual;
-- select sysdate + 1, sysdate, (sysdate + 1) + sysdate from dual; << 날짜끼리의 덧셈은 안됨

-- -- -- 날짜 조작 함수
-- 1. months_between(최근 날짜, 과거 날짜)
select first_name, months_between(sysdate, hire_date) "근속 개월"
from   employees;
-- 2. add_months, next_day(날짜, '요일'), last_day
select sysdate, add_months(sysdate, 2), next_day(sysdate, 'FRIDAY') ,
       last_day(sysdate) from dual;
--3. 날짜 round, trunc
select sysdate, round(sysdate, 'dd'), round(sysdate, 'mm'),
       trunc(sysdate, 'dd'), trunc(sysdate, 'mm') from dual;
       
-- -- -- 날짜 함수
alter session set time_zone = '+9:00';
select sysdate, current_date, systimestamp, current_timestamp from dual;

alter session set time_zone = '-7:00';
select sysdate, current_date, systimestamp, current_timestamp from dual;

-- 연습문제 3-1
select employee_id, last_name, salary, round(salary * 1.155) "New Salary"
from employees;
select employee_id, last_name, salary, trunc(salary * 1.155) "New Salary"
from employees;

-- 연습문제 3-2
select initcap(first_name) "Name", length(first_name) "Length"
from employees
where substr(first_name, 1, 1) in ('J', 'A', 'M');
/* where instr(first_name, 'J', 1, 1) = 1
   or    instr(first_name, 'A', 1, 1) = 1
   or    instr(first_name, 'M', 1, 1) = 1 */

-- 연습문제 3-3
select last_name, round(months_between(sysdate, hire_date)) "MONTHS_WORKED"
from employees
order by MONTHS_WORKED;
/* order by 2; */