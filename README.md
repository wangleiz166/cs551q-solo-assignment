## 1.用户表（user）：

该表包含注册用户的信息，用户可以通过注册页面进行注册。

| 字段名           | 数据类型 | 描述         |
| ---------------- | -------- | ------------ |
| id               | INTEGER  | 用户ID，主键 |
| username         | VARCHAR  | 用户名       |
| password         | VARCHAR  | 密码         |
| email            | VARCHAR  | 电子邮件地址 |
| recipient_name   | VARCHAR  | 收货人姓名   |
| province         | VARCHAR  | 省份         |
| city             | VARCHAR  | 城市         |
| district         | VARCHAR  | 区县         |
| address          | VARCHAR  | 详细地址     |
| phone            | VARCHAR  | 联系电话     |


```sql
CREATE TABLE user (
    id INTEGER PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    recipient_name VARCHAR(50) NOT NULL,
    province VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL,
    district VARCHAR(50) NOT NULL,
    address VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL
);
```


## 2.订单表（order）：
该表包含用户购买商品的订单信息，数据来自于用户下单购买商品时生成的订单。

| 字段名            | 数据类型 | 描述               |
| ----------------- | -------- | ------------------ |
| id                | INTEGER  | 订单ID，主键       |
| purchase_time     | DATETIME | 购买时间           |
| buyer_name        | VARCHAR  | 购买者姓名         |
| buyer_email       | VARCHAR  | 购买者电子邮件地址 |
| buyer_address     | VARCHAR  | 购买者地址         |
| buyer_phone       | VARCHAR  | 购买者电话号码     |
| product_id        | INTEGER  | 商品ID，外键       |
| product_name      | VARCHAR  | 商品名称           |
| product_price     | DECIMAL  | 商品价格           |

```sql
CREATE TABLE order (
    id INTEGER PRIMARY KEY,
    purchase_time DATETIME NOT NULL,
    buyer_name VARCHAR(50) NOT NULL,
    buyer_email VARCHAR(50) NOT NULL,
    buyer_address VARCHAR(100) NOT NULL,
    buyer_phone VARCHAR(20) NOT NULL,
    product_id INTEGER NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    product_price DECIMAL(8, 2) NOT NULL
);
```


## 3.评价表（review）：
该表包含商品的评价信息，数据来自于用户对商品的评价和评论。

| 字段名        | 数据类型 | 描述                   |
| ------------- | -------- | ---------------------- |
| id            | INTEGER  | 评价ID，主键           |
| product_id    | INTEGER  | 商品ID，外键           |
| user_id       | INTEGER  | 评价用户ID，外键       |
| rating        | INTEGER  | 商品评分（0 到 5 星） |
| content       | TEXT     | 评价内容               |
| create_time   | DATETIME | 评价创建时间           |


```sql
CREATE TABLE review (
    id INTEGER PRIMARY KEY,
    product_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    rating INTEGER NOT NULL,
    content TEXT NOT NULL,
    create_time DATETIME NOT NULL
);

```

## 4.购物车表（cart）：

该表包含用户的购物车信息，数据来自于用户在网站上添加商品到购物车时生成的购物车记录。

| 字段名            | 数据类型 | 描述         |
| ----------------- | -------- | ------------ |
| id                | INTEGER  | 购物车ID     |
| user_id           | INTEGER  | 用户ID，外键 |
| product_id        | INTEGER  | 商品ID，外键 |
| product_name      | VARCHAR  | 商品名称     |
| product_price     | DECIMAL  | 商品价格     |
| product_quantity  | INTEGER  | 商品数量     |

```sql
CREATE TABLE cart (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    product_price DECIMAL(8, 2) NOT NULL,
    product_quantity INTEGER NOT NULL
);
```

## 5.支付记录表（payment）：
该表包含用户的支付信息，数据来自于用户对订单进行支付时生成的支付记录。

| 字段名            | 数据类型 | 描述                     |
| ----------------- | -------- | ------------------------ |
| id                | INTEGER  | 支付ID，主键             |
| user_id           | INTEGER  | 用户ID，外键             |
| order_id          | INTEGER  | 订单ID，外键             |
| payment_method    | VARCHAR  | 支付方式                 |
| payment_amount    | DECIMAL  | 支付金额                 |
| payment_time      | DATETIME | 支付时间                 |

```sql
CREATE TABLE payment (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    order_id INTEGER NOT NULL,
    payment_method VARCHAR(50) NOT NULL,
    payment_amount DECIMAL(8, 2) NOT NULL,
    payment_time DATETIME NOT NULL
);
```


## 6.商品表（product）：
该表包含所有商品的信息，数据来自于您提供的 book.csv 和 amazon.csv 数据文件，以及后续您在系统中添加的商品信息。

| 字段名         | 数据类型 | 描述                       |
| -------------- | -------- | -------------------------- |
| id             | INTEGER  | 商品ID，主键               |
| name           | VARCHAR  | 商品名称                   |
| category       | VARCHAR  | 商品分类                   |
| price          | DECIMAL  | 商品价格                   |
| cover          | VARCHAR  | 封面图片链接               |
| paper          | VARCHAR  | 纸质类型                   |
| isbn           | VARCHAR  | ISBN 号                     |
| date           | DATE     | 出版日期                   |
| img_link       | VARCHAR  | 商品图片链接               |
| product_link   | VARCHAR  | 商品链接                   |


```sql
CREATE TABLE product (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    price DECIMAL(8, 2) NOT NULL,
    cover VARCHAR(50) NOT NULL,
    paper VARCHAR(50) NOT NULL,
    isbn VARCHAR(20) NOT NULL,
    date DATE NOT NULL,
    img_link VARCHAR(200) NOT NULL,
    product_link VARCHAR(200) NOT NULL
);
```

