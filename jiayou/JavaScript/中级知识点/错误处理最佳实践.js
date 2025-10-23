// 自定义错误类型
// 自定义空数据错误
class ValidationError extends Error {
    constructor(message, field) {
        super(message);
        this.name = 'ValidationError';
        this.field = field;
        this.date = new Date();
    }
}

// 自定义网络错误
class NetworkError extends Error {
    constructor(message, statusCode) {
        super(message);
        this.name = 'NetworkError';
        this.statusCode = statusCode;
    }
}

// 使用自定义错误
function ValidationUser(user) {
    if(!user.name) {
        throw new ValidationError('用户名不能为空', 'name');
    }
    if(!user.age < 0) {
        throw new ValidationError('年龄不能为负数', 'age');
    }
    return true;
}

// 错误处理
function processUser(userData) {
    try{
        ValidationUser(userData);
        
        // 模拟网络请求
        if(Math.random() < 0.5) {
            throw new NetworkError('网络链接失败', '500');
        }
        console.log('用户处理成功');
        return {success: true, data: userData};

    } catch(error) {
        if(error instanceof ValidationError) {
            console.error(`验证错误: ${error.message}(字段: ${error.field})`);
            return {success: false, error: '输入验证失败'};
        } 
        else if(error instanceof NetworkError) {
            console.error(`网络错误: ${error.message}(状态码: ${error.statusCode})`);
            return {success: false, error: '网络请求失败'};
        }
        else {
            console.error('未知错误', error);
            return {success: false, error: '系统错误'};
        }
    } finally {
        console.log('用户处理流程结束');
    }

}

const result1 = processUser({name: '张三', age: 25});
const result2 = processUser({name: '', age: -1});