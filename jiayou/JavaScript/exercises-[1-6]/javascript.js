// 练习题-1
function exercise1() {
    const info = {
        name: '李小明',
        age: 25,
        city: '北京',
        hobbies: ['阅读', '编程', '旅游']
    };

    let result = `<p><strong>姓名:${info.name}</strong></p>
                  <p><strong>年龄:${info.age}</strong></p>
                  <p><strong>城市:${info.city}</strong></p>
                  <p><strong>爱好:${info.hobbies.join(', ')}</strong></p>`;

    document.getElementById('result-1').innerHTML = result;
    document.getElementById('result-1').className = 'result success';
}

// 练习题-2
function exercise2() {
    const score = parseInt(document.getElementById('scoreInput').value);
    const resultElement = document.getElementById('result-2');

    if(isNaN(score) || score > 100 || score < 0) {
        resultElement.innerHTML = '请输入0-100之间的有效值';
        resultElement.className = 'result error';
        result;
    }

    let grade;
    if (score >= 90) {
        grage = 'A';
    }
    else if (score >= 80) {
        grage = 'B';
    } 
    else if (score >= 70) {
        grage = 'C';
    }
    else if (score >= 60) {
        grage = 'D';
    }
    else {
        grage = 'F';
    }

    resultElement.innerHTML = `<p>成绩${score}的等级是:<strong>${grage}</strong></p>`;
    resultElement.className = 'result success';
}

// 练习题-3
function exercise3() {
    
    let result = 0;

    let num = 0;

    while(num < 101) {

        num ++;
        if (num % 2 == 0) {
            result += num;
        }
        else {
            continue;
        }
        
    }

    document.getElementById('result-3').innerHTML = `<p>1到100之间所有偶数的和是<strong>${result}</strong></p>`;
    document.getElementById('result-3').className = 'result success';
}

// 练习题-4
function exercise4() {

    const num1 = parseInt(document.getElementById('number-1').value);
    const num2 = parseInt(document.getElementById('number-2').value);
    const resultElement = document.getElementById('result-4')


    if(isNaN(num1) || isNaN(num2) || num1 == null || num2 == null) {
        resultElement.innerHTML = `<p>数字1和数字2必须都是数字以及都不为空</p>`;
        resultElement.className = 'result error';
        return;
    }

    function product(a, b) {
        return a * b;
    }

    let result = product(num1, num2);

    document.getElementById('result-4').innerHTML = `<p>${num1}和${num2}的乘积为<strong>${result}</strong></p>`;
    document.getElementById('result-4').className = 'result success';
}

// 练习题-5
function exercise5() {

    let colors = ['红色', '蓝色', '绿色', '黄色', '紫色'];
    let steps = [];

    const resultElement = document.getElementById('result-5');

    steps.push(`初始数组: [${colors}]`);

    colors.push('橙色');
    steps.push(`添加’橙色‘后: [${colors}]`);

    colors.shift();
    steps.push(`删除第一个颜色后: [${colors}]`);

    colors.reverse();
    steps.push(`反转数组后: [${colors}]`);

    resultElement.innerHTML = `${steps.join('<br>')}`;
    resultElement.className = 'result success';

}

// 练习题-6
function exercise6() {

    const palindrome = document.getElementById('palindromeInput').value;
    const resultElement = document.getElementById('result-6');

    if(!palindrome) {
        resultElement.innerHTML = `<p>请输入一个字符串</p>`;
        resultElement.className = 'result error';
        return;
    }

    function isPalindrome(str) {

        const clearStr = str.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
        const reversedStr = clearStr.split('').reverse().join('');
        return clearStr === reversedStr;

    }

    const result = isPalindrome(palindrome);
    if(result) {
        resultElement.innerHTML = `'${palindrome}'<strong>是</strong>回文`;
    }
    else {
        resultElement.innerHTML = `'${palindrome}'<strong>不是</strong>回文`;
    }
    resultElement.className = 'result success';
}