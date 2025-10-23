class Animal {

    constructor(name) {
        this.name = name;
        this.energy = 100;
    }

    eat(amount) {
        this.energy += amount;
        console.log(`${this.name}进食，能量增加至${this.energy}`);
    }

    sleep(length) {
        this.energy += length;
        console.log(`${this.name}睡觉，能量增加至${this.energy}`);
    }

    static isAnimal(obj) {
        return obj instanceof Animal;
    }
}

class Dog extends Animal {

    constructor(name, breed) {
        super(name);
        this.breed = breed;
    }

    bark() {
        console.log(`${this.name}哇哇叫!`);
    }

    eat(amount) {
        super.eat(amount);
        console.log('狗狗吃的很开心!');
    }
}

const dog = new Dog('Buddy', '金毛');
dog.eat(10);
dog.bark();
console.log(Dog.isAnimal(dog));