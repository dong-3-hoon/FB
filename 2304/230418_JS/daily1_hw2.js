// 1번
const nums = [1,2,3,4,5,6,7,8]

for (var i = 0; i < nums.length; i++) {
  console.log('nums[' + i + ']: ' + nums[i])
}
// const는 변화할 수 없는 값이다. 그런데 i++로 증분을 시켜서 에러가 발생함
// for (const i = 0; i < nums.length; i++) {
//                                     ^

// TypeError: Assignment to constant variable.

// 2번
for (num of nums) {
  console.log(num, typeof num)
}
// for (num in nums) 는 인덱스값을 출력한다 하지만 for(num of nums)는 
// nums안의 정수를 출력하기 때문에 number이 출력된다

// 0 string
// 1 string
// 2 string
// 3 string
// 4 string
// 5 string
// 6 string
// 7 string
