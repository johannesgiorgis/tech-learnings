//Only change code below this line

function countdown(myArray, n){
	console.log(myArray, n);
	if (n < 1) {
		return [];
	} else {
		myArray.push(n);
		console.log(myArray);
		return countdown(myArray, n - 1);
	}
}