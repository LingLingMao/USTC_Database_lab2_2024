use sys;
-- delete a student
drop trigger if exists delete_student;
delimiter //
create trigger delete_student after delete on Student for each row
begin
    delete from Repair where Repair.r_stu_id = old.s_id;
end //   
delimiter ;

-- test
-- delete from Student where s_id = 'PB20114514';
