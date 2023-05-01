/* 
// filter
const products = [
    {name: 'cucumber', type:'vegetable'},
    {name: 'carrot', type:'vegetable'},
    {name: 'banana', type:'fruit'},
    {name: 'apple', type:'fruit'},
]

const fruitFilter = function (product){
    return product.type === 'vegetable'
}

const vegetables = products.filter(fruitFilter)
console.log(vegetables)
*/
/*
// reduce
var fruits = ["apple", "banana", "apple", "banana", "apple", "mellon"]
const f_count = fruits.reduce((counts, fruit)=>{
    if (fruit in counts){
        counts[fruit] ++
    }
    else{
        counts[fruit] = 1
    }
    return counts
},{})

f_count
*/
/*
//객체 생성

class Member {
    // init
    constructor(name, age){
        this.name = name
        this.age = age
    }
    introduce(){
        console.log(`my name is ${this.name}`)
    }
}
const me = new Member("ksh", "29")

me.name

me.introduce()
*/
/*
// 상속
  class Animal{
    constructor(name){
      this.name = name
    }
    speak(){
      console.log('${this.name} make some noise')
    }
  }
  class Dog extends Animal{
    constructor(name){
      super(name) // super 클래스의 생성자 호출
    }
    speak(){
      console.log('${this.name} barks')
    }
  }
  const d = new Dog("바둑이")
  d.speak()
*/