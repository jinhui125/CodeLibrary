let globalVar = 'global';

function outer() {

    let outerVar = 'outer';

    function inner() {
         let innerVar = 'inner';
         console.log(`全局变量: ${globalVar}`);
         console.log(`外部变量: ${outerVar}`);
         console.log(`内部变量: ${innerVar}`);
    }

    inner();
}

outer();