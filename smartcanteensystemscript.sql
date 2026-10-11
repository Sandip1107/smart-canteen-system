create database project;
use project;
create table student(
   Student_Id int auto_increment PRIMARY KEY,
    Name  varchar(100) not null,
    Department varchar(100) not null,
    email varchar(100) not null,
    phone varchar(100) not null,
    gender ENUM('Male','Female','Other')
    );
--ADDING COLUMN ROLL NO AFTER NAME
alter table student
add column roll_no varchar(7) after name;
--
--MAKING ROLL NO UNIQUE
ALTER TABLE student
ADD CONSTRAINT unique_roll_no UNIQUE (roll_no);
--
INSERT INTO student (Student_Id,Name,roll_no,Department,email,phone,gender)
values
(1,'Sandip Sawant','1025239','Computer','sandipsawant2211@gmail.com','9137960945','Male'),
(default,'Sarvesh Sawant','1025240','Computer','sarveshsawant1406@gmail.com','8692097108','Male'),
(default,'Dharmesh Shetty',1025245,'Computer','dharmeshshetty2403@gmail.com','8356841824','Male'),
(default,'Raziel Rumao',1024233,'Computer','razielrumao2711@gmail.com','9665536478','Male'),
(DEFAULT, 'Aarav Patil', 1025254, 'IT', 'aaravpatil@gmail.com', '9876543210', 'Male'),
(DEFAULT, 'Rohan Sharma', 1025255, 'EXTC', 'rohansharma@gmail.com', '9876543211', 'Male'),
(DEFAULT, 'Priya Shah', 1025256, 'Computer', 'priyashah@gmail.com', '9876543212', 'Female'),
(DEFAULT, 'Ananya Deshmukh', 1025257, 'Mechanical', 'ananyadesh@gmail.com', '9876543213', 'Female'),
(DEFAULT, 'Karan Mehta', 1025258, 'Civil', 'karanmehta@gmail.com', '9876543214', 'Male'),
(DEFAULT, 'Neha Joshi', 1025259, 'IT', 'nehajoshi@gmail.com', '9876543215', 'Female'),
(DEFAULT, 'Aditya Kulkarni', 1025260, 'EXTC', 'adityakulkarni@gmail.com', '9876543216', 'Male'),
(DEFAULT, 'Sneha Patil', 1025261, 'Computer', 'snehapatil@gmail.com', '9876543217', 'Female'),
(DEFAULT, 'Rahul Verma', 1025262, 'Mechanical', 'rahulverma@gmail.com', '9876543218', 'Male'),
(DEFAULT, 'Isha Gupta', 1025263, 'Civil', 'ishagupta@gmail.com', '9876543219', 'Female'),
(DEFAULT, 'Vivek More', 1025264, 'IT', 'vivekmore@gmail.com', '9876543220', 'Male'),
(DEFAULT, 'Pooja Nair', 1025265, 'EXTC', 'poojanair@gmail.com', '9876543221', 'Female'),
(DEFAULT, 'Siddharth Rao', 1025266, 'Computer', 'siddharthrao@gmail.com', '9876543222', 'Male'),
(DEFAULT, 'Meera Iyer', 1025267, 'Mechanical', 'meeraiyer@gmail.com', '9876543223', 'Female'),
(DEFAULT, 'Omkar Jadhav', 1025268, 'Civil', 'omkarjadhav@gmail.com', '9876543224', 'Male');
SELECT*FROM STUDENT;
--new table creation.............
create table orders(order_id int primary key,
					order_date DATE,
                    total_amount int,
                    status ENUM('Delivering','Preparing'),
                    Student_Id int,
                    foreign key(Student_Id)
                    references student(Student_Id)
                    );
--inserting data---
INSERT INTO orders
(order_id, order_date, total_amount, status, Student_Id)
VALUES
(1, '2026-10-01', 1500, 'Preparing', 1),
(2, '2026-10-02', 2500, 'Delivering', 2),
(3, '2026-10-03', 800, 'Preparing', 3),
(4, '2026-10-04', 1200, 'Delivering', 4),
(5, '2026-10-05', 3500, 'Preparing', 5),
(6, '2026-10-06', 950, 'Delivering', 6),
(7, '2026-10-07', 1800, 'Preparing', 7),
(8, '2026-10-08', 2200, 'Delivering', 8),
(9, '2026-10-09', 750, 'Preparing', 9),
(10, '2026-10-10', 1600, 'Delivering', 10),
(11, '2026-10-11', 2800, 'Preparing', 11),
(12, '2026-10-11', 1100, 'Delivering', 12),
(13, '2026-10-11', 450, 'Preparing', 13),
(14, '2026-10-11', 3200, 'Delivering', 14),
(15, '2026-10-11', 900, 'Preparing', 15),
(16, '2026-10-11', 1400, 'Delivering', 16),
(17, '2026-10-11', 2000, 'Preparing', 17),
(18, '2026-10-11', 650, 'Delivering', 18),
(19, '2026-10-11', 1750, 'Preparing', 19),
(20, '2026-10-11', 3000, 'Delivering', 1);
select*from orders;
create table FoodItem(
   food_id int primary key,
   name varchar(100) not null,
   category enum('VEG','NON-VEG','Beverage'),
   price int not null,
   stock_quantity int
);
insert into FoodItem
(food_id,name,category,price,stock_quantity)
values
(7219,'Panner-Tikka','VEG',200,10),
(7220,'Dosa','VEG',150,20),
(7231,'Mendu Vada','VEG',80,5),
(7228,'Vada Pav','VEG',30,10),
(7216,'VEG KATLET','VEG',30,10),
(7221, 'Masala Dosa', 'VEG', 180, 15),
(7222, 'Idli Sambhar', 'VEG', 60, 20),
(7223, 'Pav Bhaji', 'VEG', 120, 12),
(7224, 'Cheese Sandwich', 'VEG', 100, 10),
(7225, 'Veg Burger', 'VEG', 90, 15),
(7226, 'Paneer Roll', 'VEG', 130, 8),
(7227, 'French Fries', 'VEG', 80, 20),
(7229, 'Veg Pizza', 'VEG', 220, 10),
(7230, 'Veg Fried Rice', 'VEG', 140, 12),
(7232, 'Samosa', 'VEG', 20, 30),
(7233, 'Cold Coffee', 'BEVERAGE', 90, 15),
(7234, 'Fresh Lime Soda', 'BEVERAGE', 50, 20),
(7235, 'Chicken Sandwich', 'NON-VEG', 150, 10),
(7236, 'Chicken Burger', 'NON-VEG', 180, 8),
(7237, 'Egg Roll', 'NON-VEG', 100, 12);
select*from foodItem;
CREATE TABLE ORDERItem(
    order_item_id int primary key,
    quantity int,
    price int,
    order_id int,
    food_id int,
    foreign key(order_id)
    references orders(order_id),
    foreign key (food_id)
    references FoodItem(food_id)
)
INSERT INTO ORDERItem
(order_item_id, quantity, price, order_id, food_id)
VALUES
(1, 2, 150, 1, 7220),
(2, 1, 200, 1, 7219),
(3, 3, 30, 2, 7228),
(4, 2, 80, 3, 7231),
(5, 1, 30, 4, 7216),
(6, 2, 180, 5, 7221),
(7, 1, 60, 6, 7222),
(8, 3, 120, 7, 7223),
(9, 2, 100, 8, 7224),
(10, 1, 90, 9, 7225),
(11, 2, 130, 10, 7226),
(12, 3, 80, 11, 7227),
(13, 1, 220, 12, 7229),
(14, 2, 140, 13, 7230),
(15, 4, 20, 14, 7232),
(16, 2, 90, 15, 7233),
(17, 1, 50, 16, 7234),
(18, 2, 150, 17, 7235),
(19, 1, 180, 18, 7236),
(20, 3, 100, 19, 7237),
(21, 2, 150, 20, 7220);
select*from orderitem
--admin table
create table admin(
  admin_id int primary key,
  name varchar(100) not null,
  username varchar(100) unique not null,
  password varchar(100)  not null,
  role varchar(100) not null,
  food_id int,
  foreign key(food_id)
  references FoodItem(food_id)
);
INSERT INTO admin
(admin_id, name, username, password, role, food_id)
VALUES
(1, 'Rahul Patil', 'rahul_admin', 'Rahul@123', 'Super Admin', NULL),
(2, 'Sneha Sharma', 'sneha_manager', 'Sneha@123', 'Manager', NULL),
(3, 'Amit Shah', 'amit_food', 'Amit@123', 'Food Manager', 7219),
(4, 'Priya Joshi', 'priya_food', 'Priya@123', 'Food Manager', 7220),
(5, 'Karan Mehta', 'karan_stock', 'Karan@123', 'Stock Manager', 7231),
(6, 'Neha Kulkarni', 'neha_food', 'Neha@123', 'Food Manager', 7228),
(7, 'Rohan Verma', 'rohan_stock', 'Rohan@123', 'Stock Manager', 7216),
(8, 'Pooja Nair', 'pooja_admin', 'Pooja@123', 'Admin', NULL),
(9, 'Vivek More', 'vivek_food', 'Vivek@123', 'Food Manager', 7221),
(10, 'Isha Gupta', 'isha_stock', 'Isha@123', 'Stock Manager', 7222);
#Now , we will perform some operations...........
#1)Display the names, roll numbers, and departments of all students belonging to the Computer department.
select name,roll_no,department from student where department='Computer';
#2)Display all food items whose price is less than ₹100, showing their name, category, and price
select name,category,price from fooditem where price<100;
#3)Display all students in descending order of their roll numbers. Show Name, roll_no, and Department.
select roll_no,name,department from student order by roll_no desc;
#4)Display the different departments present in your student table, without repeating any department.
select  distinct department from student;
#5)Display the 5 most expensive food items, showing their name and price.
select  name,price from fooditem order by price desc limit 5;
#6)Find the total number of students in your student table.
select count(student_id) as no_of_student from student;
#7)Find the total stock quantity available for each food category.
select category,sum(stock_quantity) from fooditem 
group by category;
#8)Find the departments that have more than 3 students. Display the department name and the number of students.
select department,count(student_id) as no_of_student from student group by department having no_of_student>3;
#9)Q9. Find the average price of food items in each category.
#Display:
#- category
#- Average price as avg_price
select category,avg(price) as avg_price from fooditem group by category;
#10)Find the food items whose price is greater than the overall average price of all food items.
#Display:
#- name
#- price
select * from fooditem where price>(select avg(price) from fooditem) ;
#11)Display each student's name, their order ID, and the total amount of that order.
select name ,order_id,total_amount from Student
INNER JOIN ORDERS
on student.student_id=orders.student_id;
#12)Display each order's order_id, the student's Name, and the order's status.
select order_id,name,status from student
INNER join orders
on student.student_id=orders.student_id;
#13)Display the name of students and their order IDs for orders whose status is 'Preparing'
select name,order_id from student
INNER JOIN orders
ON student.student_id=orders.student_id
where orders.status='Preparing';
#14)Display the student name, order ID and total amount of all orders, sorted by total_amount from highest to lowest.
SELECT student.name,
       SUM(orders.total_amount) AS total_spent
FROM student
INNER JOIN orders
ON student.student_id = orders.student_id
GROUP BY student.student_id,student.name;
#15)Find students who have placed at least 2 orders.
select student.name,count(orders.student_id) as no_of_orders from Student
inner join orders
on student.student_id=orders.student_id
group by student.student_id
having count(orders.student_id)>=2;
#16)Find the most expensive food item in each category.
select category,max(price) from fooditem group by category;
#17)Find all food items whose stock_quantity is less than 10.
select*from fooditem where stock_quantity<10;
#18)Display the result as total_revenue.
select sum(total_amount) as total_revenue from orders;
#19)Find how many times each food item has been ordered.
select fooditem.food_id,fooditem.name,count(orderitem.food_id) as no_of_orders from fooditem
INNER JOIN orderitem
ON fooditem.food_id=orderitem.food_id
group by fooditem.food_id;
#20)Find students who have never placed an order
SELECT student.Student_Id, student.Name
FROM student
LEFT JOIN orders
ON student.Student_Id = orders.Student_Id
WHERE orders.order_id IS NULL;
####views
CREATE VIEW order_details_view AS
SELECT
    s.Student_Id,
    s.Name AS student_name,
    o.order_id,
    o.order_date,
    o.total_amount,
    o.status
FROM student s
INNER JOIN orders o
ON s.Student_Id = o.Student_Id;
SELECT * FROM order_details_view;

CREATE VIEW food_menu_view AS
SELECT
    food_id,
    name,
    category,
    price
FROM FoodItem;
select * from food_menu_view;
create view food_sales_view as
select 
fooditem.food_id,
fooditem.name as food_name,
sum(orderitem.quantity) as total_quantity_ordered
from fooditem
inner join orderitem
on fooditem.food_id=orderitem.food_id
group by fooditem.food_id;
select*from food_sales_view;
delimiter //
create procedure getStudentsOrder(IN p_student_id INT)
BEGIN
   SELECT
      student.Name,
        orders.order_id,
        orders.order_date,
        orders.total_amount,
        orders.status
	  FROM student
    INNER JOIN orders
        ON student.Student_Id = orders.Student_Id
    WHERE student.Student_Id = p_student_id;
END //
delimiter ;
call getStudentsOrder(1);