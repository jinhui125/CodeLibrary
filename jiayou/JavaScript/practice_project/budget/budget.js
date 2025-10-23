class BudgetApp {
    constructor() {
        this.records = JSON.parse(localStorage.getItem('budgetRecords')) || [];
        this.currentFilter = 'all';
        this.categories = {
            income: ['salary', 'bonus', 'investment'],
            expense: ['food', 'shopping', 'transport', 'entertainment']
        };
        
        this.categoryNames = {
            salary: '工资',
            bonus: '奖金',
            investment: '投资',
            food: '餐饮',
            shopping: '购物',
            transport: '交通',
            entertainment: '娱乐'
        };
        
        this.init();
    }
    
    init() {
        this.bindEvents();
        this.setDefaultDate();
        this.updateCategoryOptions();
        this.render();
    }
    
    bindEvents() {
        // 表单提交
        document.getElementById('recordForm').addEventListener('submit', (e) => {
            e.preventDefault();
            this.addRecord();
        });
        
        // 类型切换时更新分类选项
        document.querySelectorAll('input[name="type"]').forEach(radio => {
            radio.addEventListener('change', () => this.updateCategoryOptions());
        });
        
        // 过滤器
        document.querySelectorAll('.filter-btn').forEach(btn => {
            btn.addEventListener('click', (e) => this.setFilter(e.target.dataset.filter));
        });
    }
    
    setDefaultDate() {
        const today = new Date().toISOString().split('T')[0];
        document.getElementById('date').value = today;
    }
    
    updateCategoryOptions() {
        const type = document.querySelector('input[name="type"]:checked').value;
        const categorySelect = document.getElementById('category');
        
        // 清空现有选项（保留第一个空选项）
        categorySelect.innerHTML = '<option value="">选择分类</option>';
        
        // 添加对应类型的分类
        this.categories[type].forEach(category => {
            const option = document.createElement('option');
            option.value = category;
            option.textContent = this.categoryNames[category];
            categorySelect.appendChild(option);
        });
    }
    
    addRecord() {
        const formData = new FormData(document.getElementById('recordForm'));
        const record = {
            id: Date.now(),
            type: formData.get('type'),
            amount: parseFloat(formData.get('amount')),
            category: formData.get('category'),
            description: formData.get('description'),
            date: formData.get('date'),
            createdAt: new Date().toISOString()
        };
        
        this.records.unshift(record);
        this.saveToLocalStorage();
        this.render();
        document.getElementById('recordForm').reset();
        this.setDefaultDate();
        this.updateCategoryOptions();
    }
    
    deleteRecord(id) {
        this.records = this.records.filter(record => record.id !== id);
        this.saveToLocalStorage();
        this.render();
    }
    
    setFilter(filter) {
        this.currentFilter = filter;
        
        // 更新按钮状态
        document.querySelectorAll('.filter-btn').forEach(btn => {
            btn.classList.toggle('active', btn.dataset.filter === filter);
        });
        
        this.renderRecords();
    }
    
    getFilteredRecords() {
        switch (this.currentFilter) {
            case 'income':
                return this.records.filter(record => record.type === 'income');
            case 'expense':
                return this.records.filter(record => record.type === 'expense');
            default:
                return this.records;
        }
    }
    
    calculateSummary() {
        const income = this.records
            .filter(record => record.type === 'income')
            .reduce((sum, record) => sum + record.amount, 0);
            
        const expense = this.records
            .filter(record => record.type === 'expense')
            .reduce((sum, record) => sum + record.amount, 0);
            
        const balance = income - expense;
        
        return { income, expense, balance };
    }
    
    render() {
        this.renderSummary();
        this.renderRecords();
        this.renderChart();
    }
    
    renderSummary() {
        const { income, expense, balance } = this.calculateSummary();
        
        document.getElementById('totalIncome').textContent = `¥${income.toFixed(2)}`;
        document.getElementById('totalExpense').textContent = `¥${expense.toFixed(2)}`;
        document.getElementById('totalBalance').textContent = `¥${balance.toFixed(2)}`;
    }
    
    renderRecords() {
        const recordsList = document.getElementById('recordsList');
        const filteredRecords = this.getFilteredRecords();
        
        if (filteredRecords.length === 0) {
            recordsList.innerHTML = '<div class="empty-state">暂无记录</div>';
            return;
        }
        
        recordsList.innerHTML = filteredRecords.map(record => `
            <div class="record-item">
                <div class="record-info">
                    <div class="record-category">${this.categoryNames[record.category]}</div>
                    <div class="record-description">${this.escapeHtml(record.description)}</div>
                    <div class="record-date">${this.formatDate(record.date)}</div>
                </div>
                <div class="record-amount ${record.type}">
                    ${record.type === 'income' ? '+' : '-'}¥${record.amount.toFixed(2)}
                </div>
                <button class="delete-btn" onclick="budgetApp.deleteRecord(${record.id})">
                    删除
                </button>
            </div>
        `).join('');
    }
    
    renderChart() {
        const chartContainer = document.getElementById('chartContainer');
        const { income, expense } = this.calculateSummary();
        const maxAmount = Math.max(income, expense, 1);
        
        chartContainer.innerHTML = `
            <div class="chart-bar income" style="height: ${(income / maxAmount) * 100}%">
                <div class="chart-label">收入</div>
            </div>
            <div class="chart-bar expense" style="height: ${(expense / maxAmount) * 100}%">
                <div class="chart-label">支出</div>
            </div>
        `;
    }
    
    formatDate(dateString) {
        const date = new Date(dateString);
        return date.toLocaleDateString('zh-CN');
    }
    
    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
    
    saveToLocalStorage() {
        localStorage.setItem('budgetRecords', JSON.stringify(this.records));
    }
}

// 初始化应用
const budgetApp = new BudgetApp();