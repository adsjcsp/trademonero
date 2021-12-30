DROP if exist login

CREATE TABLE login (

    id int not null AUTOINCREMENT PRIMARY KEY,
    nome char,
    login char,
    senha char,
    idade date,
    data_de_init CURRENT_DATE
)