//Task Score : 58%

function solution(S) {
    //S : ACCAABBC -> 'AC' 
    //S : ABCBBCBA -> ''
    //S : BABABA -> 'BABABA'
    // write your code in JavaScript (Node.js 8.9.4)
    const arr = ['AA','BB','CC']
    var flag = true

    while(flag){
        var cnt = 1
        arr.forEach(val => {
            if(S.includes(val)){
                S = S.replace(val,'')
                return
            }else{
                cnt++
            }
            if(cnt > arr.length){
                flag = false
                return
            }
        })
    }

    return S
}
