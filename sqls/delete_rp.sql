use sys;
-- procedure: delete a repair record if state is 'F'
drop procedure if exists delete_repair;
delimiter //
create procedure delete_repair(
    in r_id char(24)
)
begin
    delete from Repair where Repair.r_id = r_id and r_state = 'F';
end //
delimiter ;

-- test
-- call delete_repair('202406114514');
-- call delete_repair('202406114515');
   