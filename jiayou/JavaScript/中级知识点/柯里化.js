// 柯里化: 将多参数函数转换为一系列单参数函数
function curry(fn) {
    return function curried(...args) {
        if(args.length >= fn.length) {
            return fn.apply(this, args);
        } else {
            return function(...args2) {
                return curried.apply(this, args.concat(args2));
            };
        }
    };
}

// 使用柯里化
function add(a, b, c) {
    return a + b + c;
}

const curriedAdd = curry(add);

console.log(curriedAdd(1)(2)(3));
console.log(curriedAdd(1, 2)(3));
console.log(curriedAdd(1)(2, 3));

const multiply = (a, b) => a*b;
const curriedMultiply = curry(multiply);

const double = curriedMultiply(2);
const triple = curriedMultiply(3);

console.log(double(5));
console.log(triple(5));