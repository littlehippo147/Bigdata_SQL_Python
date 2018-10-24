-- 관리자 id

grant select on hr.employees to scott;

-- 공용 만들기

create public synonym e for hr.employees;

-- 데이터 파일 만들기? 업무 별로 테이블 스페이 만듬
create tablespace insa
datafile 'c:\prod\insa01.dbf' size 50m;

alter tablespace insa
add datafile 'c:\prod1\insa02.dbf' size 10m;

-- tablespace 들의 dictionary view 
select * from dba_data_files;

select table_name from dba_tables
where tablespace_name = 'INSA';

/*
1. db 생성
2. 업무별 tablespace 생성
3. 일반 db user 생성(hr 인사, scott 급여 등등) + 권한부여(privilege, role) - 안하면 접속 X
                                                                  └connect, resource
4. 업무 table, index, view, ...
*/

-- user 생성 by 뒤에 패스워드
create user insa_adm identified by oracle;
-- user로 하여금 insa tablespace 사용하도록 함.
alter user insa_adm default tablespace insa;

-- 권한 부여하기 GRANT
grant connect, resource to insa_adm;

-- 권한 부여후 insa user 접속


