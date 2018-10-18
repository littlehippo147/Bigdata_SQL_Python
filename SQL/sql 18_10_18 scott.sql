-- -- -- Chapter 6. join
-- �׽�Ʈ�� ���̺� �����
create table emp_test
as
select empno, ename, sal, deptno from emp
where  empno in (7782, 7788, 7876, 7900);
-- �׽�Ʈ ���̺� ������ �߰�
insert into emp_test values(9000, 'Karen', 800, null);

create table dept_test as select * from dept;

-- �׽�Ʈ ���̺� ���� Ȯ��
select * from emp_test;
select * from dept_test;

-- ���̺� ����
-- drop table emp_test purge;

-- equijoin
select empno, ename, emp_test.deptno, dept_test.deptno, dname
from emp_test,dept_test /* �̻��ϰ� ���� �ݵ�� where�� �ʿ� */
where emp_test.sal >= 2000 /* ���� ���̺����� ������ ���� ���� ���� ���� */
and emp_test.deptno = dept_test.deptno;

select * from salgrade;

-- join�� �񱳴� ���� =�� ��. ���ܷδ� ������ ���� ���
-- non equijoin
select empno, ename, sal, salgrade.grade
from emp_test, salgrade
where sal between salgrade.losal and salgrade.hisal;

select empno, ename, sal, salgrade.grade, dept_test.dname
from emp_test, salgrade, dept_test
where emp_test.deptno = dept_test.deptno
and sal between salgrade.losal and salgrade.hisal;

-- ���̺� alias �̿��ϱ�
select empno, ename, e.deptno, d.deptno, dname
from emp_test e, dept_test d
where e.deptno = d.deptno;

-- ANSI ǥ��ȭ : join �������� �������� where ��� on ���� ���־����
select empno, ename, e.deptno, d.deptno, dname
from emp_test e join dept_test d
on e.deptno = d.deptno;
-- where e.sal > 2000; �߰����� �������� where ���� �� �� ������ and�� or�� ����

-- �Ϲ����� join�� �������� ��Ī�� �Ǵ� �����͸� return ���ִ� inner join
-- ��ġ���� ���� ����� return ���ֱ� ���� outer join, ASNI�� ǥ�� ������� ���

-- (+)�� ���� ���� �κ��� ���� ���� �κ��� ���߿� ��ȯ; �μ��� �Ҵ���� ���� ����� �������� Ȯ��
select empno, ename, e.deptno, d.deptno, dname
from emp_test e, dept_test d
where e.deptno = d.deptno(+);
-- �ݴ�
select empno, ename, e.deptno, d.deptno, dname
from emp_test e, dept_test d
where e.deptno(+) = d.deptno;

-- �Ҵ���� ���� �����ͱ��� ��� ǥ��
/* Ʋ�� ����
select empno, ename, e.deptno, d.deptno, dname
from emp_test e, dept_test d
where e.deptno(+) = d.deptno(+)
(+) ��ȣ�� ���ʸ� ���� */
select empno, ename, e.deptno, d.deptno, dname
from emp_test e, dept_test d
where e.deptno = d.deptno(+)
union /* union all : �ߺ�������� ǥ�� */
select empno, ename, e.deptno, d.deptno, dname
from emp_test e, dept_test d
where e.deptno(+) = d.deptno;

-- ����Ŭ ������ outer join���� ���� ū �Ǽ�
select e.empno, e.ename, e.deptno, d.deptno, d.dname
from emp_test e, dept_test d
where e.deptno = d.deptno(+)
-- and d.loc = 'NEW YORK'; �� join �������� ���߿� �������� ���̺� �������� ������ �� ���
and d.loc(+) = 'NEW YORK'; /* ���߿� �������� ���̺� �����Ϳ� �Ȱ��� (+) �ٿ��� */

-- -- ANSI ǥ�� outer join
select e.empno, e.ename, e.deptno, d.deptno, d.dname
from emp_test e left outer join dept_test d
on e.deptno = d.deptno;
-- ���� ���
select e.empno, e.ename, e.deptno, d.deptno, d.dname
from dept_test d right outer join emp_test e
on e.deptno = d.deptno;

-- ���� ���� ��ġ���� ���� �����ͱ��� ��� ǥ��
select e.empno, e.ename, e.deptno, d.deptno, d.dname
from dept_test d full outer join emp_test e
on e.deptno = d.deptno;

-- ���� ����
select e.empno, e.ename, e.deptno, d.deptno, d.dname
from emp_test e left outer join dept_test d
on e.deptno = d.deptno
and d.loc = 'NEW YORK';