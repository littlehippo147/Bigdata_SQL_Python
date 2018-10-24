/* 23�� ���
CREATE TABLE ��
char(���� ���� 2000�ڱ���) ���ٴ� varchar2(���� ���� 4000�ڱ���)�� ���� ��
���Ҿ� number, date Ÿ�� ���� ��
���� ����
primary key : �ش� column�� ������ ���� not null�̸鼭 unique �ؾ��� (���̺� �� 1��)
unique : �ش� column�� ������ ���� unique �ؾ��� (�������� null ��� X)
not null : null�� �ƴϸ� �ȴ�
check : ���� �ɾ��ֱ� (ex) salary > 0
references : �����͸� �������� �и� �����ϴ� ���� ����ȭ��� ��
foreign key : column  level ������ ���������� ������ �ʿ䰡 ����. 
              references�� �̿��� � table�� � column�� ������ ������ ���־����.

ALTER TABLE �� : �� �Ⱦ� (������ drop �ߴٰ� ������ϴ� ���� �� ���� ��)
�� �� �߰�
���� �� ���� ����
�� ���� �⺻�� ����
�� ���� 
�� �̸� �ٲٱ�
�б� ���� ���·� ���̺� ����

drop ���̺� ����(������)
cascade constraint : ���̺��� �ٸ� ���̺�κ��� �����Ǵ� ��� �������� ���� ����

PURGE ���̺� ����(���� ����)
PURGE RECYCLEBIN(������ ����)


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
-- �μ� ��ȣ�� ��ġ�ϴ� �μ� ��Ī�� �˾Ƽ� ������Ʈ

-- ���� ���� ������ �ҤѤ���
select department_name
from departments
where department_id = 90;

update emp_sample
set department_name = 'Executive'
where department_id = 90;

-- ���� ��� subquery �̿�
update emp_sample e
set department_name = (select department_name from departments d
                       where d.department_id = e.department_id);

-- ��� subquery ����
select employee_id, first_name, salary, e1.department_id, (select round(avg(salary)) from employees e3 
                                                           group by department_id 
                                                           having e1.department_id = e3.department_id) as "avg(sal) by dept"
from employees e1
where salary > (select avg(salary) from employees e2
                group by department_id
                having e1.department_id = e2.department_id);
/* ����� Ǯ��
select employee_id, first_name, salary, e1.department_id
from employees e1
where salary > (select avg(salary) 
                from employees e2
                where e1.department_id = e2.department_id);
*/                

-- ������ Object ��ü
-- -- VIEW object
-- ���� 5���� ����
select *
from (select department_id, round(avg(salary)) avg_sal 
     from   employees
     group by department_id
     order by avg_sal desc)
where rownum <= 5;

-- view object�� ����� �� ������ �ݵ�� alias �� �̸� �̿�(��ȣ ���� column�� �� �̸����� �ν� ����)
create view emp_avg
as
select department_id, round(avg(salary)) avg_sal 
from   employees
group by department_id
order by avg_sal desc;

select * from emp_avg
where rownum <= 5;

-- from �� �ȿ� �־ ���� subquery���� inline view ��� ��
-- �� ȥ�� �� select ���� �� ������ ���� ��ü�� ���� �ʿ�� ����

/* �ܼ� �� 
 ���� table���� ������� �Լ��� ������ �������� ���� �ܼ� �÷��׷� ������ view
 ������ �׷� ���� X
 DML ���� ���� ����

���� ��
 ���� table���� ������� �Լ��� ���� �� ���� �� view
 ������ �׷� ���� 
 DML ���� ���� X
*/

create view dept_vu(id, name)
as
select department_id, department_name
from departments;

select * from dept_vu;

-- view �� dml �� �� �� ������ view ��ü�� �Ǵ� ���� �ƴ�

insert into dept_v values(300, 'TEST');

-- CREATE ��� REPLACE�� view ���� ��ü ����

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

-- �ƹ� �ɼ� ���� ��� start 1 by 1
select seq1.nextval from dual;
-- max �� ����
select seq2.nextval from dual;
-- cycle : max �� �����ϸ� 1�� ���ư�
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

-- DICTIONARY table(system table) �ڿ� $ �پ�����
-- �츮�� create�� ����� object�� ���� ������ oracle ���������� �����ϴ� table
-- table�� segment, view�� segment �ƴ�(������ �ʿ� ���� ����)

-- CURRVAL ���������� �Ҵ� ���� �� �ٽ� �Ҵ�
-- sequence �� start with ���� ���� ����.

-- -- ���Ǿ�
-- datafile
-- sys / change_on_install -> oracle_4U : �ٿ�� �����͸� ��ŸƮ �� �˴ٿ� �ϰų� �����͸� ����ϴ� ��� �۾� (�뻧 ������)
-- system / manager -> oracle_4U : �� �۾� ���� �۾�

-- index�� ������ �ӵ��� ���̱� ���ؼ� ����� ��, select ���� �ӵ��� �� ������
-- ����Ŭ�� ��ü������ ������� index�� ���� ���� �ȵ�. drop �� ���� ������.
-- �ڵ� : ���̺� ���ǿ��� primary key �Ǵ� unique �������� ���ǽ� ����. ���� ������ drop �ϸ� �ڵ����� ���� drop ��
-- ���� : ���� ������ �ϴ� �ӵ� ���̱� ���� ������ ���� ����� �ε��� ����
-- index�� ���� ���� �߰��� root, ���� �߰� �� ���� �߰� �� branch -> ���� �Ѳ� ��� ���� ���߱� ó�� ���ٿ����� �ε��� ã�ư�

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

-- ���� �Լ��� �������� ������ �ָ� index�� �̿��� �� ����; ���� ������ column �״�� ����ϴ� ���� ����
select * from emp_new
where upper(ename) = upper('lex');

-- �׷� ��� �ϴ���? �ƿ� �Լ��� ������ ������ ������ index�� �����.
create index f_name_ix on emp_new(upper(ename));

