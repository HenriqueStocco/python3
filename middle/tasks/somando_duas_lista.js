const array_numbers_1 = [1, 2, 3, 4, 5, 6, 7];
const array_numbers_2 = [1, 2, 3, 4];
let arrays_numbers_soma = [];

for (let i = 0; i < array_numbers_2.length; i++) {
  arrays_numbers_soma.push(array_numbers_1[i] + array_numbers_2[i]);
}
console.log(arrays_numbers_soma)