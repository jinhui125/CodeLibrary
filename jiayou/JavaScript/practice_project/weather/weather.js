class WeatherApp {
    constructor() {
        this.apiKey = 'your_api_key_here'; // 需要替换为实际的 API key
        this.recentSearches = JSON.parse(localStorage.getItem('recentSearches')) || [];
        this.init();
    }
    
    init() {
        this.bindEvents();
        this.renderRecentSearches();
    }
    
    bindEvents() {
        document.getElementById('searchBtn').addEventListener('click', () => this.searchWeather());
        document.getElementById('cityInput').addEventListener('keypress', (e) => {
            if (e.key === 'Enter') this.searchWeather();
        });
    }
    
    async searchWeather() {
        const cityInput = document.getElementById('cityInput');
        const city = cityInput.value.trim();
        
        if (!city) {
            this.showError('请输入城市名称');
            return;
        }
        
        this.showLoading(true);
        this.hideError();
        
        try {
            const weatherData = await this.fetchWeatherData(city);
            this.displayWeather(weatherData);
            this.addToRecentSearches(city);
        } catch (error) {
            this.showError('获取天气信息失败，请检查城市名称是否正确');
            console.error('Weather API error:', error);
        } finally {
            this.showLoading(false);
        }
    }
    
    async fetchWeatherData(city) {
        // 使用模拟数据（实际项目中应该调用真实的天气 API）
        // 这里使用 OpenWeatherMap API 的格式作为示例
        await new Promise(resolve => setTimeout(resolve, 1000)); // 模拟网络延迟
        
        // 模拟响应数据
        const mockData = {
            name: city,
            main: {
                temp: Math.round(Math.random() * 30 + 5),
                humidity: Math.round(Math.random() * 50 + 30),
                pressure: Math.round(Math.random() * 100 + 1000)
            },
            weather: [{
                main: ['Clear', 'Clouds', 'Rain', 'Snow'][Math.floor(Math.random() * 4)],
                description: '晴朗天气'
            }],
            wind: {
                speed: Math.round(Math.random() * 10 + 1)
            },
            visibility: Math.round(Math.random() * 10 + 5)
        };
        
        return mockData;
        
        /* 实际 API 调用代码（需要替换为真实的 API key）
        const response = await fetch(
            `https://api.openweathermap.org/data/2.5/weather?q=${city}&units=metric&appid=${this.apiKey}`
        );
        
        if (!response.ok) {
            throw new Error('City not found');
        }
        
        return await response.json();
        */
    }
    
    displayWeather(data) {
        const weatherCard = document.getElementById('weatherCard');
        const icon = this.getWeatherIcon(data.weather[0].main);
        
        document.getElementById('cityName').textContent = data.name;
        document.getElementById('weatherIcon').textContent = icon;
        document.getElementById('temperature').textContent = `${data.main.temp}°C`;
        document.getElementById('weatherDescription').textContent = data.weather[0].description;
        document.getElementById('humidity').textContent = `${data.main.humidity}%`;
        document.getElementById('windSpeed').textContent = `${data.wind.speed} m/s`;
        document.getElementById('pressure').textContent = `${data.main.pressure} hPa`;
        document.getElementById('visibility').textContent = `${data.visibility} km`;
        
        weatherCard.classList.add('show');
    }
    
    getWeatherIcon(weatherMain) {
        const icons = {
            'Clear': '☀️',
            'Clouds': '☁️',
            'Rain': '🌧️',
            'Snow': '❄️',
            'Thunderstorm': '⛈️',
            'Drizzle': '🌦️',
            'Mist': '🌫️'
        };
        
        return icons[weatherMain] || '🌤️';
    }
    
    addToRecentSearches(city) {
        // 移除重复项
        this.recentSearches = this.recentSearches.filter(item => item !== city);
        
        // 添加到开头
        this.recentSearches.unshift(city);
        
        // 只保留最近5个
        this.recentSearches = this.recentSearches.slice(0, 5);
        
        // 保存到本地存储
        localStorage.setItem('recentSearches', JSON.stringify(this.recentSearches));
        
        this.renderRecentSearches();
    }
    
    renderRecentSearches() {
        const recentList = document.getElementById('recentList');
        const recentSearches = document.getElementById('recentSearches');
        
        if (this.recentSearches.length === 0) {
            recentSearches.style.display = 'none';
            return;
        }
        
        recentSearches.style.display = 'block';
        recentList.innerHTML = this.recentSearches.map(city => `
            <div class="recent-item" onclick="weatherApp.searchRecent('${city}')">
                ${city}
            </div>
        `).join('');
    }
    
    searchRecent(city) {
        document.getElementById('cityInput').value = city;
        this.searchWeather();
    }
    
    showLoading(show) {
        document.getElementById('loading').style.display = show ? 'block' : 'none';
    }
    
    showError(message) {
        const errorElement = document.getElementById('errorMessage');
        errorElement.textContent = message;
        errorElement.style.display = 'block';
    }
    
    hideError() {
        document.getElementById('errorMessage').style.display = 'none';
    }
}

// 初始化应用
const weatherApp = new WeatherApp();