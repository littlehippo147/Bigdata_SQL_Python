select 100 + '200' from dual; /* 오류 없음 -> 100 + to_number('200') 산술 연산 */
select 100 + 'A' from dual; /* 오류 -> to_number('A')에서 type error */

-- 오라클에서는 보통 문자를 숫자로 변환시키려는 경향이 큼
select department_id, first_name, hire_date
from employees
where department_id = '30'; /* '30' -> 30 */
-- like는 문자 데이터에만 쓸 수 있는 연산자이므로 데이터를 문자로 변환시켜서 비교
select department_id, first_name, hire_date
from employees
where department_id like '3%'; /* department_id -> to_char(department_id) */

-- -- 비교 연산자의 좌변에는 변형되지 않은 순수한 column을 써주는 것이 가장 Best!
-- 암시적 데이터 유형 변환 : 서버에서 자동으로 변환
-- 명시적 데이터 유형 변환 : 변환 함수를 사용하여 수행

-- 날짜 데이터에 to_char 함수 사용
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

-- fm 포맷
select hire_date, to_char(hire_date, 'yyyy/mm/dd'), to_char(hire_date, 'Month Day yyyy'),
       to_char(hire_date, 'DD Month yyyy'), to_char(hire_date, 'fmDD Month yyyy')
from   employees
select to_char(sysdate, 'dd'), to_char(sysdate, 'ddsp'), to_char(sysdate, 'ddspth')
from dual;

-- 숫자 데이터에 to_char 함수 사용
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
/* select 100 + '5,000' from dual; 오류 */

select first_name, hire_date
from employees
-- where hire_date = to_date('2002/06/07', 'yyyy mm dd');
where hire_date = to_date('07 JUNE/2002', 'dd MONTH/yyyy');

----------------
update employees set hire_date = sysdate
where employee_id = 166;
commit;

-- sysdate 사용시 시간 부분이 다르면 다른 값으로 나옴
select employee_id, to_char(hire_date, 'yyyy/mm/dd hh:mi:ss')
from employees;

select employee_id, first_name, hire_date
from employees
-- where round(hire_date, 'DAY') = to_date(round(sysdate, 'DAY'), 'DD-MON-YY'); << 내 방법
/* 다 가능
where hire_date >= to_date('2018/10/17', 'yyyy/mm/dd')
and hire_date < to_date('2018/10/18', 'yyyy/mm/dd');
where hire_date between to_date('2018/10/17', 'yyyy/mm/dd') and to_date('2018/10/18', 'yyyy/mm/dd'); 
또는 
select employee_id, first_name, hire_date
from employees
where to_char(hire_date, 'yyyy/mm/dd') = '2018/10/17'; << 중요한 방법 ***
*/
-- 연도 단위로 찾기
select first_name, hire_date
from employees
where to_char(hire_date, 'yyyy') = '2008';

-- -- 기타 함수 NULL 값과 관련
-- 1. NVL
select salary, commission_pct, salary + commission_pct /* null 값이 하나라도 있으면 결과도 null */
from employees;
select salary, commission_pct, salary + commission_pct, nvl(salary, 0) + nvl(commission_pct, 0)
from employees;

-- 2. NVL2, NULLIF, COALESCE
select nvl2(100, 'A', 'B'), nvl2(null, 10, 20) from dual; /* NVL2*/
select nullif(100, 100), nullif( 'A', 'B') from dual; /*nullif */
select coalesce(1, 2, 3), coalesce(null, 2, 3), coalesce(null, null, 3), coalesce(null, null, null) from dual;

-- 3. GREATEST, LEAST
select greatest('HA', 'HE', 'HI'), least(10, 20, 30) from dual;

-- 4. 조건부 표현식 DECODE 함수, CASE 식
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
            -- when salary > 20000 then 'very high' 없어도 같음 
            else 'very high' end salary_nm
from employees;

-- 연습문제 4-1
select last_name || ' earns ' || to_char(salary, '$99,999') || ' monthly but wants ' 
       || to_char(3 * salary, '$99,999') "Dream Salaries"
from   employees;
/* 강사님 풀이
select last_name || ' earns ' || to_char(salary, 'fm$999,999,999') || 
       ' monthly but wants ' || to_char(salary * 3, 'fmL999,999,999') "Dream Salaries"
from employees;
*/

-- 연습문제 4-2
select last_name, first_name, nvl(to_char(commission_pct, '.9'), 'No Commission') "COMM"
from employees;
/* 강사님 풀이
select last_name, first_name, nvl(to_char(commission_pct), 'No Commission') "COMM"
       case when commission_pct is not null then to_char(commission_pct) else 'No Commission' end
from employees;
*/

-- 연습문제 4-3
select last_name, hire_date, to_char(hire_date, 'Day') DAY
from employees
-- order by case to_char(hire_date, 'D') when '1' then '8' else to_char(hire_date, 'D') end;
order by decode(to_char(hire_date, 'D'), '1', '8', to_char(hire_date, 'D'));
/* 강사님 풀이
select last_name, hire_date, to_char(hire_date, 'Day')
from employees
order by to_char(hire_date-1, 'd');
*/

--
select salary, to_char(salary, 'L999,999'), to_char(salary, '$999,999')
from employees;

-- -- 그룹함수
select count(salary), sum(salary), avg(salary), min(salary), max(salary)
from employees;

select count(commission_pct), sum(commission_pct)
from employees;

select count(*), count(commission_pct), count(distinct department_id) 
from employees;
-- *는 조건 하에 모든 행을 counting 해라

select distinct department_id, job_id
from employees
order by department_id, job_id;
-- 결합된 값에 대한 중복 제거

select count(salary), count(commission_pct), 
       avg(salary), avg(commission_pct), avg(nvl(commission_pct, 0))
from employees;
-- null 값과 상관 없이 전체에 대한 평균을 구하려면 nvl 사용
