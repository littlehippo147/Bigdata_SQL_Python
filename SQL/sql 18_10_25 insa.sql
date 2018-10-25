-- 부서 테이블 만들기
create table dept (
  deptno  number primary key,
  dname   char(30) not null,
  loc     varchar2(30));
-- tablespace insa; 를 써서 명시적으로 table을 저장할 tablespace 정해줘도 됨.

insert into dept
values (10, '빅데이터', '서울');

commit;

select * from dept;
select * from emp1;

/* 
segment (저장공간이 필요한 Object)
    └ table
    └ index
    └ undo
    └ temporary 등
*/

-- datafile 1~16번째 블럭까지는 8K씩 할당, 17번부터는 1M 씩 할당 (Extent : 단일 할당으로 얻은 일정 수의 연속적인 데이터 블록, tablespace 생성 단계에서 결정)
-- 예를 들어 emp table에 40k를 할당하면 5block으로 방 1개 생성

/*
memory + BP(Background Process) : Instance
*/

select * from emp1;

update emp1 set ename = 'TOM';
-- commit 전에는 변경 완료가 된 것이 아니므로 sqlplus에서 확인하면 변경 전 데이터로 나타남
rollback;