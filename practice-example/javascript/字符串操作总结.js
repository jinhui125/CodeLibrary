// 字符串基础

// 字符串创建

// 字面量创建
const str_1 = 'Hello world';
const str_2 = 'Hello world';
const str_3 = 'Hello world';

// 构造函数创建
const str_4 = new String('Hello world');

// 多行字符串
const str_5 = `第一行
第二行
第三行`;

console.log(`str_1: ${str_1}; str_2: ${str_2}; str_3: ${str_3}; str_4: ${str_4}; str_5: ${str_5};`);

// 字符串模板（ES6）
const name = '张三';
const age = 25;

// 模板字符串
const greeting = `您好，我是${name}，今年${age}`;
console.log(greeting);

// 表达式计算
const a = 5, b = 10;
const result = `a+b的结果：${a+b}`;
console.log(result);

// 字符串属性和方法

// length属性
const str_6 = 'hello ';
console.log(str_6.length);

// 字符串查询方法
const text_1 = 'Hello World, welcome to JavaScript!';

// charAt / charCodeAt
console.log(text_1.charAt(0));
console.log(text_1.charCodeAt(0));

// indexOf / LastIndexOf
console.log(text_1.indexOf('o'));
console.log(text_1 .lastIndexOf('o'));

// includes / startsWith/ endsWidth（ES6）
console.log(text_1.includes('World'));
console.log(text_1.includes('world'));
console.log(text_1.startsWith('Hello'));
console.log(text_1.startsWith('hello'));
console.log(text_1.endsWith('!'));

// 正则表达式
console.log(text_1.search('/[A-Z]/'));

// 字符串修改方法

const str_7 = 'Hello';

// concat
console.log(str_7.concat(' world'));

// repeat
console.log(str_7.repeat(3));

// padStart / padEnd
console.log('5'.padStart(5, '0'));
console.log('5'.padEnd(5, '0'));

// toLowerCase / toUpperCase
console.log(str_7.toLowerCase());
console.log(str_7.toUpperCase());

// 字符串提取与分割

const str_8 = 'Hello World';

// slice
console.log(str_8.slice(3, 6));

// substring
console.log(str_8.substring(3, 6))  // substring索引不能为负数，slice的索引可以为负数

// split
console.log(str_8.split(' '));

// 字符串替换

// replace（只替换提一次匹配到的字符串）
let text_2 = 'Hello World, World is beautiful';

console.log(text_2.replace('World', 'JavaScript'));

// replaceAll
console.log(text_2.replaceAll('World', 'JavaScript'));

// 使用正则表达式替换
console.log(text_2.replace('/World/g', 'JavaScript'));

// 字符串修剪

const str_9 = '   Hello World   ';

// trim / trimStart / trimEnd
console.log(str_9.trim());
console.log(str_9.trimStart());
console.log(str_9.trimEnd());

// 字符串与正则表达式

//正则匹配
const text_3 = 'The rain in Spain falls mainly in the plain';

// match
console.log(text_3.match(/ain/g));

// matchAll
const matches = [...text_3.matchAll(/ain/g)];
console.log(matches[0]);

// 正则测试
// const pattern = '/^[A-Za-z]+@[A-Za-z]+\.[A-Za-z]+$/'

// test
// console.log(pattern.test('text@example.com'));
// console.log(pattern.test('invalid-email'));

// 字符串编码与解码

// 编码方法
const str_10 = '你好';

//encodeURI / decodeURI（用于整个URI）
console.log(encodeURI(str_10));
console.log(decodeURI(encodeURI(str_10)));

// Base64
const text_4 = 'Hello World';

// btoa / atob（Base64编码解码）
const encoded = btoa(text_4);
console.log(encoded);
console.log(atob(encoded));

// 练习题

// 编写一个函数，统计字符串中某个字符出现的次数
function countChar(str, char) {
    return str.split(char).length - 1;
}
console.log(countChar('hello world', 'l')); 

// 实现一个函数，将字符串中的单词首字母大写
function capitalizeWords(str) {
    return str.split(' ').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
}
console.log(capitalizeWords('hello world'));

// 实现一个简单的字符串压缩函数
function compressString(str) {
    let result = '';
    let count = 1;
    for(let i = 0; i < str.length; i++) {
        if(str[i] === str[i+1]) {
            count++;
        }
        else {
            result += str[i] + count;
            count = 1;
        }
    }

    return result;
}
console.log(compressString('aaabbbccca'));

// 实现一个简单的模板引擎
function renderTemplate(template, data) {

    for(const [key, value] of Object.entries(data)) {
        template = template.replace(`{{${key}}}`, value);
        // console.log(key, value);
    }
    return template
}

const template = 'Hello, {{name}}! You have {{count}} new messages.';
const data = { name: 'Alice', count: 5 };
// renderTemplate(template, data);
console.log(renderTemplate(template, data));

// 字符串反转
function reverseString(str) {
    return [...str].reverse().join('');
    // 或者
    // return str.split('').reverse().join('');
}

// 检查回文
function isPalindrome(str) {
    const cleaned = str.toLowerCase().replace(/[^a-z0-9]/g, '');
    return cleaned === [...cleaned].reverse().join('');
}
