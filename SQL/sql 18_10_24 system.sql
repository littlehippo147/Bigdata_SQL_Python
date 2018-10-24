-- ������ id

grant select on hr.employees to scott;

-- ���� �����

create public synonym e for hr.employees;

-- ������ ���� �����? ���� ���� ���̺� �����̺� ����
create tablespace insa
datafile 'c:\prod\insa01.dbf' size 50m;

alter tablespace insa
add datafile 'c:\prod1\insa02.dbf' size 10m;

-- tablespace ���� dictionary view 
select * from dba_data_files;

select table_name from dba_tables
where tablespace_name = 'INSA';

/*
1. db ����
2. ������ tablespace ����
3. �Ϲ� db user ����(hr �λ�, scott �޿� ���) + ���Ѻο�(privilege, role) - ���ϸ� ���� X
                                                                  ��connect, resource
4. ���� table, index, view, ...
*/

-- user ���� by �ڿ� �н�����
create user insa_adm identified by oracle;
-- user�� �Ͽ��� insa tablespace ����ϵ��� ��.
alter user insa_adm default tablespace insa;

-- ���� �ο��ϱ� GRANT
grant connect, resource to insa_adm;

-- ���� �ο��� insa user ����


