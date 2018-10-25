select * from dept_test;

update dept_test set loc = '����';
-- �Ǽ��� ������ ��� rollback�� �ȵ�
commit;

recyclebin;

-- 2018/10/25 14:47:27

select to_char(sysdate, 'yyyy/mm/dd hh24:mi:ss') from dual;

select * from emp;

-- �Ǽ��� ����
delete emp 
where comm is null;

commit;

-- �ð� ������ �̿��� flashback. from ���� AS OF TIMESTAMP
-- - �ð��븦 ���� �Է��ؼ� ����ϴ� ���
select * 
from emp as of timestamp 
         to_date('2018/10/25 14:47:27', 'yyyy/mm/dd hh24:mi:ss')
where comm is null;

-- - �ð� ���� �̿� : ���� ���� �̿��� 
select * 
from emp as of timestamp sysdate - 20/1440
where comm is null;

-- - systimestamp �̿��ϴ� ���
select * 
from emp as of timestamp systimestamp - interval '12' minute
where comm is null;

insert into emp
select * 
from emp as of timestamp sysdate - 20/1440
where comm is null;

select * from emp;

commit;

update emp set job = 'ADMIN'
where deptno = 30;

commit;

update emp e1 set job = 
(select job 
from emp as of timestamp sysdate - 24/1440 e2
where e1.empno = e2.empno);
