function multiplyBy(factor) {
    return function(number) {
        return number * factor;
    }
}

const double = multiplyBy(2);
const triple = multiplyBy(3);

console.log(double(5));
console.log(triple(5));

const numbers = [1, 2, 3, 4, 5];

const doubled = numbers.map(num => num * 2);
const even = numbers.filter(num => num % 2 === 0);
const sum = numbers.reduce((acc, num) => acc+num, 0);

console.log(doubled);
console.log(even);
console.log(sum);

