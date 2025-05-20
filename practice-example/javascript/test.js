let num = 123;
let str = 'Hello';
let bool = true;
let nothing = null;
let notDefine = undefined;
let sym = Symbol('id');
let bigNum = 123n;

let obj = { name: '张三'};
let arr = [1, 2, 3];
let func = function() {};

// 数据类型
console.log(typeof num);
console.log(typeof str);
console.log(typeof bool);
console.log(typeof nothing);
console.log(typeof notDefine);
console.log(typeof sym);
console.log(typeof bigNum);
console.log(typeof obj);
console.log(typeof arr);
console.log(typeof func);

// 基础运算符
console.log(10 + 10);
console.log(10 - 10);
console.log(10 * 10);
console.log(10 / 10);
console.log(10 % 3);
console.log(10 ** 5);

// 比较运算符
console.log(10 == '10');
console.log(10 === '10');
console.log(10 != '10');
console.log(10 !== '10');

// 逻辑运算符
console.log(true && false);
console.log(true || false);
console.log(!true);

// 三元运算符
let age = 18;
let result = '';
result = age >= 18 ? '可以投票':'不可以投票';
console.log(result);

// 流程控制

// 分支、判断结构
// if else 结构
let score = 90;
if (score > 90 && score <= 100) {
    console.log('优秀');
}
else if (score <= 90 && score > 70) {
    console.log('良好');
}
else if (score <= 70 && score > 60) {
    console.log('普通');
}
else {
    console.log('差');
}

// switch 结构
let day = 3;
switch(day) {
    case 1:
        console.log('星期一');
        break;
    case 2:
        console.log('星期二');
        break;
    case 3:
        console.log('星期三');
        break;
    case 4:
        console.log('星期四');
        break;
    case 5:
        console.log('星期五');
        break;
    default:
        break;
}

// 循环结构
// for 循环
for (let x = 1; x <=5; x++) {
    console.log(x)
}
console.log('for循环结构输出结果')

// while结构
let x = 1;
while(x <= 5) {
    console.log(x);
    x++;
}
console.log('while循环结构输出结果')

// do while 结构
let j = 1;
do {
    console.log(j);
    j++;
} while(j <= 5);
console.log('do while循环结构输出结果')

// 输出1到100之间所有的偶数
for (let x = 1; x <= 100; x++) {
    if (x % 2 == 0) {
        console.log(x)
    }
}

// 函数基础

// 函数声明
function greet(name) {
    return 'Hello, ' + name;
}
console.log(greet('world!'));

// 函数表达式
const square = function(x) {
    return x * x;
};
console.log(square(5));

// 箭头函数
const add = (a, b) => a + b;
console.log(add(2, 2));

// 默认参数
function multiply(a, b = 1) {
    return a * b;
}
console.log(multiply(1));
console.log(multiply(1, 2));

// 剩余参数
function sum(...numbers) {
    return numbers.reduce((total, num) => total + num);
}
console.log(sum(1, 2, 3, 4, 5));

// 接收一个参数n，返回1到n的和
function test_func01(n) {
    let tmp_var = 0;
    for (n; n > 0; n--) {
        tmp_var += n;
    }
    return tmp_var;
}
console.log(test_func01(10));
console.log(test_func01(100));

// 参数解构
function printUser({name, age}) {
    console.log(`${name} is ${age} years old`)
}
printUser({name: 'Tom', age: '18'})

// 作用域和闭包
function outer() {
    let count = 0;
    return function inner() {
        count++;
        return count;
    };
}
const counter = outer();
console.log(counter());
console.log(counter());

// 立即执行函数
(function (name) {
    console.log(`hello, ${name}`)
})('world')

// 函数作为参数
function operate(a, b, operation) {
    console.log(operation(a, b));
}
operate(5, 3, (x, y) => x * y);

// 函数作为返回值
function createMultiplier(factor) {
    return function(number) {
        return number * factor;
    };
}
const double = createMultiplier(2);
console.log(double(5));

// 递归函数
function factorial(n) {
    if (n <= 1) return 1;
    return n * factorial(n-1);
}
console.log(factorial(5));

// 生成器函数
function* idGenerator() {
    let id = 1;
    while (true) {
        yield id++;
    };
}
const gen = idGenerator();
console.log(gen.next().value);
console.log(gen.next().value);

// 编写一个函数，接收两个数字参数，返回它们的乘积
function product(a, b) {
    return a * b;
}
console.log(product(1, 2));

// 实现一个函数，将摄氏温度转换为华氏温度（公式：F = C × 9/5 + 32）
function transform(temperature_value) {
    return (temperature_value * 9/5) + 32;
}
console.log(transform(32));

