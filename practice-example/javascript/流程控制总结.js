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

// 练习题

// 输出1到100之间所有的偶数
for (let x = 1; x <= 100; x++) {
    if (x % 2 == 0) {
        console.log(x)
    }
}

// 判断奇偶
function isOdd_Even(number) {
    if(number % 2 === 0) {
        console.log(`${number}是偶数`)
    }
    else {
        console.log(`${number}是奇数`)
    }
}
isOdd_Even(2)

// 判断季节
let month = 12;
let season;

switch(month) {
    case 3:
    case 4:
    case 5: 
        season = '春季';
        break;
    case 6:
    case 7:
    case 8:
        season = '夏季';
        break;
    case 9:
    case 10:
    case 11:
        season = '秋季';
        break;
    case 12:
    case 1:
    case 2:
        season = '冬季';
        break;
    default:
        break;
}
console.log(season)

// 找出第一个能被7和9整除的数
let number = 1;
while(true) {
    number++;
    if(number % 7 === 0 && number % 9 === 0) {
        console.log(`第一个能被7和9整除的数: ${number}`);
        break;
    }
    else {
        continue;
    }
}

// 打印直角三角形
let count = '';
let line = 6;
while(line >= 0) {
    count += '*';
    console.log(count);
    line--;
}

// 猜数字游戏
const prompt = require('prompt-sync')();
let secretNumber = Math.floor(Math.random(1, 100));
let guess;
while(true) {
    guess = parseInt(prompt('请输入你猜测的数字: '))
    if(guess === secretNumber) {
        console.log('你猜对了')
        break;
    }
    else {
        console.log('猜错了，再试试吧')
    }
}

