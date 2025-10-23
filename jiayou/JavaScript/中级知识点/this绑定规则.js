// this的四种绑定规则
const obj = {
    name: '我的对象',

    // 1. 方法调用 - this指向调用对象
    regularFunction: function() {
        console.log('普通函数: ', this.name);
    },

    // 2. 箭头调用 - this继承自外层作用域
    arrowFunction: () => {
        console.log('箭头函数: ', this.name);
    },

    // 嵌套函数中的this问题
    nestedFunction: function() {
        console.log('外层this: ', this.name);

        function innerFunction() {
            console.log('内层普通函数this', this.name);
        };

        const innerArrow = () => {
            console.log('内层箭头函数this: ', this.name);
        };

        innerFunction();
        innerArrow();
    },

};

obj.regularFunction();
obj.arrowFunction();
obj.nestedFunction();

// 3. 构造函数调用 - this指向新创建的对象
function Person(name) {
    this.name = name;
    this.sayHello = function() {
        console.log(`hello, 我是${this.name}`);
    };

}

const person1 = new Person(name='张三');
person1.sayHello();

// 4. 显示绑定
function introduce(greeting, punctuation) {

    console.log(`${greeting}, 我是${this.name}${punctuation}`);
}

const user1 = {name: '李四'};
const user2 = {name: '王五'};

introduce.call(user1, '您好', '!');
introduce.apply(user2, ['嗨', '!!']);

const boundIntroduce = introduce.bind(user1, '欢迎');
boundIntroduce('...');