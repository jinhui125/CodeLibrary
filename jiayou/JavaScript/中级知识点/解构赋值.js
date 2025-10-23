// 解构赋值
// 对象解构
const person = {
    name: '张三',
    age: 30,
    address: {
        city: '北京',
        street: '长安街'
    },
    hobbies: ['读书', '编程', '旅行']
};

// 基础解构
const {name, age} = person;
// 重命名
const {name: personName, age: personAge} = person;
// 默认值
const {email = '未提供'} = person;
// 嵌套解构
const {address: {city, street}} = person;
// 数组解构
const [firstHobby, secondHobby, ...otherHobbies] = person.hobbies;
// 函数参数解构
function printPerson({name, age, address: {city}}) {
    console.log(`${name}, ${age}岁, 来自${city}`);
}

printPerson(person);
console.log(firstHobby);