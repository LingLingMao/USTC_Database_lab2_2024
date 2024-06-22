use sys;
SET GLOBAL log_bin_trust_function_creators = 1;
drop FUNCTION if exists Repair_state;
-- 如果状态为T，则返回‘已维修’，否则返回‘未维修’
DELIMITER //
create FUNCTION Repair_state(state char(2)) RETURNS varchar(10)
BEGIN
    declare result varchar(10);
    if state = 'T' then
        set result = '已维修';
    else
        set result = '未维修';
    end if;
    return result;
END //
DELIMITER ;
