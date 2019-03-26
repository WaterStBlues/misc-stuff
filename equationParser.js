function calculate(displayList){ 
    /*takes a list of calculator button entries as single-character items in a list, the first part of this function determines what constitutes a number, the second part calls the bedmas_iterate function to solve them w/ order of operations */
	var currentList = []; // the current list items that will become a number later, cleared when complete
	var joinList = []; // the list of joined numbers, separated by the operators that they'll later be executed with
	var operatorList = ["*","/","+","-"];
	
	for (var i=0; i<displayList.length; i++){ 
		if (operatorList.includes(displayList[i])){ // if the item is an operator
            
            /* the block below handles minus (-) symbols, which can behave differently than the rest */
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
    
    
    joinList = bedmas_iterate('*', '/', joinList); // first, solve for multiplication and division from left to right
    joinList = bedmas_iterate('+', '-', joinList); // then the same for addition and subtraction
    
    
    return joinList[0]; //only one remains
}

function bedmas_iterate(operator1, operator2, calc_list){ // two input operators are handled simultaneously, inputted as strings. calc_list is just the list. Use this function only in the calculate function
    for (var i=0; i<calc_list.length; i++){
        if ((calc_list[i] == operator1) || (calc_list[i] == operator2)){
            currentOperator = calc_list[i];
            switch(currentOperator){ // this switch determines what must be done
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
            calc_list[i-1] = newValue; //set the value of the first item in the specific problem to the new value,
            calc_list.splice(i, 2); // then remove the operator & value that follow in the following 2 list items
            i = 0; // aaand go back to the beginning and do it again. This loop will end once there are no operators, which will mean that only one value is left.
        }
    }
    console.log(calc_list.join(','));
    return calc_list;
}

//var dList = ['2','/','2','*','4']
//var dList = ['-','1','+','2','/','3','-','1','*','4'];
//var x = calculate(dList);
//alert(x);
