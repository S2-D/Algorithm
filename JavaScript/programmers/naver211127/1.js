function solution(record) {
  var answer = [];
  // record.forEach(element => {
  //   element
  // });
  console.log(record);
  return answer;
}

const a = ["P 300 6", "P 500 3", "S 1000 4", "P 600 2", "S 1200 1"];
// const a = ["P 300 6", "P 500 3", "S 1000 4", "P 600 1", "S 1200 2"]
// const a = ["P 100 4", "P 300 9", "S 1000 7", "P 1000 8", "S 700 7", "S 700 3"]

console.log(solution(a));

// ["P 300 6", "P 500 3", "S 1000 4", "P 600 2", "S 1200 1"]	[1500, 2400]
// ["P 300 6", "P 500 3", "S 1000 4", "P 600 1", "S 1200 2"]	[1800, 2700]
// ["P 100 4", "P 300 9", "S 1000 7", "P 1000 8", "S 700 7", "S 700 3"]	[7100, 10700]
