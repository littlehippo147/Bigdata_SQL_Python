-- �μ� ���̺� �����
create table dept (
  deptno  number primary key,
  dname   char(30) not null,
  loc     varchar2(30));
-- tablespace insa; �� �Ἥ ��������� table�� ������ tablespace �����൵ ��.

insert into dept
values (10, '������', '����');

commit;

select * from dept;
select * from emp1;

/* 
segment (��������� �ʿ��� Object)
    �� table
    �� index
    �� undo
    �� temporary ��
*/

-- datafile 1~16��° �������� 8K�� �Ҵ�, 17�����ʹ� 1M �� �Ҵ� (Extent : ���� �Ҵ����� ���� ���� ���� �������� ������ ���, tablespace ���� �ܰ迡�� ����)
-- ���� ��� emp table�� 40k�� �Ҵ��ϸ� 5block���� �� 1�� ����

/*
memory + BP(Background Process) : Instance
*/

select * from emp1;

update emp1 set ename = 'TOM';
-- commit ������ ���� �Ϸᰡ �� ���� �ƴϹǷ� sqlplus���� Ȯ���ϸ� ���� �� �����ͷ� ��Ÿ��
rollback;