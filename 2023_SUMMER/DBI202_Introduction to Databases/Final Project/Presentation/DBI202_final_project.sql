/*drop database dumpling_store
create database dumpling_store*/

/*-- Disable foreign key constraints
EXEC sp_MSforeachtable 'ALTER TABLE ? NOCHECK CONSTRAINT all'
-- Drop tables
DROP TABLE IF EXISTS Review;
DROP TABLE IF EXISTS Dumpling;
DROP TABLE IF EXISTS Order_service;
DROP TABLE IF EXISTS Discount;
DROP TABLE IF EXISTS ingredients;
DROP TABLE IF EXISTS Shift_of_employees;
DROP TABLE IF EXISTS Task;
DROP TABLE IF EXISTS Employees;
DROP TABLE IF EXISTS Invoice_customer;
DROP TABLE IF EXISTS invoice_provider;
DROP TABLE IF EXISTS Manager;
DROP TABLE IF EXISTS Store;
DROP TABLE IF EXISTS Recipe;
DROP TABLE IF EXISTS Ingredient_provider;
drop table if exists Discount_type
DROP TABLE IF EXISTS Customer;

-- Re-enable foreign key constraints
EXEC sp_MSforeachtable 'ALTER TABLE ? WITH CHECK CHECK CONSTRAINT all'*/




CREATE TABLE Customer
(
  customer_id INT primary key,
  customer_name VARCHAR(255) NOT NULL,
  customer_phone VARCHAR(20) NOT NULL,
  customer_address VARCHAR(255) NOT NULL,

);

CREATE TABLE Ingredient_provider
(
  provider_id INT NOT NULL,
  provider_name VARCHAR(255) NOT NULL,
  provider_phone VARCHAR(20) NOT NULL,
  provider_address VARCHAR(255) NOT NULL,
  PRIMARY KEY (provider_id)
);

CREATE TABLE Manager
(
  manager_id INT NOT NULL,
  manager_name VARCHAR(255) NOT NULL,
  manager_phone VARCHAR(20) NOT NULL,
  manager_address VARCHAR(255) NOT NULL,
  PRIMARY KEY (manager_id)
  
);
CREATE TABLE Store
(
  store_id INT NOT NULL,
  store_name VARCHAR(255) NOT NULL,
  store_phone VARCHAR(20) NOT NULL,
  store_address VARCHAR(255) NOT NULL,
  manager_id INT NOT NULL,
  PRIMARY KEY (store_id),
  FOREIGN KEY (manager_id) REFERENCES Manager(manager_id)
);

CREATE TABLE Employees
(
  employee_id INT NOT NULL,
  employee_name VARCHAR(255) NOT NULL,
  employee_phone VARCHAR(20) NOT NULL,
  employee_address VARCHAR(255) NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE NOT NULL,
  store_id INT NOT NULL,
  PRIMARY KEY (employee_id),
  FOREIGN KEY (store_id) REFERENCES Store(store_id)
);

CREATE TABLE Shift_of_employees
(
  shift_id INT NOT NULL,
  shift_start_time TIME NOT NULL,
  employee_id INT NOT NULL,
  shift_end_time TIME NOT NULL,
  shift_extra_hours INT NOT NULL,
  shift_date date not null, 
  PRIMARY KEY (shift_id),
  FOREIGN KEY (employee_id) REFERENCES Employees(employee_id)
);

CREATE TABLE Dumpling
(
  dumpling_id INT NOT NULL,
  dumpling_name VARCHAR(255) NOT NULL,
  dumpling_price DECIMAL(10, 2) NOT NULL,
  dumpling_description VARCHAR(255) NOT NULL,
  PRIMARY KEY (dumpling_id)
);


CREATE TABLE ingredients
(
  ingredient_id INT NOT NULL,
  ingredient_name VARCHAR(255) NOT NULL,
  provider_id INT NOT NULL,
  ingredient_cost DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (ingredient_id),
  FOREIGN KEY (provider_id) REFERENCES Ingredient_provider(provider_id)
);

CREATE TABLE Recipe
(
  recipe_id INT primary key,
  dumpling_id INT,
  ingredient_id INT NOT NULL,
  FOREIGN KEY (dumpling_id) REFERENCES Dumpling(dumpling_id),
  foreign key (ingredient_id) references ingredients(ingredient_id)
);

CREATE TABLE Review
(
  review_id INT NOT NULL,
  customer_id INT NOT NULL,
  review_description VARCHAR(255) NOT NULL,
  rating INT NOT NULL,
  review_date DATE NOT NULL,
  dumpling_id INT NOT NULL,
  PRIMARY KEY (review_id),
  FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
  FOREIGN KEY (dumpling_id) REFERENCES Dumpling(dumpling_id)
);

CREATE TABLE invoice_provider
(
  invoice_provider_id INT NOT NULL,
  provider_id INT NOT NULL,
  store_id INT NOT NULL,
  ingredient_id INT NOT NULL,
  quantity INT NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  invoice_date date not null,
  PRIMARY KEY (invoice_provider_id),
  FOREIGN KEY (store_id) REFERENCES Store(store_id),
  FOREIGN KEY (provider_id) REFERENCES Ingredient_provider(provider_id)
);

CREATE TABLE dumpling_inventory
(
	dumpling_inventory_id INT NOT NULL,
	store_id INT NOT NULL,
	dumpling_id INT NOT NULL,
	amount INT NOT NULL, 
	PRIMARY KEY (dumpling_inventory_id),
	FOREIGN KEY (store_id) REFERENCES Store(store_id),
	FOREIGN KEY (dumpling_id) REFERENCES Dumpling(dumpling_id)
);

CREATE TABLE ingredient_inventory
(
	ingredient_inventory_id INT NOT NULL,
	store_id INT NOT NULL,
	ingredient_id INT NOT NULL,
	amount INT NOT NULL, 
	PRIMARY KEY (ingredient_inventory_id),
	FOREIGN KEY (store_id) REFERENCES Store(store_id),
	FOREIGN KEY (ingredient_id) REFERENCES ingredients(ingredient_id)
);

CREATE TABLE Invoice_customer
(
  invoice_customer_id INT NOT NULL,
  order_id INT NOT NULL,
  money DECIMAL(10, 2) NOT NULL,
  customer_id INT NOT NULL,
  store_id INT NOT NULL,
  invoice_date DATE NOT NULL,
  PRIMARY KEY (invoice_customer_id),
  FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
  FOREIGN KEY (store_id) REFERENCES Store(store_id)
);

CREATE TABLE Task
(
  task_id INT NOT NULL,
  task_name VARCHAR(255) NOT NULL,
  task_description VARCHAR(255) NOT NULL,
  hour_salary int not null,
  employee_id INT NOT NULL,
  PRIMARY KEY (task_id),
  FOREIGN KEY (employee_id) REFERENCES Employees(employee_id)
);

create table Discount_type
(
	discount_type_id int primary key,
	discount_percent Decimal(10,2) not null,
	discount_end_date date not null
)


CREATE TABLE Discount
(
  discount_id INT NOT NULL,
  customer_id INT NOT NULL,
  
  invoice_customer_id INT NOT NULL,
  discount_type_id int not null,
  PRIMARY KEY (discount_id),
  FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
  FOREIGN KEY (invoice_customer_id) REFERENCES Invoice_customer(invoice_customer_id),
  foreign key (discount_type_id) references Discount_type(discount_type_id)
);

CREATE TABLE Order_service
(
  order_id INT NOT NULL,
  customer_id INT NOT NULL,
  order_quantity INT NOT NULL,
  dumpling_id INT NOT NULL,
  store_id INT NOT NULL,
  order_date DATE NOT NULL,
  PRIMARY KEY (order_id),
  FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
  FOREIGN KEY (dumpling_id) REFERENCES Dumpling(dumpling_id),
  FOREIGN KEY (store_id) REFERENCES Store(store_id)
);


