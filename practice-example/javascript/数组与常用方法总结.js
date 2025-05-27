// 数组基础

//数组创建

// 字面量创建
const fruits = [1, 2, 3];
console.log(fruits);

// 改造函数创建
const numbers = new Array(1, 2, 3);
console.log(numbers);

// 空数组+填充
const emptyArray = new Array(3).fill(0);
console.log(emptyArray);

// Array.from创建
const chars = Array.from('array');
console.log(chars);

// 基础操作

const arr = [1, 2, 3];

// 访问元素
console.log(arr[1]);

// 修改元素
arr[1] = 'a';
console.log(arr[1]);

// 数组长度
console.log(arr.length);

// 检测数组
console.log(Array.isArray(arr)? '是数组': '不是数组');

// 数组方法分类

// 修改原数组的方法

// 尾部操作
const stack = [1, 2];
stack.push(3);
console.log(stack);
stack.pop();
console.log(stack);

// 头部操作
const queue = [1, 2];
queue.shift(0);
console.log(queue);
queue.unshift();
console.log(queue);

// 万能修改
const nums = [1, 2, 3, 4];
nums.splice(0, 0, 0);   // 添加元素
console.log(nums);
nums.splice(1, 3, 'a', 'b', 'c');   // 替换元素
console.log(nums);
nums.splice(0, 1);  // 删除元素
console.log(nums);

// 反转数组
const letters = ['a', 'b', 'c'];
letters.reverse();
console.log(letters);

// 排序
const unsorted = [3, 1, 4, 2];
unsorted.sort();
console.log(unsorted);
unsorted.sort((a, b) => b - a);
console.log(unsorted);

// 不修改原数组的方法

// 切片
const arr_1 = [1, 2, 3, 4, 5];
const subArr = arr_1.slice(1, 4);
console.log(subArr);

// 合并
const arr_2 = [1, 2];
const arr_3 = [3, 4];
const combined = arr_2.concat(arr_3);
console.log(combined);

// 连接字符串
const words = ['Hello', 'World'];
const sentence = words.join(' ');
console.log(sentence);

// 查找索引
const numbs = [1, 2, 3, 2, 1];
console.log(`numbs数组第一次出现元素2的索引：${numbs.indexOf(2)}`);
console.log(`numbs数组最后一次出现元素2的索引：${numbs.lastIndexOf(2)}`);

// 包含检查
console.log(numbs.includes(3)? '包含': '不包含');

// 迭代方法

const numbes = [1, 2, 3, 4, 5, 6];

// 遍历
numbes.forEach(element => console.log(element));

// 映射新数组
const squares = numbes.map(element => element * element);
squares.forEach(element => console.log(element));

// 过滤
const event = numbes.filter(element => element % 2 === 0);
console.log(`数组中的元素满足指定过滤条件的元素：${event}`);

// 累积
const sum = numbes.reduce((total, element) => total + element, 0);
console.log(`numbes数组元素值之和：${sum}`);

// 查找元素
const findEven = numbes.find(element => element % 2 === 0);
const findEvenIndex = numbes.findIndex(element => element % 2 === 0);
console.log(`numbes数组中满足指定条件的元素值：${findEven}、元素索引：${findEvenIndex}`);

// 条件检查
const hasEven = numbes.some(element => element % 2 === 0);
console.log(hasEven? '数组元素中至少存在一个满足条件的元素': '数组元素中没有一个元素满足条件');

const allEven = numbers.every(element => element % 2 === 0);
console.log(allEven? '数组中所有元素都满足条件': '数组中所有元素都不满足条件');

// ES6+ 新增方法

// 从类数组创建
const set = new Set([1, 2, 3]);
const arrFromSet = Array.from(set);
console.log(arrFromSet);

// 创建数组
const arr_4 = Array.of(1, 2, 3);
console.log(arr_4);

// 反向查找元素
const number_arr = [1, 2, 3, 4, 2];
const findLastEven = number_arr.findLast(element => element === 2);
const findLastEvenIndex = number_arr.findLastIndex(element => element === 2);
console.log(`反向查找number_arr数组中满足指定条件元素值：${findLastEven}、元素索引：${findLastEvenIndex}`);

// 扁平化
const nested = [1, 2, [3, [4, [5, [6]]]]];
console.log(nested.flat());  // 默认值：1
console.log(nested.flat(2));
console.log(nested.flat(3));
console.log(nested.flat(4));

// 数组解构与扩展运算符

const [first, second, ...rest] = [1, 2, 3, 4];
console.log(`first: ${first}; second: ${second}; ...rest: ${rest}`);

// 扩展运算符
const arr_5 = [1, 2];
const arr_6 = [3, 4];
const merged = [...arr_5, ...arr_6];
console.log(merged);

// 复制数组
const original = [1, 2, 3];
const copy = [...original];
console.log(copy);

// 练习题

// 编写一个函数，接收一个数字数组，返回所有偶数组成的数组
function getEven(arr) {
    return arr.filter(element => element % 2 === 0);
}
console.log(getEven(Array.of(1, 2, 3, 4)));

// 实现一个函数，将二维数组扁平化
function flatten(arr) {
    return arr.reduce((acc, element) => acc.concat(element), []);
}
console.log(flatten([[1, 2], [3, 4], [5]]));

// 实现一个数组去重函数
function unique(arr) {
    return [...new Set(arr)];
}
console.log(unique([1, 2, 2, 3, 4, 4, 5]));

// 实现一个数组分组函数
function groupBy(arr, keyFunc) {
    return arr.reduce((acc, item) => {
            const key = keyFunc(item);
            if (!acc[key]) acc[key] = [];
            acc[key].push(item);
            return acc;
        }, {});
}

function chunk(arr, size) {
    const result = [];
    for (let i = 0; i < arr.length; i += size) {
      result.push(arr.slice(i, i + size));
    }
    return result;
  }

const data = [
    { id: 1, category: 'A' },
    { id: 2, category: 'B' },
    { id: 3, category: 'A' }
];

console.log(groupBy(data, item => item.category));
console.log(chunk(data, 2));

// 多数组交集
function intersection(...arrays) {
    return arrays.reduce((acc, curr) => {
      return acc.filter(item => curr.includes(item));
    });
  }