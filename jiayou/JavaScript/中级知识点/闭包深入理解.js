function createCounter() {

    let count = 0;

    return {
        increment: function() {
            count++;
            return count;
        },
        decrement: function() {
            count--;
            return count;
        },
        getCount: function() {
            return count;
        }
    };
}

const counter = createCounter();
console.log(`计数加1: ${counter.increment()}`);
console.log(`计数减1: ${counter.decrement()}`);
console.log(`获取计数值: ${counter.getCount()}`);

// 闭包单独作用域
const counter1 = createCounter();
const counter2 = createCounter();
console.log(`counter1计数加1: ${counter1.increment()}`)
console.log(`counter2计数加1: ${counter2.increment()}`)