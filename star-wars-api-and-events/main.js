/* globals fetch */

function q (sel) {
  return document.querySelector(sel)
}

function qs (sel) {
  return document.querySelectorAll(sel)
}

function planetNode (planet) {
  const planetDiv = document.createElement('div')
  planetDiv.classList.add('planet', 'ba', 'bw2', 'purple')
  planetDiv.innerHTML = `
    <h3 class="f1 pink">${planet.name}</h3>
    <p>Population: ${planet.population}</p>
    <p>Climate: ${planet.climate}</p>
    <button class="get-planet-data" data-url="${planet.url}">Find out more about ${planet.name}</button>
  `
  return planetDiv
}

function displayPlanetData (planetUrl) {
  fetch(planetUrl)
    .then(res => res.json())
    .then(function (data) {
      const dataDisplay = q('#planet-data')
      dataDisplay.innerHTML = `
        <h3>More info about ${data.name}</h3>
        <dl>
          <dt>Terrain</dt>
          <dd>${data.terrain}</dd>
          <dt>Gravity</dt>
          <dd>${data.gravity}</dd>
        </dl>
      `
    })
}

/* Main execution */

document.addEventListener('DOMContentLoaded', function () {
  q('#planet-results').addEventListener('click', function (event) {
    console.log(event.target)
    if (event.target && event.target.matches('button.get-planet-data')) {
      displayPlanetData(event.target.dataset['url'])
    }
  })

  q('form').addEventListener('submit', function (event) {
    event.preventDefault()
    const searchTerm = q('#planet-name').value
    const url = `https://swapi.co/api/planets/?search=${encodeURIComponent(searchTerm)}`

    const resultsDiv = q('#planet-results')

    fetch(url)
      .then(response => response.json())
      .then(function (data) {
        resultsDiv.innerHTML = ''
        for (let planet of data.results) {
          resultsDiv.appendChild(planetNode(planet))
        }
      })
  })
})
