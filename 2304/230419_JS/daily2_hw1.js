let ans = "";

for (var i = 0; i < 5; i++) {
    for (var j = 5; j > i; j--) {
        ans += " "
    }
    for (var k = 0; k < i * 2 + 1; k++) {
        ans += "*"
    }
    ans += "\n"
}
console.log(ans);