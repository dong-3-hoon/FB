/*
map: 배열의 값들을 어떤 기준으로 나눈 후, 동일한 자료형을 취해서 리스트 생성
filter: 배열의 값들을 어떤 조건을 충족하는 값들만 뽑아 새로운 리스트 생성
find: 주어진 판별 함수를 만족하는 첫 번째 요소의 값을 반환
every: 배열 안의 모든 요소가 판별 함수를 통과하는지 테스트
some: 배열 안의 어떤 요소가 하나라도 함수를 통과하는지 테스트
reduce: 배열의 각 요소에 주어진 리듀서 함수를 실행하고 결과 반환
*/
const nums = [1, 2, 3, 4]
for (var i =0;i<nums.length;i++){
    nums[i] = nums[i]*nums[i]*nums[i]
}
console.log(nums)