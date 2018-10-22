-- DML

select * from emp_test;

-- �� �྿ �߰� INSERT INTO VALUES
insert into emp_test
values (9010, 'mike', 1000, 40);

select * from emp_test;

insert into emp_test(sal, empno, ename)
values (2000, 9050, 'laura');
select * from emp_test;

insert into emp_test(empno, ename)
values (9100, 'linda');
select * from emp_test;

select * from emp_test;

-- ���ο� �� �߰� ALTER TABLE ADD
alter table dept_test add(create_dt date);

insert into dept_test
values (50, 'MARKETING', 'LA', to_date('2018/01/01', 'yyyy/mm/dd'));

insert into dept_test
values (60, 'EDUCATION', 'LAS VEGAS', null);

select * from dept_test;

-- ���� ���ϰ� �ǵ�����
rollback;

-- ���� ���� ������ �ѹ��� �߰�(subquery �̿�) INSERT INTO SELECT
insert into dept_test
select deptno + 5 deptno, substr(dname, 1, 5), loc, sysdate
from dept_test
where deptno <= 40;

select * from dept_test
order by deptno;

-- ����
commit;

-- �� ���� �� ���� UPDATE SET
update dept_test SET create_dt = sysdate;
update dept_test SET create_dt = to_date('2018/01/01', 'yyyy/mm/dd')
where deptno = 50;

select * from emp_test;

update emp_test
set deptno = 30
where deptno is null;

update emp_test
set ename = initcap(ename);

update emp_test
set sal = sal * 1.1, deptno = deptno + 5
where deptno = 20;

-- ������ ���� DELETE WHERE
select * from dept_test;

delete dept_test
where deptno > 40;

commit;

insert into dept_test
select * from dept_test
where deptno = 40;

-- �ߺ��Ǵ� �ڷḦ ã�� ���� rowid �Ǵ� ������ ��
-- -- deptno 40�� �ߺ��� �ڷḦ ����
delete dept_test
where rowid > (select min(rowid) from dept_test
               where deptno=40)
and deptno=40;