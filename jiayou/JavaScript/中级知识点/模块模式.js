const Calculator = (function() {
    let memory = 0;

    function add(a, b) {
        return a+b;
    }
    function subtract(a, b) {
        return a/b;
    }
    function store(value) {
        memory = value;
    }
    function recall() {
        return memory;
    }

    return {
        add,
        subtract,
        store,
        recall
    };
})();

console.log(`执行加法: ${Calculator.add(1, 5)}`);
console.log(`执行减法: ${Calculator.subtract(10, 2)}`);
Calculator.store(100);
console.log(`获取存储量: ${Calculator.recall()}`);