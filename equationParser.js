function calculate(displayList){
	var currentList = []; // the current list items that will become a number later, cleared when complete
	var joinList = []; // the list of joined numbers, separated by the operators that they'll later be executed with
	var operatorList = ["*","/","+","-"];
	
	for (var i=0; i<displayList.length; i++){ 
		if (operatorList.includes(displayList[i])){ // if the item is an operator
			if ((displayList[i] == '-') && (currentList.length == 0)){
				currentList.push(displayList[i]); // check if the minus symbol is part of a number or acting as an operator, add it to the currentList if it's part of it
			}
			else{ /* if it's just a regular operator */
                if (i == (displayList.length - 1)){
                    joinList.push(parseFloat(currentList.join('')));
                    /* if it's an operator at the end w/ nothing in front of it, ignore the operator and simply push the current values in currentList to joinList to end the function */
                    }
                else{
                    joinList.push(parseFloat(currentList.join(''))); // join and parseFloat the current number stored in currentList, append to the joinList
                    currentList = []; // clear the currentList
                    joinList.push(displayList[i]); //add the operator after the number(s) before it
                }
			}
		}
		else{ // if it's a regular-ass number
			currentList.push(displayList[i]); //push to currentList
			if (i == (displayList.length - 1)){
				joinList.push(parseFloat(currentList.join('')));
                /*if it's at the end, parseFloat the joined version of the currentList and append that to joinedList, as there won't be an operator to execute the block above. If the last item is an operator, ignore it. */
			}
		}
	}
    
    var newValue;
    console.log("Beginning calculation function"); 
    console.log(joinList.join(','));
    
    
    for (var i=0; i<operatorList.length; i++){
        joinList = bedmas_iterate(operatorList[i], joinList); //run through each operator in bedmas_iterate, modifying joinList each time
        console.log(joinList.join(','))
    }
    
    
    return joinList[0]; //only one remains
}

function bedmas_iterate(operator, calc_list){ // input operator is "-" or "*" etc, calc_list is just the list
    for (var i=0; i<calc_list.length; i++){
        if (calc_list[i] == operator){
            switch(operator){
                case "+":
                    newValue = calc_list[i-1] + calc_list[i+1];
                    break;
                case "-":
                    newValue = calc_list[i-1] - calc_list[i+1];
                    break;
                case "*":
                    newValue = calc_list[i-1] * calc_list[i+1];
                    break;
                case "/":
                    newValue = calc_list[i-1] / calc_list[i+1];
                    break;    
            }
            calc_list[i-1] = newValue;
            calc_list.splice(i, 2);
            i = 0; // go back to beginning
        }
    }
    return calc_list;
}
    
//var dList = ['-','1','+','2','/','3','-','1','*','4'];
//var x = calculate(dList);
//alert(x);
