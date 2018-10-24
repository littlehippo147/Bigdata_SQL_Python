-- 다른 유저의 table 참조

select * from hr.employees;

-- 권한 부여 안되면 안 불러짐
select * from hr.departments;

select employee_id, first_name from e;