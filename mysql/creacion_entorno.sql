##Creación del usuario técnico, role y asignación de permisos
create user 'tesoro'@'localhost' identified by 'tesoro2023';
grant insert, select on tesoro.bancocentral to 'tesoro'@'localhost';
flush privileges;

CREATE ROLE DEV_TESORO;

GRANT DEV_TESORO TO 'tesoro'@'localhost';

##Creación de la base de datos y las tablas necesarias
create database Tesoro;
create table Tesoro.BancoCentral(
Cantidad float,
Concepto varchar(99));

create table Tesoro.MinisterioTrabajo_Raw(
Cantidad float,
Concepto varchar(99));

##Asignación de privilegios al role y al usuario
GRANT INSERT, SELECT ON Tesoro.BancoCentral TO DEV_TESORO;
GRANT INSERT, SELECT ON Tesoro.MinisterioTrabajo_Raw TO DEV_TESORO;
GRANT DEV_TESORO TO 'tesoro'@'localhost';

#select * from tesoro.bancocentral;
#select * from Tesoro.MinisterioTrabajo_Raw;
#set sql_safe_updates = 0;
#delete from tesoro.bancocentral;
#delete from tesoro.MinisterioTrabajo_Raw;


## Creación de nuestro trigger.
SET GLOBAL event_scheduler = ON;

DELIMITER //
use Tesoro;
CREATE TRIGGER insert_TrabajoGarantizado
AFTER INSERT ON Tesoro.BancoCentral
FOR EACH ROW
BEGIN
  IF NEW.concepto = 'Trabajo Garantizado' THEN
    INSERT INTO Tesoro.MinisterioTrabajo_Raw (cantidad, concepto)
    VALUES (NEW.cantidad, NEW.concepto);
  END IF;
END //
DELIMITER ;
