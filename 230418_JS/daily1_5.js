const participantNums =  [[1, 3, 2, 2, 1], 
[3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21],
[9, 1, 8, 7, 71, 33, 62, 35, 11, 4, 7, 71, 33, 8, 9, 1, 4, 11, 35]
]
for(lst of participantNums){
    for(k in lst){
        var stk = 0
        for(m in lst){
            if(k != m && (lst[k]==lst[m])){
                stk = 1
            }
        }
        if(stk==0){
            console.log(lst[k])
        }
    }
}
// 3
// 100
// 62