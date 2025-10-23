// async/await
async function fetchUserData(userID) {

    try {
        console.log('开始获取用户数据...');

        // 模拟异步操作
        const user = await new Promise(resolve => {
            setTimeout(() => resolve({id: userID, name: '张三'}), 1000);
        });
        const posts = await new Promise(resolve => {
            setTimeout(() => resolve(['文章1', '文章2']), 500);
        });

        return {
            user,
            posts
        };
    } catch(error) {
        console.error('获取数据失败:', error);
        throw error;
    }
}

// 使用async函数
async function  displayUserData() {
    
    try {

        const data = await fetchUserData(userID = 1);
        console.log('用户数据:', data);
    } catch(error) {
        console.error('显示数据失败:', error);
    }
}

displayUserData();

// 并行处理
async function paralleRequests() {
    
    const [user, posts] = await Promise.all([
        fetchUserData(1),
        fetchUserData(2)
    ]);
    console.log('并行请求结果:', user, posts);
}

paralleRequests();