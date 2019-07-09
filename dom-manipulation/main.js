function q (selector, node) {
  let node
  if (!node) {
    node = document
  }

  return node.querySelector(selector)
}

function qs (selector, node) {
  let node
  if (!node) {
    node = document
  }

  return node.querySelectorAll(selector)
}

const newLikeButton = document.querySelector('#new-like-button')
// const newLikeButton = q('#new-like-button')

const newLikeForm = document.querySelector('#new-like-form')
newLikeButton.addEventListener('click', function () {
  newLikeButton.classList.add('hidden')
  newLikeForm.classList.remove('hidden')
  // q('input', newLikeForm).focus()
  newLikeForm.querySelector('input').focus()
})

const newLikeAdd = document.querySelector('#new-like-add')
newLikeAdd.addEventListener('click', function () {
  const listItem = document.createElement('li')
  listItem.innerText = newLikeForm.querySelector('input').value
  newLikeForm.querySelector('input').value = ''
  document.querySelector('#likes').appendChild(listItem)

  newLikeForm.classList.add('hidden')
  newLikeButton.classList.remove('hidden')
})
