// 变量声明

// var函数作用域，可以重复声明
var name = '张三';
var name = '李四';

// let块状作用域，不可以重复声明，可以重新赋值
let count = 25;

// const块状作用域，不可以重复声明，不可以重新赋值
const PI = 3.14;

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