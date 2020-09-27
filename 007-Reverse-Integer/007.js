/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
  const number = Number(Math.abs(x).toString().split('').reverse().join(''))    
      if (x < 0) {
          if (number > 2**31) {
              return 0 
          } else {
              return -number   
          }
      } else {
          if (number > 2**31-1) {
              return 0 
          } else {
              return number   
          }
      }   
};
