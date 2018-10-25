
-- dept ���̺� ����Ƴ� Ȯ��
select table_name from dba_tables
where tablespace_name = 'INSA';

/*
1. DB ���� - SYSTEM  dictionary table  
          - SYSAUX  dictionary table
          - UNDO
          - TEMPORARY
*/

select tablespace_name, contents
from dba_tablespaces;

-- Undo data
/*
 - Ʈ����� �۾� ���
 - rollback
 - �б� �ϰ��� query
 - ������ Ʈ����� recovery
 - flashback query
   ex ) flashback drop : ������(recyclebin)
*/

show parameter undo;

alter system set undo_retention = 3600;