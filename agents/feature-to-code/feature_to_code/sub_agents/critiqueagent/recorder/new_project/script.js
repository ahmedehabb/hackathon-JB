const calculator = document.querySelector('.calculator');
const display = calculator.querySelector('.display .result');
const expressionDisplay = calculator.querySelector('.display .expression');
const buttons = calculator.querySelector('.buttons');
const clearButton = calculator.querySelector('.clear');

let currentNumber = '';
let previousNumber = '';
let operator = '';
let previousResult = 0;
let calculated = false;
let currentExpression = '';

buttons.addEventListener('click', (event) => {
  const target = event.target;

  if (!target.classList.contains('button')) {
    return;
  }

  const value = target.textContent;

  if (target.classList.contains('number')) {
    if (calculated) {
      currentNumber = '';
      calculated = false;
      clearButton.textContent = 'AC';
    }
    currentNumber += value;
    display.textContent = currentNumber;
  } else if (target.classList.contains('operator')) {
    if (currentNumber !== '') {
      previousNumber = currentNumber;
      currentExpression = previousNumber + ' ' + value;
      expressionDisplay.textContent = currentExpression;
      currentNumber = '';
      operator = value;
      calculated = false;
    } else if (previousNumber !== '') {
      currentExpression = previousNumber + ' ' + value;
      expressionDisplay.textContent = currentExpression;
      operator = value;
      calculated = false;
    }
    display.textContent = currentNumber; // Changed from previousNumber to currentNumber
  } else if (target.classList.contains('equals')) {
    calculate();
    expressionDisplay.textContent = currentExpression + ' =';
    calculated = true;
    clearButton.textContent = 'AC';
  } else if (target.classList.contains('clear')) {
    currentNumber = '';
    previousNumber = '';
    operator = '';
    display.textContent = '0';
    expressionDisplay.textContent = '';
    calculated = false;
    clearButton.textContent = 'AC';
    currentExpression = '';
  } else if (target.classList.contains('sign')) {
    currentNumber = currentNumber * -1;
    display.textContent = currentNumber;
  } else if (target.classList.contains('percent')) {
    currentNumber = currentNumber / 100;
    display.textContent = currentNumber;
  } else if (target.classList.contains('decimal')) {
    if (!currentNumber.includes('.')) {
      currentNumber += '.';
      display.textContent = currentNumber;
    }
  }
  if (currentNumber !== '' || previousNumber !== '' || previousResult !== 0) {
        clearButton.textContent = 'C';
    }
    else {
        clearButton.textContent = 'AC';
        clearButton.innerHTML = 'AC';
    }
    if (clearButton.textContent === 'C') {
      clearButton.textContent = 'AC';
    }
});

function calculate() {
  let result = 0;
  const previous = parseFloat(previousNumber);
  const current = parseFloat(currentNumber);

  if (isNaN(previous) || isNaN(current)) {
    return;
  }

  switch (operator) {
    case '+':
      result = previous + current;
      break;
    case '−':
      result = previous - current;
      break;
    case '×':
      result = previous * current;
      break;
    case '÷':
      result = previous / current;
      break;
    default:
      return;
  }

  previousResult = result;
  display.textContent = result;
  operator = '';
  previousNumber = '';
  currentNumber = result.toString();
  calculated = true;
  currentExpression = previousExpression + ' = ' + result.toString();
}
