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

// 多行箭头函数
const greetUser = (name) => {
    const message = `hello, ${name}`;
    return message;
};
console.log(greetUser('world!!!'));

// 默认参数
function multiply(a, b = 1) {
    return a * b;
}
console.log(multiply(1));
console.log(multiply(1, 2));

function createUser(name, age = 18, isAdmin = false) {
    return {name, age, isAdmin};
}
user_1 = createUser('Bob');
console.log(`name: ${user_1.name} age: ${user_1.age} isAdmin: ${user_1.isAdmin}`);
console.log(createUser('Joh', 27, true));

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