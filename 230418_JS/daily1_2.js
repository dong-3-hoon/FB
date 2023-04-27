words = ['level', 'noon', 'mom', 'happy', 'ssafy', 'life']

function palindrome(word) {
    // word가 회문인지 아닌지 판별
    var leng=word.length
    var ans =true
    var i
    for(i=0;i<leng/2;i++){
      if (word[i]!==word[word.length-(i+1)]){
        ans=false
      }
    }
    return ans
  }

for (const word of words) {
  console.log(palindrome(word))
}

// 출력 예시
// true
// true
// true
// false
// false
// false
