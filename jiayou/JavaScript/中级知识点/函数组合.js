// 函数组合
function compose(...fns) {
    return function(x) {
        return fns.reduceRight((acc, fn) => fn(acc), x);
    };
}

function pipe(...fns) {
    return function(x) {
        return fns.reduce((acc, fn) => fn(acc), x);
    };
}

const add5 = x => x + 5;
const multiply3 = x => x * 3;
const subtract2 = x => x - 2;

const composed = compose(subtract2, multiply3, add5);
const piped = pipe(add5, multiply3, subtract2);

console.log(composed(5));
console.log(piped(5));