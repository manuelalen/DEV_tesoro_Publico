CREATE USER 'manolito_lee'@'%' IDENTIFIED BY 'manolito_lee';
CREATE USER 'manolita_lee'@'%' IDENTIFIED BY 'manolita_lee';
create role user_api;
GRANT SELECT ON tesoro.* TO user_api;
GRANT SELECT ON tesoro.* TO 'manolito_lee'@'%';
GRANT  'user_api'@'%' TO 'manolito_lee'@'%';
flush privileges;
#select * from tesoro.bancocentral;