/* 23일 요약
CREATE TABLE 문
char(고정 길이 2000자까지) 보다는 varchar2(가변 길이 4000자까지)를 많이 씀
더불어 number, date 타입 많이 씀
제약 조건
primary key : 해당 column에 들어오는 값이 not null이면서 unique 해야함 (테이블 당 1개)
unique : 해당 column에 들어오는 값이 unique 해야함 (여러개의 null 상관 X)
not null : null만 아니면 된다
check : 조건 걸어주기 (ex) salary > 0
references : 데이터를 조각내서 분리 저장하는 것을 정규화라고 함
foreign key : column  level 에서는 제약조건을 선언할 필요가 없음. 
              references를 이용해 어떤 table의 어떤 column을 참조할 것인지 써주어야함.

ALTER TABLE 문 : 잘 안씀 (오히려 drop 했다가 재생성하는 것을 더 많이 씀)
새 열 추가
기존 열 정의 수정
새 열의 기본값 정의
열 삭제 
열 이름 바꾸기
읽기 전용 상태로 테이블 변경

drop 테이블 삭제(휴지통)
cascade constraint : 테이블이 다른 테이블로부터 참조되는 경우 제약조건 먼저 삭제

PURGE 테이블 삭제(완전 삭제)
PURGE RECYCLEBIN(휴지통 비우기)


update emp_sample e
set department_name = 'aa'
where exists (select 1 from departments d
              where d.department_id = e.department_id);
*/

create table emp_sample
as
select * from employees;

select * from emp_sample;

alter table emp_sample add (department_name varchar2(30));
-- 부서 번호와 일치하는 부서 명칭을 알아서 업데이트

-- 다음 같은 과정은 불ㅡㅡ편
select department_name
from departments
where department_id = 90;

update emp_sample
set department_name = 'Executive'
where department_id = 90;

-- 따라서 상관 subquery 이용
update emp_sample e
set department_name = (select department_name from departments d
                       where d.department_id = e.department_id);

-- 상관 subquery 예시
select employee_id, first_name, salary, e1.department_id, (select round(avg(salary)) from employees e3 
                                                           group by department_id 
                                                           having e1.department_id = e3.department_id) as "avg(sal) by dept"
from employees e1
where salary > (select avg(salary) from employees e2
                group by department_id
                having e1.department_id = e2.department_id);
/* 강사님 풀이
select employee_id, first_name, salary, e1.department_id
from employees e1
where salary > (select avg(salary) 
                from employees e2
                where e1.department_id = e2.department_id);
*/                

-- 데이터 Object 객체
-- -- VIEW object
-- 상위 5개만 보기
select *
from (select department_id, round(avg(salary)) avg_sal 
     from   employees
     group by department_id
     order by avg_sal desc)
where rownum <= 5;

-- view object를 만들어 쓸 때에는 반드시 alias 열 이름 이용(괄호 섞인 column을 열 이름으로 인식 못함)
create view emp_avg
as
select department_id, round(avg(salary)) avg_sal 
from   employees
group by department_id
order by avg_sal desc;

select * from emp_avg
where rownum <= 5;

-- from 절 안에 넣어서 쓰는 subquery들을 inline view 라고 함
-- 나 혼자 저 select 문을 쓸 때에는 굳이 객체로 만들 필요는 없음

/* 단순 뷰 
 단일 table에서 만들어진 함수나 수식을 포함하지 않은 단순 컬러瀏 구성된 view
 데이터 그룹 포함 X
 DML 문장 수행 가능

복합 뷰
 다중 table에서 만들어진 함수나 수식 등 포함 된 view
 데이터 그룹 포함 
 DML 문장 수행 X
*/

create view dept_vu(id, name)
as
select department_id, department_name
from departments;

select * from dept_vu;

-- view 는 dml 문 쓸 수 있지만 view 자체에 되는 것은 아님

insert into dept_v values(300, 'TEST');

-- CREATE 대신 REPLACE로 view 내용 대체 가능

-- -- SEQUENCE object
create table dept_new (
deptno number,
dname varchar2(30),
"LOCATION" varchar2(20)); 

insert into dept_new
select d.department_id deptno, d.department_name dname, l.city "LOCATION"
from departments d join locations l
on d.location_id = l.location_id;

select * from dept_new;

create sequence seq1;

create sequence seq2
start with 100
increment by 10
maxvalue 200;

create sequence seq3
start with 5
increment by 5
maxvalue 100
cycle;

drop sequence seq4;

create sequence seq4
start with 5
increment by 5
minvalue 5
maxvalue 100
cycle
nocache;


commit;

-- 아무 옵션 없는 경우 start 1 by 1
select seq1.nextval from dual;
-- max 값 제한
select seq2.nextval from dual;
-- cycle : max 값 도달하면 1로 돌아감
select seq3.nextval from dual;
select seq4.nextval from dual;

insert into dept_new
values(dept_seq.nextval, 'AAA', 'Seoul');

insert into dept_new
values(dept_seq.nextval, 'BBB', 'Seoul');

create sequence dept_seq
start with 290
increment by 10
maxvalue 9999;

-- DICTIONARY table(system table) 뒤에 $ 붙어있음
-- 우리가 create로 만드는 object에 대한 정보를 oracle 내부적으로 저장하는 table
-- table은 segment, view는 segment 아님(저장이 필요 없기 때문)

-- CURRVAL 마지막으로 할당 받은 값 다시 할당
-- sequence 는 start with 빼고 변경 가능.

-- -- 동의어
-- 객체에 다른 이름 부여
-- 공용 동의어 public
-- 개별 동의어 private


-- datafile
-- sys / change_on_install -> oracle_4U : 다운된 데이터를 스타트 업 셧다운 하거나 데이터를 백업하는 등등 작업 (대빵 관리자)
-- system / manager -> oracle_4U : 위 작업 외의 작업

-- index는 색인의 속도를 높이기 위해서 사용할 뿐, select 문의 속도는 더 느려짐
-- 오라클이 자체적으로 만들어준 index는 절대 삭제 안됨. drop 할 때만 삭제됨.
-- 자동 : 테이블 정의에서 primary key 또는 unique 제약조건 정의시 생성. 제약 조건을 drop 하면 자동으로 같이 drop 됨
-- 수동 : 행이 엑세스 하는 속도 높이기 위해 유저가 열의 비고유 인덱스 생성
-- index로 색인 과정 중간값 root, 상위 중간 값 하위 중간 값 branch -> 소주 뚜껑 까기 숫자 맞추기 처럼 업다운으로 인덱스 찾아감

select * from emp_new;

drop table emp_new;
create table emp_new (
empno number primary key,
ename varchar2(20),
email varchar2(25) not null,
salary number,
hiredate date not null,
deptno number);

insert into emp_new
select employee_id, first_name, email, salary, hire_date, department_id
from employees;

create index name_ix on emp_new(ename);

select * from emp_new
where ename = 'Lex';

-- 값에 함수나 수식으로 변형을 주면 index를 이용할 수 없음; 따라서 순수한 column 그대로 사용하는 것이 최적
select * from emp_new
where upper(ename) = upper('lex');

-- 그럼 어떻게 하느냐? 아예 함수나 수식을 적용한 값으로 index를 만든다.
create index f_name_ix on emp_new(upper(ename));

