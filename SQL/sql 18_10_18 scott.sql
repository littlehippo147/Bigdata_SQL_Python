-- -- -- Chapter 6. join
-- 테스트용 테이블 만들기
create table emp_test
as
select empno, ename, sal, deptno from emp
where  empno in (7782, 7788, 7876, 7900);
-- 테스트 테이블에 데이터 추가
insert into emp_test values(9000, 'Karen', 800, null);

create table dept_test as select * from dept;

-- 테스트 테이블 생성 확인
select * from emp_test;
select * from dept_test;

-- 테이블 삭제
-- drop table emp_test purge;

-- equijoin
select empno, ename, emp_test.deptno, dept_test.deptno, dname
from emp_test,dept_test /* 이상하게 나옴 반드시 where절 필요 */
where emp_test.sal >= 2000 /* 단일 테이블에서의 조건절 먼저 쓰는 것이 좋음 */
and emp_test.deptno = dept_test.deptno;

select * from salgrade;

-- join의 비교는 보통 =로 들어감. 예외로는 다음과 같은 경우
-- non equijoin
select empno, ename, sal, salgrade.grade
from emp_test, salgrade
where sal between salgrade.losal and salgrade.hisal;

select empno, ename, sal, salgrade.grade, dept_test.dname
from emp_test, salgrade, dept_test
where emp_test.deptno = dept_test.deptno
and sal between salgrade.losal and salgrade.hisal;

-- 테이블 alias 이용하기
select empno, ename, e.deptno, d.deptno, dname
from emp_test e, dept_test d
where e.deptno = d.deptno;

-- ANSI 표준화 : join 열에서는 조건절을 where 대신 on 절에 써주어야함
select empno, ename, e.deptno, d.deptno, dname
from emp_test e join dept_test d
on e.deptno = d.deptno;
-- where e.sal > 2000; 추가적인 조건절은 where 절을 쓸 수 있으나 and나 or를 권장

-- 일반적인 join은 조건절에 매칭이 되는 데이터만 return 해주는 inner join
-- 일치되지 않은 행까지 return 해주기 위해 outer join, ASNI의 표준 방법으로 사용

-- (+)가 붙지 않은 부분을 기준 붙은 부분이 나중에 반환; 부서가 할당되지 않은 사원의 정보까지 확인
select empno, ename, e.deptno, d.deptno, dname
from emp_test e, dept_test d
where e.deptno = d.deptno(+);
-- 반대
select empno, ename, e.deptno, d.deptno, dname
from emp_test e, dept_test d
where e.deptno(+) = d.deptno;

-- 할당되지 않은 데이터까지 모두 표시
/* 틀린 예시
select empno, ename, e.deptno, d.deptno, dname
from emp_test e, dept_test d
where e.deptno(+) = d.deptno(+)
(+) 기호는 한쪽만 가능 */
select empno, ename, e.deptno, d.deptno, dname
from emp_test e, dept_test d
where e.deptno = d.deptno(+)
union /* union all : 중복결과까지 표시 */
select empno, ename, e.deptno, d.deptno, dname
from emp_test e, dept_test d
where e.deptno(+) = d.deptno;

-- 오라클 고유의 outer join에서 가장 큰 실수
select e.empno, e.ename, e.deptno, d.deptno, d.dname
from emp_test e, dept_test d
where e.deptno = d.deptno(+)
-- and d.loc = 'NEW YORK'; 비 join 조건절에 나중에 읽혀야할 테이블 데이터의 조건을 쓴 경우
and d.loc(+) = 'NEW YORK'; /* 나중에 읽혀야할 테이블 데이터에 똑같이 (+) 붙여줌 */

-- -- ANSI 표준 outer join
select e.empno, e.ename, e.deptno, d.deptno, d.dname
from emp_test e left outer join dept_test d
on e.deptno = d.deptno;
-- 같은 결과
select e.empno, e.ename, e.deptno, d.deptno, d.dname
from dept_test d right outer join emp_test e
on e.deptno = d.deptno;

-- 기준 없이 일치하지 않은 데이터까지 모두 표시
select e.empno, e.ename, e.deptno, d.deptno, d.dname
from dept_test d full outer join emp_test e
on e.deptno = d.deptno;

-- 조건 포함
select e.empno, e.ename, e.deptno, d.deptno, d.dname
from emp_test e left outer join dept_test d
on e.deptno = d.deptno
and d.loc = 'NEW YORK';