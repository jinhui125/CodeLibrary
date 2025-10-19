// 随机生成颜色

function randomColor() {
    const color = '#' + Math.floor(Math.random() * 16777215).toString(16).padStart(6, '0');
    return color;
}

// 随机生成数组

function randomArray(array_size) {
    const random_array = new Array();

    for(let i = 0; i < array_size; i++) {

        random_array.push(Math.floor(Math.random() * 100));
    }

    return random_array;
}

// 跟踪练习题进度条

let completedExercise = new Set();

function updateProgress() {

    const progress = (completedExercise.size / 27) * 100;
    document.getElementById('progressBar').style.width = `${progress}%`;
    document.getElementById('finish-number').textContent = `${completedExercise.size}`
}

// 练习题-1

function exercise1() {

    const resultElement = document.getElementById('run-result-1');
    resultElement.innerHTML = `<p>Hello, World!</p>`;
    resultElement.className = 'run-result success';

    if(resultElement.className == 'run-result success') {
        completedExercise.add(1);
        updateProgress();
    }
}

// 练习题-2

function exercise2() {

    const color = '#' + Math.floor(Math.random() * 16777215).toString(16).padStart(6, '0');
    // document.getElementById('color-show').style.backgroundColor = color;
    document.getElementsByClassName('run-container')[1].style.backgroundColor = color;
    document.getElementById('run-result-2').innerHTML = `<p>背景颜色已改为: ${color}</p>`;
    document.getElementById('run-result-2').className = 'run-result success';
    
    if(document.getElementById('run-result-2').className == 'run-result success') {
        completedExercise.add(2);
        updateProgress();
    }
}

// 练习题-3

function exercise3() {

    const num1 = parseInt(document.getElementById('num-1').value);
    const num2 = parseInt(document.getElementById('num-2').value);

    const resultElement = document.getElementById('run-result-3');

    if(isNaN(num1) || isNaN(num2)) {
        resultElement.innerHTML = `<p>${num1}或者${num2}不能为空</p>`;
        resultElement.className = 'run-result error';
        return;
    }

    resultElement.innerHTML = `<p>${num1}和${num2}之和: ${num1 + num2}</p>`;
    resultElement.className = 'run-result success';

    if(resultElement.className == 'run-result success') {
        completedExercise.add(3);
        updateProgress();
    }
}

// 练习题-4

function exercise4() {

    const datetime = new Date();
    const resultElement = document.getElementById('run-result-4');

    resultElement.innerHTML = `<p>当前时间: ${datetime.toLocaleString()}</p>`;
    resultElement.className = 'run-result success';

    if(resultElement.className == 'run-result success') {
        completedExercise.add(4);
        updateProgress();
    }
}

// 练习题-5

function exercise5() {

    const resultElement = document.getElementById('run-result-5');
    const hideElement = document.getElementsByClassName('hide-div')[0];
    
    if(hideElement.style.display == 'block') {
        hideElement.style.display = 'none';
        resultElement.innerHTML = `<p>内容隐藏</p>`;
        
    }
    else {
        hideElement.style.display = 'block';
        resultElement.innerHTML = `<p>内容显示</p>`;
    }
    
    resultElement.className = 'run-result success';
    if(resultElement.className == 'run-result success') {
        completedExercise.add(5);
        updateProgress();
    }
}

// 练习题-6 

function exercise6() {
    const resultElement = document.getElementById('run-result-6');
    const inputText = document.getElementById('input-text').value;

    if(inputText.length == 0) {
        resultElement.innerHTML = `<p>输入内容不能为空</p>`;
        resultElement.className = 'run-result error';
        return;
    }

    resultElement.innerHTML = `<p>输入内容: ${typeof(inputText)} ${inputText.length}</p>`;
    resultElement.className = 'run-result success';
    if(resultElement.className == 'run-result success') {
        completedExercise.add(6);
        updateProgress();
    }
}

// 练习题-7

function exercise7() {
    const resultElement = document.getElementById('run-result-7');
    const inputNumber = document.getElementById('input-number').value;
    const ulElement = document.getElementById('list-item');

    if(inputNumber.length == 0) {
        resultElement.innerHTML = `<p>输入内容不能为空</p>`;
        resultElement.className = 'run-result error';
        return;
    }

    const newItem = document.createElement('li');
    newItem.textContent = inputNumber;
    ulElement.appendChild(newItem);
    resultElement.innerHTML = `<p>列表项已添加</p>`;
    resultElement.className = 'run-result success';
    if(resultElement.className == 'run-result success') {
        completedExercise.add(7);
        updateProgress();
    }
}

// 练习题-8

function exercise8(mode) {

    const resultElement = document.getElementById('run-result-8');
    const showNumber = document.getElementById('show-number');
    let count = parseInt(showNumber.textContent);

    if(mode == 'increase') {
        count++;
    }
    else if(mode == 'reduce') {
        count--;
    }
    else {
        count = 0;
    }

    showNumber.textContent = count;
    resultElement.innerHTML = `当前计数: ${count}`;
    resultElement.className = 'run-result success';
    if(resultElement.className == 'run-result success') {
        completedExercise.add(8);
        updateProgress();
    }

}

// 练习题-9

function exercise9(mode) {

    const resultElement = document.getElementById('run-result-9');
    const switchStyle = document.getElementById('switch-style');
    switch(mode) {
        case 'blod':
            switchStyle.style.fontWeight = switchStyle.style.fontWeight === 'bold'? 'normal': 'bold';
            break;
        case 'italic':
            switchStyle.style.fontStyle = switchStyle.style.fontStyle === 'italic'? 'normal': 'italic';
            break;
        case 'underline':
            switchStyle.style.textDecoration = switchStyle.style.textDecoration === 'underline'? 'none': 'underline';
            break;
        case 'color':
            switchStyle.style.color = randomColor();
            break;
        case 'reset':
            switchStyle.style.fontWeight = 'normal';
            switchStyle.style.fontStyle = 'normal';
            switchStyle.style.textDecoration = 'none';
            switchStyle.style.color = 'black';
        default:
            break;
    }

    resultElement.innerHTML = `当前应用样式: ${mode}`;
    resultElement.className = 'run-result success';
    if(resultElement.className == 'run-result success') {
        completedExercise.add(9);
        updateProgress();
    }

}

// 练习题-10

function exercise10(mode) {

    const resultElement = document.getElementById('run-result-10');
    const num1 = parseInt(document.getElementById('number-1').value);
    const num2 = parseInt(document.getElementById('number-2').value);

    let result;

    switch(mode) {
        case 'add':
            result = num1 + num2;
            break;
        case 'subtract':
            result = num1 - num2;
            break;
        case 'multiply':
            result = num1 * num2;
            break;
        case 'divide':
            result = num2 !== 0? num1 / num2: '错误被除数不能为0';
            break;
        default:
            break;
    }

    resultElement.innerHTML = `结果: ${result}`;
    resultElement.className = 'run-result success';
    if(resultElement.className == 'run-result success') {
        completedExercise.add(10);
        updateProgress();
    }
}

// 练习题-11

function exercise11() {

    const resultElement = document.getElementById('run-result-11');
    const showArray = document.getElementById('array-max');
    const random_array = randomArray(array_size = 5);

    showArray.textContent = `数组: [${random_array.toString(16)}]`;
    
    let result;

    // result = random_array.sort()[random_array.length - 1]
    result = Math.max(...random_array);
    resultElement.innerHTML = `数组最大值: ${result}`;
    resultElement.className = 'run-result success';
    if(resultElement.className == 'run-result success') {
        completedExercise.add(11);
        updateProgress();
    }
}

// 练习题-12

function exercise12() {

    const resultElement = document.getElementById('run-result-12');
    const reverse_str = document.getElementById('reverse-string').value;
    let result;

    result = Array.from(reverse_str).reverse().join('');
    resultElement.innerHTML = `反转后的字符串: ${result}`;
    resultElement.className = 'run-result success';
    if(resultElement.className == 'run-result success') {
        completedExercise.add(12);
        updateProgress();
    }
}

// 练习题-13

function exercise13() {

    const resultElement = document.getElementById('run-result-13');
    const factorialNumber = parseInt(document.getElementById('factorial-number').value);
    let result = 1;

    for(let i = factorialNumber; i > 0; i--) {
        result *= i;
    }

    resultElement.innerHTML = `${factorialNumber}的阶乘值: ${result}`;
    resultElement.className = 'run-result success';
    if(resultElement.className == 'run-result success') {
        completedExercise.add(13);
        updateProgress();
    }
}

// 练习题-14

function exercise14() {

    const resultElement = document.getElementById('run-result-14');
    const palindromeStr = document.getElementById('palindrome-string').value;

    if(palindromeStr !== Array.from(palindromeStr).reverse().join('')) {
        resultElement.innerHTML = `${palindromeStr}是否为回文: 否`;
        return;
    }
    
    resultElement.innerHTML = `${palindromeStr}是否为回文: 是`;
    resultElement.className = 'run-result success';
    if(resultElement.className == 'run-result success') {
        completedExercise.add(14);
        updateProgress();
    }
}

// 练习题-15

function exercise15() {

    const resultElement = document.getElementById('run-result-15');
    const vowelString = document.getElementById('vowel-string').value;
    let result = 0;

    Array.from(vowelString).forEach(value => {
        
        if(value == 'a' || value == 'e' || value == 'i' || value == 'o' || value == 'u') {
            result++;
        }
    });

    resultElement.innerHTML = `${vowelString}字符串中的元音字母数量: ${result}`;
    resultElement.className = 'run-result success';
    if(resultElement.className == 'run-result success') {
        completedExercise.add(15);
        updateProgress();
    }
}

// 练习题-16

function exercise16() {

    const resultElement = document.getElementById('run-result-16');
    const showArray = document.getElementById('show-array');
    const random_array = [1, 2, 3, 4, 5, 6, 6, 7, 7, 8];
    let result;

    showArray.textContent = `数组: [${random_array}]`;
    result = new Set(random_array);
    result = [...result];

    resultElement.innerHTML = `除重后的数组: [${result}]`;
    resultElement.className = 'run-result success';
    if(resultElement.className == 'run-result success') {
        completedExercise.add(16);
        updateProgress();
    }
}

// 练习题-17

function exercise17() {

    const resultElement = document.getElementById('run-result-17');
    const fizzbuzzNumber = parseInt(document.getElementById('fizzbuzz-number').value);

    
    if(fizzbuzzNumber % 3 == 0 && fizzbuzzNumber % 5 != 0) {
        resultElement.innerHTML = `${fizzbuzzNumber}的FizzBuzz计算结果: Fizz`;
        // return;
    }
    else if(fizzbuzzNumber % 3 != 0 && fizzbuzzNumber % 5 == 0) {
        resultElement.innerHTML = `${fizzbuzzNumber}的FizzBuzz计算结果: Buzz`;
        // return;
    }
    else if(fizzbuzzNumber % 15 == 0) {
        resultElement.innerHTML = `${fizzbuzzNumber}的FizzBuzz计算结果: FizzBuzz`;
        // return;
    }
    else {
        resultElement.innerHTML = `${fizzbuzzNumber}的FizzBuzz计算结果: ${fizzbuzzNumber}`;
    }
    
    resultElement.className = 'run-result success';
    if(resultElement.className == 'run-result success') {
        completedExercise.add(17);
        updateProgress();
    }
}

// 练习题-18 

function exercise18() {

    const resultElement = document.getElementById('run-result-18');
    const original_array = document.getElementById('original-array');
    const random_array = randomArray(array_size = 7);
    let result;

    original_array.textContent = `原数组: [${random_array.toString(16)}]`
    result = random_array.sort().reverse();
    resultElement.innerHTML = `[${random_array}]数组升序排列结果: [${result}]`;
    resultElement.className = 'run-result success';
    if(resultElement.className == 'run-result success') {
        completedExercise.add(18);
        updateProgress();
    }
}

// 练习题-19 

function exercise19() {

    const resultElement = document.getElementById('run-result-19');
    const wordStrings = document.getElementById('words-string').value;
    const words_array = wordStrings.split(' ');
    let length_array = [];
    let max_length;
    let min_indexOf, max_indexOf;
    let result = [];

    words_array.forEach(value => {
        length_array.push(value.length);
    });

    max_length = Math.max(...length_array);
    min_indexOf = length_array.indexOf(max_length);
    max_indexOf = length_array.lastIndexOf(max_length);

    if(min_indexOf != max_indexOf) {
        for(let i = min_indexOf; i <= max_indexOf; i++) {
            result.push(words_array[i]);
        }
    }
    else {
        result.push(words_array[min_indexOf]);
    }
    
    resultElement.innerHTML = `${wordStrings}字符串中最长的单词: [${result}]`;
    resultElement.className = 'run-result success';
    if(resultElement.className == 'run-result success') {
        completedExercise.add(19);
        updateProgress();
    }
}

// 练习题-20

function exercise20() {

    const resultElement = document.getElementById('run-result-20');
    const transformString = document.getElementById('transform-string').value;
    const transformArray = transformString.split(' ');
    let result = [];

    transformArray.forEach(value => {
        result.push(Array.from(value)[0].toUpperCase() + Array.from(value).splice(1).join(''));
    });

    result = result.join(' ');
    resultElement.innerHTML = `${transformString}首字母大写后的字符串: ${result}`;
    resultElement.className = 'run-result success';
    if(resultElement.className == 'run-result success') {
        completedExercise.add(20);
        updateProgress();
    }
}

// 练习题-21

function exercise21() {

    const resultElement = document.getElementById('run-result-21');
    const sumArray = document.getElementById('sum-array');
    const random_array = randomArray(array_size = 6);
    let result;

    sumArray.textContent = `数组: [${random_array.toString(16)}]`;
    result = random_array.reduce((sum, value) => sum + value);

    resultElement.innerHTML = `[${random_array}]数组之和结果: ${result}`;
    resultElement.className = 'run-result success';
    if(resultElement.className == 'run-result success') {
        completedExercise.add(21);
        updateProgress();
    }
}

// 练习题-22

function exercise22() {

    const resultElement = document.getElementById('run-result-22');
    const checkStrings = document.getElementById('check-specific-string').value;
    const showArray = document.getElementById('show-arr');
    const checkArray = ['apple', 'banana', 'orange', 'pizza', 'water'];
    let includeElement = checkArray.includes(checkStrings)? '包含': '不包含';

    showArray.textContent = `数组: [${checkArray}]`;
    resultElement.innerHTML = `[${checkArray}]是否包含${checkStrings}: ${includeElement}`;
    resultElement.className = 'run-result success';
    if(resultElement.className == 'run-result success') {
        completedExercise.add(22);
        updateProgress();
    }
}

// 练习题-23

function exercise23() {

    const resultElement = document.getElementById('run-result-23');
    const merge_array_1 = document.getElementById('merge-array-1');
    const merge_array_2 = document.getElementById('merge-array-2');
    const random_array_1 = randomArray(array_size = 4);
    const random_array_2 = randomArray(array_size = 6);
    let result = [];

    merge_array_1.textContent = `数组1: [${random_array_1.toString(16)}]`;
    merge_array_2.textContent = `数组2: [${random_array_2.toString(16)}]`;
    result = random_array_1.concat(...random_array_2);

    result = new Set(result);
    result = [...result];
    resultElement.innerHTML = `[${random_array_1}]和[${random_array_2}]的并集除重后的数组: [${result}]`;
    resultElement.className = 'run-result success';
    if(resultElement.className == 'run-result success') {
        completedExercise.add(23);
        updateProgress();
    }
}

// 练习题-24

function exercise24() {

    const resultElement = document.getElementById('run-result-24');
    const statStrings = document.getElementById('stat-array').value;
    const statArray = Array.from(statStrings);
    let statDict = {};
    let result;

    statArray.forEach(value => {
        let min_index = statArray.indexOf(value);
        let max_index = statArray.lastIndexOf(value);
        statDict[value] = (max_index - min_index) + 1;
    });
    result = Object.entries(statDict);
    resultElement.innerHTML = `${statStrings}字符串中各个字符出现的次数: [${result}]`;
    resultElement.className = 'run-result success';
    if(resultElement.className == 'run-result success') {
        completedExercise.add(24);
        updateProgress();
    }
}

// 练习题-25

function exercise25() {

    const resultElement = document.getElementById('run-result-25');
    const original_array = document.getElementById('delayering-array');
    const random_array = [1, 2, 3, [4, 5, 6, [7, 8, [9]]]];

    original_array.textContent = `数组: [1, 2, 3, [4, 5, 6, [7, 8, [9]]]]`;
    random_array.flat(3);

    resultElement.innerHTML = `扁平化后的数组: [${random_array}]`;
    resultElement.className = 'run-result success';
    if(resultElement.className == 'run-result success') {
        completedExercise.add(25);
        updateProgress();
    }
}

// 练习题-26

function exercise26() {

    const resultElement = document.getElementById('run-result-26');
    const original_array_1 = document.getElementById('test-array-1');
    const original_array_2 = document.getElementById('test-array-2');
    const test_array_1 = [1, 2, 3, 4, 5];
    const test_array_2 = [3, 4, 5, 6, 7];
    const test_set_1 = new Set(test_array_1);
    const test_set_2 = new Set(test_array_2);
    const in_result = Array.from(test_set_1.intersection(test_set_2));
    let result = [];

    test_array_1.forEach(value => {
        if(in_result.includes(value)) {
            result.push(value);
        }
    });

    test_array_2.forEach(value => {
        if(in_result.includes(value)) {
            result.push(value);
        }
    });

    original_array_1.textContent = `数组: [${test_array_1}]`;
    original_array_2.textContent = `数组: [${test_array_2}]`;
    resultElement.innerHTML = `数组[${test_array_1}]和数组[${test_array_2}]的交集: [${result}]`;
    resultElement.className = 'run-result success';
    if(resultElement.className == 'run-result success') {
        completedExercise.add(26);
        updateProgress();
    }
}

// 练习题-27

function exercise27() {

    const resultElement = document.getElementById('run-result-27');
    const password = document.getElementById('password').value;
    let score = 0;

    if(password.length >= 8) score++;
    if(/[A-Z]/.test(password)) score++;
    if(/[a-z]/.test(password)) score++;
    if(/[0-9]/.test(password)) score++;
    if(/[^a-zA-Z0-9]/.test(password)) score++;

    if(score > 4) {
        resultElement.innerHTML = '密码强度: 强';
    }
    else if(score > 2) {
        resultElement.innerHTML = '密码强度: 中';
    }
    else {
        resultElement.innerHTML = '密码强度: 弱';
    }
    resultElement.className = 'run-result success';
    if(resultElement.className == 'run-result success') {
        completedExercise.add(27);
        updateProgress();
    }
}