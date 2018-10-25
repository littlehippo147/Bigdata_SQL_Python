
-- dept 테이블 저장됐나 확인
select table_name from dba_tables
where tablespace_name = 'INSA';

/*
1. DB 생성 - SYSTEM  dictionary table  
          - SYSAUX  dictionary table
          - UNDO
          - TEMPORARY
*/

select tablespace_name, contents
from dba_tablespaces;

-- Undo data
/*
 - 트랜잭션 작업 기록
 - rollback
 - 읽기 일관성 query
 - 실패한 트랜잭션 recovery
 - flashback query
   ex ) flashback drop : 휴지통(recyclebin)
*/

show parameter undo;

alter system set undo_retention = 3600;