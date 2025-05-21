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
