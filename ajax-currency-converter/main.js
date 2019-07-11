/* globals fetch */

let rates
const amountField = document.querySelector('#amount')
const fromDropdown = document.querySelector('#currency-from')
const toDropdown = document.querySelector('#currency-to')

function populateCurrencies (currencyData) {
  for (let row of currencyData.rates) {
    for (let dropdown of document.querySelectorAll('.currency-dropdown')) {
      let option = document.createElement('option')
      option.value = row.abbr
      option.innerText = row.name
      dropdown.appendChild(option)
    }
  }
}

function convertCurrency () {
  if (!rates) { return }

  const amount = parseFloat(amountField.value)
  const fromCurrency = fromDropdown.value
  const toCurrency = toDropdown.value

  const fromRate = rates.find(function (row) { return row.abbr === fromCurrency }).rateInUSD
  const toRate = rates.find(function (row) { return row.abbr === toCurrency }).rateInUSD

  let computedAmount = amount * fromRate / toRate
  computedAmount = roundToDecimal(computedAmount, 2)

  document.querySelector('#converted-amount').innerText = computedAmount
}

function roundToDecimal (number, decimalPlaces) {
  return Math.round(number * 10 ** decimalPlaces) / 10 ** decimalPlaces
}

/* Main execution */

document.addEventListener('DOMContentLoaded', function () {
  fetch('https://fantasy-currency.glitch.me/rates')
    .then(function (response) {
      return response.json()
    })
    .then(function (data) {
      rates = data.rates
      populateCurrencies(data)
    })

  amountField.addEventListener('input', convertCurrency)
  fromDropdown.addEventListener('input', convertCurrency)
  toDropdown.addEventListener('input', convertCurrency)
})
