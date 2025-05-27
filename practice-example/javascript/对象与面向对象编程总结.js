// 对象与面向对象编程总结


// 对象自变量
const preson = {
    name : '张三',
    age : '18',
    greet() {
        console.log(`您好，我是${this.name}`);
    }
};

// 使用构造函数
const preson2 = new Object()
preson2.name = '李四';
preson2.age = '19';

// 点表示法
console.log(preson.name);
// 括号表示法
console.log(preson['age']);
// 动态属性名
const prop = 'name';
console.log(preson[prop]);
// 访问对象方法
preson.greet();

// 构造函数
// 自定义构造函数
function Preson(name, age) {
    this.name = name;
    this.age = age;
    this.greet = () => console.log(`你好，我是${this.name}`);
}
const preson_1 = new Preson(name='kylee', age=18);
preson_1.greet();

// 原型与继承

// 原型基础
Preson.prototype.sayAge = () => console.log(`我今年${age}岁`);
preson_1.sayAge();

// 原型链继承
function Student(name, age, grade) {
    Preson.call(this, name, age);
    this.grade = grade;
}

Student.prototype = Object.create(Preson.prototype);
Student.prototype.constructor = Student;

const student_1 = new Student('sylar', 20, '高三');
student_1.greet();

// 类

// 类定义
class Animal {
    constructor(name) {
        this.name = name;
    }

    speak() {
        console.log(`${this.name}发出声音`);
    }

}

const dog = new Animal(name='小狗');
dog.speak();

// 类继承
class Cat extends Animal {
    constructor(name, color) {
        super(name);
        this.color = color;
    }
    speak() {
        super.speak();
        console.log(`${this.name}喵喵喵叫`);
    }
}

const cat = new Cat(name='小花', color='白色');
cat.speak();

// 高级特性

class Circle {
    constructor(radius) {
        this._radius = radius;
    }
    get radius() {
        return this._radius;
    }

    set radius(value) {
        if(value <= 0) { console.log('半径必须大于0');}
        this._radius = value;
    }

    get area() {
        return Math.PI * this._radius ** 2;
    }
}

const circle = new Circle(radius=0.5);
console.log(`半径为${circle.radius}的面积为${circle.area}`);
circle.radius = 1;
console.log(`半径为${circle.radius}的面积为${circle.area}`);

// 静态方法

class MathUtils {
    static add(a, b) {
        return a + b;
    }
}

console.log(MathUtils.add(a = 1, b = 1));

// 私有字段

class User {

    //声明私有字段
    #password;

    constructor(username, password) {
        this.username = username;
        this.#password = password;
    }

    checkPassword(pwd) {
        return this.#password === pwd;
    }
}

const user = new User('admin', '123456');
console.log(user.checkPassword('123456')? '密码正确': '密码错误');
console.log(user.checkPassword('12345')? '密码正确': '密码错误');
// console.log(user.#password)  //报错

// 练习题

// 创建一个Book类，包含title、author和year属性，以及一个getInfo()方法返回书籍信息。
class Book {
    constructor(title, author, year) {
        this._title = title;
        this._author = author;
        this._year = year;
    }

    get getInfo() {
        console.log(`书名：${this._title}；作者：${this._author}；年份：${this._year}`);
    }
}

const book = new Book(title='三体', author='刘慈欣', year='2016')
book.getInfo;

// 创建一个Rectangle类，包含width和height属性，以及计算面积的area属性和计算周长的perimeter属性。

class Rectangle {
    constructor(width, height) {
        this._width = width;
        this._height = height;
    }

    get width() {
        return this._width;
    }

    get height() {
        return this._height;
    }

    set width(value) {
        this._width = value;
    }

    set height(value) {
        this._height = value;
    }

    get area() {
        return this._width * this._height;
    }

    get perimeter() {
        return (this._width + this._height) * 2;
    }
}

const rect = new Rectangle(width=10, height=20);
console.log(`宽：${rect.width}；长：${rect.height}；面积：${rect.area}；周长：${rect.perimeter}`)
rect.width = 20;
rect.height = 30;
console.log(`宽：${rect.width}；长：${rect.height}；面积：${rect.area}；周长：${rect.perimeter}`)

// 实现一个继承链：Vehicle → Car → ElectricCar，每层添加特有属性和方法。

class Vehicle {
    constructor(name, year) {
        this._name = name;
        this._year = year;
    }

    get name() {
        return this._name;
    }

    get year() {
        return this._year;
    }

    set name(value) {
        this._name = value;
    }

    set year(value) {
        this._year = value;
    }

    carInfo() {
        console.log(`车辆品牌：${this._name}；生成年份：${this._year}`)
    }
}

class Car extends Vehicle {
    constructor(name, year, carType) {
        super(name, year);
        this._carType = carType;
    }

    get carType() {
        return this._carType;
    }

    set carType(value) {
        this._carType = value;
    } 

    carInfo() {
        super.carInfo();
        console.log(`汽车类型：${this._carType}`);
    }
}

class ElectricCar extends Car {
    constructor(name, year, carType, range) {
        super(name, year, carType);
        this._range = range;
    }

    get range() {
        return this._range;
    }

    set range(value) {
        this._range = value;
    } 

    carInfo() {
        super.carInfo();
        console.log(`电池续航：${this._range}`);
    }
}

const lixiang = new ElectricCar(name='理想', year='2025', carType='新能源', range='635km');
lixiang.carInfo();

// 创建一个BankAccount类，包含私有字段#balance，以及deposit()、withdraw()和checkBalance()方法。

class BankAccount {

    #balance;

    constructor(balance) {
        this.#balance = balance;
    }

    checkBalance() {
        console.log(`银行账户余额：${this.#balance}`);
    }

    deposit(value) {
        this.#balance += value;
        console.log('存钱...')
        this.checkBalance();
    }

    withdraw(value) {
        this.#balance -= value;
        console.log('取钱...')
        this.checkBalance();
    }
}

const account = new BankAccount(balance=1000);
account.deposit(1000);
account.withdraw(1000);
account.checkBalance();