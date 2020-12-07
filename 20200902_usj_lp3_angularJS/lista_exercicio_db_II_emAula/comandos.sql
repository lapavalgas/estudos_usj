CREATE TABLE accounts (
	user_id serial PRIMARY KEY,
	username VARCHAR ( 50 ) UNIQUE NOT NULL,
	password VARCHAR ( 50 ) NOT NULL,
	email VARCHAR ( 255 ) UNIQUE NOT NULL,
	created_on TIMESTAMP NOT NULL,
        last_login TIMESTAMP 
);

insert into accounts (username, password, email, created_on)
values ('Rafael', 'minha_senha_criptografada', 'rafa@gmail.com', current_timestamp); 

insert into accounts (username, password, email, created_on)
values ('Josefina', 'josefininha123', 'giuseppina@gmail.com', current_timestamp); 

Select * from accounts;

CREATE TABLE roles(
   role_id serial PRIMARY KEY,
   role_name VARCHAR (255) UNIQUE NOT NULL
);

insert into roles (role_name) values ('Gerente');

insert into roles (role_name) values ('Funcionário');

select * from roles;

CREATE TABLE account_roles (
  user_id INT NOT NULL,
  role_id INT NOT NULL,
  grant_date TIMESTAMP,
  PRIMARY KEY (user_id, role_id),
  FOREIGN KEY (role_id)
      REFERENCES roles (role_id),
  FOREIGN KEY (user_id)
      REFERENCES accounts (user_id)
);

insert into account_roles values (1, 2);

select * from account_roles;